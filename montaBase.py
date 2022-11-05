import pandas as pd
import string
import random
from datetime import datetime, date, time

def random_timestamp ():
    dia = random.randint(1,30)
    mes = random.randint(1,12)
    if (mes == 2 and dia > 28):
        mes = 3
    ano = random.randint(1950,2022)
    hora = random.randint(9,16)
    min = random.randint(0,59)
    seg = random.randint(0,59)
    d = date(ano, mes, dia)
    t = time(hora,min)
    dt = datetime.combine(d,t)

    return dt


def random_data_mov ():
    dia = random.randint(1,30)
    mes = random.randint(1,12)
    if (mes == 2 and dia > 28):
        mes = 3
    ano = random.randint(2005,2022)
    hora = random.randint(9,16)
    min = random.randint(0,59)
    seg = random.randint(0,59)
    d = date(ano, mes, dia)
    t = time(hora,min)
    dt = datetime.combine(d,t)

    return dt


def geraAssociado ():
    df_nomes = pd.read_csv('nomes6mil.csv',header = None)
    df_dados = df_nomes

    df_conta = pd.DataFrame(data=None)
    df_cartao =pd.DataFrame(data=None)
    df_movimento = pd.DataFrame(data=None)

    lista_nconta = []

    #CRIANDO demais dados para serem consumidos
    #id int, nome varchar, sobrenome varchar, idade int, email varchar,

    qnt = len(df_nomes.index) 
    lista_id = []
    lista_nome = []
    lista_sobrenome = []
    lista_idade = []
    lista_email =[]

    #cartao
    lista_ncart = []
    lista_nome_cart = []
    lista_conta_cart = []
    lista_assoc_cart = []

    #conta
    lista_id_conta=[]
    lista_tipoc = [] #ContaCorrente, poupanca, salario
    lista_datacriacao = []
    lista_idassoc = []

    #movimento
    lista_id_mov = []
    lista_vlr_trans = []
    lista_desc_mov =[]
    lista_data_mov = []
    lista_id_cartao = []


    for i in range (0,qnt):
        lista_id.append(i+1)
        nome_df = df_dados[0][i]
        tamanho = len(nome_df.split(" "))

        nome = str(nome_df.split(" ")[0])
        if nome.find('.') >= 0:
            nome = str(nome_df.split(" ")[1])
        lista_nome.append(nome)

        sobrenome = str(nome_df.split(" ")[tamanho-1])
        lista_sobrenome.append(sobrenome)

        idade = random.randint(15,99)
        lista_idade.append(idade)

        dominios = ['hotmail','bol','terra','sicredi','gmail','live','globo']
        email = str(nome.casefold() + '.' + sobrenome.casefold() + '@' + random.choice(dominios) + '.com')
        lista_email.append(email)

        #gerando conta
        qnt_conta = random.randint(1,3)
        for laco in range(1,qnt_conta):
            numero = random.randint(0,999999)
            while lista_nconta.count(numero) != 0 :
                numero = random.randint(0,999999)
            lista_nconta.append(numero)
            lista_tipoc.append(random.randint(1,9))
            lista_datacriacao.append(random_timestamp())
            lista_idassoc.append(i+1)

            #cartão
            numero_cart = random.randint(0,999999)
            while lista_ncart.count(numero_cart) != 0 :
                numero_cart = random.randint(0,999999)
            lista_ncart.append(numero_cart) 
            card_name = nome + ' ' + sobrenome 
            lista_nome_cart.append(card_name)
            lista_conta_cart.append(numero)
            lista_assoc_cart.append(i+1)

            
            #movimentos
            numero_mov = random.randint(0,10000000)
            while lista_id_mov.count(numero_mov) != 0 :
                numero_mov = random.randint(0,10000000)
            lista_id_mov.append(numero_mov)
            lista_vlr_trans.append(round(random.uniform(0,1000000),2))
            op_desc = ['Credito','Debito']
            lista_desc_mov.append(random.choice(op_desc))
            lista_data_mov.append(random_data_mov())
            lista_id_cartao.append(numero_cart)

    #associados
    df_dados['id'] = lista_id 
    df_dados['nomes'] = lista_nome
    df_dados['sobrenome'] = lista_sobrenome
    df_dados['idade'] = lista_idade
    df_dados['email'] = lista_email
    df_dados = df_dados.rename({0:'nome_completo'}, axis = 'columns')

    #contas
    df_conta['id']=lista_nconta
    df_conta['tipo'] = lista_tipoc
    df_conta['data_criacao'] = lista_datacriacao
    df_conta['id_associado'] = lista_idassoc

    #Cartao 
    df_cartao['id']= lista_id_cartao
    df_cartao['num_cartao']= lista_ncart
    df_cartao['nom_impresso']= lista_nome_cart
    df_cartao['id_conta']= lista_conta_cart
    df_cartao['id_associado']= lista_assoc_cart
    

    #movimentos
    df_movimento['id'] = lista_id_mov
    df_movimento['vlr_transacao'] =  lista_vlr_trans
    df_movimento['des_transacao'] = lista_desc_mov
    df_movimento['data_movimento'] =  lista_data_mov
    df_movimento['id_cartao'] = lista_id_cartao

    df_dados.to_csv("./bruto/associado.csv")
    df_conta.to_csv("./bruto/conta.csv")
    df_cartao.to_csv("./bruto/cartao.csv")
    df_movimento.to_csv("./bruto/movimento.csv")
    return df_dados

