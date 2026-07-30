from datetime import date
from pydantic import BaseModel, field_validator

class Agenda(BaseModel):
    status: str
    horario_inicial: str
    horario_final: str
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

    @field_validator('horario_inicial', 'horario_final')
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

    @field_validator('horario_final')
    def horario_final_validacao(cls, v, values):
        if 'horario_inicial' in values:
            horario_inicial = values['horario_inicial']
            if horario_inicial >= v:
                raise ValueError('Horário final inválido. O horário final deve ser posterior ao horário inicial.')
        
        return v

    @field_validator('horario_inicial', 'horario_final')
    def horario_diferente_validacao(cls, v, values):    
        if 'horario_inicial' in values and 'horario_final' in values:
            horario_inicial = values['horario_inicial']
            horario_final = values['horario_final']
            if horario_inicial == horario_final:
                raise ValueError('Horários inválidos. O horário inicial e o horário final não podem ser iguais.')
        
        return v

    @field_validator('horario_inicial', 'horario_final')
    def horario_duracao_validacao(cls, v, values):  
        if 'horario_inicial' in values and 'horario_final' in values:
            horario_inicial = values['horario_inicial']
            horario_final = values['horario_final']
            hora_inicial, minuto_inicial = map(int, horario_inicial.split(':'))
            hora_final, minuto_final = map(int, horario_final.split(':'))
            duracao = (hora_final * 60 + minuto_final) - (hora_inicial * 60 + minuto_inicial)
            if duracao < 30:
                raise ValueError('Duração inválida. O agendamento deve ter no mínimo 30 minutos de duração.')
        
        return v
    
    
    @field_validator('horario_inicial', 'horario_final')
    def horario_intervalo_validacao(cls, v, values):
        if 'horario_inicial' in values and 'horario_final' in values:
            horario_inicial = values['horario_inicial']
            horario_final = values['horario_final']
            hora_inicial, minuto_inicial = map(int, horario_inicial.split(':'))
            hora_final, minuto_final = map(int, horario_final.split(':'))
            if (hora_inicial * 60 + minuto_inicial) % 15 != 0:
                raise ValueError('Horário inválido. O horário inicial deve estar em intervalos de 15 minutos.')
            if (hora_final * 60 + minuto_final) % 15 != 0:
                raise ValueError('Horário inválido. O horário final deve estar em intervalos de 15 minutos.')
        
        return v

    @field_validator('horario_inicial', 'horario_final')
    def horario_dia_util_validacao(cls, v, values):  
        if 'data' in values:
            data = values['data']
            if data.weekday() >= 6:  # , 6 = domingo
                raise ValueError('Data inválida. O agendamento não pode ser feito em finais de semana.')
        
        return v

    