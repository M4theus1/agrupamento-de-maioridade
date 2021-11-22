from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range (1, 8):
    nasc = int(input('Em que ano a {}a pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior+= 1
    else:
        totmenor += 1
print('='*16)
print('C O N T A G E M')
print('='*16)
print('Ao todo tivemos {} pessoas de maior!'.format(totmaior))
print('E também tivemos {} pessoas de menor'.format(totmenor))
