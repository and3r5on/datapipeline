import pandas as pd
import random
import string
from montaBase import geraAssociado
from sql_func import *

#Gera os dados brutos em CSV
geraAssociado()

#gera DLL das tabelas
sql_dll()

#insere os dados do associado
df = pd.read_csv("bruto/associado.csv")
nome_tabela = 'associado'
sql_insert_bruto(df,nome_tabela,2)
print("Associado ok")

#insere os dados de conta
df = pd.read_csv("bruto/conta.csv")
nome_tabela = 'conta'
sql_insert_bruto(df,nome_tabela,1)
print("Conta ok")

#insere os dados de cartao
df = pd.read_csv("bruto/cartao.csv")
nome_tabela = 'cartao'
sql_insert_bruto(df,nome_tabela,1)
print("Cartao ok")

#insere os dados de movimento
df = pd.read_csv("bruto/movimento.csv")
nome_tabela = 'movimento'
sql_insert_bruto(df,nome_tabela,1)
print("Movimento ok")

#fazerndo movimento_flat
sql_m_flat = (open('/home/ander/Documentos/datapipeline/sql/movimento_flat.sql','r').read())

#cria movimento_flat no postgres
sql_run(sql_m_flat)

sql_c_m_flat = (open('/home/ander/Documentos/datapipeline/sql/consulta_movimento_flat.sql','r').read())
df = sql_get(sql_c_m_flat)
df.to_csv("movimento_flat.csv")

