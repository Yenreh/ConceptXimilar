# ConceptXimilar - Demostración de API de Ximilar

Aplicación de demostración para explorar las capacidades de la API de Ximilar usando el **SDK oficial de Python**, con servicios disponibles en el **plan gratuito**:
- ✅ **Background Removal**: Eliminación de fondo de imágenes
- ✅ **Dominant Colors**: Extracción de colores dominantes
- ✅ **Custom Image Recognition**: Reconocimiento personalizado de imágenes
- ✅ **Object Detection**: Detección de objetos personalizados
- ❌ **Fashion Tagging**: No disponible en plan free (requiere plan de pago)
- ❌ **Visual Search**: No disponible en plan free (requiere plan de pago)

## ⚠️ Nota sobre el Plan Gratuito

El plan gratuito de Ximilar incluye acceso limitado a servicios. Los servicios de **Fashion Tagging**, **Home Decor Tagging** y **Fashion Search** **NO** están disponibles en el plan gratuito.

### Servicios Disponibles en Plan Free:
- ✅ Background Removal
- ✅ Dominant Colors
- ✅ Photo Tagging (Generic)
- ✅ Custom Image Classification
- ✅ Custom Object Detection
- ✅ Photo Similarity
- ✅ Product Similarity
- ✅ Person Detection & Recognition
- ✅ OCR
- ✅ AI Card Grading

## Tecnologías

- **Python 3.8+**
- **Flask** - Framework web
- **Ximilar Python SDK** - Cliente oficial de Ximilar
- **HTML/CSS/JavaScript** - Frontend moderno

## Requisitos

- Python 3.8+
- Cuenta en [Ximilar App](https://app.ximilar.com/)
- Token de API de Ximilar

## Instalación

1. Clonar el repositorio
2. Instalar dependencias (incluye el SDK oficial de Ximilar):
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
```bash
cp .env.example .env
```

4. Editar `.env` y agregar tu token de API de Ximilar:
```
XIMILAR_API_TOKEN=tu_token_aqui
SECRET_KEY=tu_clave_secreta_aqui
```

## Uso

1. Ejecutar la aplicación:
```bash
python app.py
```

2. Abrir el navegador en `http://localhost:5000`

3. Explorar las diferentes funcionalidades en las pestañas disponibles

## Servicios Disponibles

### Fashion Tagging
- Detecta prendas de vestir en imágenes
- Extrae categorías, colores, estilos, materiales, etc.
- Soporta detección de múltiples objetos

### Background Removal
- Elimina el fondo de imágenes
- Modelos: Precise (alta calidad) y Fast (rápido)
- Genera versiones con fondo transparente, blanco, o máscara binaria

### Dominant Colors
- Extrae colores dominantes de imágenes completas
- Identifica colores de productos específicos
- Proporciona códigos RGB y nombres de colores

### Visual Search
- Búsqueda visual de productos similares
- Búsqueda por texto en múltiples idiomas
- Filtrado por categorías y atributos

## Documentación

- [Ximilar API Docs](https://docs.ximilar.com/)
- [Ximilar Python SDK](https://gitlab.com/ximilar-public/ximilar-client)
- [Fashion Tagging](https://docs.ximilar.com/tagging/fashion)
- [Background Removal](https://docs.ximilar.com/image-tools/remove-background)
- [Dominant Colors](https://docs.ximilar.com/image-tools/dominant-colors)
- [Visual Search](https://docs.ximilar.com/visual-search/fashion)

## Ventajas del SDK

El SDK oficial de Ximilar ofrece:
- ✅ Clases especializadas para cada servicio
- ✅ Manejo automático de autenticación
- ✅ Tipos de datos bien definidos
- ✅ Manejo de errores mejorado
- ✅ Código más limpio y mantenible
- ✅ Documentación integrada

## Licencia

Proyecto educativo - PI-II
