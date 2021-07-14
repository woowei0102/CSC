class BaseClass(Object):
    def __init__(self, value):
        self.value = value
        print('Init BaseClass')
        print('value is :{0}'.format(self.value))

class TimesTwo(object):
    def __init__(self):
        self.value *=2
        print('Init TimesTwo')
        print('value is :{0}'.format(self.value))        
        
class PlusFive(object):
    def __init__(self):
        self.value +=5
        print('Init PlusFive')
        print('value is :{0}'.format(self.value))     
        
class SubClass(BaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        BaseClass.__init(self.value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)
        
subclass = SubClass(1)
print(subclass.value)