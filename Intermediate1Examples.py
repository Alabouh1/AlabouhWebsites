variable1 = 5
while variable1 > 0:
  variable1 = variable1 - 1

for i in range(variable1):
  print(i)
  variable1 = variable1 - 1

array = ["1", "2", "3"]

array1 = array[0]
array2 = array[1]

array[0] = array1
array[1] = array2


def Subroutine(userInput, newValue):
  newValue = userInput + 1
  return newValue