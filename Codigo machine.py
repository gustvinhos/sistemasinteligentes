#pelo longo?
#perna curta?
#faz au au?

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
# 0 - cachorro
# 1 - porco

treino_y = [1,1,1,0,0,0]

from sklearn.svm import LinearSVC
#inicializar o modelo
modelo = LinearSVC()
#treinar o modelo
modelo.fit(treino_x, treino_y)

animal_misterioso = [1, 1, 1]
result = modelo.predict([animal_misterioso])

if result == 0:
  print ("Este animal é um cachorro")
if result == 1:
  print ("Este animal é um porco")


animal_misterioso1 = [1, 1, 1]
animal_misterioso2 = [1, 1, 0]
animal_misterioso3 = [0, 1, 1]

teste_x = [animal_misterioso1, animal_misterioso2, animal_misterioso3]

previsoes = modelo.predict(teste_x)

previsoes

teste_y = [0, 1, 1]


from sklearn.metrics import accuracy_score

acuracia = accuracy_score(teste_y, previsoes)

print ("A acurácia do modelo de aprendizado de máquina é de: {}%".format(acuracia * 100))


# desenvolvendo o código de um classificador não guiado

from sklearn.dummy import DummyClassifier

salva_acuracia_dummy = []
testes = 300

for i in range(testes):

  dummy = DummyClassifier(strategy="uniform")

  dummy.fit(teste_x, teste_y)

  predicao_dummy = dummy.predict(teste_x)

  acuracia_dummy = accuracy_score(teste_y, predicao_dummy)

  # print ("A acurácia do modelo dummy é de: {}%".format(acuracia_dummy * 100))

  salva_acuracia_dummy.append(acuracia_dummy)

salva_acuracia_dummy

media = 0
for i in range (testes):
  media = media + salva_acuracia_dummy[i]

print ("A média da acuracia do algoritmo dummy é: {}%".format((media/testes)*100))


