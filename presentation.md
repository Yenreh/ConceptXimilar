# Demostración Ximilar API

## Resumen

Ximilar ofrece una plataforma completa de inteligencia artificial para procesamiento y análisis de imágenes, especializada en soluciones para e-commerce, moda, decoración del hogar y coleccionables.

Esta demostración utiliza el **SDK oficial de Python de Ximilar** para una integración más robusta y mantenible.

## SDK de Python

### Instalación

```bash
pip install ximilar-client
```

### Clientes Disponibles

El SDK proporciona clases especializadas para cada servicio:

```python
from ximilar.client.recognition import FashionTaggingClient
from ximilar.client.remove_bg import RemoveBackgroundClient
from ximilar.client.dominant_color import DominantColorClient
from ximilar.client.search import SimilarityFashionClient

# Inicializar clientes
fashion_client = FashionTaggingClient(token="TU_API_TOKEN")
removebg_client = RemoveBackgroundClient(token="TU_API_TOKEN")
color_client = DominantColorClient(token="TU_API_TOKEN")
```

### Ventajas del SDK

- ✅ **Clases especializadas**: Un cliente para cada servicio
- ✅ **Type hints**: Autocompletado y verificación de tipos
- ✅ **Manejo de errores**: Excepciones específicas y mensajes claros
- ✅ **Documentación integrada**: Docstrings detallados
- ✅ **Mantenimiento**: Actualizaciones automáticas con nuevas features
- ✅ **Código limpio**: Menos boilerplate, más legibilidad

## Servicios Implementados

### 1. Fashion Tagging (Etiquetado de Moda)

**Endpoint:** `https://api.ximilar.com/tagging/fashion/v2/detect_tags`

#### Capacidades:
- Detección automática de prendas de vestir y accesorios
- Clasificación en 7 categorías principales:
  - Clothing (Ropa)
  - Footwear (Calzado)
  - Jewellery (Joyería)
  - Bags (Bolsos)
  - Accessories (Accesorios)
  - Underwear (Ropa interior)
  - Watch (Relojes)
- Más de 50 subcategorías específicas
- Cientos de etiquetas descriptivas

#### Características Detectadas:
- **Categoría y Subcategoría**: Tipo específico de prenda
- **Color**: Colores dominantes
- **Estilo**: Casual, formal, deportivo, etc.
- **Material**: Algodón, lino, cuero, etc.
- **Género**: Hombre, mujer, unisex
- **Longitud**: Largo, corto, medio
- **Ajuste**: Slim, regular, holgado
- **Edad**: Adulto, niño, bebé
- **Diseño**: Estampados, texturas, etc.

#### Endpoints Disponibles:
- `/v2/detect_tags` - Detecta y etiqueta el objeto más grande
- `/v2/detect_tags_all` - Detecta y etiqueta todos los objetos
- `/v2/detect` - Solo detección sin etiquetas
- `/v2/tags` - Solo etiquetado sin detección
- `/v2/meta` - Meta tags (fondo, escena, vista)
- `/v2/region` - Identificación de región geográfica (indio, genérico)

#### Casos de Uso:
- Categorización automática de productos
- Búsqueda y filtrado avanzado
- Sistemas de recomendación
- Gestión de inventarios
- Moderación de contenido

---

### 2. Background Removal (Eliminación de Fondo)

**Endpoints:**
- `https://api.ximilar.com/removebg/precise/removebg` (Alta calidad)
- `https://api.ximilar.com/removebg/fast/removebg` (Rápido)

#### Modelos Disponibles:
1. **Precise Model**
   - Detección de bordes de alta calidad
   - Ideal para fotos de productos, retratos
   - Mayor costo en créditos

2. **Fast Model**
   - Procesamiento rápido
   - Menor costo
   - Adecuado para procesamiento en lote

#### Formatos de Salida:
- **Fondo Transparente** (PNG): `_output_url`
- **Fondo Blanco** (JPG): `_output_url_whitebg`
- **Máscara Binaria** (JPG): `_output_url_mask`

#### Opciones:
- Formato de imagen: PNG, JPG, WebP
- Calidad de imagen: 1-100
- URLs válidas por 24 horas

#### Casos de Uso:
- Preparación de fotos de productos para e-commerce
- Creación de catálogos
- Marketing y publicidad
- Diseño gráfico
- Automatización de procesamiento de imágenes

---

### 3. Dominant Colors (Colores Dominantes)

**Endpoint:** `https://api.ximilar.com/tagging/colors/v2/dominant_colors`

#### Capacidades:
- Extracción de colores dominantes de imágenes completas
- Identificación de colores de productos específicos
- Códigos RGB precisos
- Nombres de colores
- Porcentaje de cobertura de cada color

#### Información Proporcionada:
- **RGB Values**: Valores RGB exactos (r, g, b)
- **Color Name**: Nombre descriptivo del color
- **Coverage**: Porcentaje de la imagen que ocupa el color
- **Hex Code**: Código hexadecimal del color

#### Casos de Uso:
- Búsqueda por color en catálogos
- Análisis de tendencias de color
- Matching de productos por color
- Filtrado avanzado en e-commerce
- Coordinación de conjuntos

---

## Comparación con Soniox

| Característica | Ximilar | Soniox |
|---------------|---------|--------|
| **Tipo de IA** | Visión por Computadora | Procesamiento de Audio |
| **Input** | Imágenes (JPG, PNG, WebP, etc.) | Audio (MP3, WAV, OGG, etc.) |
| **Servicios** | Tagging, Background Removal, Colors, Search | Speech-to-Text, Transcripción |
| **Casos de Uso** | E-commerce, Moda, Inventarios | Subtítulos, Transcripciones, Asistentes de voz |
| **Procesamiento** | Sincrónico y Asincrónico | Streaming y Batch |
| **Pricing** | Por créditos según operación | Por minuto de audio |

## Arquitectura de la Aplicación

```
ConceptXimilar/
├── app.py                      # Servidor Flask con endpoints
├── controller_ximilar.py       # Controlador usando SDK oficial
├── requirements.txt            # Dependencias (incluye ximilar-client)
├── .env                        # Variables de entorno (API keys)
├── templates/
│   └── index.html             # Interfaz web con tabs
└── static/
    └── css/
        └── style.css          # Estilos personalizados
```

## Ejemplos de Uso del SDK

### Fashion Tagging

```python
from ximilar.client.recognition import FashionTaggingClient

client = FashionTaggingClient(token="TU_API_TOKEN")

# Detectar y etiquetar
result = client.tags([{"_url": "https://example.com/image.jpg"}])

# Detectar todos los objetos
result = client.tags_detect_all([{"_url": "https://example.com/image.jpg"}])

# Solo detección
result = client.detect([{"_url": "https://example.com/image.jpg"}])

# Obtener categorías
categories = client.top_categories()
```

### Background Removal

```python
from ximilar.client.remove_bg import RemoveBackgroundClient

client = RemoveBackgroundClient(token="TU_API_TOKEN")

# Modelo preciso
result = client.precise([{
    "_url": "https://example.com/image.jpg",
    "white_background": True,
    "binary_mask": False
}])

# Modelo rápido
result = client.fast([{"_url": "https://example.com/image.jpg"}])
```

### Dominant Colors

```python
from ximilar.client.dominant_color import DominantColorClient

client = DominantColorClient(token="TU_API_TOKEN")

result = client.dominant_color([{"_url": "https://example.com/image.jpg"}])

# Acceder a los colores
for color in result['records'][0]['_dominant_colors']:
    print(f"RGB({color['r']}, {color['g']}, {color['b']}) - {color['name']}")
```

## Flujo de Datos

1. **Usuario** → Selecciona imagen (URL o archivo local)
2. **Frontend** → Envía petición a Flask endpoint
3. **Backend** → Procesa con SDK de Ximilar (`controller_ximilar.py`)
4. **Ximilar API** → Analiza imagen y devuelve resultados
5. **Backend** → Formatea respuesta JSON
6. **Frontend** → Muestra resultados visuales

## Comparación: SDK vs API Directa

| Aspecto | Con SDK | Sin SDK (requests) |
|---------|---------|-------------------|
| **Código** | `client.tags([record])` | `requests.post(url, headers, json)` |
| **Setup** | `FashionTaggingClient(token)` | Headers + URL manual |
| **Errores** | Excepciones específicas | HTTP status codes genéricos |
| **Tipos** | Type hints integrados | Diccionarios genéricos |
| **Mantenimiento** | Actualización automática | Actualización manual |
| **Documentación** | Docstrings + IDE autocomplete | Referencia externa |

## Autenticación

```python
headers = {
    "Authorization": f"Token {XIMILAR_API_TOKEN}",
    "Content-Type": "application/json"
}
```

## Formato de Request

```json
{
  "records": [
    {
      "_url": "https://example.com/image.jpg",
      // o
      "_base64": "base64_encoded_image_data"
    }
  ]
}
```

## Formato de Response

```json
{
  "records": [
    {
      "_id": "uuid",
      "_url": "image_url",
      "_width": 1024,
      "_height": 768,
      "_objects": [...],
      "_tags": {...},
      "_status": {
        "code": 200,
        "text": "OK"
      }
    }
  ],
  "status": {
    "code": 200,
    "text": "OK"
  },
  "statistics": {
    "processing time": 1.23
  }
}
```

## Ventajas de Ximilar

1. **Taxonomía Completa**: Más de 50 categorías y cientos de tags
2. **Multilingüe**: Soporte para español, portugués y más idiomas
3. **Batch Processing**: Procesar hasta 10 imágenes por request
4. **Modelos Personalizables**: Posibilidad de entrenar modelos custom
5. **Alta Precisión**: Detección de bordes y clasificación avanzada
6. **Integración Fácil**: API REST con documentación completa
7. **SDK Python**: Cliente oficial para Python

## Limitaciones

- Formatos no soportados: AVIF, JP2, PSD, SVG, HEIF, PDF
- GIF solo procesa el primer frame
- URLs de imágenes deben ser públicas y directas
- Límite de 10 imágenes por batch
- Resultados de Background Removal expiran en 24 horas

## Costos (Ejemplos)

- **Fashion Tagging**: 5-10 créditos por imagen
- **Background Removal Precise**: 15 créditos por imagen
- **Background Removal Fast**: 10 créditos por imagen
- **Dominant Colors**: 3 créditos por imagen

## Recursos Adicionales

- **Documentación API**: https://docs.ximilar.com/
- **SDK Python (GitLab)**: https://gitlab.com/ximilar-public/ximilar-client
- **Ximilar App**: https://app.ximilar.com/
- **Demos Públicos**: https://demo.ximilar.com/
- **Blog**: https://ximilar.com/blog/
- **Pricing**: https://ximilar.com/pricing

## Conclusiones

Ximilar ofrece una suite completa de herramientas de IA para procesamiento de imágenes, especialmente potente para aplicaciones de e-commerce y moda. Su **SDK oficial de Python** facilita enormemente la integración, reduciendo el código boilerplate y mejorando la mantenibilidad.

### Beneficios del SDK:
1. **Desarrollo más rápido**: Menos código, más productividad
2. **Menos errores**: Type hints y validación automática
3. **Mejor experiencia de desarrollo**: Autocompletado en IDE
4. **Actualizaciones transparentes**: Nuevas features sin cambiar código
5. **Documentación accesible**: Integrada en el código

La capacidad de detección y etiquetado automático puede ahorrar horas de trabajo manual en catalogación de productos.

La combinación de Fashion Tagging, Background Removal y Dominant Colors permite crear catálogos de productos completamente automatizados con:
- Categorización automática
- Fondos profesionales
- Búsqueda por color
- Metadata rica para SEO y recomendaciones

Comparado con Soniox, ambas APIs muestran cómo diferentes tecnologías de IA (visión vs. audio) pueden resolver problemas específicos con alta precisión y facilidad de integración, especialmente cuando se usan los SDKs oficiales.

---

**Proyecto**: PI-II - Integración de APIs de IA  
**Fecha**: Noviembre 2025  
**Tecnologías**: Python, Flask, **Ximilar Python SDK**, HTML/CSS/JavaScript
