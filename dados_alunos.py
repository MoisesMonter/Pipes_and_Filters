import pandas as pd


class Dados_Alunos():
    def __init__(self,Ano_Turma):
        self.at = Ano_Turma
        self.tabela = 

def Planilha(aluno_info):
    planilha = pd.read_excel("Dados_Alunos.xlsx")
    planilha2 = planilha[planilha['Anos']==5]
    planilhaend = planilha2[planilha2['Turmas']=='ADS'] 
    print(planilhaend)
    return planilhaend