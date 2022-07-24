#
#  file  push - ESaul1135
#
#  minimum destination address length

minimun_address_length=6  

#--------------------

from os import getcwd,listdir
from os.path import isfile,isdir
from platform import system  as platsys

#--------------------

slash="/"
if platsys()=="Windows":slash="\\"

#--------------------

def concat_strings(*args):
    string=""; first=True
    for x in args:
        if  first: first=False;string=str(x)
        else: string+=" "+str(x)
    return string    

#--------------------
class object_arguments:

    def __init__(self,path):
        self.path=path
        self.arguments=[]
        #content  analyzed
        #path filenames
        self.__dirs=[]
        self.__files=[]
        #arguments
        self.__extensions=[]
        self.__nameFiles=[]


    def list(self): return self.arguments

    def add_extension(self,extension):
        if extension!=" "*len(extension):
            self.arguments.append(extension)
    
    def __scan_path(self):
        for x in listdir(self.path):
            xx=self.path+slash+x
            if isdir(xx):self.__dirs.append(xx)
            elif isfile(xx):self.__files.append(xx)




    def analyze_content(self):
        self.__scan_path()
        pass

#--------------------

class filepush_data:

    def __init__(self,location_path):
        self.data=[]
        try:
            file=open(location_path+slash+".filepush","r")
            self.data=file.read().split("\n")
            file.close()
        except:
            print("error reading .filepush")
            print("error on path: "+location_path)
        a=self.sorting_arguments_filepush()
        self.list_objects=self.generate_objects_arguments(a)

    def list(self): return self.list_objects

    def sorting_arguments_filepush(self):
        list_no_empty=[]
        for x in self.data:
            if len(x.split()):list_no_empty.append(x)
        list_no_comment=[]    
        for  x in list_no_empty:
            if x.split()[0]!="#":list_no_comment.append(x)
        list_arguments_to_push=[]    
        #format list_arguments_to_push :  [ path_destination  [extensions]  ]      
        list_aux_destination=[]
        list_aux_extensions=[]
        for x in list_no_comment:
            split=x.split()
            destination_path=concat_strings(*tuple(split[1:len(split)]))
            extension=concat_strings(*tuple(split[0:len(split)]))
            if split[0]=="##" and list_aux_destination==[]:
                #first iteration
                list_aux_destination.append(destination_path)
            elif split[0]=="##" and list_aux_destination!=[]:
                #new  path destination
                list_aux_destination.append(list_aux_extensions)
                list_arguments_to_push.append(list_aux_destination)
                list_aux_extensions=[]
                list_aux_destination=[destination_path]
            else:list_aux_extensions.append(extension)
        if len(list_aux_extensions):
            list_aux_destination.append(list_aux_extensions)
            list_arguments_to_push.append(list_aux_destination)
        return list_arguments_to_push

    def generate_objects_arguments(self,list_arguments):
        list_objects=[]
        for x in list_arguments:
            p=x[0] # destination path
            if len(p)>minimun_address_length and isdir(p) and len(x[1]):
                obj=object_arguments(x[0])
                for extension in x[1]:obj.add_extension(extension)
                obj.analyze_content()
                list_objects.append(obj)
        return list_objects
                
#--------------------

def push(path):
    file_data=filepush_data(path)
    local=object_arguments(path)
    
    print("hello  ")
    print(path)



#--------------------

if __name__=="__main__":

    def  write_filepush():
        f=open(".filepush","w")
        f.write("# filepush -  by Edwin Saul - @ESaul1135\n")
        f.write("# '# '  for comment\n")
        f.write("# '## ' for set  destination path\n")
        f.write("# write bellow extensions, file names\n")
        f.write("# or folder names to push")
        f.close()

    if isfile(".filepush"): push(str(getcwd()))
    else: write_filepush(); print(".filepush created!")

