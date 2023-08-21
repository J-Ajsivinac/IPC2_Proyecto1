import xml.etree.ElementTree as ET
from xml.dom import minidom
from Matrix.likedListReduce import LinkedListReduce


class Write:
    def __init__(self, route):
        self.route = route

    def write_document(self, data: LinkedListReduce):
        senalesReducidas = ET.Element("senalesReducidas")

        xmlstr = minidom.parseString(ET.tostring(senalesReducidas)).toprettyxml(
            indent="   "
        )
        with open(self.route, "w", encoding="utf-8") as f:
            f.write(xmlstr)
