#!/bin/bash
set -e

echo "🚀 Iniciando Neo4j..."
/startup/docker-entrypoint.sh neo4j &

echo "⏳ Esperando que Neo4j esté completamente listo..."

# Espera hasta que Bolt esté disponible
until cypher-shell -a bolt://localhost:7687 -u neo4j -p neo4j1234 "RETURN 1;" >/dev/null 2>&1; do
  echo "⌛ Aún no responde..."
  sleep 5
done

echo "🧠 Ejecutando script de inicialización en la base 'neo4j'..."
cypher-shell -u neo4j -p neo4j1234 -d neo4j -f /var/lib/neo4j/import/init.cypher

echo "✅ Script ejecutado correctamente. Base de datos creada y poblada."
tail -f /logs/neo4j.log
