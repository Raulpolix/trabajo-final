# Simulador de Carrera con Condiciones Climáticas Variables

Este es un simulador de carrera simple que utiliza datos de vuelta y simula la posición de los pilotos en cada vuelta. La simulación también incorpora condiciones climáticas variables que pueden afectar el rendimiento de los pilotos. La interfaz de usuario permite ajustar la probabilidad de cambio climático y visualizar la simulación en tiempo real.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python antes de ejecutar el código:

- pandas
- numpy
- matplotlib
- PySimpleGUI

Puedes instalar estas bibliotecas utilizando el siguiente comando:

pip install pandas numpy matplotlib PySimpleGUI

# Cómo usar el simulador

Ejecuta el código proporcionado en un entorno de Python.
Ajusta la probabilidad de cambio climático utilizando la barra en la interfaz.
Haz clic en el botón "Simular" para iniciar la simulación.
Observa la simulación en tiempo real de la carrera con las condiciones climáticas variables.(Lluvia, frio, soleado, etc)
Puedes salir de la aplicación en cualquier momento haciendo clic en el botón "Salir" o cerrando la ventana.


## Detalles del código

#El código consta de tres funciones principales:

simular_carrera(datos_carrera, condiciones_climaticas): Esta función simula la carrera utilizando datos de vuelta y condiciones climáticas variables.
visualizar_simulacion(datos_carrera): Esta función visualiza la simulación de la carrera, mostrando la posición de cada piloto en cada vuelta.
crear_interfaz(datos_carrera): Esta función crea una interfaz de usuario simple utilizando PySimpleGUI, permitiendo ajustar la probabilidad de cambio climático y realizar la simulación.
Los datos de ejemplo proporcionados son un marco de datos de Pandas que representa el número de vueltas de la carrera. Puedes personalizar estos datos para adaptar la simulación a tus necesidades.

¡Disfruta simulando carreras!
