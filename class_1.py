class Arthamatic():
    name = 'sriram'     # Class name
    def __init__(self, a, b):
        self.num1 = a     # instance variable unique to each instanc
        self.num2 = b
        self.num3 = 30   

    def add(self, x, y):
        print ' addition is ::', x + y  + self.num3
        print ' Call a class name ', Arthamatic.name      #   Calling a class name
        #print 'self is :', self

    def sub(self):
       print ' Substruction is ::', self.num1 - self.num2
       print ' Call a class name ', Arthamatic.name      #   Calling a class name

inst = Arthamatic(15,8)
inst1 = Arthamatic(10,8)

print ' old class and new class difference :', inst,  '::: ', dir(Arthamatic)

#print 'inst is :', inst

inst.add(4,4)
inst1.add(5,5)

inst.sub()
inst1.sub()