temp = 1
while temp == 1:
   numero = int(input("inserisci un numero: "))
   for i in range(numero, -1, -1) :
    print(i)

   temp = int(input("Vuoi ripetere l'operazione? \n no [0] \n si [1]"))
   continue
   if temp == 1 :
      continue
   else:
      break
