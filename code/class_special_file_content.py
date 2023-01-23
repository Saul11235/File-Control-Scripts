# class explorer .filepush filepull file
# -------------------------------------

# -------------------------------------

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

def is_string_path(line_text): # for decode command
    if line_text.find("##")!=-1: return True
    else: return False

#----------------------------

def clear_list(list_to_clear):
    list_response=[]
    for x in list_to_clear:
        line=uncoment_line(x)
        clean_line=clear_spaces(line)
        if clean_line!="" and clean_line!="-" and clean_line!="##":
            list_response.append(clean_line)
    return(list_response)

#----------------------------
def is_negative_input(string):
    if string[0]=="-": return True
    else: return False
#----------------------------
def smart_split_for_path(string):
    # return  [path commands]
    text=string.replace("##","")
    text=clear_spaces(text)
    if text=="": return ["",[]]
    #-----
    if text[0]=="'" or text[0]=='"':
        separator=text[0]
        path=""
        str_commands=""
        list_commands=[]
        first=False
        second=False
        for x in text:
            if x==separator:
                if first: second=True
                else: first=True
            else:
                if second: str_commands=str_commands+x
                else: path=path+x
        path=clear_spaces(path)    
        str_commands=clear_spaces(str_commands)
        list_commands=str_commands.split(" ")
        return [path,list_commands][:]
    else:
        list_vars=text.split(" ")
        first=True
        path=""
        commands=[]
        for x in list_vars:
            if first: first=False; path=x
            else: commands.append(x)
         
        return [path,commands][:]
    #-----

#----------------------------

def compute_group(list_args):
    first=True
    path=""
    commands=[]
    positive=[]
    negative=[]
    for x in list_args:
        if first:
            first=False
            #clear path and commands
            atributes_path=smart_split_for_path(x)
            path=atributes_path[0]
            commands=atributes_path[1]
        else:
            neg=clear_spaces(x[1:len(x)])
            if is_negative_input(x): negative.append(neg)
            else: positive.append(x)
    return([path,commands,positive,negative][:])

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
    computed_paths=[]
    for x in all_content:
        computed_paths.append(compute_group(x))
    return computed_paths    




#----------------------------

class special_file_content:

    def __init__(self):
        self.text=""
        self.list=[]
        #---------
        self.IndexPath  =[] #path  beggins on ##

    def add_text(self,text):
        self.text=str(text)
        self.__configure_atributes()

    def __configure_atributes(self):
        #----------------
        self.list=compute_text(self.text)
        #----------------

    def return_lists(self): return self.list




#------------------------

if __name__=="__main__":
    print("test")
    a=special_file_content()
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
    for x in a.return_lists():
        print("""["path",[commands],[positive args][negative_args]]""")
        print(x)
        print("-------")




