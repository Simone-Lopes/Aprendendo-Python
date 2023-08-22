import psutil
import time

while True:
    limite_uso_cpu = 80
    limite_uso_disco = 90
    uso_da_cpu = psutil.cpu_percent(interval=1)
    uso_do_disco = psutil.disk_usage('C:\\').percent
    info_disco = psutil.disk_usage('C:\\')
    tamanho_disco = info_disco.total
    disco_em_uso = info_disco.used
    tamanho_em_GB = tamanho_disco / (1024**3)
    uso_em_GB = disco_em_uso / (1024**3)
    print(f"Uso da CPU: {uso_da_cpu}%")

    if 0 <= uso_do_disco <= 20:
        print(f"Disco está normal, usando: {uso_do_disco}%")
        print(f"Total de espaço em disco: {tamanho_em_GB:.2f} GB")
        print(f"Espaço em uso: {uso_em_GB:.2f} GB")
    elif uso_do_disco >= limite_uso_disco:
        print(f"Disco sendo utilizado de forma Exessiva, usando: {uso_do_disco}% de espaço")
        print(f"Total de espaço em disco: {tamanho_em_GB:.2f} GB")
        print(f"Espaço em uso: {uso_em_GB:.2f} GB")
    else:
         print(f"Disco em operação normal, usando: {uso_do_disco}% de espaço")
         print(f"Total de espaço em disco: {tamanho_em_GB:.2f} GB")
         print(f"Espaço em uso: {uso_em_GB:.2f} GB")

    if uso_da_cpu >= limite_uso_cpu:
        print(f"Limite de uso da CPU atingido. Encerrando processo.")
        break

    time.sleep(2)
