#use xml.sax parse dblp.xml. Give each author an ID and put them in a file.
#find collaboration relations of all authors and output them to a file. One relation's format is like (id1,id2)

import xml.sax
class authorHandler(xml.sax.ContentHandler):   #extract all authors
	def __init__(self):
		self.CurrentData=""     #tag's name
		self.dict={}   #save all authors. The key is an author's name, the value is his id
		self.name=""   #the name of an author
		self.id=0      #the ID of an author
	def startElement(self, tag, attributes):   
		self.CurrentData = tag

	def endElement(self, tag):
		if self.CurrentData == 'author':    #this tag is author, save it in the dict
			exist = self.dict.get(self.name, -1)    
			if exist == -1:     #if this author have not been added into dict
				self.dict[self.name] = self.id
				self.id = self.id + 1

	def characters(self, content):
		if self.CurrentData == 'author':
			self.name = content


class collabrationHandler(xml.sax.ContentHandler):    #extract all collaboration relations
	def __init__(self, dict, file):
		self.CurrentData=""     #tag's name
		self.dict = dict   #the dict which is received ago
		self.name=""   #the name of an author
		self.id=0      #the ID of an author
		self.paper=False   #if the tag is article or inproceeding, paper = True
		self.author=[]  #all authors' id in one <article> or <inproceeding>
		self.file = file   #Output collaboration relation to file
		self.edge = set()   #Edge's set
	def startElement(self, tag, attributes):   
		self.CurrentData = tag
		if tag == 'article' or tag == 'inproceeding':
			self.author.clear()   #start processing a new paper, old collaboration neen to be deleted
			self.paper = True

	def endElement(self, tag):
		if (tag == 'article' or tag == 'inproceeding') and self.paper == True:   #One paper's tag close
			self.paper = False
			for i in self.author:
				for j in self.author:
					if i < j and (i,j) not in self.edge:    #edge
						self.file.write(str(i) + ' ' + str(j) + '\n')
						self.edge.add((i,j))

	def characters(self, content):
		if self.paper == True:
			self.name = content
			isAuthor = self.dict.get(self.name, -1)   # isAuthor == -1 means that this content is not an author's name
			if isAuthor != -1:
				self.author.append(self.dict[self.name])    #add this author's id 

#set xml parser
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler1 = authorHandler()
parser.setContentHandler(handler1)
parser.parse('E:\\dataset\\dblp.xml')

with open('author.txt','w') as f:
	for k,v in handler1.dict.items():
		f.write(str(v))
		f.write(' '+k)
		f.write('\n')
f.close()


with open('collaboration.txt', 'w') as f:
	handler2 = collabrationHandler(handler1.dict, f)
	parser.setContentHandler(handler2)
	parser.parse('E:\\dataset\\dblp.xml')
f.close()