# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. o,É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bord e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

fortwo = []
embarcados = []
terminal = ['piloto','official1','official2','comissaria1','comissaria2','chefe','policial','preso']
hsaida = ''
hchegada = ''
hora = {'Hs':hsaida ,'Hc':hchegada}
print('Tripulação completa = Piloto, Chefe de serviço de bordo, 2 comissárias , 1 policial e 1 preso, 2 oficiais')
print('Etinerário:\n 1 viagem - piloto + oficial \n2 viagem - piloto + oficial \n 3 viagem - chefe + comissaria \n 4 viagem - chefe + piloto \n 5 viagem -chefe + comissaria \n 6 viagem - policia + preso \n 7 viagem - chefe + piloto ')
proc = input('Deseja iniciar? s/n')
while proc == 's':

    opcao = input('qual viagem voce gostaria de consultar?')
    if opcao == '1':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('official1')
        terminal.remove('piloto')
        print(f'pessoas no terminal: {terminal}')
        fortwo.append('piloto')
        fortwo.append('official1')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('official1')
        fortwo.remove('official1')
        print(f'pessoas no avião {embarcados}')
        print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')
    elif opcao == '2':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('official2')
        terminal.append('Chefe')
        terminal.append('Comissaria1')
        terminal.append('Comissaria2')
        terminal.append('Policial')
        terminal.append('Ladrão')
        print(f'pessoas no terminal: {terminal}')
        fortwo.append('official2')
        fortwo.append('piloto')
        print(f'Pessoas que passaram pelo fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('official1')
        embarcados.append('official2')
        fortwo.remove('official2')
        print(f'pessoas no avião {embarcados}')
        print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')
    elif opcao == '3':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('chefe')
        terminal.remove('comissaria1')
        terminal.append('piloto')
        terminal.append('Comissaria2')
        terminal.append('Policial')
        terminal.append('Ladrão')
        print(f'pessoas no terminal: {terminal}')
        fortwo.append('chefe')
        fortwo.append('comissaria1')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('comissaria1')
        embarcados.append('official1')
        embarcados.append('official2')
        fortwo.remove('comissaria1')
        print(f'pessoas no avião {embarcados}')
        print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')       
    elif opcao == '4':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('piloto')
        terminal.append('Policial')
        terminal.append('Ladrao')
        print(f'pessoas no terminal: {terminal}')
        fortwo.append('piloto')
        fortwo.append('chefe')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('piloto')
        embarcados.append('comissaria1')
        embarcados.append('official1')
        embarcados.append('official2')
        fortwo.remove('piloto')
        print(f'pessoas no avião {embarcados}')
        print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')
    elif opcao == '5':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('comissaria2')
        terminal.append('piloto')
        terminal.append('policial')
        terminal.append('Ladrao')
        print(f'pessoas no terminal: {terminal}')
        fortwo.append('chefe')
        fortwo.append('comissaria2')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('comissaria2')
        embarcados.append('comissaria1')
        embarcados.append('official1')
        embarcados.append('official2')
        fortwo.remove('comissaria2')
        print(f'pessoas no avião {embarcados}')
        print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}') 

    elif opcao == '6':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.append(piloto)
        terminal.remove('policial')
        terminal.remove('ladrao')
        terminal.append('chefe')
        print(f'pessoas no terminal: {terminal}')
        fortwo.append('policial')
        fortwo.append('ladrao')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('ladrao')
        embarcados.append('policial')
        embarcados.append('comissaria2')
        embarcados.append('comissaria1')
        embarcados.append('official1')
        embarcados.append('official2')
        fortwo.remove('ladrao')
        fortwo.remove('policial')
        fortwo.append('chefe')
        print(f'pessoas no avião {embarcados}')
        print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')
    elif opcao == '7':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('piloto')
        print('terminal vaziu')
        fortwo.append('chefe')
        fortwo.append('piloto')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('chefe')
        embarcados.append('ladrao')
        embarcados.append('policial')
        embarcados.append('comissaria2')
        embarcados.append('piloto')
        embarcados.append('comissaria1')
        embarcados.append('official1')
        embarcados.append('official2')
        fortwo.remove('chefe')
        fortwo.remove('piloto')
        print(f'pessoas no avião {embarcados}')
        print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')
    else: 
        print('Opção inexistente, voltar para o menu')
    proc = input('Deseja iniciar? s/n')