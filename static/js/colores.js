const colores = {
  'Negro': '#000000',
  'Cafe': '#8B4513',
  'Rojo': '#FF0000',
  'Naranja': '#FFA500',
  'Amarillo': '#FFFF00',
  'Verde': '#008000',
  'Azul': '#0000FF',
  'Violeta': '#8A2BE2',
  'Gris': '#808080',
  'Blanco': '#FFFFFF'
};

const tolorencia = {
  'Dorado 5': '#FFD700',
  'Plata 10': '#C0C0C0'
};

function asignarColor(tdId) {
  const td = document.getElementById(tdId);

  if (tdId == "tlrR") {
    const codigoColor = td.getAttribute('data-color');
    color = tolorencia[codigoColor];
  } else {
    const codigoColor = td.getAttribute('data-color');
    color = colores[codigoColor];
  }

  if (color) {
    td.style.backgroundColor = color;
  }
}

asignarColor('c1');
asignarColor('c2');
asignarColor('c3');
asignarColor('tlrR');