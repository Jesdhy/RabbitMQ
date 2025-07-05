import pika
import json

# Configuración de RabbitMQ
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'cola_transcripciones'

def callback(ch, method, properties, body):
    mensaje = json.loads(body)
    print("Mensaje recibido de la cola:")
    print(mensaje)
    print("-----------------------------")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    # Asegurarse de que la cola existe
    channel.queue_declare(queue=QUEUE_NAME)

    print(f"Esperando mensajes en la cola '{QUEUE_NAME}'. Presiona CTRL+C para salir.")

    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()

if __name__ == '__main__':
    main()
