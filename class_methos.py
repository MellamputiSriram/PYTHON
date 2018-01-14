class Parent(object):
    @classmethod
    def altered(self):
        print "PARENT altered()"




c = Parent()

c.altered()