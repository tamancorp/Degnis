import os
from pathlib import Path

# Configuración de rutas
BASE_DIR = Path(r'C:\Degnis Music')
SOURCE_DIR = BASE_DIR / 'Degnis Jazz'
OUTPUT_FILE = BASE_DIR / 'index.html'

# Lista de pistas
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
        body {{ background: #0b0b0b; color: #fff; font-family: 'Oswald', sans-serif; margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; }}
        
        /* Contenedor de imagen y título */
        .hero {{ position: relative; width: 100%; max-width: 800px; margin-top: 20px; line-height: 0; }}
        img.cover {{ width: 100%; height: auto; border-radius: 4px 4px 0 0; }}
        
        /* Banda Oro con letras Negras al borde */
        .gold-bar {{ 
            background: #f1c40f; 
            width: 100%; 
            padding: 20px 0; 
            text-align: center; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        h1 {{ 
            font-family: 'Playfair Display', serif; 
            font-weight: 900; 
            font-size: 1.8rem; 
            text-transform: uppercase; 
            color: #000 !important; /* Letras Negras */
            margin: 0; 
            letter-spacing: 5px; 
        }}
        
        .section-title {{ color: #f1c40f; font-family: 'Playfair Display', serif; font-size: 1.5rem; text-align: center; margin-top: 60px; letter-spacing: 3px; text-transform: uppercase; }}
        
        .list {{ width: 90%; max-width: 800px; margin: 30px auto; }}
        .track {{ background: rgba(255, 255, 255, 0.03); margin-bottom: 2px; padding: 12px 25px; display: flex; align-items: center; justify-content: space-between; border-left: 3px solid #f1c40f; }}
        .track-name {{ font-size: 1rem; color: #eee; text-transform: uppercase; font-weight: 300; letter-spacing: 1px; }}
        
        audio {{ filter: invert(1) grayscale(1) brightness(1.5); width: 220px; }}
        
        .footer {{ width: 100%; max-width: 800px; text-align: center; margin: 80px 0; padding: 40px 0; border-top: 1px solid #222; }}
        .bio {{ font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.1rem; color: #888; margin-bottom: 25px; }}
        .contact-btn {{ display: inline-block; padding: 12px 30px; border: 1px solid #f1c40f; color: #f1c40f; text-decoration: none; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem; transition: 0.3s; }}
        .contact-btn:hover {{ background: #f1c40f; color: #000; }}
    </style>
</head>
<body>
    <div class="hero">
        <img src="Degnis Jazz/cover.jpg" class="cover">
        <div class="gold-bar">
            <h1>Degnis Jazz | Gold Edition</h1>
        </div>
    </div>

    <h2 class="section-title">Repertorio Seleccionado</h2>
    <div class="list">
"""

for t in tracks:
    html_template += f"""
            <div class="track">
                <span class="track-name">{t.replace('.wav', '')}</span>
                <audio controls src="Degnis Jazz/{t}"></audio>
            </div>"""

html_template += """
    </div>

    <div class="footer">
        <div class="bio">
            "Explorando las texturas del Jazz con una visión cinematográfica."
        </div>
        <a href="mailto:degnis@gmail.com" class="contact-btn">Solicitar Licencia / Contacto</a>
    </div>
</body>
</html>
"""

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(html_template)

print("--- REINICIO DE ESTILO COMPLETADO ---")