# Graph Recommendation DB

Este proyecto implementa un sistema de recomendación basado en grafos utilizando **Neo4j** como base de datos y **Python (FastAPI)** como backend.

---

## ⚙️ 1. Clonación del repositorio

```bash
git clone https://github.com/NicolasT08/Graph-recommendation-DB.git
cd Graph-recommendation-DB
```

---

## 🐳 2. Levantar el contenedor de Neo4j

Ejecuta el siguiente comando para construir y levantar el contenedor:

```bash
docker-compose up -d
```

---

## 🐍 3. Crear y activar el entorno virtual

En una nueva terminal, crea el entorno virtual y actívalo:

```bash
python3 -m venv venv
source venv/bin/activate
```

> 💡 En Windows:
> ```bash
> venv\Scripts\activate
> ```

---

## 📦 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## 🔗 5. Verificar la conexión a Neo4j

Ejecuta el script de conexión para comprobar que la base de datos está activa:

```bash
python3 src/connection.py
```

**Salida esperada:**

```
Connected to Neo4j database successfully.
```

---

## 🧠 6. Ejecutar el sistema de recomendación

Para levantar la API (desarrollada en **FastAPI**), ejecuta directamente desde la raíz del proyecto:

```bash
uvicorn src.recommendationapi:app --reload
```

Esto iniciará el servidor local en el puerto **8000**.

---

## 🧩 10. Estructura del proyecto

```
Graph-recommendation-DB/
│
├── docker-compose.yml
├── .gitignore
├── requirements.txt
├── README.md
│
├── neo4j/
│   ├── import/
│   ├── neo4j/
│   ├── init.cypher
│   └── init.sh
│
└── src/
    ├── connection.py
    ├── recommendation_service.py
    ├── run_recommendation.py
    ├── recommendationapi.py
    └── student_service.py
```

---

**Autores:**  
Jose Luis Salamanca Lopez  
Nicolás Samuel Tinjacá Topia  
Dumar Hernan Malpica  
Daniel Mauricio Vargas Cely

Proyecto académico — *Universidad Pedagógica y Tecnológica de Colombia (UPTC)*
