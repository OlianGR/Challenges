import xml.etree.ElementTree as xml
import os
import json


data ={

    "name": "Angel Garcia",
    "age": 26,
    "birth_date": "04-03-1997",
    "languages": [
        "Phyton", 
        "Kotilin", 
        "Swift"]
    }

xml_file = "angeldev.xml"

# Xml

def save_xml ():

   root = xml.Element("data")

   for key,value in data.items():
        child = xml.SubElement(root,key)
        if isinstance(value,list):
            for item in value:
                xml.SubElement(child,"item").text = item
        else:
            child.text = str(value)

   tree = xml.ElementTree(root)
   tree.write(xml_file)

save_xml()

with open(xml_file,"r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON

json_file = "mouredev.json"

def save_json ():
    with open (json_file,"w")as json_data:
        json.dump(data,json_data )

save_json()

with open(json_file,"r") as json_data:
    print(json_data.read())

os.remove(json_file)

save_xml()
save_json()

class Data:
    def __init__(self,name,age,birth_date,languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languages = languages

with open (xml_file,"r") as xml_data:
    
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    languages = []
    for item in root.find("languages"):
        languages.append(item.text)

    xml_class = Data(name,age,birth_date,languages)
    print(xml_class.__dict__)

with open (json_file,"r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["languages"])

    print(json_class.__dict__)

os.remove(json_file)
os.remove(xml_file)

