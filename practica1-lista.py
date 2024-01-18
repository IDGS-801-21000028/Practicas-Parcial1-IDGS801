class Lista:
  
  lista = []
  numeros_pares = []
  numeros_impares = []
  
  def __init__(self,list):
    self.lista = list
    
  def ordenar(self):
    self.lista.sort()    
    print(f"La lista ordenada es: {self.lista}")
    
  def pares(self):
    for num in self.lista:
      if num % 2 == 0: self.numeros_pares.append(num)
    print(f"Números pares en la lista: {self.numeros_pares}")
  
  def impares(self):
    for num in self.lista:
      if num % 2 != 0: self.numeros_impares.append(num)
    print(f"Números impares en la lista: {self.numeros_impares}")
    
  def repetidos(self):  
    cant = 0
    repetidos = []
    for num in self.lista:
      cant = self.lista.count(num)
      if cant > 1 and num not in repetidos:
        repetidos.append(num)
        print(f"El número {num} se repite: {cant}")

def main():  
  
  listaIngresar = []
  cant = int(input("Dame la cantidad de números a ingresa (enteros): "))    
  
  for i in range(cant):
    listaIngresar.append(int(input(f"Ingresa el número {i+1}: ")))
    
  obj = Lista(listaIngresar)
  
  print("-"*10)
  obj.ordenar()
  obj.pares()
  obj.impares()
  obj.repetidos()
  print("-"*10)
  
if __name__ == "__main__":
  main()