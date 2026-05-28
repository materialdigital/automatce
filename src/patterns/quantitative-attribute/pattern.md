# Pattern: Quantitative Attribute

## Purpose

Represent a measurable quality, process attribute, or simulation parameter with an ontology class and a scalar value specification in instance data.

## Description

The class is placed under the closest PMD Core or BFO genus, such as `PMD_0020133` mass, `PMD_0020150` volume, `PMD_0000967` temperature, or `OBI_0001933` value specification. Instance data should keep the bearer, value specification, numeric value, and unit separate. This follows the PMD Core scalar value pattern.

## Shapes and Example Data

[shape-data.ttl](shape-data.ttl)

[shape.ttl](shape.ttl)
