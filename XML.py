# Here we are goint to use XML in python
# First we need to import a new package and we are going to save it as ET to save us time
import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        07762588969
    </phone>
    <email hide="yes"/>
</person>'''

# now we pass our string into a new object. This could have a sintax error
tree = ET.fromstring(data)
# We are going to look data stored in our XML
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

# another example with two simple element
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Giuseppe</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Gennaro</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
list = stuff.findall('users/user')
print('User count:', len(list))
for item in list:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get('x'))
