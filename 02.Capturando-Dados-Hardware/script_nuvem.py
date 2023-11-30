import mysql.connector 
import psutil
import time
from datetime import datetime
import platform
import pymssql

# Configurações SQL Server
sql_server_cnx = pymssql.connect(
    server='52.45.220.247',
    database='test',
    user='sa',
    password='#####'
)
cursor_sql_server = sql_server_cnx.cursor()

# Criando a estrutura de repetição para que os valores dos componentes se atualizam
while True:
    nome_processador = platform.processor()
    arquitetura_processador = platform.architecture()[0]
    nucleos_fisicos = psutil.cpu_count(logical=False)
    nucleos_logicos = psutil.cpu_count(logical=True)
    frequencia_hz = psutil.cpu_freq().current

    dia = datetime.now()

    # SQL para inserir na tabela RegistrosTRUSTED (CPU)

    # SQL para inserir na tabela RegistrosTRUSTED do MySQL (CPU)
    sql8_sql = "INSERT INTO RegistrosTRUSTED (dataHora, fkComponente, fkIdServidor, textoCapturado) VALUES (%s, %s, %s, %s)"
    values8_sql = (dia.strftime('%Y-%m-%d %H:%M:%S'), 8, 5, nome_processador)

    sql9_sql = "INSERT INTO RegistrosTRUSTED (dataHora, fkComponente, fkIdServidor, textoCapturado) VALUES (%s, %s, %s, %s)"
    values9_sql = (dia.strftime('%Y-%m-%d %H:%M:%S'), 9, 5, arquitetura_processador)

    sql10_sql = "INSERT INTO RegistrosTRUSTED (dadosCapturados, dataHora, fkComponente, fkIdServidor) VALUES (%s, %s, %s, %s)"
    values10_sql = (nucleos_fisicos, dia.strftime('%Y-%m-%d %H:%M:%S'), 10, 5)

    sql11_sql = "INSERT INTO RegistrosTRUSTED (dadosCapturados, dataHora, fkComponente, fkIdServidor) VALUES (%s, %s, %s, %s)"
    values11_sql = (nucleos_logicos, dia.strftime('%Y-%m-%d %H:%M:%S'), 11, 5)

    sql12_sql = "INSERT INTO RegistrosTRUSTED (dadosCapturados, dataHora, fkComponente, fkIdServidor) VALUES (%s, %s, %s, %s)"
    values12_sql = (frequencia_hz, dia.strftime('%Y-%m-%d %H:%M:%S'), 12, 5)


    try:
        # Executa a inserção
        cursor_sql_server.execute(sql8_sql, values8_sql)
        cursor_sql_server.execute(sql9_sql, values9_sql)
        cursor_sql_server.execute(sql10_sql, values10_sql)
        cursor_sql_server.execute(sql11_sql, values11_sql)
        cursor_sql_server.execute(sql12_sql, values12_sql)

        # Confirma as alterações no banco de dados
        sql_server_cnx.commit()
        print("Inserção de dados realizada com sucesso!")

    except pymssql.OperationalError as op_err:
        print("Erro operacional ao inserir nas tabelas:", op_err)
    except pymssql.ProgrammingError as prog_err:
        print("Erro de programação ao inserir nas tabelas:", prog_err)
    except Exception as e:
        print("Erro inesperado ao inserir nas tabelas:", e)

    time.sleep(1)
