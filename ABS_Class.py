from abc import ABCMeta,abstractmethod
## For Abstract class we cann't create an object
class One(metaclass=ABCMeta):
    @abstractmethod  # It won't allow to create instance
    def add(self):
        print('okok')
        #raise NotImplementedError
#a=One()
#print(a)
## If you inheritence an abstaruact class you should impliment that all those methods which are abstract
class Two(One):
    def add(self):
        print('ok')
ins = Two()
ins.add()