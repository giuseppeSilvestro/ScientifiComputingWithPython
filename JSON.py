# Here we are going to use Python to process JSON
# The data are similar to the one used in XML.py, so you see the difference
# between XML and JSON
# First we import the package
import json

# Now the data to be processed later on
# Notice that "phone" is an object with another object inside
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

# The next line will parse the data and return a dictionary, because if you've noticed
# in line 9 we used {} to store our data
info = json.loads(data)
# Because info is a dictionary we can use the standard sintax of Python instead of
# .find() or .get() like we did in XML.py
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print("Phone:", info["phone"]["number"])

# now another example but this time json.loads() will return the data as a list
input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    },
    { "id" : "009",
      "x" : "2",
      "name" : "Chuck"
    }
]'''

info = json.loads(input)
print("User count:", len(info))
for item in info:
    print("Name: ", item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])
