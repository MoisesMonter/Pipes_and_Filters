import pandas as pd



class Info_Alunos():
    def __init__(self,aluno_info,titulo):
        self.a_if = aluno_info
        self.titulo = titulo

    def planilha(self):
        '''se Passar All como parametro, Será pego todos no filtro'''
        planilha = pd.read_excel("Dados_Alunos.xlsx")
        planilha2 = None
        planilha3 = None
        #Filtrar Por Ano
        if str(self.a_if['Ano']).lower() != 'all':
            planilha2 = planilha[planilha['Ano']==self.a_if['Ano']]
        else:
            planilha2 = planilha[planilha['Ano']!='a']
        del(planilha)#tirar da memória

        #Filtrar Por Turma
        if str(self.a_if['Turma']).lower() != 'all':
            planilha3 = planilha2[planilha2['Turma']=='ADS']
        else:
            planilha3 = planilha2[planilha2['Turma']!='0']
        del(planilha2)#tirar da memória
        print(planilha3)
        return planilha3

    def main(self):
        #Filtrar listas
        dados = self.planilha()
        print(dados)
        #Html
        html = "<body>"
        html1 =  self.body(dados)
        html += html1+"<body>"
        return html

    def body(self,dados):
        html = "<h1> "+self.titulo+" </h1>"

        html+= "<h3>Truma: "+str(self.a_if['Turma'])+" </h3>"
        html+= "<h3>Ano: "+str(self.a_if['Ano'])+" </h3>"
        
        '''for Titulos in dados:#Informações da Coluna da tabela
            if Titulos != 'Aluno':
                html+= "<h3> "+Titulos+": "+str(dados[Titulos][0])+" </h3>"'''


        html += "<h3>Alunos:</h3><ul>"
        for nome_em_listas in dados['Aluno']:#Lista de Alunos
            html+="<li>"+nome_em_listas+"</li>"
        html += "</ul>"
        
        return html



