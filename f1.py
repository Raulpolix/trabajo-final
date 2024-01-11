import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

def simular_carrera(datos_carrera, condiciones_climaticas):
    posiciones_iniciales = np.random.permutation(range(1, len(datos_carrera) + 1))
    
    for vuelta in datos_carrera['Vuelta']:
        # Simular cambios climáticos (solo como ejemplo, ajusta según tus necesidades)
        if np.random.rand() < condiciones_climaticas['probabilidad_cambio']:
            # Realizar ajustes en la simulación según las condiciones climáticas
            # (por ejemplo, afectar la velocidad de los autos, cambios en la visibilidad, etc.)
            pass

        posiciones_iniciales = np.random.permutation(posiciones_iniciales)

        # Agregar las posiciones calculadas a los datos de la carrera
        datos_carrera[f'Posiciones_Vuelta_{vuelta}'] = posiciones_iniciales

    return datos_carrera

def visualizar_simulacion(datos_carrera):
    plt.figure(figsize=(10, 6))

    for vuelta in datos_carrera['Vuelta']:
        plt.plot(datos_carrera[f'Posiciones_Vuelta_{vuelta}'], label=f'Piloto {vuelta}')

    plt.title('Simulación de Carrera con Condiciones Climáticas Variables')
    plt.xlabel('vuelta')
    plt.ylabel('posicion')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def crear_interfaz(datos_carrera):
    sg.theme('DarkBlue3')

    layout = [
        [sg.Text('Probabilidad de cambio climático: '), sg.Slider(range=(0, 1), default_value=0.2, resolution=0.01, orientation='h', key='probabilidad_cambio')],
        [sg.Button('Simular'), sg.Button('Salir')],
    ]

    window = sg.Window('Simulador de Carrera sin Elección de Pit Stops', layout, resizable=True, finalize=True, element_justification='c')

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Salir'):
            break
        elif event == 'Simular':
            condiciones_climaticas = {'probabilidad_cambio': values['probabilidad_cambio']}
            datos_simulados = simular_carrera(datos_carrera.copy(), condiciones_climaticas)
            visualizar_simulacion(datos_simulados)
    
    window.close()

# Datos de ejemplo para la simulación
datos_carrera = pd.DataFrame({
    'Vuelta': range(1, 11),  # Ajustado para una simulación más rápida
})

# Crear la interfaz de usuario y realizar la simulación
crear_interfaz(datos_carrera)
