class One:
    def add(self):
        print(' One add is ')
     
    def sub(self):
        print('One sub is')

class Two():
    def add(self):
        print(' Two add is ')

class Three(Two, One):
    def add(self):
        print(' Three add is')
        inst = One()
        inst.add()
        #super(Three, self).sub()

ins = Three()

ins.add()

