import math # Para función sqrt()

class MathDojo:
	def __init__(self):
		self.result = 0
	def add(self, num, *nums):
		self.result += num
		for n in nums:
			self.result += n 
		return self
	def subtract(self, num, *nums):
		self.result -= num
		for n in nums:
			self.result -= n 
		return self

	# Método de promedio para agilizar el cálculo de desviación estandar
	def prom(self, num, *nums):
		self.result += num
		contador = 0
		for n in nums:
			self.result += n
			contador += 1
		#print(self.result, contador+1)
		self.result = self.result/(contador+1)
		return self

	def desvest(self, num, *nums):
		promedio = self.prom(num,*nums).result # No entra al resultado de la función sin agregar .result
		self.result = 0 # Se vuelve a iniciar self.result, porque el resultado anterior es el 
						#promedio y empieza las operaciones desde este número
		contador = 0
		self.result += (num - promedio)**2 # Se realiza la primera operación con el primer número para entrar a *nums
		for n in nums:
			self.result += (n - promedio)**2
			contador += 1
		self.result = math.sqrt(self.result/(contador))
		return self

# crear una instruccion:
md = MathDojo()
# para probar:
q = md.add(2).add(2,5,1).subtract(3,2).result
print(q)	# debe imprimir 5

# Escriba el método add y pruébelo llamándolo 3 veces, con diferentes 
# números de argumentos cada vez
# 1
met1=MathDojo()
x = met1.add(-2,-4,7,-1).result
print("x =",x)
# 2
met2=MathDojo()
y = met1.add(1,2,3,4,5,6,7,8,9,10).add(-10,-9,-8,-7,-6,-5).result
print("y =",y)
# 3
met3=MathDojo()
z = met3.add(3,4,2,6).add(3,2).result
print("z =",z)

# Escriba el método de subtract y pruébelo llamándolo 3 veces, con diferentes 
# números de argumentos cada vez
# 1
met4=MathDojo()
x1 = met4.subtract(-10,2,2,1).result # 0 - (-10) - 2 - 2 - 1 = 5 
print("x1 =",x1)
# 2
met5=MathDojo()
y1 = met5.subtract(1,2,3,4,5,6,7,8,9,10).subtract(-10,-9,-8,-7,-6,-5).result
print("y1 =",y1)
# 3
met6=MathDojo()
z1 = met6.subtract(-100).subtract(30,20).subtract(-30,-20).result
print("z1 =",z1)
# Se agrgan 3 pruebas de promedio
met7 = MathDojo()
x2 = met7.prom(2,4,8,10).result 
print("x2 (promedio) =",x2)
met8 = MathDojo()
y2 = met8.prom(3,6,9,12).result 
print("y2 (promedio) =",y2)
met9 = MathDojo()
z2 = met9.prom(12,6,7,15,3,10,18,5).result 
print("z2 (promedio) =",z2)
# Para posteriormente calcular la desviación estándar de cada una
met10= MathDojo()
x3 = met10.desvest(12,6,7,15,3,10,18,5).result 
print("x3 (desvest) =",x3)
met11= MathDojo()
y3 = met11.desvest(2,4,8,10).result 
print("y3 (desvest) =",y3)
met12 = MathDojo()
z3 = met12.desvest(3,6,9,12).result  #12,6,7,15,3,10,18,5
print("z3 (desvest) =",z3)