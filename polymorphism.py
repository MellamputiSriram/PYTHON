class Document:
    def add(self):
        print(30 + 9)
 
class Pdf(Document):
    def add(self):
        print(10 + 10)
 
class Word(Document):
    def add(self):
        print(5 + 5)

ins = Word()
ins1 = Pdf()
#ins.add()
ins1.add()