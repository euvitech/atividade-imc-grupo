nome = input("Como posso te chamar? ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/altura**2

print("{}, seu IMC é de {:.2f}".format(nome, imc))

if imc < 18.5:
    print("Com magreza")
    print("Recomendação: Exercícios como levantamento de peso, musculação e treinamento com pesos podem ajudar a construir músculos e promover um ganho de peso saudável")
elif imc >= 18.5 and imc < 25:
    print("meus parabéns, seu peso está normal")
elif imc >= 25 and imc < 30:
    print("Com sobrepeso")
    print("Recomendação: iniciar uma atividade física, mesmo que não seja na intensidade ideal ainda, mas que pode ir progredindo ao longo do tempo")
elif imc >= 30 and imc < 40:
    print("Com obesidade")
    print("Recomendação: iniciar uma atividade física, mesmo que não seja na intensidade ideal ainda, mas que pode ir progredindo ao longo do tempo")
else:
    print("Com obesidade grave")
    print("Recomendação: iniciar uma atividade física, mesmo que não seja na intensidade ideal ainda, mas que pode ir progredindo ao longo do tempo")








    


