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
    - Example class ID: `https://w3id.org/pmd/automatce/AUTOMATCE_0000001` (PREFIX is uppercase).
- Use the `Makefile` for automation:
    - `make test`: Run quality control (OWL reasoner checks, syntax validation).
    - `make refresh-imports`: Update imported ontologies (e.g., PMD Core, LOGO) with SLME extraction.
    - `make release`: Build release artifacts (full, base, etc.) in TTL/OWL/JSON formats.
    - `make update_repo`: Sync changes to the repo structure.
Quick start: After setup, edit in Protégé, commit, and push to trigger CI builds.

## Repository Structure
This repository provides the modular implementation of automatce, developed and maintained using the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit).

### Top-level directories

* **.github/:** GitHub configuration files, including CI workflows and templates.
* **docs/:** Documentation sources for the ontology website and user guides (optional; add as needed).
* **patterns/:** Logical patterns and SHACL shapes used to maintain consistent ontology design (optional).
* **src/:** Main development folder generated and managed through ODK.
  * **ontology/components/:** – Modular ontology components (classes, properties, axioms).
  * **ontology/automatce-edit.owl:** – Primary editable ontology file used during development (ontology editors' version).
  * **ontology/imports/:** Extracted terms from imported ontologies (via SLME).
### Ontology versions (generated on release)
* **automatce-full.owl/ttl:** Complete ontology with all imports and full axiomatization.
* **automatce-base.owl/ttl:** Core entities without extended imports.
* **automatce-simple.owl/ttl:** Simplified version with basic subclass and existential axioms.
* **automatce-minimal.owl/ttl:** Lightweight minimal version for quick onboarding (recommended for beginners).
* **automatce.owl/ttl:** Main ontology file contains the full version.
### Other files
* README.md, LICENSE.txt, CONTRIBUTING.md – Project overview, license, and contribution guidelines.
* imports.txt, components.txt, creators.txt – Configuration for setup (optional edits).

## Contribution

We welcome contributions! 
- Please use the [Issue tracker](https://github.com/materialdigital/automatce/issues).
- For creation of application ontologies using PMD core ontologies, we advise using the **[application-ontology-template](https://github.com/materialdigital/application-ontology-template/)**. It applies the same framework used here and mirrors the pmdco with all its modules.
- Write about your specific modeling concerns or any other discussable topics in the **[discussion forum](https://github.com/POTUSAITEJA/Automce/discussions)**.
- Participate in our **PMD Playground Meetings**: Our Ontology Playground, organized online every second Friday from 1-2 pm (CET), is a great opportunity to connect with developers and our proactive community to shape the PMDco. Please register via our [mailing list](https://www.lists.kit.edu/sympa/subscribe/ontology-playground?previous_action=info).
- If you need further information, please feel free to contact us via **[info@material-digital.de](mailto:info@material-digital.de)**
