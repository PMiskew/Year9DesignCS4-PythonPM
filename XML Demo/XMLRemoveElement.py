import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()

for country in root.findall('country'):
	rank = int(country.find('rank').text)
	if rank > 50:
		root.remove(country)


tree.write('outputr.xml')