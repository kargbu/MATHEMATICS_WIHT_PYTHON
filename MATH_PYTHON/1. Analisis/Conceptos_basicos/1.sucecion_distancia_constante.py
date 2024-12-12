import numpy as np
import matplotlib.pyplot as plt

'''
Una sucesión a_n es un listado de términos que se comportan de una determinada manera. Por ejemplo,
a_n = 1/n^2. Nos interesa el comportamiento de la sucesión cuando los términos son infinitos. El
comportamiento de los términos infinitos no es materialmente posible pero Python nos sirve para 
manifestar el comportamiento de la sucesión lo suficientemente grande para saber cómo se comporta.
¿Qué usasmos?, ¿listas o arreglos?
'''

# Una sucesión que tienen espaciados de igual distancia cada uno de sus términos se utiliza:
# np.linspace(primer elemento, último elemento, cuántos elementos)

a_n =np.linspace(1, 5, 100)
print(a_n)

