
from datetime import date
import simplejson as json
from bson import json_util,ObjectId

import src.connectRedis as connectRedis
import src.connectDb as connectDb
import src.utils.dias_do_mes as dias_do_mes

cursor = connectRedis.connect()
bd_mercado_livre = connectDb.connect()

hoje = date.today()

hoje_formatado = hoje.strftime("%d/%m/%Y")


def incrementar_view_produto(request):
  col = bd_mercado_livre.produto

  produto = request.get_json()
  try:
    doc = col.find({"_id": ObjectId(produto["id"])})
    for x in doc:
      retorno = json.loads(json_util.dumps(x))

    cursor.incr(f'produto:{produto["id"]}:{hoje_formatado}:views_dia')
    cursor.incr(f'produto:{produto["id"]}:views_total')
    return json.dumps({
      "produto": retorno,
      "views_hoje": {
      "data_hoje": hoje_formatado,
       "views_hoje": int(cursor.get(f'produto:{produto["id"]}:{hoje_formatado}:views_dia')),
      },
      "total_views": int(cursor.get(f'produto:{produto["id"]}:views_total'))
    })   

  except:
    return json.dumps({
      "message": "ocorreu um erro, tente mais tarde."
    })




def incrementar_view_website():
  cursor.incr(f'website:{hoje_formatado}:views_dia')
  cursor.incr(f'website:views_total')
  return json.dumps({
    "views_total": int(cursor.get(f'website:views_total')),
    "views_hoje":{
      "data_hoje": hoje_formatado,
      "numero_views": int(cursor.get(f'website:{hoje_formatado}:views_dia'))
    }
  })   




def relatorio_geral():

  lista_dias_views = []
  contador_views_mensal = 0
  for dia in dias_do_mes.dias_do_mes():
    if (cursor.get(f'website:{dia}:views_dia')):
      lista_dias_views.append({
        "dia": dia,
        "views_dia": int(cursor.get(f'website:{dia}:views_dia'))
      })
      contador_views_mensal += int(cursor.get(f'website:{dia}:views_dia'))
    else:
      lista_dias_views.append({
        "dia": dia,
        "views_dia": 0
      })

  return json.dumps({
    "views_total": int(cursor.get(f'website:views_total')),
    "views_mensal": contador_views_mensal,
    "lista_views_mensal_dia": lista_dias_views
  })



def salvar_relatorio():
  hoje = date.today()
  hoje_formatado = hoje.strftime("%d/%m/%Y")

  relatorio = bd_mercado_livre.relatorio

  relatorio_salvo = {
    "backup_dia": hoje_formatado,
    "dados": json.loads(relatorio_geral())
  }

  print(relatorio_salvo)

  relatorio.insert_one(relatorio_salvo)

  return json.dumps({"message":"salvo com sucesso"})


def delete_all_keys():
  cursor.flushall()

  return json.dumps({
    "message":"chaves deletadas com sucesso"
  })
      