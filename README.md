
📊 Análisis de la Transición Energética en LATAM (ETL & BI)
Este proyecto desarrolla un ecosistema completo de datos para analizar la evolución de las energías renovables en América Latina. El flujo abarca desde la extracción automatizada de datos oficiales hasta la visualización estratégica en Power BI, utilizando una arquitectura moderna de contenedores.

<img width="1494" height="793" alt="Screenshot 2026-03-11 105630" src="https://github.com/user-attachments/assets/254d68ca-9a71-4707-b465-9102d1b45452" />


🛠️ Tecnologías Utilizadas
Lenguaje: Python 

Librerías de Datos: Pandas, SQLAlchemy (para procesamiento y carga).

Infraestructura: Docker & Docker Compose (para orquestación de servicios).

Base de Datos: PostgreSQL (almacenamiento relacional).

Gestión de Datos: pgAdmin 4.

Visualización: Power BI Desktop.

🚀 Arquitectura del Proyecto
Para demostrar un flujo de trabajo profesional, el proyecto se divide en capas:

Capa de Extracción (ETL): Un script de Python conecta con la API/CSV de Our World in Data, filtrando específicamente registros de países latinoamericanos desde el año 2000.

Capa de Almacenamiento: Uso de Docker para levantar un servidor PostgreSQL independiente, evitando conflictos con instalaciones locales y garantizando la portabilidad del proyecto.

Capa de Transformación: Procesamiento de datos con Pandas para calcular métricas de negocio, como el porcentaje de participación solar y eólica sobre el total de generación.

Capa de Visualización: Conexión mediante el puerto 5433 a Power BI para el análisis de tendencias históricas y comparación entre países.

📂 Estructura del Repositorio
scripts/: Contiene los scripts de carga (cargar_energia.py) y transformación (limpieza.py).

data/: (Ignorado por Git) Espacio para datos locales.

pbix/: Archivo de reporte de Power BI.

docker-compose.yml: Configuración de la infraestructura.

.env: Gestión segura de credenciales.

🛡️ Buenas Prácticas Implementadas
Variables de Entorno: Uso de archivos .env para proteger credenciales de la base de datos (seguridad).

Entornos Virtuales: Aislamiento de dependencias mediante venv.

Control de Versiones: Uso estratégico de .gitignore para mantener un repositorio limpio y profesional.



