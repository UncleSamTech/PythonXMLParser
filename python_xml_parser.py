import xml.dom.minidom
#the module used for parsing the xml file is imported
 
#This function is declared with three arguements namely the xml file to be parsed, the tag name and the attribute name and it does the magic
def generic_dom(xml_file,tag_name,attr_name):
	doc = xml.dom.minidom.parse(xml_file)
	tags = doc.getElementsByTagName(tag_name)
	for any_attr in  tags:
		attr = any_attr.getAttribute(attr_name)
		print(attr)
