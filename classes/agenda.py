from datetime import date, time
from typing import Literal
from pydantic import BaseModel, Field, field_validator, model_validator

class Agenda(BaseModel):
    status: Literal['pendente', 'confirmado', 'cancelado', 'concluido']
    horario_inicio: time
    horario_fim: time
    data: date
    cliente_id: int = Field(..., gt=0, description="O ID deve ser maior que 0")
    profissional_id: int = Field(..., gt=0, description="O ID deve ser maior que 0")
    servico_id: int = Field(..., gt=0, description="O ID deve ser maior que 0")

    # Validação do campo DATA
    @field_validator('data')
    @classmethod
    def data_validacao(cls, v: date) -> date: 
        if v < date.today():
            raise ValueError('Data inválida. A data não pode ser anterior à data atual.')
        if v.weekday() == 6:  # 6 = Domingo
            raise ValueError('Data inválida. O agendamento não pode ser feito para domingo.')
        return v

    # Validação dos horários em múltiplos de 15 minutos
    @field_validator('horario_inicio', 'horario_fim')
    @classmethod
    def horario_intervalo_validacao(cls, v: time) -> time:
        if v.minute % 15 != 0:
            raise ValueError('Horário inválido. O horário deve estar em intervalos de 15 minutos.')
        return v

    # Validação CRUZADA (compara início e fim após carregar todos os dados)
    @model_validator(mode='after')
    def validar_regras_horario(self) -> 'Agenda':
        # Valida se horário final é estritamente posterior ao inicial
        if self.horario_fim <= self.horario_inicio:
            raise ValueError('Horário final inválido. O horário final deve ser posterior ao horário inicial.')

        # Calcula duração em minutos usando o tipo time nativo
        minutos_inicio = self.horario_inicio.hour * 60 + self.horario_inicio.minute
        minutos_fim = self.horario_fim.hour * 60 + self.horario_fim.minute
        duracao = minutos_fim - minutos_inicio

        if duracao < 30:
            raise ValueError('Duração inválida. O agendamento deve ter no mínimo 30 minutos de duração.')
        
        return self

    @validar_cancelamento_horario
    def validar_cancelamento_horario(Horario_inicio: time, Horario_fim: time) -> None:
        # Valida se o horário de cancelamento é permitido (exemplo: não permitir cancelamento em menos de 1 hora antes do início)
        from datetime import datetime, timedelta
        agora = datetime.now().time()
        if Horario_inicio <= (datetime.combine(date.today(), agora) + timedelta(hours=1)).time():
            raise ValueError('Cancelamento inválido. O agendamento não pode ser cancelado com menos de 1 hora de antecedência.')
   