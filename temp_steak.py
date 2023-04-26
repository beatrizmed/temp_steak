'''
Programa que dependendo da temperatura (ºC) do steak, irá retornar o ponto do cozimento em português. O usuário deverá fornecer a temperatura.

Temperaturas - cozimento
120ºF ou 48ºC - Selada
130ºF ou 54ºC - Ao ponto pra mal
140ºF ou 60ºC - Ao ponto
150ºF ou 65ºC - Ao ponto pra bem
160ºF ou 71ºC - Bem passada
'''

temp_cels = int(input('Informe qual a temperatura da carne? '))

if temp_cels < 48:
  print('Cozinhar por mais alguns minutos.')

elif temp_cels in range(48, 53):
  print('Selada')

elif temp_cels in range(54, 59):
  print('Ao ponto pra mal')

elif temp_cels in range(60, 64):
  print('Ao ponto')

elif temp_cels in range(65, 70):
  print('Ao ponto pra bem')

elif temp_cels >=71:
  print('Bem passada')