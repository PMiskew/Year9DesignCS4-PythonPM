import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()


for child in root:
	print(child.tag, child.attrib)
#Access all childs with "country"
#returns array of elements 
c = tree.findall("country")

print(c[0][1].text)

print("*******")
element = root.find('Panama')
if element is None:
    print("element not found")
else:
	print(element)
print("*******")
print(root[0][1].text)
