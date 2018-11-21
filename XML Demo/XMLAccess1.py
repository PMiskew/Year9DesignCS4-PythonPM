#Not Recommended
from xml.dom import minidom
xmldoc = minidom.parse('data1.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value)