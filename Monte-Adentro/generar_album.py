import os

# --- CONFIGURACIÓN DEL ÁLBUM ---
TITULO_ALBUM = Suite "Monte Adentro"
SUBTITULO = "Composición Cinemática de Degnis Romero"
SUBTITULO = "Atmósferas y Narrativas Sonoras"
COLOR_ACCENTO = "#ff9e7d"  # Un tono cálido que combine con el atardecer
ID_GTM = "GTM-MNK5FR7B"
IMAGEN_FONDO = "background.jpg" # Nombre de tu imagen

def generar_html():
    archivos_mp3 = [f for f in os.listdir('.') if f.endswith('.mp3')]
    archivos_mp3.sort()

    items_html = ""
    for pista in archivos_mp3:
        nombre_pista = pista.replace('.mp3', '').replace('_', ' ')
        items_html += f"""
        <div class="track">
            <p>{nombre_pista}</p>
            <audio controls>
                <source src="{pista}" type="audio/mpeg">
            </audio>
        </div>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
        new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        }})(window,document,'script','dataLayer','{ID_GTM}');</script>
        
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{TITULO_ALBUM}</title>
        <style>
            body {{
                background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{IMAGEN_FONDO}');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: white;
                font-family: 'Segoe UI', sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                padding: 40px 20px;
            }}
            h1 {{ font-size: 2.5em; letter-spacing: 5px; text-transform: uppercase; text-shadow: 2px 2px 10px rgba(0,0,0,0.8); }}
            h2 {{ color: {COLOR_ACCENTO}; font-weight: 300; margin-bottom: 40px; text-shadow: 1px 1px 5px rgba(0,0,0,0.8); }}
            .container {{ width: 100%; max-width: 700px; }}
            .track {{
                background: rgba(255, 255, 255, 0.1); /* Transparencia elegante */
                backdrop-filter: blur(8px); /* Efecto de cristal esmerilado */
                margin-bottom: 20px;
                padding: 25px;
                border-radius: 12px;
                border: 1px solid rgba(255,255,255,0.1);
                transition: 0.3s;
            }}
            .track:hover {{ background: rgba(255, 255, 255, 0.15); transform: translateY(-3px); }}
            .track p {{ margin: 0 0 15px 0; font-weight: bold; letter-spacing: 1px; }}
            audio {{ width: 100%; height: 35px; border-radius: 5px; filter: opacity(0.8); }}
            footer {{ margin-top: auto; padding-top: 40px; font-size: 0.8em; opacity: 0.6; }}
        </style>
    </head>
    <body>
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={ID_GTM}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
        
        <h1>{TITULO_ALBUM}</h1>
        <h2>{SUBTITULO}</h2>

        <div class="container">
            {items_html}
        </div>

        <footer>&copy; 2026 Degnis Romero | Proyecto Cinemático</footer>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("¡Web Cinemática generada con éxito!")

if __name__ == "__main__":
    generar_html()