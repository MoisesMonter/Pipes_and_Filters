
from my_head import Head_info as head
from estilo_Arq import  Info_Alunos

def save(html):
    with open('save.html', 'w+') as arquivo:
        arquivo.write(html)


if __name__ == "__main__":
    head_info = ['utf-8','-t:Lista de Alunos','css','js']
    aluno_info= {'Ano':4,'Turma':'ALL'}
    titulo_da_pagina = "Alunos de ADS do 5 Periodo"


    htmlEND = "<!DOCTYPE html><html>" #HTML
    html,rotas =head(head_info).main() # Main
    html += Info_Alunos(aluno_info,titulo_da_pagina).main() #Body
    htmlEND +=html+"</html>" #ENDHTML
    print(htmlEND)
    save(htmlEND)

