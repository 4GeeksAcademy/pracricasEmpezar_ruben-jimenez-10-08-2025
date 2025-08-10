# pracricasEmpezar_ruben-jimenez-10-08-2025

1.Configuración del backend (Flask)
Crear un entorno virtual y activarlo:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate
Instalar Flask y CORS:

bash
Copiar
Editar
pip install flask flask-cors
Estructura de carpetas:

css
Copiar
Editar
src/
  ├── models/
  └── routes/
Crear app.py:

python
Copiar
Editar
from flask import Flask
from flask_cors import CORS
from src.routes.animal_routes import animal_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(animal_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")


2.Configuración del frontend (Vite)
Crear el proyecto:

bash
Copiar
Editar
npm create vite@latest frontend
Si pide nombre del paquete, puedes dejar el predeterminado o usar frontend.

Entrar en la carpeta, instalar dependencias y levantar el servidor:

bash
Copiar
Editar
cd frontend
npm install
npm run dev
