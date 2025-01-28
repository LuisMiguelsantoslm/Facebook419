import os
import http.server
import socketserver
import subprocess

# Configuración del servidor
PORT = 8000  # Puerto del servidor local
HTML_FILE = "index.html"  # Archivo HTML que deseas servir

def start_server():
    """Inicia un servidor HTTP para servir el archivo HTML."""
    if not os.path.exists(HTML_FILE):
        print(f"❌ El archivo '{HTML_FILE}' no existe en el directorio actual.")
        print("🔍 Asegúrate de colocarlo en el mismo directorio que este script.")
        return

    # Cambiar al directorio del archivo HTML
    os.chdir(os.path.dirname(os.path.abspath(HTML_FILE)))

    # Configurar el servidor
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"✅ Servidor iniciado en el puerto {PORT}")
        print(f"🌐 Abre en tu navegador: http://localhost:{PORT}")
        print("🔗 Usa una herramienta como ngrok para hacerlo público.")
        print("Presiona Ctrl+C para detener el servidor.")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor detenido.")

def expose_with_ngrok():
    """Exponer el servidor local usando ngrok."""
    try:
        print("🌐 Iniciando ngrok...")
        subprocess.run(["ngrok", "http", str(PORT)])
    except FileNotFoundError:
        print("❌ ngrok no está instalado o no se encuentra en el PATH.")
        print("🔍 Instala ngrok con el siguiente comando: pkg install ngrok")
    except Exception as e:
        print(f"⚠️ Ocurrió un error al ejecutar ngrok: {e}")

def main():
    """Menú principal para seleccionar acciones."""
    while True:
        print("\n=== Menú ===")
        print("https://github.com/LuisMiguelsantoslm")
        print("1. Iniciar servidor local")
        print("2. Exponer servidor con ngrok")
        print("3. Salir")
        
        choice = input("Selecciona una opción: ").strip()

        if choice == "1":
            start_server()
        elif choice == "2":
            expose_with_ngrok()
        elif choice == "3":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
