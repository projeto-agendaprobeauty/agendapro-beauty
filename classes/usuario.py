from typing import Literal
from pydantic import BaseModel, Field, EmailStr, field_validator


class Usuario(BaseModel):

    nome: str = Field(min_length=3)

    senha: str = Field(min_length=6, max_length=16)

    email: EmailStr

    telefone: str

    tipo_usuario: Literal['cliente', 'profissional', 'admin']


    @field_validator('nome')
    def nomeEspaco(cls, value: str) -> str:

        if value.count(' ') == 0:
            raise ValueError('O nome deve conter pelo menos um sobrenome')

        return value.title()


    @field_validator('telefone')
    def validaTelefone(cls, value: str) -> str:

        partes = value.split()

        if len(partes) != 2:
            raise ValueError(
                'Digite o telefone no formato: 51 991155248'
            )

        ddd, numero = partes

        if not ddd.isdigit() or not numero.isdigit():
            raise ValueError(
                'DDD e telefone devem conter apenas números'
            )

        if len(ddd) != 2:
            raise ValueError(
                'O DDD deve possuir 2 números'
            )

        if len(numero) != 9:
            raise ValueError(
                'O telefone deve possuir 9 números'
            )

        return value