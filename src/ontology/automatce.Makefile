## Customize Makefile settings for automatce
## 
## If you need to customize your Makefile, make
## changes here rather than in the main Makefile

# Preserve annotated bridge axioms that keep imported PMD/LOG classes readable
# in asserted class hierarchy views after the ODK reason/relax/reduce pipeline.
REDUCE_OPTIONS = --include-subproperties true --preserve-annotated-axioms true

# Avoid ambiguous Protege display labels for imported LOG dependency-closure
# classes that intentionally coexist with preferred PMD/OBI classes.
SHARED_ROBOT_COMMANDS = query --update ../sparql/display-label-cleanup.ru remove --term https://w3id.org/pmd/log/LOG_0080000 --term https://w3id.org/pmd/log/LOG_1000017 --term https://w3id.org/pmd/log/LOG_1000037 --term https://w3id.org/pmd/log/LOG_1000050 --term https://w3id.org/pmd/log/LOG_1000061 --term https://w3id.org/pmd/log/LOG_1000131 --term https://w3id.org/pmd/log/LOG_1000090 --term https://w3id.org/pmd/log/LOG_1000032 --term https://w3id.org/pmd/log/LOG_1000146 --term https://w3id.org/pmd/co/PMD_0040029 --term https://w3id.org/pmd/co/PMD_0040030 --term http://www.w3.org/ns/org\#Site --term http://purl.obolibrary.org/obo/BFO_0000082 --term http://purl.obolibrary.org/obo/BFO_0000183 --trim true
