# Pattern: Process Input Output

## Purpose

Represent manufacturing, dismantling, recycling, and logistics processes with participants, inputs, and outputs.

## Description

Use PMD Core process classes when they exist, such as PMD manufacturing process. Use LOG only for logistics concepts absent from PMD. Connect material inputs with `RO_0002233`, outputs with `RO_0002234`, participants with `RO_0000057`, and realized plans with `BFO_0000055`.

## Shape and Example Data

[shape.ttl](shape.ttl)

[shape-data.ttl](shape-data.ttl)

