import math

class Warning:
    
    def __init__(self):
        pass
    
    def in_wearable(self, data):
        if data['wearable']['blood_pressure'] > 110 or data['wearable']['temperature'] > 37.5 or data['wearable']['heart_rate'] > 110:
            return True
        else:
            return False

    def in_accelerometer(self, data):
        if math.sqrt(pow(data['accelerometer']['Xaxis'], 2) + 
                    pow(data['accelerometer']['Yaxis'], 2) +
                    pow(data['accelerometer']['Zaxis'], 2)) < 50:
            return True
        else:
            return False
    
    def in_timer(self, data):
        if data['timer']['medicine_time'] == 1:
            return True
        else:
            return False

    def select_warning_monitor(self, data):
        if self.in_wearable(data):
            print("ADVERTENCIA!!!")
            print("Signos vitales anormales.")
            print(f"[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']}")
            print(f"ssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}")
            print()
        if self.in_accelerometer(data):
            print("ADVERTENCIA!!!")
            print("Se detectó una caída.")
            print(f"[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']} y acelerómetro {data['accelerometer']['id']}")
            print()
        if self.in_timer(data):
            print("ADVERTENCIA!!!")
            print("Hora de administrar un medicamento.")
            print(f"[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']}")
            print(f"Medicamento: {data['timer']['medicine']} - Dosis: {data['timer']['dose']}")
            print()
    
    def select_warning_notifier(self, data):
        messages = [None, None, None]
        if self.in_wearable(data):
            messages[0] = f"ADVERTENCIA!!!\nSignos vitales anormales.\n[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']}\nssn: {data['ssn']}, edad: {data['age']}, temperatura: {round(data['wearable']['temperature'], 1)}, ritmo cardiaco: {data['wearable']['heart_rate']}, presión arterial: {data['wearable']['blood_pressure']}" 
        if self.in_accelerometer(data):
            messages[1] = f"ADVERTENCIA!!!\nSe detectó una caída.\n[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']} y acelerómetro {data['accelerometer']['id']}"
        if self.in_timer(data):
            messages[2] = f"ADVERTENCIA!!!\nHora de administrar un medicamento.\n[{data['wearable']['date']}]: asistir al paciente {data['name']} {data['last_name']}... con wearable {data['wearable']['id']}\nMedicamento: {data['timer']['medicine']} - Dosis: {data['timer']['dose']}"
        return messages