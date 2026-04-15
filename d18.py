from math import radians, cos, sin, tan
angulo = float(input('Digite o ângulo que deseja consultar: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan (radians(angulo))

print(f""" 
    Seno de {angulo} é {seno:.2f}
    Cosseno de {angulo} é {cosseno:.2f}
    Tangente de {angulo} é {tangente:.2f}
    """)