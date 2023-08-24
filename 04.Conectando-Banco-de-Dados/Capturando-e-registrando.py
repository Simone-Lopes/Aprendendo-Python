import mysql.connector
import psutil
import platform
import time

while True:
    CPU1 = psutil.cpu_percent(interval=1)
    CPU2 = CPU1 + (CPU1 * 0.10)
    CPU3 = CPU2 - (CPU2 * 0.05)
    MEM1 = psutil.swap_memory()[3]
    MEM2 = MEM1 + (MEM1 * 0.15)
    MEM3 = MEM2 - (MEM2 * 0.05)
    DISC1 = psutil.disk_usage('C:\\').percent
    DISC2 = DISC1 - (DISC1 * 0.05)
    DISC3 = DISC2 * 3
    meu_so = platform.system()

    # Valores obtidos das métricas do sistema
    processador = CPU1
    memoria = MEM1
    disco = DISC1
    SO = meu_so
    fkTotens = 1  # Use o ID da unidade correta

    sql1 = "INSERT INTO liltotem (processador, memoria, disco, SO, fkTotens) VALUES (%s, %s, %s, %s, %s)"
    values1 = [processador, memoria, disco, SO, fkTotens]

    processador = CPU2
    memoria = MEM2
    disco = DISC2
    SO = meu_so
    fkTotens = 2  # Use o ID da unidade correta

    sql2 = "INSERT INTO liltotem (processador, memoria, disco, SO, fkTotens) VALUES (%s, %s, %s, %s, %s)"
    values2 = [processador, memoria, disco, SO, fkTotens]

    processador = CPU3
    memoria = MEM3
    disco = DISC3
    SO = meu_so
    fkTotens = 3  # Use o ID da unidade correta

    # SQL para inserir na tabela dados
    sql3 = "INSERT INTO liltotem (processador, memoria, disco, SO, fkTotens) VALUES (%s, %s, %s, %s, %s)"
    values3 = [processador, memoria, disco, SO, fkTotens]

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='APUXxx2707',
            database='Totem'
        )
        cursor = connection.cursor()
        # Executa a inserção
        cursor.execute(sql1, values1)
        cursor.execute(sql2, values2)
        cursor.execute(sql3, values3)

        # Confirma as alterações no banco de dados
        connection.commit()
        print("Inserção de dados realizada com sucesso!")

    except mysql.connector.Error as err:
        print("Erro ao inserir os dados:", err)

    time.sleep(5)  # Espera por 5 segundos antes de executar novamente

# Fecha o cursor e a conexão
cursor.close()
connection.close()
