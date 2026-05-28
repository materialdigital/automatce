# Pattern: Object Property Bridge

## Purpose

Reuse object properties from BFO, RO, PMD Core, OBI, IAO, and LOG without minting duplicate AutoMatCE properties.

## Description

If an SLME import brings only a property declaration, add display annotations to the imported IRI itself. Do not create a local replacement property. This keeps axioms interoperable while preventing Protege from showing bare CURIEs or IRIs.

## Shape and Example Data

[shape.ttl](shape.ttl)

[shape-data.ttl](shape-data.ttl)

