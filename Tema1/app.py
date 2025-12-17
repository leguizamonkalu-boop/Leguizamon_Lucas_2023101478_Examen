from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "EP2 UNIDA"

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  
        port=5005,        
        debug=True        
    )


# Para subir el servicio:
# Acceder desde: http://IP_DEL_EQUIPO:5005
