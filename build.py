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
        body {{ background: #000; color: #fff; font-family: 'Oswald', sans-serif; margin: 0; padding: 0; display: flex; flex-direction: column; align-items: center; }}
        .hero {{ position: relative; width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; background: #000; overflow: hidden; }}
        img.cover {{ height: 100%; width: auto; max-width: 100%; object-fit: contain; -webkit-box-reflect: below 2px linear-gradient(transparent, rgba(0,0,0,0.3)); }}
        h1 {{ font-family: 'Playfair Display', serif; font-weight: 900; font-size: 2.2rem; text-transform: uppercase; color: #f1c40f !important; position: absolute; bottom: 5%; z-index: 10; margin: 0; text-shadow: 0 0 15px rgba(241, 196, 15, 0.6); letter-spacing: 6px; }}
        
        .section-title {{ color: #f1c40f; font-family: 'Playfair Display', serif; font-size: 1.8rem; text-align: center; margin-top: 80px; letter-spacing: 4px; text-transform: uppercase; border-bottom: 1px solid #332b00; padding-bottom: 10px; width: 80%; }}
        
        .list {{ width: 90%; max-width: 850px; margin: 40px auto; }}
        .track {{ background: rgba(241, 196, 15, 0.02); margin-bottom: 5px; padding: 15px 30px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #332b00; transition: 0.3s; }}
        .track:hover {{ background: rgba(241, 196, 15, 0.1); border-bottom: 1px solid #f1c40f; }}
        .track-name {{ font-size: 1.1rem; color: #f1c40f !important; text-transform: uppercase; font-weight: 700; letter-spacing: 2px; }}
        
        audio {{ filter: invert(1) brightness(1.2) sepia(1) saturate(3) hue-rotate(10deg); width: 250px; opacity: 0.6; }}
        
        .footer {{ width: 80%; max-width: 850px; text-align: center; margin: 100px 0 100px 0; padding: 40px; border: 1px solid #332b00; background: rgba(241, 196, 15, 0.01); }}
        .bio {{ font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.2rem; color: #ccc; line-height: 1.8; margin-bottom: 30px; }}
        .contact-btn {{ display: inline-block; padding: 15px 40px; border: 1px solid #f1c40f; color: #f1c40f; text-decoration: none; text-transform: uppercase; letter-spacing: 3px; font-weight: 700; transition: 0.3s; }}
        .contact-btn:hover {{ background: #f1c40f; color: #000; box-shadow: 0 0 20px rgba(241, 196, 15, 0.4); }}
    </style>
</head>
<body>
    <div class="hero">
        <img src="Degnis Jazz/cover.jpg" class="cover">
        <h1>Degnis Jazz | Gold Edition</h1>
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
            "Explorando las texturas del Jazz con una visión cinematográfica. <br> 
            Composiciones diseñadas para narrar historias a través del sonido."
        </div>
        <a href="mailto:degnis@gmail.com" class="contact-btn">Solicitar Licencia / Contacto</a>
    </div>
</body>
</html>
"""

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(html_template)

print("--- CATÁLOGO CINEMATOGRÁFICO COMPLETO ---")