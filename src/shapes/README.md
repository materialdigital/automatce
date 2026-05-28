# AutoMatCE SHACL shapes

`automatce-ontology-shapes.ttl` contains SHACL constraints for ontology QA and
data-exchange conventions:

- local AutoMatCE classes require English label, definition, example, and a
  logical placement axiom;
- VDA material-classification `skos:Concept` individuals require notation and
  scheme membership;
- value specifications follow the PMD Core scalar value pattern, using
  `OBI_0001937` for the numeric value and `IAO_0000039` for the unit.

These shapes are not imported into the OWL ontology. Run them as a separate QA
step with a SHACL engine after converting or materializing the ontology graph.
