import xml.etree.ElementTree as ET
from xml.dom import minidom
from Nodes.linkedListP import LinkedListPrincipal


class Write:
    def __init__(self, route):
        self.route = route

    def write_document(self, data: LinkedListPrincipal):
        senalesReducidas = ET.Element("senalesReducidas")

        data.create_elements_XML(ET, senalesReducidas)

        xmlstr = minidom.parseString(ET.tostring(senalesReducidas)).toprettyxml(
            indent="   "
        )
        with open(self.route, "w", encoding="utf-8") as f:
            f.write(xmlstr)
