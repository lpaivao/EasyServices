# EasyServices

## Rotas Cliente

Ver clientes [GET]
```console
/api/clientes/
```

Create cliente [POST]
```console
/api/clientes/

{
    "id": 1,
    "nome": "João Silva",
    "email": "joao@example.com",
    "password": "senhasecreta",
    "rg": "123456",
    "cpf": "78901234567",
    "data_nascimento": "1990-01-01",
    "cep": "12345-678",
    "endereco": "Rua Principal",
    "numero_casa": "123",
    "cidade": "Cidade",
    "bairro": "Bairro",
    "telefone": "987654321"
}
```
Ver/Deletar/Editar cliente Específico [GET, PUT, DELETE]
```console
/api/clientes/<int:id>/

Exemplo: /api/clientes/1/
```

Para Obter token de autenticação [POST]
```console
/api/clientes/token/

{
    "email": "joao@example.com",
    "password": "senhasecreta"
}
```

Para Logout [POST]
```console
/api/clientes/logout/

{
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMjQ0NTM2NiwiaWF0IjoxNzAyMzU4OTY2LCJqdGkiOiI0ZmUwZTQzYTg5MjE0YjA5YTdjOTc2YjhmNWE0MjgxNSIsInVzZXJfaWQiOjF9.fmt4uKfoag1VCyzruUcS9aSCLa8Koky-FLggL3hkEy0"
}
```


## Rotas prestador

```console
/api/prestadores/

/api/prestadores/<int:id>/

/api/prestadores/token/

/api/prestadores/logout/
```
