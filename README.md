#Graph Recommendation DB

Este proyecto implementa un sistema de recomendación basado en grafos utilizando Neo4j como base de datos y Python (FastAPI) como backend.


⚙️ 1. Clonación del repositorio
git clone https://github.com/NicolasT08/Graph-recommendation-DB.git
cd Graph-recommendation-DB

🐳 2. Levantar el contenedor de Neo4j

Ejecuta el siguiente comando para construir y levantar el contenedor:

docker-compose up -d


Esto iniciará un contenedor de Neo4j 5.26 expuesto en los puertos:

7474 → Interfaz web

7687 → Conexión Bolt (usada por Python)

🐍 3. Crear y activar el entorno virtual

En una nueva terminal, crea el entorno virtual y actívalo:

python3 -m venv venv
source venv/bin/activate


(En Windows: venv\Scripts\activate)

📦 4. Instalar las dependencias
pip install -r requirements.txt

🔗 5. Verificar la conexión a Neo4j

Ejecuta el script de conexión para comprobar que la base de datos está activa:

python3 src/connection.py


Salida esperada:

Connected to Neo4j database successfully.

🧠 6. Ejecutar el sistema de recomendación

Corre el servicio principal:

python3 src/run_recommendation.py

Deberías ver nuevamente:

Connected to Neo4j database successfully.

🌐 7. Acceder a la interfaz de Neo4j

Abre tu navegador en:

👉 http://localhost:7474/browser/

🔑 8. Ingresar las credenciales de acceso
Usuario	Contraseña
Esto te permitirá acceder al panel de Neo4j y visualizar los nodos y relaciones creados.

⚡ 9. Ejecutar la API de recomendación

Para levantar la API (desarrollada en FastAPI), ingresa a la carpeta src y ejecuta:

cd src
uvicorn recommendationapi:app --reload --port 8000

Una vez corriendo, podrás acceder a:

http://localhost:8000
 → Inicio de la API

http://localhost:8000/docs
 → Documentación interactiva (Swagger UI)