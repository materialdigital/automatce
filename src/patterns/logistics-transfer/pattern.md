# Pattern: Logistics Transfer

## Purpose

Represent recycling batch and shipment transfer information without duplicating LOG terms.

## Description

Use LOG for logistics classes not present in PMD Core. A recycling batch should carry an identifier and at least one supply chain actor. Locations and transport processes use imported BFO, RO, PMD, and LOG properties where available.

## Shape and Example Data

[shape.ttl](shape.ttl)

[shape-data.ttl](shape-data.ttl)

