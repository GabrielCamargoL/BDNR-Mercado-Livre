
from datetime import date, timedelta
import datetime


def dias_do_mes():
  hoje = datetime.datetime.now()

  dia_hoje = hoje.strftime('%d')
  dia_mes = hoje.strftime('%m')
  dia_ano = hoje.strftime('%Y')

  data_inicio = date(int(dia_ano), int(dia_mes), 1)
  data_fim = date(int(dia_ano), int(dia_mes), int(dia_hoje))

  delta = data_fim - data_inicio

  lista_datas = []
  for i in range(delta.days + 1):
    dia = data_inicio + timedelta(days=i)
    lista_datas.append(dia)

  lista_datas_str = [datetime.datetime.strftime(dt, format="%d/%m/%Y") for dt in lista_datas]

  return lista_datas_str
