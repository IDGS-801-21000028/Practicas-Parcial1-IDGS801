from wtforms import Form
from wtforms import FloatField, IntegerField

class PuntosForm(Form):
  p1_x = FloatField("PUNTO 1 (X)")  
  p1_y = FloatField("PUNTO 1 (Y)")
  p2_x = FloatField("PUNTO 2 (X)")
  p2_y = FloatField("PUNTO 2 (Y)")