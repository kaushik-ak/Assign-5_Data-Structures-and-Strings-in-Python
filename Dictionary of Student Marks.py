d = {}
r = int(input("Enter No. of records to Add :- "))
for i in range(r):
    name = input("Enter the name of the student :- ")
    marks = float(input("Enter the marks of the student :- "))
    d[name] = marks

print("\n*** To find the record of the student. ***\n")

m = input("Enter the name of the student :- ")
if m in d:
    print(m,"'s marks:",d[m])

else:
    print("Student Not Found.")