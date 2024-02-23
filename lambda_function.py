import awsgi
from flask import Flask, jsonify
from faker import Faker
app = Flask(__name__)

@app.route('/monitor')
def monitor():
    return jsonify(status=200, message='Echo: I\'m good')

@app.route('/register')
def register():
    register_data = {
        "Nombre": fake.first_name(),
        "Apellido": fake.last_name(),
        "Edad": fake.random_int(min=18, max=80),
        "Email": fake.email(),
        "Telefono": fake.phone_number()
        }
    
    return jsonify(status=200, data=register_data, message='Usuario creado exitosamente')
    
def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})