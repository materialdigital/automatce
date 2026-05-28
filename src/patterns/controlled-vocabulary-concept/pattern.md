# Pattern: Controlled Vocabulary Concept

## Purpose

Represent controlled values such as VDA material classes as SKOS concepts, not OWL classes.

## Description

Each concept belongs to one concept scheme, carries one notation, and has one English label. German source names are retained as `skos:altLabel` where needed to keep `rdfs:label` aligned with the PMD Core labeling style.

## Shapes and Example Data

[shape-data.ttl](shape-data.ttl)

[shape.ttl](shape.ttl)
