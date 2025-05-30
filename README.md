# Scraper de Comentarios de YouTube – Proyecto Final Econometría II

Este proyecto forma parte del trabajo final del curso Econometría II. Extrae comentarios de los videos más recientes del canal de YouTube de Claudia Sheinbaum usando la API de YouTube Data v3.

##  Objetivo

Recolectar comentarios de videos de las "mañaneras" de Claudia Sheinbaum para analizarlos posteriormente con herramientas econométricas o de análisis de texto.

## Estructura del Proyecto
### Estructura del Proyecto

```
claudia-mananeras-comments/
├── README.md
├── .gitignore
├── .env          # No se incluye en GitHub
├── requirements.txt
├── code/
│   └── scrape_comments.py
└── data/
    └── dataset.csv  # Dataset final con comentarios
```


## Instrucciones

1. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate

## instala dependencias 
pip install -r requirements.txt


## crea un archivo .env donde coloques 

API_KEY=tu_clave

## ejecuta el codigo 

python code/scrape_comments.py

## Información del dataset
comment_id: ID único del comentario

text: contenido del comentario

video_id: ID del video de YouTube

video_title: Título del video fuente


