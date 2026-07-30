from datetime import date
from pydantic import BaseModel, field_validator

class Agenda(BaseModel):
    status: str
    horario_inicio: str
    horario_fim: str
    data: date
    cliente_id: int
    profissional_id: int
    servico_id: int

    @field_validator('status')
    def status_validacao(cls, v):
        status_validos = ['pendente', 'confirmado', 'cancelado', 'concluido']
        if v not in status_validos:
            raise ValueError('Status inválido. Utilize: pendente, confirmado, cancelado, concluido.')
        
        return v

    @field_validator('horario_inicio', 'horario_fim')
    def horario_validacao(cls, v):
        if len(v) != 5 or v[2] != ':' or not v.replace(':', '').isdigit():
            raise ValueError('Formato de horário inválido. Utilize o formato HH:MM.')
        
        return v

    @field_validator('data')
    def data_validacao(cls, v): 
        if v < date.today():
            raise ValueError('Data inválida. A data não pode ser anterior à data atual.')
        
        return v

    @field_validator('cliente_id', 'profissional_id', 'servico_id')
    def id_validacao(cls, v):
        if v <= 0:
            raise ValueError('ID inválido. O ID deve ser um número inteiro positivo.')
        
        return v

    @field_validator('horario_fim')
    def horario_fim_validacao(cls, v, values):
        if 'horario_inicio' in values:
            horario_inicio = values['horario_inicio']
            if horario_inicio >= v:
                raise ValueError('Horário final inválido. O horário final deve ser posterior ao horário inicial.')
        
        return v

    @field_validator('horario_inicio', 'horario_fim')
    def horario_diferente_validacao(cls, v, values):    
        if 'horario_inicio' in values and 'horario_fim' in values:
            horario_inicio = values['horario_inicio']
            horario_fim = values['horario_fim']
            if horario_inicio == horario_fim:
                raise ValueError('Horários inválidos. O horário inicial e o horário final não podem ser iguais.')
        
        return v

    @field_validator('horario_inicio', 'horario_fim')
    def horario_duracao_validacao(cls, v, values):  
        if 'horario_inicio' in values and 'horario_fim' in values:
            horario_inicio = values['horario_inicio']
            horario_fim = values['horario_fim']
            hora_inicio, minuto_inicio = map(int, horario_inicio.split(':'))
            hora_fim, minuto_fim = map(int, horario_fim.split(':'))
            duracao = (hora_fim * 60 + minuto_fim) - (hora_inicio * 60 + minuto_inicio)
            if duracao < 30:
                raise ValueError('Duração inválida. O agendamento deve ter no mínimo 30 minutos de duração.')
        
        return v
    
    
    @field_validator('horario_inicio', 'horario_fim')
    def horario_intervalo_validacao(cls, v, values):
        if 'horario_inicio' in values and 'horario_fim' in values:
            horario_inicio = values['horario_inicio']
            horario_fim = values['horario_fim']
            hora_inicio, minuto_inicio = map(int, horario_inicio.split(':'))
            hora_fim, minuto_fim = map(int, horario_fim.split(':'))
            if (hora_inicio * 60 + minuto_inicio) % 15 != 0:
                raise ValueError('Horário inválido. O horário inicial deve estar em intervalos de 15 minutos.')
            if (hora_fim * 60 + minuto_fim) % 15 != 0:
                raise ValueError('Horário inválido. O horário final deve estar em intervalos de 15 minutos.')
        
        return v

    @field_validator('horario_inicio', 'horario_fim')
    def horario_dia_util_validacao(cls, v, values):  
        if 'data' in values:
            data = values['data']
            if data.weekday() >= 6:  # , 6 = domingo
                raise ValueError('Data inválida. O agendamento não pode ser feito em finais de semana.')
        
        return v

    