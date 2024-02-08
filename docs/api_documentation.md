
# Crear usuario

Crear Usuario con username y contraseña

**URL** : `/users/`

**Method** : `POST`

**Auth required** : NO

## Payload request
```json
  {
    "username": "rodrigo",
    "password": "somepassword"
  }
```

## Success Response

**Code** : `201 Created`

**Content example**

```json
{
  "password":"$2b$12$BeFltNg8ehzo4iVLTHiK1O/E5id3oZM20rYBD4yeMm5k4KSXvWrXK",
  "id":6,"updated_at":null,"created_at":"2024-02-08T18:18:02.895464",
  "username":"another"
}
```


# Login

Iniciar sesión para obtener el token

**URL** : `/users/`

**Method** : `POST`

**Auth required** : NO

## Payload request
```json
{
  "username": "rodrigo",
  "password": "somepassword"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImVsZW5hIiwiZXhwIjoxNzA3NDE4MTgwfQ.XBg9S2ygmqopNfDdYQJgYBkQl-AlOqJwBP6P5xhCGWE",
    "token_type": "bearer"
}
```

# Wordle

**URL** : `/wordle/`

**Method** : `POST`

**Auth required** : YES

**Headers**
{
  "Authorization": "bearer  <ANY_TOKEN>"
}


## Payload request
```json
{
  "word": "atole"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
[
    {
        "letter": "a",
        "value": 3
    },
    {
        "letter": "t",
        "value": 2
    },
    {
        "letter": "o",
        "value": 2
    },
    {
        "letter": "l",
        "value": 3
    },
    {
        "letter": "e",
        "value": 3
    }
]
```

