

class ITest(object):
    '''
    '''
    def test(self):
        pass
    

class ITestExtend(ITest):
    def test(self):
        pass


abc = ITest()
if isinstance(abc, ITestExtend):
    print('aaa')
else:
    print('bbb')