import mysql.connector 
import psutil
import time
from datetime import datetime
import platform 

#Meu banco local
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='APUXxx2707',
    database='test'
)

cursor = connection.cursor()

# Criando a estrutura de repetição para que os valores dos componentes se atualizam
while True:
    nome_processador = platform.processor()
    arquitetura_processador = platform.architecture()[0]
    nucleos_fisicos = psutil.cpu_count(logical=False)
    nucleos_logicos = psutil.cpu_count(logical=True)
    frequencia = round(psutil.cpu_freq().current, 2)
    dia = datetime.now()

    # SQL para inserir na tabela RegistrosTRUSTED (CPU)
   
    sql7 = "INSERT INTO RegistrosTRUSTED (textosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    values7 = (nome_processador, dia.strftime('%Y-%m-%d %H:%M:%S'), 7, 1)

    sql8 = "INSERT INTO RegistrosTRUSTED (textosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    values8 = (arquitetura_processador, dia.strftime('%Y-%m-%d %H:%M:%S'), 8, 1)

    sql9 = "INSERT INTO RegistrosTRUSTED (dadosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    values9 = (nucleos_fisicos, dia.strftime('%Y-%m-%d %H:%M:%S'), 9, 1)

    sql10 = "INSERT INTO RegistrosTRUSTED (dadosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    values10 = (nucleos_logicos, dia.strftime('%Y-%m-%d %H:%M:%S'), 10, 1)

    sql11 = "INSERT INTO RegistrosTRUSTED (dadosCapturados, dataHora, fkComponente, fkIdservidor) VALUES (%s, %s, %s, %s)"
    values11 = (frequencia, dia.strftime('%Y-%m-%d %H:%M:%S'), 11, 1)

    try:
        # Executa a inserção
        cursor.execute(sql7, values7)
        cursor.execute(sql8, values8)
        cursor.execute(sql9, values9)
        cursor.execute(sql10, values10)
        cursor.execute(sql11, values11)

        # Confirma as alterações no banco de dados
        connection.commit()
        print("Inserção de dados realizada com sucesso!")

    except mysql.connector.Error as err:
        print("Erro ao inserir nas tabelas Registros:", err)

    time.sleep(1)
