from flask import Flask, render_template, request

from forms import *
from math import sqrt
from io import open

app = Flask(__name__)

# Obtener una pagina desde otra carpeta (Templates)
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/operaciones")
def opera():
  return render_template("OperaBas.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado():
  if request.method == "POST":
    num1 = request.form.get("n1")
    num2 = request.form.get("n2")
    
    opera = request.form.get("op")
    
    print(opera)
    
    if opera == "suma":
      return "<h2 style='font-family: sans-serif'>La suma de {} + {} = {} </h2>".format(num1, num2, str(int(num1) + int(num2)))
    elif opera == "resta":
      return "<h2 style='font-family: sans-serif'>La resta de {} - {} = {} </h2>".format(num1, num2, str(int(num1) - int(num2)))
    elif opera == "divi":
      return "<h2 style='font-family: sans-serif'>La división de {} / {} = {} </h2>".format(num1, num2, str(int(num1) / int(num2)))
    elif opera == "multi":
      return "<h2 style='font-family: sans-serif'>La multiplicación de {} * {} = {} </h2>".format(num1, num2, str(int(num1) * int(num2)))

@app.route("/puntos", methods=["GET","POST"])
def puntos():
  datos = PuntosForm(request.form)
  puntos = {'p1_x': 0.0, 'p1_y': 0.0, 'p2_x': 0.0, 'p2_y': 0.0, 'resu': 0.0}
  
  if request.method == "POST":
    puntos['p1_x'] = datos.p1_x.data
    puntos['p1_y'] = datos.p1_y.data
    puntos['p2_x'] = datos.p2_x.data
    puntos['p2_y'] = datos.p2_y.data
    
    puntos['resu'] = round(sqrt(((puntos['p2_x']-puntos['p1_x'])**2)+((puntos['p2_y']-puntos['p1_y'])**2)),2)          
  
  return render_template("distanciaPuntos.html", form=datos, data=puntos)

@app.route("/resistencia", methods=["GET","POST"])
def resistencia():
  datos = Resistencia(request.form) 
  res = {'c1':'','c2':'','c3':'','tlr':0,'valor':0.0,'vMax':0.0,'vMin':0.}
  
  if request.method == "POST":
    
    porcentaje = 0
    res['c1'] = datos.cl1.data
    res['c2'] = datos.cl2.data
    res['c3'] = datos.cl3.data
    res['tlr'] = datos.tlr.data
    
    res['valor'] = float(res['c1'] + res['c2']) * float(res['c3'])
    
    if res['tlr'] == '1':          
      porcentaje = res['valor'] * .05
    else:
      porcentaje = res['valor'] * .1

    res['vMax'] = res['valor'] + porcentaje
    res['vMin'] = res['valor'] - porcentaje
    
    for clave, valor in datos.cl1.choices:
      if clave == res['c1']:
        res['c1'] = valor
        
      if clave == res['c2']:
        res['c2'] = valor
        
    for clave, valor in datos.cl3.choices:
      if clave == res['c3']:
        res['c3'] = valor
        
    if res['tlr'] == '1':
      res['tlr'] = 'Dorado 5'
    else:
      res['tlr'] = 'Plata 10'         
  return render_template("resistencias.html", form=datos, data=res)

@app.route("/palabras", methods=["GET","POST"])
def palabras():
  rqst = request.form
  plbr = Palabras(rqst) 
  res = {'palabra':'','ukn':''}   
      
  if request.method == "POST":      
    if 'Registrar' in rqst.get('btn'):    
      plbr.op.validators = []
      plbr.bs.validators = []
      if plbr.validate():
        arch = open("palabras.txt",'a')
        arch.write(f"{plbr.pl1.data.upper().strip()},{plbr.pl2.data.upper().strip()}\n")
        arch.close()
        plbr.pl1.data = ''
        plbr.pl2.data = ''
    elif 'Buscar' in rqst.get('btn'):   
      plbr.pl1.validators = []
      plbr.pl2.validators = []
      if plbr.validate():    
        arch = open("palabras.txt",'r')      
        for ln in arch.readlines():
          palabras = ln.strip().split(",")
          plb_Buscar = plbr.bs.data.upper().strip()  
          opcion_Buscar = plbr.op.data
          if opcion_Buscar == "Inglés" and palabras[0] == plb_Buscar:
            res['palabra'] = palabras[1]
            res['ukn'] = ""
          elif opcion_Buscar == "Español" and palabras[1] == plb_Buscar:
            res['palabra'] = palabras[0]     
            res['ukn'] = ""
          else:
            res['ukn'] = "Palabra no encontrada"
        arch.close()                        
  
  return render_template("archivos.html", form=plbr, res=res)


if __name__ == "__main__":
  app.run(debug=True)