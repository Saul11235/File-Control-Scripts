
from os.path import isfile
from os import getcwd
from os import get_terminal_size

try:    from get_info_from_file  import get_info
except: from .get_info_from_file import get_info

try:    from class_special_file_content  import special_file_content
except: from .class_special_file_content import special_file_content

cicles=0;line_count=abs(list(get_terminal_size())[0]-1)

def line_break(): print(line_count*"-")
#----------------------------------


def pull(path):
    info=get_info(path,".filepull")
    # ---------------------------------
    # structure instructions
    # [in1  in2 ---]
    #  in  = [path, [commands],[positive],[negative]]
    # ----------------------------------
    instructions=special_file_content()
    instructions.add_text(info)
    list_=instructions.return_lists()
    for arg in list_:
        #-- cicle actions -----  []
        cicle_pull(path,arg[0],arg[1:4][:])
    line_break()    
    print(" Total cicles: "+str(cicles))
    line_break()    

#-----------------------------------

def cicle_pull(path1,path2,arguments):
    global cicles
    cicles=cicles+1  #counter var
    line_break()
    print(" PULL       cicle: "+str(cicles))
    print("  from:     "+str(path1))
    print("  to:       "+str(path2))
    print("  commands: "+str(arguments[0]))
    print("  positive: "+str(arguments[1]))
    print("  negative: "+str(arguments[2]))






text_default="""
# filepull -  by Edwin Saul - @Saul11235
# use # for comment
# use ##  for set destination path
# write bellow extensions, file names or folder names to pull

"""

if __name__=="__main__":

    if isfile(".filepull"):
        pull((getcwd()))
    else: 
        f=open(".filepull","w")
        f.write(text_default)
        f.close()
        print(".filepull created!")

