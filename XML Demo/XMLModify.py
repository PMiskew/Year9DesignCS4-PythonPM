import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()

for rank in root.iter('rank'):
	new_rank = int(rank.text) + 1
	rank.text = str(new_rank)
	rank.set('updatedm', 'yes')

tree.write('output1.xml')