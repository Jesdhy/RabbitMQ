# 📨 Flask + RabbitMQ: Messaging System for Transcription

## 📘 About The Project  
This project is a simple messaging system using Python and RabbitMQ. It allows you to send a JSON message to an HTTP endpoint, filter the audio transcript field, and send it to a RabbitMQ queue. A consumer then reads that message and processes it (for now, it simply prints it).

## 📑 Table of Contents  
- [📘 About The Project](#-about-the-project)  
- [🚀 Getting Started](#-getting-started)  
  - [🔧 Prerequisites](#-prerequisites)  
  - [📥 Installation](#-installation)  
  - [⚙️ Running](#-running)  
- [📸 Screenshots](#-screenshots)  
- [🤝 Contributing](#-contributing)  

---
## 🚀 Getting Started

### 🔧 Prerequisites  
To run this project you need:

- Python 3.8 or higher
- Docker (to run RabbitMQ easily)

## 📥 Installation 

1.- Clone the repository
```bash
git clone https://github.com/Jesdhy/RabbitMQ.git
```
2.- Install image Docker
```bash
docker run -d --hostname my-rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
3.- Install dependencies:
```bash
python -m venv venv
source venv/bin/activate
```
4.- Install dependencies:
```bash
pip install pika
pip install flask
```
## ⚙️ Running
Getting RabbitMQ up and running with Docker:

- Access the web panel: http://localhost:15672

```bash
Username: guest
Password: guest
```

Run in visual code 

```bash
python consumer.py
```
```bash
python producer.py
```

## 📸 Screenshots

![RabbitMQ3](https://github.com/user-attachments/assets/1a6c5cf2-6040-455d-88ae-056334cb8786)

![RABBITMQ](https://github.com/user-attachments/assets/86a8fba5-5108-4cce-886c-ba3cfa9f100f)

![RABBITMQ2](https://github.com/user-attachments/assets/2f53044e-3245-4ed2-8378-f9bf0b4c70db)


## 🤝 Contributing
Thank you for your interest in contributing to this project! Here are some guidelines for doing so:
1. **Fork the repository** and clone the project to your local machine.
2. **Create a new branch** for your changes.
3. **Commit your changes** with a clear, descriptive message.
4. **Submit a Pull Request** with a description of your changes.

Thank you for helping improve this project!