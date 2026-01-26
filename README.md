# Automotive Circular Economy Ontology

Description: PMD Core application ontology generated via ODK Template.


More information can be found at http://obofoundry.org/ontology/automatce

## Versions

### Stable release versions

The latest version of the ontology can always be found at:

https://w3id.org/pmd/automatce.owl

(note this will not show up until the request has been approved by obofoundry.org)

### Editors' version

Editors of this ontology should use the edit version, [src/ontology/automatce-edit.owl](src/ontology/automatce-edit.owl)

## Contact

Please use this GitHub repository's [Issue tracker](https://github.com/materialdigital/materialdigital/automatce/issues) to request new terms/classes or report errors or specific concerns related to the ontology.

## Acknowledgements

This ontology repository was created using the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit).
## Development
This ontology is developed using OWL and managed with the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit). To edit:
- Open `automatce-edit.owl` in [Protégé](https://protege.stanford.edu/).
- Create new entities within the namespace `https://w3id.org/pmd/automatce/`.
- Use the `Makefile` for automation (`make test`, `make refresh-imports`, `make release`).

### Top-level directories
**.github/:** GitHub configuration files, including CI workflows and templates.
**src/:** Main development folder generated and managed through ODK.
**ontology/components/:** – Modular ontology components (classes, properties, axioms).
**ontology/pmdco-edit.owl:** – Primary editable ontology file used during development (ontology editors' version).

## Import Architecture
```
imports-edit.owl
    └── imports all *_import.owl modules (pmdco_import.owl, etc.)

automatce-shared.owl
    └── imports imports-edit.owl

automatce-{component}.owl (each component)
    └── imports automatce-shared.owl

automatce-axioms-shared.owl
    └── imports ALL automatce-{component}.owl files
```

## Contribution
We welcome contributions! Please use the [Issue tracker](https://github.com/materialdigital/automatce/issues).
