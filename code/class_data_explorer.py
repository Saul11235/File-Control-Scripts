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

def get_path_atributes(line_text):
    text=line_text.replace("##","")
    print(text)

#----------------------------

def is_string_path(line_text):
    if line_text.find("##")!=-1: return True
    else: return False

#----------------------------

def clear_list(list_to_clear):
    list_response=[]
    for x in list_to_clear:
        line=uncoment_line(x)
        clean_line=clear_spaces(line)
        if clean_line!="" and clean_line!="-":
            list_response.append(clean_line)
    return(list_response)

#----------------------------
def is_negative_input(string):
    if string[0]=="-": return True
    else: return False
#----------------------------

def compute_group(list_args):
    print("#################################")
    first=True
    path="pp"
    commands=[]
    positive=[]
    negative=[]
    for x in list_args:
        if first:
            first=False
            #clear path and commands
            
        else:
            neg=clear_spaces(x[1:len(x)])
            if is_negative_input(x): negative.append(neg)
            else: positive.append(x)
    print(list_args)
    print(positive)
    print(negative)


#----------------------------

def compute_text(text_to_order):
    #
    # return lists
    # [  [path, commands, positive_args, negative_args ] ..... ]
    #
    split_text=str(text_to_order).split("\n")
    clean_content=clear_list(split_text)
    have_path=False
    all_content=[]
    content=[]
    for x in clean_content:
        if is_string_path(x):
            have_path=True
            if len(content):
                all_content.append(content[:])
                content=[x]
            else: content.append(x)
        else:
            if have_path:
                content.append(x)
    if len(content):all_content.append(content)
    #---------
    for x in all_content:
        compute_group(x)




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
        l=compute_text(self.text)
        #----------------











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
 -l
 kasjdfkl
## "kddk  ddd" clear_origin
 dkdkd
 - ajskldj
 -
 o
 -*.swp
    """
    print(nn)
    print("------------")
    a.add_text(nn)




