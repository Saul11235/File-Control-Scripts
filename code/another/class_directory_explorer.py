# directory_explorer for get and analize 
# paths

from os       import listdir
from os.path  import isdir,isfile
from platform import system

#-------------------------------------------
 
def uniform_slash_path(name,slash):
    help_string=name.replace("/",str(slash))
    replaced=help_string.replace("\\",slash)
    return replaced[:]

def is_slash_ended(name,slash):
    try:   return  name[-1]==slash
    except:return False


#-------------------------------------------
class directory_explorer:

    def __init__(self,path):
        self.slash="/"
        if system()=="Windows":self.slash="\\"
        #--------
        self.path=uniform_slash_path(path,self.slash)
        #--------
        self.files=[];self.dirs =[]
        self.full_files=[]; self.full_dirs=[]
        extra_strig=self.path[:]
        if is_slash_ended(self.path,self.slash):
            extra_strig=extra_strig+self.slash
        #--------
        for x in listdir(self.path):
            if isdir(x): 
                self.dirs.append(x)
                self.full_dirs.append(extra_strig+x)
            else: 
                if x!=".filepush" and x!=".filepull":
                   self.files.append(x)
                   self.full_files.append(extra_strig+x)
        #--------

    def print(self):
        print("\nPath: "+str(self.path))
        print("  Subfiles: "+str(len(self.files)))
        for x in self.files: print("    "+str(x))
        print("  Subdirs:  "+str(len(self.dirs)))
        for x in self.dirs:  print("    "+str(x))
        print("")

    def print_full(self):
        print("\nPath: "+str(self.path))
        print("  Subfiles: "+str(len(self.files)))
        for x in self.full_files: print("    "+str(x))
        print("  Subdirs:  "+str(len(self.dirs)))
        for x in self.full_dirs:  print("    "+str(x))
        print("")
        pass

    def get_files(self): return self.files
    def get_dirs(self):  return self.dirs
    def get_full_files(self): return self.full_files
    def get_full_dirs(self):  return self.full_dirs





#-------------------------------------------



if __name__=="__main__":
    from os import getcwd 
    a=directory_explorer(getcwd())
    print("test")
    #a.print_full()
    a.print()


