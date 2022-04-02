##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: timer.py
# Capitulo: Estilo Publica-Suscribe
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define el publicador que enviará mensajes hacia el distribuidor de mensajes
#
#   A continuación se describen los métodos que se implementaron en esta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |       __init__()       |  - self: definición de   |  - constructor de la  |
#           |                        |    la instancia de la    |    clase              |
#           |                        |    clase                 |                       |
#           +------------------------+--------------------------+-----------------------+
#           |          run()         |  - self: definición de   |  - simula la          |
#           |                        |    la instancia de la    |    alarma que         |
#           |                        |    clase                 |    determina el       |
#           |                        |                          |    momento en el que  |
#           |                        |                          |    se debe            |
#           |                        |                          |    administrar algún  |
#           |                        |                          |    medicamento a los  | 
#           |                        |                          |    adultos mayores    |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from faker import Faker
import random

class Timer:

    def __init__(self):
        fake = Faker()
        self.id = fake.numerify(text="%%######")

    def run(self):
        self.time = random.choice([4, 8])
        self.dose = random.choice(['10 mg','20 ml'])
        self.medicine = random.choice(['Paracetamol', 'Dipirona magnésica', 'Dipirona hioscina', 'Tramadol', 'Antidepresivo', 'Aspirina', 'Antiarritmico', 'Diuretico'])
        self.medicine_time = 0