##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: main.py
# Capitulo: Estilo Publica-Suscribe
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Este archivo define el punto de ejecución del Publicador
#
#-------------------------------------------------------------------------
import random, time
from src.patient import Patient
from src.helpers.publicador import publish

if __name__ == '__main__':
    print("Iniciando simulación del sistema SMAM...")
    older_patients = []
    total_patients = random.randint(1, 5)
    print(f"actualmente hay {total_patients} adultos mayores...")
    for _ in range(total_patients):
        older_patients.append(Patient())
    print("comenzando monitoreo...")
    print()
    for _ in range(20):
        timer_time = random.choice([4, 8])
        medicine = random.choice(['Paracetamol', 'Dipirona magnésica', 'Dipirona hioscina', 'Tramadol', 'Antidepresivo', 'Aspirina', 'Antiarritmico', 'Diuretico'])

        for patient in older_patients:
            print("Extrayendo datos del adulto mayor...")
            patient.check_devices()
            print("Analizando datos del adulto mayor...")

            if (timer_time % patient.timer.time == 0) and patient.timer.medicine==medicine:
                patient.timer.medicine_time = 1

            print("Notificando eventos detectados...")
            publish('monitor', patient.to_json())
            publish('notifier', patient.to_json())

            if patient.wearable.blood_pressure > 110 or patient.wearable.temperature > 37.5 or patient.wearable.heart_rate > 110:
                print("Actualizando expediente...")
                publish('record', patient.to_json())
            print()

            time.sleep(1)
