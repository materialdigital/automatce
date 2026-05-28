PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX pmd: <https://w3id.org/pmd/co/>
PREFIX log: <https://w3id.org/pmd/log/>

DELETE {
  ?s ?p ?old .
}
INSERT {
  ?s ?p ?preferred .
}
WHERE {
  VALUES (?old ?preferred) {
    (log:LOG_0080000 obo:IAO_0020000)
    (log:LOG_1000017 obo:OBI_0000835)
    (log:LOG_1000037 pmd:PMD_0020138)
    (log:LOG_1000050 obo:OBI_0000245)
    (log:LOG_1000061 obo:OBI_0000571)
    (log:LOG_1000131 pmd:PMD_0000833)
  }
  ?s ?p ?old .
}
;

DELETE {
  obo:OBI_0000571 rdfs:subClassOf log:LOG_1000054 .
}
WHERE {
  obo:OBI_0000571 rdfs:subClassOf log:LOG_1000054 .
}
