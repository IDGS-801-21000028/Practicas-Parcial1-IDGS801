from wtforms import Form
from wtforms import FloatField, RadioField, StringField, SelectField, SubmitField
from wtforms import validators

class PuntosForm(Form):
  p1_x = FloatField("PUNTO 1 (X)")  
  p1_y = FloatField("PUNTO 1 (Y)")
  p2_x = FloatField("PUNTO 2 (X)")
  p2_y = FloatField("PUNTO 2 (Y)")
  
class Resistencia(Form):          
  cl1 = SelectField("Color 1", choices=[('0','Negro'),('1','Cafe'),('2','Rojo'),('3','Naranja'),('4','Amarillo'),('5','Verde'),('6','Azul'),('7','Violeta'),('8','Gris'),('9','Blanco')])
  cl2 = SelectField("Color 2", choices=[('0','Negro'),('1','Cafe'),('2','Rojo'),('3','Naranja'),('4','Amarillo'),('5','Verde'),('6','Azul'),('7','Violeta'),('8','Gris'),('9','Blanco')])
  cl3 = SelectField("Color 3", choices=[('1','Negro'),('10','Cafe'),('100','Rojo'),('1000','Naranja'),('10000','Amarillo'),('100000','Verde'),('1000000','Azul'),('10000000','Violeta'),('100000000','Gris'),('1000000000','Blanco')])
  tlr = RadioField("Tolerancia", choices=[(1,"Oro"),(2,"Plata")])
    
class Palabras(Form):
  pl1 = StringField("Inglés",[
    validators.DataRequired(message="El campo es requerido.")
  ])
  pl2 = StringField("Español",[
    validators.DataRequired(message="El campo es requerido.")
  ])
  op = RadioField("Selecciona una opcion",choices=[("Inglés"),("Español")], validators=[
    validators.DataRequired(message="Selecciona una opción.")    
  ],validate_choice=False)
  bs = StringField("Buscar",[
    validators.DataRequired(message="El campo es requerido.")
  ])