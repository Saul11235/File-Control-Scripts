# class explorer .filepush filepull file

def uncoment_line(text):
    if not(text.find("##"))==-1: return text.replace("##"," ## ")[:]
    else: 
        response="";comment=False
        for x in text:
            if x=="#":comment=True
            if not(comment):response=response+x
        return response[:]

#----------------------------

def clear_spaces(text):
    var_text=text.replace("\t"," ")[:]
    while  var_text.find("  ")!=-1:
        var_text=var_text.replace("  "," ")[:]
    response="";  First=True;  Limit=len(var_text)    
    #----------
    for x in range(Limit):
        char=var_text[x]
        if First:
            First=False
            if char!=" ":response=response+char
        else:    
            if x>=Limit-1 and char!=" ":
                response=response+char
            elif x>=Limit-1 and char==" ":pass
            else:response=response+char
    return response

#----------------------------
def clear_list(list_to_clear):
    list_response=[]
    for x in list_to_clear:
        line=uncoment_line(x)
        clean_line=clear_spaces(line)
        if clean_line!="":list_response.append(clean_line)
    return list_response

#----------------------------

class special_file:

    def __init__(self):
        self.text=""
        #---------
        self.IndexPath  =[] #path  beggins on ##
        self.path_True  =[]
        self.path_False =[]
        self.file_True  =[]
        self.file_False =[]


    def add_text(self,text):
        self.text=str(text)
        self.__configure_atributes()

    def __configure_atributes(self):
        self.IndexPath  =[]
        self.path_True  =[]
        self.path_False =[]
        self.file_True  =[]
        self.file_False =[]
        #----------------
        list_text_input=self.text.split("\n")
        lines_uncoment=clear_list(list_text_input)
        #----------------
        print(lines_uncoment)











#------------------------

if __name__=="__main__":
    print("test")
    a=special_file()
    nn="""
# askldfklasd    
# alajskldfjsad
## C:/img/04-Puertas
 *.pdf
 *.xls
   ##corintians           \t   .
 holo #comment
 kasjdfkl
## "kddk  ddd" clear_origin
 dkdkd
    """
    print(nn)
    print("------------")
    a.add_text(nn)




