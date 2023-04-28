class Head_info():
    def __init__(self,list):
        self.filter_meta = list
        self.save =""
        self.rota=[]
    
    def main(self):
        self.save+="<head>"
        self.metas()
        self.save+="</head>"
        return self.save,self.rota
    '''
    1-As listas devem existir utf-16 ou será normalizado inexistencia utf, utf-8 será padrão.
    2-Titulo tem que existir na lista meta com as tag -t:, ou nome page será usado como padrão
    3- viewport padrão
    4-passar css para criar rota css
    5-passar js para criar rota
    '''
    def metas(self):
        #UTF 8/16
        utf = "'utf-8'" if "'utf-16'" not in self.filter_meta else "'utf-16'"
        self.save+="<meta charset="+utf+">"
        del(utf)

        #TITLE
        title = ""
        for x in self.filter_meta:
            if x[:3] == "-t:":
                title="'"+x[3:]+"'"
        self.save+=" <title>"+title+"</title>"
        del(title)

        #viewport
        self.save+=" <meta name='viewport' content='width=device-width, initial-scale=1'>"

        #css
        self.save+="<link rel='stylesheet' type='text/css' media='screen' href='main.css'>" if "css" in self.filter_meta else ""
        self.rota.append('main.css' if 'css' in self.filter_meta else None)
        #js
        self.save+="<script src='main.js'></script>" if "js" in self.filter_meta else ""
        self.rota.append('main.js' if 'js' in self.filter_meta else None)


        
