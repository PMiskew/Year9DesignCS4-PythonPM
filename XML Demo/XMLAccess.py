import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
print(root.tag)

for child in root:
	print(child.tag, child.attrib)

print("*******")
print(root[0][1].text)