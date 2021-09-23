import os #importando a biblioteca os
import time #importando a biblioteca time (trabalha com o tempo)

with open("hosts.txt", "r") as file: #com a abertura do hosts.txt como arquivo, foi criada uma variável chamada dump, e depois vai ler o arquivo e jogar pra variável dump
    dump = file.read()
    dump = dump.splitlines()

    for ip in (dump): #colocando dump em linhas separadas, para cada ip no dump, printar verificando o ip
        print("Verificando o ip: ", ip)
        print("-" * 60)
        os.system("ping -n 2 {}".format(ip)) #vai jogar o comando pra enviar dois pacotes
        print("-" * 60)
        time.sleep(1) #espera de 1 segundo de um comando para outro.
