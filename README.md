
# Este proyecto es una prueba técnica para DD360


## Overview:
Creación de un API REST para jugar Wordle.
Se trata de que el sistema va a escoger una palabra de 5 letras con un tiempo de vida de 5 minutos.
El usuario podra intentar adivinar cual es la palabra con 5 intentos.

## Diagram

![Diagram](./docs/diagram.png)

## Casos de uso que soporta:
- Login
- Registrar Usuario
- Wordle (Necesita autenticación y enviar el token en los headers)
- Cambiar la palabra cada 5 minutos (Necesita autenticación)
- Obtener las palabras más acertadas (Necesita autenticación)
- Obtener a los Diez mejores jugadores con sus victorias (Necesita autenticación)

## Casos de uso que no soporta
- Obtener partidas que ha jugado un usuario y sus victorias

## Stack

- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose


## Instrucciones para levantar el proyecto

- docker compose build
- docker compose up


## Documentación
Para ver la documentación de las APIS click [aquí](https://github.com/roodrigoroot69/wordle/blob/main/docs/api_documentation.md).


**Postman**:
Download collection and import on your Postman
[Collection of Postman](https://drive.google.com/file/d/1Q4saIRLmZ2V8kc8JAurr8q3kE3siJ0SY/view?usp=sharing)


## Usuarios disponibles para hacer pruebas:
**Los usuarios son player1 sucesivamente hasta player25 y la contraseña es la misma para todos**

**username**: player1...player25

**password**: password123
