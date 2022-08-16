#
# string actions
#


def concat_strings(*args):
    nargs=[]
    for x in args:
        if not(x==" "*len(x)):
            nargs.append(x)
    string=""; first=True
    for x in nargs:
        if  first:
            first=False;
            string=str(x)
        else: 
            string+=" "+str(x)
    return string    


def is_end(string,end):
    if len(end)>len(string):
        return False
    nend=string[len(string)-len(end):len(string)]
    if nend==end:
        return True
    else:
        return False


def is_extension(extension):
    if extension[0]=="*"  and len(extension)>1:
        if extension[1]=="." and extension!="*.":
            return True
        else:
            return False
    else:
        return False


def is_folder_name(filename):
    slash_name=False
    slash_name=filename[0]=="/" or  filename[0]=="\\"
    if slash_name  and len(filename)!=1:  
        return True
    else: 
        return False


def is_exception(argument):
    first_char=""
    have_first_char=True
    for x in str(argument):
        if x==" " or x=="\t":
            pass
        else:
            if have_first_char:
                have_first_char=False
                first_char=x
    if first_char=="-":
        return True
    else:
        return False


def get_extension(extension): 
    txt="";first=True
    for x in extension:
        if first:first=False
        else: txt+=x
    return extension[1:len(extension)]


def get_exception(exception):
    text=str(exception)
    text=text.replace("\t"," ")
    list_var=text.split()
    def _del_first(string):
        lenstr=len(string)
        if lenstr==0 or lenstr==1: return ""
        return(string[1:lenstr])
    if len(list_var):
        list_response=[];first=True
        for x in list_var:
            if first:
                first=False
                list_response.append(_del_first(x))
            else: list_response.append(x)
        return concat_strings(*tuple(list_response))
    else: return ""

if __name__=="__main__":
    # test
    test="test"

    #print(concat_strings(1,2,3,4))

    #print(is_end("hola","ola"))
    #print(is_end("dd","df"))

    #print(is_extension("*.py"))
    #print(is_extension(".py"))

    #print(is_folder_name("fo"))
    #print(is_folder_name("/fo"))
    #print(is_folder_name("\\ho"))

    #print(is_exception(""))
    #print(is_exception("-"))
    #print(is_exception("  -sasdf"))

    #print(get_extension("*.exe"))
    #print(get_extension("*.xls"))
    #print(get_extension("*.pdf"))

    print(get_exception("-lolo"))
    print(get_exception("-como es esto "))
    print(get_exception("- como es esto "))
    print(get_exception("   - como es esto "))





    pass

