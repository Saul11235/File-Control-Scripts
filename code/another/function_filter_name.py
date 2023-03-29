#  filter to analize filenames
#
#  filter_name(name,filter)
#
#  return True or False if approppiate 
#
# ------------------------------

def __replace_only_one(full_text,part):
    #function to replace the parts
    # if to_replace=""
    if not(__is_on_string(full_text,part)) or part=="":
        return full_text[:]
    else:
        original=full_text[:]
        changed=original[:].replace(part,"*"*len(part))
        # vars to analize if change new character
        count=full_text.find(part) #number of chars before the part
        count=count+len(part)    
        replaced=""
        for x in range(len(full_text)):
            if x<count: replaced=replaced+"*"
            else: replaced=replaced+original[x]
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
    if name==" "*len(filterr): return False
    # case * full text
    if __is_on_string(filterr,"*"):
        # case only a *
        if filterr=="*": return True
        # sorting
        list_filter=filterr.split("*")
        if not(len(list_filter)): return False
        new_text=name[:]
        for x in list_filter:
            if __is_on_string(new_text,x):
                new_text=__replace_only_one(new_text,x)[:]
            else: return False
        # compare newtext
        if new_text==len(new_text)*"*": return True
        else: 
            # verify +final * case
            if len(list_filter):
                last=list_filter[len(list_filter)-1]
                if last=="":return True
            return False
    else: return False

# ----------------------------------

if __name__=="__main__":
    print("test filter name\n")
    names=["hola","file.txt","holo.pdf","raaa.pdfkk","dato3julio.dox","poli.mp3","poli.pdf"]
    filters=["*.pdf","hola","dato*julio.dox","poli.*"]
    #-------
    for name in names:
        for fil in  filters:
            print("name: "+str(name)+
                    " \tfilter: "+str(fil)+
                    " \tstatus: "+str(
                        filter_name(name,fil)))
    #.......................





