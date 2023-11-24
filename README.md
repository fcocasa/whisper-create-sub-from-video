# Generador Automático de Subtítulos en Español 🎥📝

Este repositorio aloja un script escrito en Python que utiliza la biblioteca Whisper de OpenAI para generar automáticamente subtítulos en español a partir de videos. Aborda la escasez de herramientas en español para esta tarea, permitiéndote generar un archivo de audio (mp3) y subtítulos (srt) con un simple paso.

## Características Principales:

### Fácil de Usar
Con solo ejecutar el script video_srt.py se abre una ventana del sistema para elegir el video, el sistema procesa el video, generando un archivo de audio y subtítulos en la misma carpeta original del video y con el mismo nombre que el video original.
#### Ejemplo: 
* Video -> C:/Users/user/Downloads/capa de transporte.mp4
* Audio -> C:/Users/user/Downloads/capa de transporte.mp3
* Subs -> C:/Users/user/Downloads/capa de transporte.srt

### Tecnología
Utiliza el modelo "small" de la biblioteca Whisper de OpenAI, proporcionando resultados similares al modelo "medium" pero con una considerable mejora en velocidad y peso.

## Tecnologías Utilizadas
* Lenguaje de Programación -> Python
* Biblioteca Principal -> Whisper (https://github.com/openai/whisper)

## Instrucciones de Uso
### Instalar Dependencias
    pip install -r requirements.txt
### Ejecutar el Script
    python video_srt.py

## Capturas de Pantalla
![image](https://github.com/fcocasa/whisper-create-sub-from-video/assets/44985620/ad10b3bd-078d-4419-b2a7-8e8686acd354)

## Estado del Proyecto

En desarrollo activo. ¡Tu ayuda y retroalimentación son bienvenidas y fundamentales para hacer de este proyecto una solución aún mejor!
