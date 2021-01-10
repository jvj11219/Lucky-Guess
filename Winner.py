def func3(arg10, arg11):
    var12 = func6()
    var13 = func9()
    var20 = var16(var12, arg11)
    var21 = (((624315164 | ((var20 ^ arg11 ^ var20) - 686083137)) & arg10 + var12 | var12) | var20 - 1101563577 + var20) & var20 & (arg10 ^ arg10) - var12
    var22 = 680554825 - ((var21 & arg10 | (var21 ^ var21 | ((716 + (arg11 - var21)) + (var12 + 917) + (var12 + (arg11 + ((var20 ^ arg11) + var12 & (arg10 | -2002340024))))) - -871 + var20) | -62) & 592676654 ^ var13)
    var23 = ((var21 | -318 + var12) ^ var21) ^ ((594 | var22 - arg11) & -585) ^ arg10 | 948334812
    result = (-810 + (-37169037 & 828508715 ^ ((var13 ^ var23) & var20 & var13))) - var20 | (((var13 ^ var22) + arg11) - var21)
    return result
def func12(arg17, arg18):
    var19 = (arg17 ^ ((((217 - -1884922024) - arg17) ^ -389731531 & -1541394698) - -1784737643) - arg18) - arg17 - arg18 & 1388105870 ^ -165 - arg17
    result = arg18 + arg18
    return result
def func11():
    closure = [-5]
    def func10(arg14, arg15):
        closure[0] += func12(arg14, arg15)
        return closure[0]
    func = func10
    return func
var16 = func11()
def func9():
    func7()
    result = len(xrange(12))
    func8()
    return result
def func8():
    global len
    del len
def func7():
    global len
    len = lambda x : 9
def func6():
    func4()
    result = len(xrange(28))
    func5()
    return result
def func5():
    global len
    del len
def func4():
    global len
    len = lambda x : -5
def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var8 = (414721233 ^ -1562590882 | -261735761) - (-409 + arg1 & (931 ^ ((-865729118 + arg1) + arg1) + arg2) | (arg1 + -938 & arg1) ^ ((195 + ((arg2 - arg2 | arg2 - arg2) - arg1)) ^ arg1) ^ 867717750 | arg1)
    var9 = 663 | arg1
    result = var9 - (var7 + (var8 | var9))
    return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in (var5 + arg3 for i in xrange(48)):
        var5 += (var5 + var6) & var6
    return var5
if __name__ == "__main__":
    print 'prog_size: 2'
    print 'func_number: 3'
    print 'arg_number: 10'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 24'
    for i in xrange(25000):
        x = 5
        x = func3(x, i)
        print x,
