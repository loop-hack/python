#using int datatype for calculating sum

x= input("What's x? ")
y= input("What's y? ")
z = int(x)+int(y)
print(z)


#using nested function for code simplification

x = int(input("What's x? "))
y = int(input("What's y? "))
print(x+y)


#dealing in float variable

x = float(input("What's x? "))
y = float(input("What's y? "))
print(x+y)


#using round() function for rounding decimal to like 1 or 3 or any places

#if we want integeral round then no need to mention places u want to round to

x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x+y)
print(z)


#formatting output number with comma eg: 1256459 into 1,256,459

x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(f"{z:,}")


#printing output upto 2 or lets say 3 places of decimal

x = float(input("What's x? "))
y = float(input("What's y? "))

        #Method 1
z = round(x / y, 2)
print(z)

        #Method 2
z = x/y
print(f"{z:.2f}")
