# Creating a dictionary while getting data from the user
no_of_records=int(input())
data={}
for i in range(no_of_records):
    key=input()
    value=int(input())
    data[key]=value#inserting the record
print(data)
