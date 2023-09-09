def multiply(*nums):
    pro=1
    #nums of tuple that contains
    #all the elements passed as
    #arguments
    for i in nums:
        pro *=i
    return pro
# function calls with arbitary number of arguments
print(multiply(10,20))
print(multiply(10,20,30))
print(multiply(10,20,30,40))
print(multiply(10,20,30,40,50))
print(multiply(10,20,30,40,50,60))
