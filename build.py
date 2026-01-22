import os
from pathlib import Path

# Configuración de rutas
BASE_DIR = Path(r'C:\Degnis Music')
SOURCE_DIR = BASE_DIR / 'Degnis Jazz'
OUTPUT_DIR = BASE_DIR / 'dist'
OUTPUT_DIR.mkdir(exist_ok=True)

# Lista de tus temas
tracks = [
    "01 Alborada.wav", "02 Denisse.wav", "03 Desirée.wav",
    "04 Victoria.wav", "05 Valentina.wav", "06 Valeria.wav",
    "07 Alejandra.wav", "08 Cristina.wav", "09 Elianne.wav", "10 Suzie Q.wav"
]

html_template = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Degnis Jazz | Gold Edition</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@900&family=Oswald:wght@300;700&display=swap" rel="stylesheet">
    <style>
        body {{ 
            background: #000;
            color: #fff; 
            font-family: 'Oswald', sans-serif; 
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        /* HERO MAXIMIZADO AL 100% */
        .hero {{
            position: relative;
            width: 100%;
            height: 100vh; 
            display: flex;
            justify-content: center;
            align-items: center;
            background: #000;
        }}

        img.cover {{ 
            height: 100%; 
            width: auto;
            max-width: 100%;
            object-fit: contain;
            -webkit-box-reflect: below 2px linear-gradient(transparent, rgba(0,0,0,0.3));
        }}

        /* TÍTULO DEGNIS JAZZ - FORZADO AMARILLO ORO */
        h1 {{ 
            font-family: 'Playfair Display', serif;
            font-weight: 900;
            font-size: 2.2rem; 
            text-transform: uppercase;
            color: #f1c40f !important; /* Amarillo Oro Jazz Club */
            position: absolute;
            bottom: 2%; 
            z-index: 10;
            margin: 0;
            text-shadow: 0 0 15px rgba(241, 196, 15, 0.6), 0 0 25px rgba(0,0,0,1);
            letter-spacing: 6px;
        }}

        /* LISTA DE PISTAS */
        .list {{ 
            width: 90%; 
            max-width: 850px;
            margin: 120px auto 100px auto; 
        }}

        .track {{ 
            background: rgba(241, 196, 15, 0.02); 
            margin-bottom: 5px; 
            padding: 15px 30px; 
            display: flex; 
            align-items: center; 
            justify-content: space-between; 
            border-bottom: 1px solid #332b00;
            transition: 0.3s;
        }}
        
        .track:hover {{
            background: rgba(241, 196, 15, 0.1);
            border-bottom: 1px solid #f1c40f;
        }}

        /* NOMBRES DE PISTAS - FORZADO AMARILLO ORO */
        .track-name {{ 
            font-size: 1.1rem; 
            color: #f1c40f !important; /* Amarillo Oro Jazz Club */
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 2px;
            text-shadow: 0 0 5px rgba(241, 196, 15, 0.3);
        }}

        /* REPRODUCTOR */
        audio {{ 
            filter: invert(1) brightness(1.2) sepia(1) saturate(3) hue-rotate(10deg); 
            width: 250px; 
            opacity: 0.6;
        }}
    </style>
</head>
<body>
    <div class="hero">
        <img src="../Degnis Jazz/cover.jpg" class="cover">
        <h1>Degnis Jazz</h1>
    </div>

    <div class="list">
"""

for t in tracks:
    html_template += f"""
            <div class="track">
                <span class="track-name">{t.replace('.wav', '')}</span>
                <audio controls src="../Degnis Jazz/{t}"></audio>
            </div>"""

html_template += """
    </div>
</body>
</html>
"""

with open(OUTPUT_DIR / 'index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("--- CATÁLOGO ACTUALIZADO: TODO EN AMARILLO ORO ---")