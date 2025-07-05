from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)

# Config RabbitMQ
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'cola_transcripciones'

def enviar_a_rabbitmq(mensaje):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_publish(exchange='',
                          routing_key=QUEUE_NAME,
                          body=json.dumps(mensaje))
    connection.close()

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        datos = request.get_json()

        if not datos:
            return jsonify({"error": "JSON inválido o vacío"}), 400

        # Filtrar el campo deseado
        audio_transcripcion = datos.get("transcripción_de_audio")
        if not audio_transcripcion:
            return jsonify({"error": "El campo 'transcripción_de_audio' no existe"}), 400

        # Empaquetar solo ese campo
        mensaje_filtrado = {"transcripción_de_audio": audio_transcripcion}

        # Enviar a RabbitMQ
        enviar_a_rabbitmq(mensaje_filtrado)

        return jsonify({"status": "ok", "mensaje_enviado": mensaje_filtrado}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
