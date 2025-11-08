// Limpiar la base de datos
MATCH (n) DETACH DELETE n;

// --- CREACIÓN DE NODOS Y RELACIONES ---

CREATE
  // Estudiantes
  (e1:Estudiante {id: 1, nombre: "Carlos Pérez", perfil: "Analítico", semestre: 4, intereses: ["IA", "Programación"]}),
  (e2:Estudiante {id: 2, nombre: "Laura Gómez", perfil: "Creativa", semestre: 3, intereses: ["Diseño", "Bases de Datos"]}),
  (e3:Estudiante {id: 3, nombre: "Miguel Torres", perfil: "Técnico", semestre: 6, intereses: ["Redes", "Bases de Datos"]}),
  (e4:Estudiante {id: 4, nombre: "Ana Valencia", perfil: "Emprendedora", semestre: 5, intereses: ["Gestión", "Mercadeo", "Costos"]}),
  (e5:Estudiante {id: 5, nombre: "Sofia Rojas", perfil: "Investigadora", semestre: 6, intereses: ["IA", "Algoritmos", "Software"]}),

  // Áreas temáticas
  (a1:AreaTematica {id: 301, nombre: "Informática"}),
  (a2:AreaTematica {id: 302, nombre: "Inteligencia Artificial"}),
  (a3:AreaTematica {id: 303, nombre: "Interdisciplinar"}),
  (a4:AreaTematica {id: 304, nombre: "General"}),
  (a5:AreaTematica {id: 305, nombre: "Disciplinar y Profundización"}),

  // Semestres
  (s1:Semestre {id: 401, numero: 1}),
  (s2:Semestre {id: 402, numero: 3}),
  (s3:Semestre {id: 403, numero: 4}),
  (s4:Semestre {id: 404, numero: 5}),
  (s5:Semestre {id: 405, numero: 6}),

  // Cursos originales (mantenidos para compatibilidad)
  (c1:Curso {id: 101, nombre: "Programación I", area: "Informática", nivel: "Básico", creditos: 3}),
  (c2:Curso {id: 102, nombre: "Programación II", area: "Informática", nivel: "Intermedio", creditos: 3}),
  (c3:Curso {id: 103, nombre: "Bases de Datos", area: "Informática", nivel: "Intermedio", creditos: 4}),
  (c4:Curso {id: 104, nombre: "Inteligencia Artificial", area: "IA", nivel: "Avanzado", creditos: 3}),

  // Cursos Ing. Sistemas - Semestre 1
  (c5:Curso {id: 8107550, nombre: "Algoritmos y Programación", area: "Interdisciplinar", nivel: "Básico", creditos: 4}),
  (c6:Curso {id: 8107351, nombre: "Cálculo I", area: "Interdisciplinar", nivel: "Básico", creditos: 4}),
  (c7:Curso {id: 8107349, nombre: "Cátedra Universidad y Entorno", area: "General", nivel: "Básico", creditos: 3}),
  (c8:Curso {id: 8107565, nombre: "Competencias Comunicativas", area: "General", nivel: "Básico", creditos: 4}),
  (c9:Curso {id: 8107533, nombre: "Socio Humanística I", area: "General", nivel: "Básico", creditos: 3}),

  // Cursos Ing. Sistemas - Semestre 5
  (c10:Curso {id: 8108259, nombre: "Bases de Datos I", area: "Disciplinar y Profundización", nivel: "Intermedio", creditos: 4}),
  (c11:Curso {id: 8108261, nombre: "Electrónica General", area: "Disciplinar y Profundización", nivel: "Intermedio", creditos: 4}),
  (c12:Curso {id: 8108258, nombre: "Ingeniería de Requisitos", area: "Disciplinar y Profundización", nivel: "Intermedio", creditos: 4}),
  (c13:Curso {id: 8108224, nombre: "Métodos Numéricos", area: "Interdisciplinar", nivel: "Intermedio", creditos: 3}),
  (c14:Curso {id: 8108260, nombre: "Teoría General de Sistemas", area: "Disciplinar y Profundización", nivel: "Intermedio", creditos: 3}),

  // Cursos Ing. Sistemas - Semestre 6
  (c15:Curso {id: 8108263, nombre: "Bases de Datos II", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 4}),
  (c16:Curso {id: 8108265, nombre: "Comunicaciones", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 4}),
  (c17:Curso {id: 8108262, nombre: "Ingeniería del Software I", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 4}),
  (c18:Curso {id: 8108266, nombre: "Investigación de Operaciones", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 4}),
  (c19:Curso {id: 8108264, nombre: "Matemáticas Discretas", area: "Disciplinar y Profundización", nivel: "Intermedio", creditos: 3}),

  // Cursos Adm. Empresas - Semestre 1
  (c20:Curso {id: 8107548, nombre: "Cálculo Diferencial", area: "Interdisciplinar", nivel: "Básico", creditos: 3}),
  (c21:Curso {id: 8107547, nombre: "Introducción a la Administración", area: "Disciplinar y Profundización", nivel: "Básico", creditos: 3}),
  (c22:Curso {id: 8107570, nombre: "Ética y Política", area: "General", nivel: "Básico", creditos: 4}),
  (c23:Curso {id: 8107684, nombre: "Fundamentos de Economía", area: "Interdisciplinar", nivel: "Básico", creditos: 3}),

  // Cursos Adm. Empresas - Semestre 3
  (c24:Curso {id: 8108142, nombre: "Administración de Costos", area: "Interdisciplinar", nivel: "Intermedio", creditos: 3}),
  (c25:Curso {id: 8108139, nombre: "Enfoques Modernos de Administración", area: "Disciplinar y Profundización", nivel: "Intermedio", creditos: 3}),
  (c26:Curso {id: 8108141, nombre: "Estadística Descriptiva", area: "Interdisciplinar", nivel: "Intermedio", creditos: 3}),
  (c27:Curso {id: 8108143, nombre: "Legislación Comercial", area: "Disciplinar y Profundización", nivel: "Intermedio", creditos: 3}),
  (c28:Curso {id: 8109140, nombre: "Macroeconomía", area: "Interdisciplinar", nivel: "Intermedio", creditos: 3}),
  (c29:Curso {id: 81075332, nombre: "Socio Humanística II", area: "General", nivel: "Intermedio", creditos: 3}),

  // Cursos Adm. Empresas - Semestre 5
  (c30:Curso {id: 8108155, nombre: "Administración Laboral", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 3}),
  (c31:Curso {id: 8108151, nombre: "Gestión Pública", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 3}),
  (c32:Curso {id: 8108153, nombre: "Investigación de Mercadeo", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 3}),
  (c33:Curso {id: 8108154, nombre: "Mercado de Capitales", area: "Interdisciplinar", nivel: "Avanzado", creditos: 3}),
  (c34:Curso {id: 8108150, nombre: "Organización", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 3}),
  (c35:Curso {id: 8108152, nombre: "Tributación", area: "Disciplinar y Profundización", nivel: "Avanzado", creditos: 3}),

  // Docentes
  (d1:Docente {id: 201, nombre: "Dr. Rodríguez", especialidad: "Programación"}),
  (d2:Docente {id: 202, nombre: "Mtra. López", especialidad: "IA"}),
  (d3:Docente {id: 203, nombre: "Ing. Martínez", especialidad: "Bases de Datos"}),
  (d4:Docente {id: 204, nombre: "Dr. Sánchez", especialidad: "Matemáticas"}),
  (d5:Docente {id: 205, nombre: "Mtra. García", especialidad: "Administración"}),
  (d6:Docente {id: 206, nombre: "Dr. Fernández", especialidad: "Economía"}),
  (d7:Docente {id: 207, nombre: "Ing. Vargas", especialidad: "Ingeniería de Software"}),

  // --- RELACIONES ESTUDIANTES-SEMESTRES ---
  (e1)-[:PERTENECE_A]->(s3),
  (e2)-[:PERTENECE_A]->(s2),
  (e3)-[:PERTENECE_A]->(s5),
  (e4)-[:PERTENECE_A]->(s4),
  (e5)-[:PERTENECE_A]->(s5),

  // --- RELACIONES ESTUDIANTES-CURSOS (HA_TOMADO) ---
  // Estudiante 1 (Carlos)
  (e1)-[:HA_TOMADO]->(c1),
  (e1)-[:HA_TOMADO]->(c5),
  (e1)-[:HA_TOMADO]->(c6),
  
  // Estudiante 2 (Laura)
  (e2)-[:HA_TOMADO]->(c3),
  (e2)-[:HA_TOMADO]->(c20),
  (e2)-[:HA_TOMADO]->(c21),
  
  // Estudiante 3 (Miguel - Sistemas Sem 6)
  (e3)-[:HA_TOMADO]->(c5),
  (e3)-[:HA_TOMADO]->(c6),
  (e3)-[:HA_TOMADO]->(c10),
  (e3)-[:HA_TOMADO]->(c12),
  
  // Estudiante 4 (Ana - Admon Sem 5)
  (e4)-[:HA_TOMADO]->(c21),
  (e4)-[:HA_TOMADO]->(c24),
  (e4)-[:HA_TOMADO]->(c25),
  
  // Estudiante 5 (Sofia - Sistemas Sem 6)
  (e5)-[:HA_TOMADO]->(c10),
  (e5)-[:HA_TOMADO]->(c13),
  (e5)-[:HA_TOMADO]->(c14),

  // --- RELACIONES ESTUDIANTES-CURSOS (LE_INTERESA) ---
  // Estudiante 1
  (e1)-[:LE_INTERESA]->(c4),
  (e1)-[:LE_INTERESA]->(c17),
  
  // Estudiante 2
  (e2)-[:LE_INTERESA]->(c3),
  (e2)-[:LE_INTERESA]->(c10),
  
  // Estudiante 3
  (e3)-[:LE_INTERESA]->(c15),
  (e3)-[:LE_INTERESA]->(c16),
  
  // Estudiante 4
  (e4)-[:LE_INTERESA]->(c31),
  (e4)-[:LE_INTERESA]->(c32),
  
  // Estudiante 5
  (e5)-[:LE_INTERESA]->(c4),
  (e5)-[:LE_INTERESA]->(c17),

  // --- RELACIONES CURSOS-SEMESTRES ---
  // Semestre 1
  (c5)-[:ES_PARTE_DE]->(s1),
  (c6)-[:ES_PARTE_DE]->(s1),
  (c7)-[:ES_PARTE_DE]->(s1),
  (c8)-[:ES_PARTE_DE]->(s1),
  (c9)-[:ES_PARTE_DE]->(s1),
  (c20)-[:ES_PARTE_DE]->(s1),
  (c21)-[:ES_PARTE_DE]->(s1),
  (c22)-[:ES_PARTE_DE]->(s1),
  (c23)-[:ES_PARTE_DE]->(s1),

  // Semestre 3
  (c1)-[:ES_PARTE_DE]->(s2),
  (c3)-[:ES_PARTE_DE]->(s2),
  (c24)-[:ES_PARTE_DE]->(s2),
  (c25)-[:ES_PARTE_DE]->(s2),
  (c26)-[:ES_PARTE_DE]->(s2),
  (c27)-[:ES_PARTE_DE]->(s2),
  (c28)-[:ES_PARTE_DE]->(s2),
  (c29)-[:ES_PARTE_DE]->(s2),

  // Semestre 4
  (c2)-[:ES_PARTE_DE]->(s3),
  (c4)-[:ES_PARTE_DE]->(s3),

  // Semestre 5
  (c10)-[:ES_PARTE_DE]->(s4),
  (c11)-[:ES_PARTE_DE]->(s4),
  (c12)-[:ES_PARTE_DE]->(s4),
  (c13)-[:ES_PARTE_DE]->(s4),
  (c14)-[:ES_PARTE_DE]->(s4),
  (c30)-[:ES_PARTE_DE]->(s4),
  (c31)-[:ES_PARTE_DE]->(s4),
  (c32)-[:ES_PARTE_DE]->(s4),
  (c33)-[:ES_PARTE_DE]->(s4),
  (c34)-[:ES_PARTE_DE]->(s4),
  (c35)-[:ES_PARTE_DE]->(s4),

  // Semestre 6
  (c15)-[:ES_PARTE_DE]->(s5),
  (c16)-[:ES_PARTE_DE]->(s5),
  (c17)-[:ES_PARTE_DE]->(s5),
  (c18)-[:ES_PARTE_DE]->(s5),
  (c19)-[:ES_PARTE_DE]->(s5),

  // --- RELACIONES CURSOS-ÁREAS TEMÁTICAS ---
  // Área Informática
  (c1)-[:PERTENECE_A]->(a1),
  (c2)-[:PERTENECE_A]->(a1),
  (c3)-[:PERTENECE_A]->(a1),

  // Área Inteligencia Artificial
  (c4)-[:PERTENECE_A]->(a2),

  // Área Interdisciplinar
  (c5)-[:PERTENECE_A]->(a3),
  (c6)-[:PERTENECE_A]->(a3),
  (c13)-[:PERTENECE_A]->(a3),
  (c20)-[:PERTENECE_A]->(a3),
  (c23)-[:PERTENECE_A]->(a3),
  (c24)-[:PERTENECE_A]->(a3),
  (c26)-[:PERTENECE_A]->(a3),
  (c28)-[:PERTENECE_A]->(a3),
  (c33)-[:PERTENECE_A]->(a3),

  // Área General
  (c7)-[:PERTENECE_A]->(a4),
  (c8)-[:PERTENECE_A]->(a4),
  (c9)-[:PERTENECE_A]->(a4),
  (c22)-[:PERTENECE_A]->(a4),
  (c29)-[:PERTENECE_A]->(a4),

  // Área Disciplinar y Profundización
  (c10)-[:PERTENECE_A]->(a5),
  (c11)-[:PERTENECE_A]->(a5),
  (c12)-[:PERTENECE_A]->(a5),
  (c14)-[:PERTENECE_A]->(a5),
  (c15)-[:PERTENECE_A]->(a5),
  (c16)-[:PERTENECE_A]->(a5),
  (c17)-[:PERTENECE_A]->(a5),
  (c18)-[:PERTENECE_A]->(a5),
  (c19)-[:PERTENECE_A]->(a5),
  (c21)-[:PERTENECE_A]->(a5),
  (c25)-[:PERTENECE_A]->(a5),
  (c27)-[:PERTENECE_A]->(a5),
  (c30)-[:PERTENECE_A]->(a5),
  (c31)-[:PERTENECE_A]->(a5),
  (c32)-[:PERTENECE_A]->(a5),
  (c34)-[:PERTENECE_A]->(a5),
  (c35)-[:PERTENECE_A]->(a5),

  // --- RELACIONES PREREQUISITOS (ES_REQUISITO_DE) ---
  // Prerequisitos originales
  (c1)-[:ES_REQUISITO_DE]->(c2),
  (c3)-[:ES_REQUISITO_DE]->(c4),
  
  // Prerequisitos nuevos - Sistemas
  (c5)-[:ES_REQUISITO_DE]->(c12),
  (c5)-[:ES_REQUISITO_DE]->(c17),
  (c6)-[:ES_REQUISITO_DE]->(c13),
  (c10)-[:ES_REQUISITO_DE]->(c15),
  (c12)-[:ES_REQUISITO_DE]->(c17),
  (c13)-[:ES_REQUISITO_DE]->(c18),
  
  // Prerequisitos - Administración
  (c21)-[:ES_REQUISITO_DE]->(c25),
  (c23)-[:ES_REQUISITO_DE]->(c28),
  (c24)-[:ES_REQUISITO_DE]->(c30),
  (c25)-[:ES_REQUISITO_DE]->(c34),
  (c26)-[:ES_REQUISITO_DE]->(c32),

  // --- RELACIONES COMPLEMENTARIAS (COMPLEMENTA) ---
  // Complementarios originales
  (c2)-[:COMPLEMENTA]->(c3),
  
  // Complementarios nuevos
  (c10)-[:COMPLEMENTA]->(c12),
  (c12)-[:COMPLEMENTA]->(c17),
  (c15)-[:COMPLEMENTA]->(c17),
  (c16)-[:COMPLEMENTA]->(c18),
  (c21)-[:COMPLEMENTA]->(c24),
  (c24)-[:COMPLEMENTA]->(c32),
  (c25)-[:COMPLEMENTA]->(c31),
  (c27)-[:COMPLEMENTA]->(c35),

  // --- RELACIONES DOCENTES-CURSOS ---
  // Docentes originales
  (d1)-[:IMPARTE]->(c1),
  (d1)-[:IMPARTE]->(c2),
  (d1)-[:IMPARTE]->(c5),
  (d2)-[:IMPARTE]->(c4),
  (d3)-[:IMPARTE]->(c3),
  (d3)-[:IMPARTE]->(c10),
  (d3)-[:IMPARTE]->(c15),
  (d4)-[:IMPARTE]->(c6),
  (d4)-[:IMPARTE]->(c13),
  (d4)-[:IMPARTE]->(c20),
  (d5)-[:IMPARTE]->(c21),
  (d5)-[:IMPARTE]->(c25),
  (d5)-[:IMPARTE]->(c30),
  (d5)-[:IMPARTE]->(c31),
  (d5)-[:IMPARTE]->(c34),
  (d6)-[:IMPARTE]->(c23),
  (d6)-[:IMPARTE]->(c28),
  (d6)-[:IMPARTE]->(c33),
  (d7)-[:IMPARTE]->(c12),
  (d7)-[:IMPARTE]->(c17);
