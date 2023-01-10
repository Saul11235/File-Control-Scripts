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
        print("itsnt")
        text=full_text[:]
        return text
    else:
        # comparing
        print("its on")
        original=full_text[:]
        new=full_text[:].replace(part,"*"*len(part))
        replaced=""
        # cicle of comparating
        first_diferent=False
        end_first_diferent=False
        for x in range(len(original)):
            let_org=original[x]
            let_new=new[x]
            its_equal=let_org==let_new
            c="" #character to change
            #--------------------
            if end_first_diferent: c=let_org
            else: #no end_first_diferent
                if first_diferent:
                    if its_equal: c=let_new
                    else: c=let_new;end_first_diferent=True
                else: #not first_diferent
                    if its_equal: c="*"
                    else: c=let_new,first_diferent=True 
            #---------------------
            replaced=replaced+c
            pass
        print("......")
        print(original)
        print(new)
        print(replaced)
        print("......")
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
        for x in list_filter:
            new_text=__replace_only_one(new_text,x)
        # compare newtext
        if new_text==len(new_text)*"*": return True
        else: return False
    else: return False

# ----------------------------------

if __name__=="__main__":
    print("test filter name\n")
    names=["hola","file.txt","holo.pdf","raaa.pdfkk"]
    filters=["*.pdf","hola"]
    #-------
    for name in names:
        for fil in  filters:
            print("name: "+str(name)+
                    " \tfilter: "+str(fil)+
                    " \tstatus: "+str(
                        filter_name(name,fil)))
