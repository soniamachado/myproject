

import segno #mais recente e leve
from datetime import date
hoje=date.today()
indice_dia=hoje.weekday() #0=segunda, 6=domingo

menu="Menu de hoje:"+str(hoje)+"\n"
menu=menu+"Sopa 1.2€ \n"
menu=menu+"legumes 1.8€\n"
menu=menu+"prato do dia 5.9€"

qrcode=segno.make_qr(menu)
qrcode.save(r"/home/sonia_machado/myproject/python/menu.png",
            scale=5,
            border=10,
            dark='darkred',
            light='lightblue')

print('exercicio8')
import segno #mais recente e leve
from datetime import date


pratos_semana=[
    ["Domingo", "Sopa 2.1€", "Feijoada 6.5€"],#Pratos de domingo
    ["Segunda-feira","Cabrito 5.0€", "Bacalhau 7.5€"],#Pratos de segunda-feira
    ["Terça-feira","Lasanha 5.5€","Peixe Grelhado 6.8€"],#Pratos de terça-feira
    ["Quarta-feira","Esparguete 4.5€", "Frango Assado 6.0€"],#Partos de quarta-feira
    ["Quinta-feira", "Salmão 8.0€", "Carne de Porco 7.0€"],#Pratos de quinta-feira
    ["Sexta-feira","Pizza 6.0€","Bacalhau à Brás 7.0€"],#Pratos de sexta-feira
    ["Sábado", "Churrasco 8.5€", "Grelhado 7.0€"]#Pratos de sábado
]
hoje=date.today()
indice_dia=hoje.weekday() #0=segunda, 6=domingo
#apresenta o menu
for i in range(len(pratos_semana)):
    nome_dia=pratos_semana[i][0] #o primeiro é o prato do dia
    pratos=','.join(pratos_semana[i][1:])#outros pratos
    print (f'Pratos disponíveis para {nome_dia}: {pratos}')
#apresenta o prato do dia, de acordo com dia exato
for i in range(len(pratos_semana)):
    if pratos_semana[i][0]==indice_dia:
        dia=pratos_semana[i][0] #o primeiro é o prato do dia
        for prato in range(1, len(pratos_semana[i][1:])):
            print (f'Para {indice_dia}, temos o prato: {[prato]}')
            #Guardar o prato atual para gerar o QRCode (se só quiser o último prato)
            prato_para_qr=prato
    break # para parar o loop depois de encontrar o dia corretp, evitando processamento desnecessário

qrcode=segno.make_qr(prato_para_qr)
qrcode.save(r"/home/sonia_machado/myproject/python/menu.png",
            scale=5,
            border=10,
            dark='darkred',
            light='lightblue')