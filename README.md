# ConceptXimilar - Demostración de API de Ximilar

Aplicación de demostración para explorar las capacidades de la API de Ximilar usando el **SDK oficial de Python**.

## Servicios Principales

- **Background Removal**: Eliminación de fondo de imágenes
- **Dominant Colors**: Extracción de colores dominantes
- **Photo Tagging**: Etiquetado automático de fotos

## Tecnologías

- **Python 3.9+**
- **Flask** - Framework web
- **Ximilar Python SDK** - Cliente oficial de Ximilar
- **HTML/CSS/JavaScript** - Frontend

## Instalación

1. Clonar el repositorio

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar token de API:
```bash
cp .env.example .env
```

4. Editar `.env` y agregar tu token:
```
XIMILAR_API_TOKEN=tu_token_aqui
```

## Uso

1. Ejecutar la aplicación:
```bash
python app.py
```

2. Abrir en el navegador: `http://localhost:5001`

3. Subir imágenes y probar los diferentes servicios

## Documentación

- [Ximilar API Docs](https://docs.ximilar.com/)
- [Python SDK](https://gitlab.com/ximilar-public/ximilar-client)
- [Pricing & Plans](https://www.ximilar.com/pricing/)

## Licencia

Proyecto educativo - PI-II

