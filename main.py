from flask import Flask, render_template, request

from forms import PuntosForm
from math import sqrt

app = Flask(__name__)

# Obtener una pagina desde otra carpeta (Templates)
@app.route("/")
def index():
  return render_template("OperaBas.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado():
  if request.method == "POST":
    num1 = request.form.get("n1")
    num2 = request.form.get("n2")
    
    opera = request.form.get("op")
    
    if opera == "suma":
      return "La suma de {} + {} = {}".format(num1,num2,str(int(num1)+int(num2)))
    elif opera == "resta":
      return "La resta de {} - {} = {}".format(num1,num2,str(int(num1)-int(num2)))
    elif opera == "div":
      return "La división de {} / {} = {}".format(num1,num2,str(int(num1)/int(num2)))
    elif opera == "multi":
      return "La multiplicación de {} * {} = {}".format(num1,num2,str(int(num1)*int(num2)))


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

if __name__ == "__main__":
  app.run(debug=True)