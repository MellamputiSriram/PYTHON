
class Parent(object):
    __name = 'sriram'
    def __altered(self):
        print "PARENT altered()"

c = Parent()

print c._altered()





class Parent(object):
    def altered():
        print "altered()"


c = Parent()

c.altered()