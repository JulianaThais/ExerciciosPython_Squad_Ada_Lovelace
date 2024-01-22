#ExercíciosTuplas,ListaseDicionários
#1.Utilizandolistasfaçaumprogramaquefaça5perguntasparaumapessoasobreumcrime.
'''O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
2 sim classificacao ""Suspeita"", 3 4 cúmplice" 5  ""Assassino"".
Casocontrário,eleseráclassificadocomo""Inocente"".'''

Classificacao = 0

programa_perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?','Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']

for pergunta in programa_perguntas:

   print(pergunta)

   resposta = input(' ').lower( ).replace( 'ã' , 'a' )

   if resposta == 'sim':
    Classificacao +=1
# Oprogramadevenofinalemitirumaclassificaçãosobreaparticipaçãodapessoanocrime.
       

if Classificacao == 2:
    

   print('É um suspeito...')

elif 3 <= Classificacao<= 4:

   print('É um cúmplice!')

elif Classificacao == 5:

   print('É um assassina(o)!')

else:

   print('É um inocente.')


