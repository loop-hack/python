# defining a function

"""def add_numbers(a, b):
      sum = a + b
      return sum

result= add_numbers(5,3)
print(result)
"""

#defining main to help us write any function in any order
#giving function some parameter also defining its default value

"""def main():
      name= input("What's your name? ")
      hello()
      hello(name)
      
def hello(to="World"):
      print("Hello,",to)

main()
"""

#using return while defining a function

def main():
      x = int(input("What's x? "))
      print("x square is",square(x))

def square(n):
      return n*n
#or we can do 

""" return n**2 """

""" ** means we want power and next number says how much"""

#or we can do 

""" return pow(n,2) """
      
""" pow(n,2) it is python library which is used for squaring a number"""

main()