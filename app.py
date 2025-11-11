#!/usr/bin/env python3
"""
Aplicación Flask para demostración de Ximilar API
Servicios disponibles en el plan gratuito: Background Removal, Dominant Colors
"""

import os
import base64
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from controller_ximilar import ximilar_controller

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

@app.route('/')
def index():
    """Página principal con interfaz de demostración"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Endpoint de salud"""
    return jsonify({'status': 'ok'})

# --- BACKGROUND REMOVAL ENDPOINTS ---

@app.route('/removebg', methods=['POST'])
def remove_background():
    """Eliminar fondo de una imagen"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No request data provided'}), 400
    
    image_url = data.get('url')
    image_base64 = data.get('base64')
    model = data.get('model', 'precise')
    
    if not image_url and not image_base64:
        return jsonify({'error': 'No image URL or base64 provided'}), 400
    
    if model not in ['precise', 'fast']:
        return jsonify({'error': 'Invalid model. Use "precise" or "fast"'}), 400
    
    try:
        if image_url:
            result = ximilar_controller.remove_background(
                image_url, is_url=True, model=model
            )
        else:
            result = ximilar_controller.remove_background(
                image_base64, is_url=False, model=model
            )
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/removebg/upload', methods=['POST'])
def removebg_upload():
    """Subir archivo para eliminación de fondo"""
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    model = request.form.get('model', 'precise')
    
    try:
        image_bytes = file.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        
        result = ximilar_controller.remove_background(
            image_base64, is_url=False, model=model
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- DOMINANT COLORS ENDPOINTS ---

@app.route('/colors/dominant', methods=['POST'])
def dominant_colors():
    """Extraer colores dominantes de una imagen"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No request data provided'}), 400
    
    image_url = data.get('url')
    image_base64 = data.get('base64')
    max_colors = data.get('max_colors', 5)
    
    if not image_url and not image_base64:
        return jsonify({'error': 'No image URL or base64 provided'}), 400
    
    try:
        if image_url:
            result = ximilar_controller.get_dominant_colors(
                image_url, is_url=True, max_colors=max_colors
            )
        else:
            result = ximilar_controller.get_dominant_colors(
                image_base64, is_url=False, max_colors=max_colors
            )
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/colors/upload', methods=['POST'])
def colors_upload():
    """Subir archivo para extracción de colores"""
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    max_colors = int(request.form.get('max_colors', 5))
    
    try:
        image_bytes = file.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        
        result = ximilar_controller.get_dominant_colors(
            image_base64, is_url=False, max_colors=max_colors
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- PHOTO TAGGING ENDPOINTS ---

@app.route('/tagging/upload', methods=['POST'])
def tagging_upload():
    """Subir archivo para etiquetado de fotos"""
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    try:
        image_bytes = file.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        
        result = ximilar_controller.tag_photo(
            image_base64, is_url=False
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("Servidor de Demostración Ximilar API - Plan Gratuito")
    print("=" * 60)
    print(f"URL: http://localhost:5001")
    print("=" * 60)    
    app.run(host='0.0.0.0', port=5001, debug=True)

