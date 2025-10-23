// Limpiar la base de datos
MATCH (n) DETACH DELETE n;

// --- CREACIÓN DE NODOS Y RELACIONES ---

CREATE
  // Estudiantes
  (e1:Estudiante {id: 1, nombre: "Carlos Pérez", perfil: "Analítico", semestre: 4, intereses: ["IA", "Programación"]}),
  (e2:Estudiante {id: 2, nombre: "Laura Gómez", perfil: "Creativa", semestre: 3, intereses: ["Diseño", "Bases de Datos"]}),

  // Cursos
  (c1:Curso {id: 101, nombre: "Programación I", area: "Informática", nivel: "Básico", creditos: 3}),
  (c2:Curso {id: 102, nombre: "Programación II", area: "Informática", nivel: "Intermedio", creditos: 3}),
  (c3:Curso {id: 103, nombre: "Bases de Datos", area: "Informática", nivel: "Intermedio", creditos: 4}),
  (c4:Curso {id: 104, nombre: "Inteligencia Artificial", area: "IA", nivel: "Avanzado", creditos: 3}),

  // Docentes
  (d1:Docente {id: 201, nombre: "Dr. Rodríguez", especialidad: "Programación"}),
  (d2:Docente {id: 202, nombre: "Mtra. López", especialidad: "IA"}),

  // Áreas temáticas
  (a1:AreaTematica {id: 301, nombre: "Informática"}),
  (a2:AreaTematica {id: 302, nombre: "Inteligencia Artificial"}),

  // Semestres
  (s1:Semestre {id: 401, numero: 3}),
  (s2:Semestre {id: 402, numero: 4}),

  // --- RELACIONES ---
  (e1)-[:HA_TOMADO]->(c1),
  (e1)-[:LE_INTERESA]->(c4),
  (e2)-[:HA_TOMADO]->(c3),

  (d1)-[:IMPARTE]->(c1),
  (d1)-[:IMPARTE]->(c2),
  (d2)-[:IMPARTE]->(c4),

  (c1)-[:PERTENECE_A]->(a1),
  (c2)-[:PERTENECE_A]->(a1),
  (c3)-[:PERTENECE_A]->(a1),
  (c4)-[:PERTENECE_A]->(a2),

  (c1)-[:ES_REQUISITO_DE]->(c2),
  (c2)-[:COMPLEMENTA]->(c3),
  (c3)-[:ES_REQUISITO_DE]->(c4),

  (e1)-[:PERTENECE_A]->(s2),
  (e2)-[:PERTENECE_A]->(s1),
  (c1)-[:ES_PARTE_DE]->(s1),
  (c2)-[:ES_PARTE_DE]->(s2),
  (c3)-[:ES_PARTE_DE]->(s1),
  (c4)-[:ES_PARTE_DE]->(s2);
