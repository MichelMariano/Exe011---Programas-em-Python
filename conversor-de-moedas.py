#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres, euro e iene ela pode comprar:

Considere dolar 1,00 = 5.02 cotação dia 30/03/24
Considere euro 1,00 = 5.42  cotação dia 30/03/24
Considere iene 1,00 =  0.033 cotação dia 30/03/24

real = float(input('Quanto tenho na Carteira? R$ '))

dolar = real / 5.02 #cotação dolar dia 30/03/24
euro = real / 5.42 #cotação euro dia 30/03/24
iene = real / 0.033 #cotação iene dia 30/03/24

print('Com R$ {:.2f} consigo comprar {:.2f} US$ '.format(real, dolar))
print('Com R$ {:.2f} consigo comprar {:.2f} Euro '.format(real, euro))
print('Com R$ {:.2f} consigo comprar {:.2f} Iene '.format(real, iene))
