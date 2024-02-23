import awsgi
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/monitor')
def monitor():
    return jsonify(status=200, message='Echo: I\'m good')

@app.route('/register')
def register():
    register_data = {
        "Nombre": "Juan",
        "Apellido": "Perez",
        "Edad": 25,
        "Email": "123@123.com",
        "Telefono": "1234567890"
        }
    
    return jsonify(status=200, message='Usuario creado exitosamente')
    
def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})