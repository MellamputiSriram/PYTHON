class One():
    def __init__(self, c):
        self.c = c
    name = 'kumar'
    
    def add(self, a, b):
        print('sum is:', a + b + self.c)

ins = One(34)

print(ins.name)
ins.add(20, 30)