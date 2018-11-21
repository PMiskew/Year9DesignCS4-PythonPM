import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
print(tree)
ET.dump(a)
root.append(a)
tree.write("outputbe.xml")