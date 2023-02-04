a = int(input("a: "))
b = int(input("b: "))

def add():
  return a+b; 
def sub():
  return a-b; 
def mul():
  return a*b; 
def div():
  return a//b; 
def mod():
  return a%b ;

print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.mod")

n = int(input("Enter the number: "))

if(n==1):
 print("The sum of a and b are: ", add())
elif(n==2):
 sub()
 print("The sub of a and b are: ",sub())
elif(n == 3):
 print("The mul of a and b are: ", mul())
elif(n == 4):
 print("The div of a and b are:",div())
else:
 print("the mod of a and b are: ",mod())

