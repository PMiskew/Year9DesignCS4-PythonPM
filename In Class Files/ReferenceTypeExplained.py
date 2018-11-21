#A reference type is a variable where we store the reference to where
#the variable is stored in the computer, not the value

def doThis(a):
	a = a + 1


def doThat(a):
	a = a + 1
	return a

def doSomething(nums):
	nums[0] = 999

value = 1 	#This is a pimative type int.  All programming languages deal
			#with primative types the same way. 
print("Before Function: ",value)
doThis(value)
print("After Function: ",value)
print("********************")
#Value does change because it is a primative type. W e are making a dulplicate
#that we pass to the function.  The only way for that change to carray
#over is to pass the value back
value1 = 1
print("Before Function: ",value1)
value1 = doThat(value1)
print("After Function: ",value1)


list = [1,2,3]
list2 = list
print(list)
list[0] = 100
print(list2)
print("Before Function: ",list)
doSomething(list)
print("After Function: ",list)

