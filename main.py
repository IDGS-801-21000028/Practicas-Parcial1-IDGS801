from flask import Flask, render_template, request

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






if __name__ == "__main__":
  app.run(debug=True)