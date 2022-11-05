import psycopg2
from psycopg2 import Error
import pandas as pd


def sql_run (sql):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="admin",
                                    password="admin",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")

        cursor = connection.cursor()
        # Execute a command: this creates a new table
        cursor.execute(sql)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def sql_dll():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="admin",
                                    password="admin",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")

        cursor = connection.cursor()
        cursor.execute(open('/home/ander/Documentos/datapipeline/sql/DLL.sql','r').read())

        connection.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def sql_insert_bruto(df,nome_tabela,n):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="admin",
                                    password="admin",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
        cursor = connection.cursor()
        tamanho = len(df.values[1])
        valores =[]    
        for i in range (0,len(df)):           
            for j in range(n,tamanho):
                valores.append(df.values[i][j]) 
                row_val = str(valores)
                row_val = row_val.replace('[','')
                row_val = row_val.replace(']','')
            sql_input = f"INSERT INTO {nome_tabela} VALUES ({row_val});"
            print(sql_input)            
            cursor.execute(sql_input)
            connection.commit()
            print("Table LINHA inserida successfully in PostgreSQL ")

            valores=[]
            cursor = connection.cursor()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



def sql_get (sql):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="admin",
                                    password="admin",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")

        cursor = connection.cursor()
        # Execute a command: this creates a new table
        cursor.execute(sql)
        pd_query = pd.DataFrame(cursor.fetchall())
        connection.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return pd_query

