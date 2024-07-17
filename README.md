# SemanticRSM
RSM recast, based on direct RDF/OWL modelling.

RSM stands for Rail System Model. RSM is a UIC IRS (International Railway Standard), first released in 2016 as RailTopoModel (RTM): see https://rsm.uic.org.

## License
EUPL 1.2

## Purpose
RTM 1.0, RTM 1.1, RSM 1.2 and its extensions, all published by UIC, follow principles generally observed in conceptual modelling, 
using UML. RSM 1.2 model was successfully transformed into an OWL ontology, using the Ontorail toolset developed by UIC.

However, the expressiveness of OWL differs from UML class diagrams.
OWL offers possibilities to make RSM both more compact and more expressive, while remaining compatible with former, UML-based versions. The present repository summarizes the re-casting efforts.

## Design goals
* Backward compatibility ("easy" automated transformations).
* Simplification (not: dumbing down).
* Separation into small vocabularies (high-cohesion, low-dependency principle) to facilitate ontology management.
* Improvements:
    - about topology:
        - navigability as a transitive property,
        - internal navigability in "operational points" (yards, stations),
        - more flexible composition of net elements.
* Systematic, explicit usage of well-established external vocabularies, where relevant: SOSA/SSN, GeoSPARQL, w3c time...
* Ability to determine paths under constraints using SPARQL and inference engines, even though bespoke code may be recommended for computing efficiency.

## Design process
The process currently considers
* the [RINF](https://uat.ld4rail.fpfis.tech.ec.europa.eu/) use case, with priority to topology (expressed at micro level, or track level) and geographic referencing.
* the System Pillar requirements regarding rolling stock modelling (typology)
* FP5-TRANSF4M-R data requirements regarding the description of the "last mile of infrastructure" and of rolling stock defects.

However the design, as previously with RSM, emphasizes generality and avoids ad-hoc solutions.

Other use cases may come from other pieces of EU Law, such as TAF TSI, or from ongoing EU projects.

## Tools
* [Protégé](https://protege.stanford.edu/) desktop 5.x for RDF edition, checking, and saving to different formats.
* [EasyRdf](https://www.easyrdf.org/converter) for format conversion (between RDF/XML and Turtle, mostly).
* Graphics:
    - Sparx Enterprise Architect (v. 16 or later) for UML diagrams, possibly using the built-in [ODM](https://www.omg.org/odm/) UML profile.
    - Visual Paradigm also for UML diagrams, possibly using the [OntoUML](https://ontouml.org/) profile (linked with the UFO general ontology).
    - Draw.io for hand-drawn graphics.
    - Other diagrams (in the Wiki) were generated from an extended markdown using [Mermaid](https://github.com/mermaid-js/mermaid) scripts, or
    - from ttl files using [OntoMermaid](https://github.com/floresbakker/OntoMermaid), a Python program returning a Mermaid script.
 As Sparx Enterprise Architect and Visual Paradigm are paid applications, copies of the diagrams are also provided in PNG.
 
## Data
* Sample data sets:
    - based on fictive or real networks, or
    - based on OpenStreetMap, using [Overpass Turbo](https://overpass-turbo.eu/).

## Languages
RDF, [RDF-star](https://www.w3.org/2022/08/rdf-star-wg-charter/), OWL, SHACL (for constraints), SPARQL (for queries), SPARQL-star, Python; some SWI Prolog (for demo purposes).

# Documentation
## Wiki
The Wiki documents the design process, esp. main design choices. This is an integrated wiki, accessible via the GitHub menu bar.

## Documentation folder
Only contains diagrams (class diagrams for instance) and illustrations. Full documentation is in the wiki.
