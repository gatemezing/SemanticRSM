# SemanticRSM
RSM recast, based on direct RDF/OWL modelling

## License
EUPL 1.2

## Purpose
RTM 1.0, RTM 1.1, and RSM 1.2, all published by UIC, follow principles generally observed in object-oriented modelling, using UML. RSM 1.2 model was successfully transformed into an OWL ontology, using the Ontorail toolset developed by UIC. However, the expressiveness of OWL differs from UML class diagrams. OWL offers possibilities to make RSM both more compact and more expressive, while remaining compatible with former, UML-based versions. The present repository summarizes the re-casting efforts.

## Design goals
* Backward compatibility.
* Simplification.
* Improvements: navigability as a transitive property, internal navigability in "operational points" (yards, stations), more flexible composition of net elements...
* Systematic usage of well-established external vocabularies, where relevant.
* Ability to determine paths under constraints using SPARQL and inference engines, rather than bespoke code.

## Design process
The process considers the RINF use case, with priority to topology and geographic referencing. However the design, as previously with RSM, emphasizes generality and avoids ad-hoc solutions.

## Tools
* Protégé desktop for RDF edition and reasoning.
* Sparx Enterprise Architect for UML diagrams.
* Sample data set based on a fictive network.
* Draw.io for graphics.

## Languages
RDF/OWL/SHACL, SPARQL, Python, SWI Prolog.

# Documentation
## Wiki
The Wiki documents the design process, esp. main design choices.
