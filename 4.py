import xml.etree.ElementTree as ET
tree = ET. parse('currency.xml')
root = tree.getroot()
allNames = []
allValues = []
for Name in root.iter('Name'):
    allNames.append(Name.text)
for Value in root.iter('Value'):
    allValues.append(Value.text)

print (allNames)
print (allValues)

