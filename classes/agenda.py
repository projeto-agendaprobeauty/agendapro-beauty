f@router.post('/agendar')
def agendar_servico(agenda :Agenda):
    try:
        with engine.begin() as con:
            sql = """INSERT INTO public.agenda
                    (status, horario_inicial, horario_final, data, cliente_id, profissional_id, servico_id)
                VALUES ( :status, :horario_inicial, :horario_final, :data, :cliente_id, :profissional_id, :servico_id)"""            
            dados = {
                "status": agenda.status,
                "horario_inicial": agenda.horario_inicial,
                "horario_final": agenda.horario_final,
                "data": agenda.data,
                "cliente_id": agenda.cliente_id,
                "profissional_id": agenda.profissional_id,
                "servico_id": agenda.servico_id
            }

            resultado = con.execute(text(sql), dados)
            print("Linhas afetadas:", resultado.rowcount)

    except Exception as erro:
        print("ERRO:", erro)
        return {"erro": str(erro)}
        
    engine.dispose()
    return 'Serviço agendado com sucesso!'
