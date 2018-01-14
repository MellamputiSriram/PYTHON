class One():
    @staticmethod
    def add():
        print('add is')
    name = 'sriram'
    @classmethod
    def sub(k):
        print('class methos', One.name)

#One.add()
#One.sub()
ins = One()
#ins.add()
ins.sub()