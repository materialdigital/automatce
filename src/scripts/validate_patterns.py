#!/usr/bin/env python3
"""Validate AutoMatCE pattern files and example references."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import yaml
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
from rdflib.plugins.sparql.parser import parseQuery


SH = "http://www.w3.org/ns/shacl#"
AUTOMATCE = "https://w3id.org/pmd/automatce/"
PATTERNS = "https://w3id.org/pmd/automatce/patterns/"

NON_CLASS_PATTERNS = {
    "controlled vocabulary concept",
    "object property bridge",
}


def parse_turtle(paths: Iterable[Path]) -> None:
    for path in paths:
        Graph().parse(path.as_posix(), format="turtle")


def parse_sparql(paths: Iterable[Path]) -> None:
    for path in paths:
        parseQuery(path.read_text(encoding="utf-8"))


def parse_yaml_patterns(paths: Iterable[Path]) -> None:
    errors: list[str] = []
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            errors.append(f"{path}: pattern file is not a YAML mapping")
            continue

        for key in ("pattern_name", "pattern_iri", "description"):
            if key not in data:
                errors.append(f"{path}: missing required key '{key}'")

        pattern_name = str(data.get("pattern_name", ""))
        if pattern_name not in NON_CLASS_PATTERNS:
            if "name" not in data:
                errors.append(f"{path}: class-generating pattern has no name block")
            if "def" not in data:
                errors.append(f"{path}: class-generating pattern has no def block")

    if errors:
        raise SystemExit("\n".join(errors))


def check_pattern_shape_namespaces(pattern_root: Path) -> None:
    errors: list[str] = []
    node_shape = URIRef(f"{SH}NodeShape")
    for path in sorted(pattern_root.glob("*/shape.ttl")):
        graph = Graph().parse(path.as_posix(), format="turtle")
        for shape in graph.subjects(RDF.type, node_shape):
            if isinstance(shape, URIRef) and not str(shape).startswith(PATTERNS):
                errors.append(
                    f"{path}: SHACL node shape {shape} should use the /patterns/ namespace"
                )
    if errors:
        raise SystemExit("\n".join(errors))


def check_shape_data_references(pattern_root: Path, ontology_path: Path) -> None:
    if not ontology_path.exists():
        raise SystemExit(f"{ontology_path}: ontology file not found")

    ontology = Graph().parse(ontology_path.as_posix(), format="turtle")
    errors: list[str] = []

    for path in sorted(pattern_root.glob("*/shape-data.ttl")):
        graph = Graph().parse(path.as_posix(), format="turtle")
        terms: set[URIRef] = set()
        for subject, predicate, obj in graph:
            for term in (subject, predicate, obj):
                if isinstance(term, URIRef):
                    text = str(term)
                    if text.startswith(AUTOMATCE) and not text.startswith(PATTERNS):
                        terms.add(term)

        for term in sorted(terms, key=str):
            if (term, None, None) not in ontology:
                errors.append(f"{path}: {term} is not present in {ontology_path}")

    if errors:
        raise SystemExit("\n".join(errors))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--patterns", default="src/patterns", type=Path)
    parser.add_argument(
        "--shapes", default="src/shapes/automatce-ontology-shapes.ttl", type=Path
    )
    parser.add_argument("--ontology", default="src/ontology/automatce-full.ttl", type=Path)
    args = parser.parse_args()

    pattern_ttls = sorted(args.patterns.glob("**/*.ttl"))
    yaml_patterns = sorted(args.patterns.glob("*.yaml"))
    queries = sorted((args.patterns / "queries").glob("*.rq"))

    parse_turtle([*pattern_ttls, args.shapes])
    parse_sparql(queries)
    parse_yaml_patterns(yaml_patterns)
    check_pattern_shape_namespaces(args.patterns)
    check_shape_data_references(args.patterns, args.ontology)

    print(
        f"Validated {len(pattern_ttls)} pattern Turtle files, "
        f"{len(yaml_patterns)} YAML patterns, and {len(queries)} SPARQL queries."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
