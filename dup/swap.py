a=(input("Enter the first Name:"))
b=(input("Enter the second Name:"))
a=a+b
b=a[0:(len(a)-len(b))]
a=a[len(b)]
print("a is:",a)
print("b is:",b)
