class Arthamatic():
    name = 'sriram'     # Class name
    def __init__(self, a, b):
        self.num1 = a     # instance variable unique to each instanc
        self.num2 = b
        self.num3 = 30   

    def add(self, x, y):
        print ' First addition is ::', x + y

    def sub(self):
       print ' Substruction is ::', self.num1 - self.num2
       #print ' Call a class name ', Arthamatic.name      #   Calling a class name


class Operations(object):

      def __init__(self, a , b):
          self.num3 = 99

      def dev(self):
          print ' dev is :' , 11 % 5

      def add(self, x, y):
          print ' Second addition is ::', x + y

class C(Operations, Arthamatic):

      def __init__(self, a , b):
          self.num3 = 99

      def dev(self):
          print ' dev is :' , 11 % 5

          super(C, self).add(34,34)

      def add(self, x, y):

          print ' Third addition is ::', x + y

inst = C(23,27)

inst.dev()
 


