print("Hello")

def menu():
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print('4. divide')

  print() 

  userpick = input("which  one you want")

  if userpick == "1":
    x=int(input('first number'))
    y=int(input('2nd number'))
    z=x+y
    print(z)
    menu()

  if userpick == '2':
    x=int(input('first number'))
    y=int(input('2nd number'))
    z=x-y
    print(z)
    menu()

  if userpick == '3':
    x=int(input('first number'))
    y=int(input('2nd number'))
    z=x*y
    print(z)
    menu()

  if userpick == '4':
    x=int(input('first number'))
    y=int(input('2nd number'))
    z=x/y
    print(z)
    menu()

  return

menu()


