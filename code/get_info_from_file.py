from platform import system
from os.path  import isfile

#---------------------------------

slash="/"
if system()=="Windows":slash="\\"

#--------------------------------

def uniform_slash_path(name,slash):
    help_string=name.replace("/",str(slash))
    replaced=help_string.replace("\\",slash)
    return replaced[:]

#--------------------------------

def is_slash_ended(name,slash):
    try:   return  name[-1]==slash
    except:return False

#--------------------------------

def get_info (path,namefile):
    # return "" string if no data
    path=uniform_slash_path(path,slash)
    if not(is_slash_ended(path,slash)):path=path+slash
    npath=path+str(namefile) #full path of data file
    information=""
    #-------------
    if isfile(npath):
        try:
            file_=open(npath,mode="r",encoding="utf-8")
            information=file_.read()[:]
        except:pass
    return information

#--------------------------------

if __name__=="__main__":

    pass
