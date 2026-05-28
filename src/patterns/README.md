# AutoMatCE ontology patterns

These patterns document the repeatable modelling choices used in the component
files. The YAML files are lightweight ODK/DOSDP-style class templates. The
subfolders follow the PMD Core pattern layout with `pattern.md`, `shape.ttl`,
and `shape-data.ttl`.

- `quantitative-attribute.yaml`: material, process, simulation, and vehicle
  quantities with expected datatype and unit annotations.
- `identifier.yaml`: manufacturer, vehicle, material, batch, and business
  partner identifiers.
- `controlled-vocabulary-concept.yaml`: VDA 231-106 material classification
  concepts modelled as `skos:Concept` individuals.
- `object-property-bridge.yaml`: annotation bridge pattern for reused external
  BFO, RO, PMD, OBI, IAO, and LOG properties.
- `material-composition.yaml`: product, component, material, and batch
  composition records.
- `process-input-output.yaml`: manufacturing, dismantling, recycling, and
  logistics processes with participants, inputs, and outputs.
- `circular-strategy-selection.yaml`: selected circular economy strategy records.
- `lifecycle-footprint.yaml`: lifecycle and scenario carbon footprint records.
- `logistics-transfer.yaml`: recycling batch or shipment transfer records.
- `pressure-volume-temperature-data-point.yaml`: pressure-volume-temperature
  tuple records.
- `dismantling-information.yaml`: dismantling instructions and related
  dismantlability records.
- `condition-damage-assessment.yaml`: component condition and damage assessment
  records.

PMD-style pattern folders:

- `quantitative-attribute/`: quantitative qualities and value specifications.
- `identifier/`: IAO identifiers used for manufacturer, batch, product, and
  Catena-X records.
- `controlled-vocabulary-concept/`: SKOS concepts for controlled values.
- `object-property-bridge/`: external object properties used without minting
  AutoMatCE replacements.
- `material-composition/`: material composition records linked from products,
  components, materials, and batches.
- `process-input-output/`: process instances with participants, inputs, outputs,
  and optional realized plan specifications.
- `circular-strategy-selection/`: circular economy information with one selected
  R-strategy.
- `lifecycle-footprint/`: product carbon footprint values and lifecycle-stage
  context.
- `logistics-transfer/`: recycling batch and shipment actor modeling.
- `pressure-volume-temperature-data-point/`: pVT data with pressure,
  temperature, and specific volume values.
- `dismantling-information/`: dismantling plan, time, and disposition modeling.
- `condition-damage-assessment/`: quality and damage information about used
  components.
- `queries/`: competency queries for composition, process, circular strategy,
  lifecycle footprint, logistics transfer, pVT data, dismantling, and condition
  records.
