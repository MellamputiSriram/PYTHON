class One():
    def __init__(self, a):
        self.a = a
    
    @staticmethod
    def add():
        print('sum is ')
    
    @classmethod
    def sub(cls):
        print('sub is:', dir(cls))
        cls.add()
ins = One(23)
#print(ins.name)
#ins.add()
ins.sub()
One.add()
#One.sub()

