These notes are for editors of AutoMatCE.

The active ODK configuration is `automatce-odk.yaml`. Curated ontology content
belongs in `components/`, with shared cross-module axioms in
`components/automatce-axioms-shared.owl`.

For routine changes, update the relevant component and open a pull request.
GitHub Actions builds the ontology, validates SHACL shapes and pattern examples,
checks SPARQL syntax, and verifies that root release artifacts match the
generated `src/ontology` artifacts.

For the full public workflow, use the repository root `README.md`.
