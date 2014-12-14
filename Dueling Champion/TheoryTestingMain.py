from TheoryTesting import Test

def doTest():
    test7 = Test(2,2,2)
    return test7
test1 = Test()
print (test1)
test2 = Test("Apple")
print (test2)
test3 = Test("Apple","Blue")
print (test3)
test4 = Test(1,"Apple","Blue")
print (test4)
test5 = Test([1,2,3])
print (test5)
test6 = Test([1,2,3],"Blue Jay",["Banana"])
print (test6)

test7 = doTest()
print (test7)