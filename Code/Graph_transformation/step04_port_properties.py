import itertools
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF
from rdflib.term import Node
from typing import Optional
from Code.Namespaces import *


def set_port_connections(input_ttl: str, output_ttl: Optional[str] = None):
    g = Graph()
    g.parse(input_ttl, format="turtle")

    print("Setting the connections between ports")

    # Get all the ports in the graph
    ports = g.subjects(RDF.type, RSM_TOPOLOGY.Port)  # a generator
    list_ports = list(itertools.islice(ports, None))
    print(f"    {len(list_ports)} ports found")

    # Iterate over each port
    connections_count = 0
    for index, port1 in enumerate(list_ports[:-2]):
        c1 = g.value(port1, GSP.asWKT)
        for port2 in list_ports[index + 1:]:
            c2 = g.value(port2, GSP.asWKT)
            if c1 == c2:
                g.add((port1, RSM_TOPOLOGY.connectedWith, port2))
                connections_count += 1

    print(f"    {connections_count} ports connected")

    # Output
    if output_ttl:
        g.serialize(destination=output_ttl, format='turtle')
    else:
        print(g.serialize(format='turtle'))


def possible_navigability(azimuth_1: float, azimuth_2: float) -> bool:
    """
    Determines whether it is possible to navigate between linear elements basing on the azimuths of their connected
    extremities. Azimuths values are provided in degrees, in the range [-180, 180] (this is a pyproj setting).
    "Possibility" is provided when the azimuth difference, modulo 180 degrees, is "small".
    :param azimuth_1:
    :param azimuth_2:
    :return: True if navigability is possible, else False
    """
    small = 30  # could be set to a much smaller value, given the quality of the geometry in OSM
    diff = azimuth_1 - azimuth_2 - 180
    if abs(diff) > 180:
        diff = 360 - abs(diff)
    return abs(diff) <= small


def opposite_port(g: Graph, a_port: Node) -> Node | None:
    """
    Leads from a_port to the other port in the same linear element
    :returns the opposite port, or None if the element is not a Linear Element
    """
    element = list(g.objects(a_port, RSM_TOPOLOGY.onElement))  # only one element is expected; better check
    if len(element) == 1 and (g.value(element[0], RDF.type) == RSM_TOPOLOGY.LinearElement):
        other_port = [x for x in g.subjects(RSM_TOPOLOGY.onElement, element[0]) if x != a_port]
        if len(other_port) == 1:
            return other_port[0]
    return None


def set_navigabilities(input_ttl: str, output_ttl: Optional[str] = None, double_slip_crossings: bool = True):
    g = Graph()
    g.parse(input_ttl, format="turtle")

    print("setting the navigabilities between ports")
    navigabilities_count = 0
    # Get all the ports in the graph
    ports = g.subjects(RDF.type, RSM_TOPOLOGY.Port)  # a generator
    for port in list(ports):
        # Get the connected ports (subjects or objects in the connectedWith property, which is symmetric)
        directly_connected_ports = set(g.objects(port, RSM_TOPOLOGY.connectedWith))
        inverse_connected_ports = set(g.subjects(RSM_TOPOLOGY.connectedWith, port))
        connected_ports_list = list(directly_connected_ports.union(inverse_connected_ports))
        case = len(connected_ports_list)
        if case == 1:
            print(f"WARNING: Port {port} has exactly 1 other port connected; should be 0 or >= 2.")
        if case in (2, 3):  # switch, or assumed double-slip crossing
            # TODO: change default assumption from double slip to diamond crossing
            for other_port in connected_ports_list:
                opposite = opposite_port(g, other_port)
                if opposite:
                    azimuth1 = float(g.value(port, RSM_TOPOLOGY.azimuth))
                    azimuth2 = float(g.value(other_port, RSM_TOPOLOGY.azimuth))
                    if possible_navigability(azimuth1, azimuth2):
                        g.add((port, RSM_TOPOLOGY.navigableTo, opposite))
                        navigabilities_count += 1
                        # We assume all navigabilities to be bi-directional by default.
                        # Also, connectedTo is a symmetric property but the listed connectedWith properties
                        # are expressed one way. Consequently, the navigability the other way round is
                        # expressed below:
                        opposite = opposite_port(g, port)
                        if opposite:
                            g.add((other_port, RSM_TOPOLOGY.navigableTo, opposite))
                            navigabilities_count += 1
        elif case == 0:  # dead-end
            pass

    print(f"    {navigabilities_count} navigabilities were set")

    # Output
    if output_ttl:
        g.serialize(destination=output_ttl, format='turtle')
    else:
        print(g.serialize(format='turtle'))
