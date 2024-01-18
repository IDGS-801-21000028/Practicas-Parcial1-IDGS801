class Piramide:
  num = 0
  
  def __init__(self,num):
    self.num = num
  
  def crearPiramide(self):
    for i in range(1, self.num + 1):
      print('*' * i)
    
def main():
  num = int(input("Dame un número: "))
  obj = Piramide(num)
  obj.crearPiramide()
  
if __name__ == "__main__":
  main()