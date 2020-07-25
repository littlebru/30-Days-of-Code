def printPair(charList, sizeOfList):
  for i in range(0, sizeOfList):
    print(charList[i], end="")

def oddEven(text): 
  odd = [] 
  even = []
  for j in range(0,len(text)):
    
    if (j % 2) == 0:
      odd.append(text[j])
    else:
      even.append(text[j])
    
  printPair(odd, len(odd))
  print(" ", end="")
  printPair(even, len(even))
  print()
      
      
qtdText = int(input())

for i in range(0,qtdText):
  text = input()
  
  oddEven(text)
