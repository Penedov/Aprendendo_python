#Introdução a Python, Dia 02
#É possivel atribuir valor a múltiplas variáveis na mesma linha

#primeira utilização de mdulos
import random

print(random.randrange(1, 10))

a, b, c = "banana", "uva", "abacate"
print(a, b, c)

# Uma variável pode ter o mesmo valor de outra usando o '=' ao invés de ","

x = y = z = "orange"
print(x)
print(y)
print(z)

# Obtendo o tipo de dado de uma variavél

print(type(x+y+z))

# nesse escopo o "x" é uma variavél global ou seja não está conjunta a nenhuma função, por isso pode ser requisitada em todo o codigo
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

