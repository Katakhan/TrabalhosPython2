fortwo = []
embarcados = []
terminal = ['piloto','official1','official2','comissaria1','comissaria2','chefe','policial','ladrao']
def viagem1(terminal,fortwo,embarcados):
    print('~~'*40, '1º Viagem','~~'*40)
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

def viagem2(terminal,fortwo,embarcados):
    print('~~'*40, '2º Viagem','~~'*40)
    hsaida = input('informe o horario de saida')
    hchegada = input('informe o horario de chegada')
    hora = {'Hs':hsaida ,'Hc':hchegada}
    terminal.remove('official2')
    print(f'pessoas no terminal: {terminal}')
    fortwo.append('official2')
    fortwo.append('piloto')
    print(f'Pessoas que passaram pelo fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
    embarcados.append('official2')
    fortwo.remove('official2')
    print(f'pessoas no avião {embarcados}')
    print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')

def viagem3(terminal,fortwo,embarcados):
    print('~~'*40, '3º Viagem','~~'*40)
    hsaida = input('informe o horario de saida')
    hchegada = input('informe o horario de chegada')
    hora = {'Hs':hsaida ,'Hc':hchegada}
    terminal.remove('chefe')
    terminal.remove('comissaria1')
    terminal.append('piloto')
    print(f'pessoas no terminal: {terminal}')
    fortwo.remove('piloto')
    fortwo.remove('piloto')
    fortwo.append('chefe')
    fortwo.append('comissaria1')
    print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
    embarcados.append('comissaria1')
    fortwo.remove('comissaria1')
    print(f'pessoas no avião {embarcados}')
    print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')     

def viagem4(terminal,fortwo,embarcados):
    print('~~'*40, '4º Viagem','~~'*40)
    hsaida = input('informe o horario de saida')
    hchegada = input('informe o horario de chegada')
    hora = {'Hs':hsaida ,'Hc':hchegada}
    terminal.remove('piloto')
    print(f'pessoas no terminal: {terminal}')
    fortwo.append('piloto')
    fortwo.append('chefe')
    print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
    embarcados.append('piloto')
    fortwo.remove('piloto')
    print(f'pessoas no avião {embarcados}')
    print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')

def viagem5(terminal,fortwo,embarcados):
    print('~~'*40, '5º Viagem','~~'*40)
    hsaida = input('informe o horario de saida')
    hchegada = input('informe o horario de chegada')
    hora = {'Hs':hsaida ,'Hc':hchegada}
    terminal.remove('comissaria2')
    terminal.append('piloto')
    print(f'pessoas no terminal: {terminal}')
    fortwo.append('comissaria2')
    fortwo.remove('chefe')
    print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
    embarcados.append('comissaria2')
    embarcados.remove('piloto')
    embarcados.append('chefe')
    fortwo.remove('comissaria2')
    fortwo.remove('chefe')
    print(f'pessoas no avião {embarcados}')
    print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')

def viagem6(terminal,fortwo,embarcados):
    print('~~'*40, '6º Viagem','~~'*40)
    hsaida = input('informe o horario de saida')
    hchegada = input('informe o horario de chegada')
    hora = {'Hs':hsaida ,'Hc':hchegada}
    terminal.remove('policial')
    terminal.remove('ladrao')
    terminal.append('chefe')
    print(f'pessoas no terminal: {terminal}')
    fortwo.append('policial')
    fortwo.append('ladrao')
    print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
    fortwo.append('chefe')
    embarcados.append('ladrao')
    embarcados.append('policial')
    embarcados.remove('chefe')
    fortwo.remove('ladrao')
    fortwo.remove('policial')
    print(f'pessoas no avião {embarcados}')
    print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')

def viagem7(terminal,fortwo,embarcados):
    print('~~'*40, '7º Viagem','~~'*40)
    hsaida = input('informe o horario de saida')
    hchegada = input('informe o horario de chegada')
    hora = {'Hs':hsaida ,'Hc':hchegada}
    terminal.remove('piloto')
    print('terminal vaziu')
    fortwo.append('piloto')
    print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
    embarcados.append('chefe')  
    embarcados.append('piloto')
    fortwo.remove('piloto')
    print(f'pessoas no avião {embarcados}')
    print(f'A hora de saida foi: {hora["Hs"]} e a de chegada foi {hora["Hc"]}')


hsaida = ''
hchegada = ''
hora = {'Hs':hsaida ,'Hc':hchegada}
print('~~'*40, 'Bem Vindo','~~'*40)
print('Tripulação completa = Piloto, Chefe de serviço de bordo, 2 comissárias , 1 policial e 1 ladrao, 2 oficiais')
print('Etinerário:\n 1 viagem - piloto + oficial \n2 viagem - piloto + oficial \n 3 viagem - chefe + comissaria \n 4 viagem - chefe + piloto \n 5 viagem -chefe + comissaria \n 6 viagem - policia + ladrao \n 7 viagem - chefe + piloto ')
print('~~'*80)
proc = input('Deseja iniciar? s/n')
while proc == 's':

    opcao = input('qual viagem voce gostaria de consultar?')
    if opcao == '1':
        viagem1(terminal,fortwo,embarcados)
        
    elif opcao == '2':
        viagem2(terminal,fortwo,embarcados)
    elif opcao == '3':
        viagem3(terminal,fortwo,embarcados)
    elif opcao == '4':
        viagem4(terminal,fortwo,embarcados)
    elif opcao == '5':
        viagem5(terminal,fortwo,embarcados)

    elif opcao == '6':
        viagem6(terminal,fortwo,embarcados)
    elif opcao == '7':
        viagem7(terminal,fortwo,embarcados)
    else: 
        print('Opção inexistente, voltar para o menu')
    proc = input('Deseja iniciar? s/n')


    