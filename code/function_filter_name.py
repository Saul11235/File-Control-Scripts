#  filter to analize filenames
#
#  filter_name(name,filter)
#
#  return True or False if approppiate 
#
# ------------------------------

def __replace_only_one(full_text,part):
    # if to_replace=""
    if __is_on_string(full_text,part):
        text=full_text[:]
        return text
    else:
        replaced="dd"
        # comparing
        return replaced


#--------------------------------

def __is_on_string(full_text,part):
    try: 
        a=full_text.index(part);
        return True
    except: return False

#--------------------------------

def filter_name(name,filterr):
    # case specific
    if name==filterr: return True
    # case no name
    if name=="": return False
    # case * full text
    if __is_on_string(filterr,"*"):
        # case only a *
        if filterr=="*": return True
        # sorting
        list_filter=filterr.split("*")
        # print(list_filter)
        new_text=name[:]
        print("text strings")
        print(new_text)
        for x in list_filter:
            if __is_on_string(new_text,x):
                new_text=__replace_only_one(new_text,x)[:]
            else: return False
        print(new_text)
        # compare newtext
        if new_text==len(new_text)*"*": return True
        else: return False
    else: return False

# ----------------------------------

if __name__=="__main__":
    print("test filter name\n")
    names=["hola","file.txt","holo.pdf","raaa.pdfkk"]
    filters=["*.pdf","hola"]
#    names=[]
    #-------
    for name in names:
        for fil in  filters:
            print("name: "+str(name)+
                    " \tfilter: "+str(fil)+
                    " \tstatus: "+str(
                        filter_name(name,fil)))
    #.......................





