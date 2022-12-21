# Básico: imprime todos los números enteros del 0 al 150.

# for basico in range (0,151):
#     print(basico)

# Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

# for multiplosCinco in range (5,1001,5):
#     print(multiplosCinco)

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".

# for contarDojo in range (1,101):
#     if contarDojo % 10 == 0:
#         print("Coding Dojo")
#     elif contarDojo % 5 == 0:
#         print("Coding")
#     else:
#         print(contarDojo)

#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.

# sum = 0
# for whoa in range (0,500001):
#     if whoa % 2 != 0 :
#         sum = sum + whoa
# print(sum)

#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

# for regresiva in range (2018,0,-4):
#     print(regresiva)

#Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

# lowNum = 2 
# highNum = 9
# mult = 3

# for contador in range (lowNum,highNum+1):
#     if contador % mult == 0 :
#         print(contador)