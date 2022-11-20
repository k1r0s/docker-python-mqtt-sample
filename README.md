### MQTT - Python (paho) - Docker

This small project showcases docker containers
interacting with each other using MQTT protocol.

```
.
├── client_receive
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── client_send
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── mosquitto.conf
└── README.md
```
# Running

`docker compose up`

> You may add --build flag so you can tweak python code and see results
