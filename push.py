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

def DELETE_FOLDER(folder):
    print("folder "+str(folder)+" eliminado")

def DELETE_FILE(filepath):
    print("file "+str(filepath)+" eliminado")

def REPLACE_FILE(origin,destination):
    print("")
    print("replace file")
    print(origin)
    print(destination)
    print("")

#--------------------
def concat_strings(*args):
    string=""; first=True
    for x in args:
        if  first: first=False;string=str(x)
        else: string+=" "+str(x)
    return string    
#--------------------
def is_end(string,end):
    pass
    


def is_extension(extension):
    if extension[0]=="*"  and len(extension)>1:
        if extension[1]=="." and extension!="*.": return True
        else: return False
    else:return False
#-------------------
def is_file_name(filename):
    if (filename=="/" or  filename=="\\")  and len(filename)!=1:  
        return True
    else: return False
#-------------------
def is_exception(argument):
    list_arg=argument.split()
    if list_arg[0]=="-":return True
    else: return False
#-------------------
def get_extension(extension): return extension[1:len(extension)]
#-------------------
def get_exception(exception):
    tupleargs=[]
    first=True
    for x in exception.split():
        if first:first=False
        else: tupleargs.append(x)
    return concat_strings(*tuple(tupleargs))
#-------------------

#--------------------
class object_arguments:

    def __init__(self,path):
        self.path=path
        self.arguments=[]
        #content  analyzed
        #path filenames
        self.dirs=[]
        self.files=[]
        #arguments
        self.__AllFiles=False # case *
        #-----------
        self.__extensions=[]
        self.__files=[]
        self.__folders=[]
        #-----------
        self.__No_extensions=[]
        self.__No_files=[]
        self.__No_folders=[]
        #files analized -----
        self.__pushfiles=[]
        self.__files=[]
        self.__folders=[]

    def list(self): return self.arguments
    def get_is_all_files(self): return self.__AllFiles

    def add_extension(self,extension):
        if extension!=" "*len(extension):
            self.arguments.append(extension)

    def add_extension_list(self,list_extensions):
        for x in list_extensions:
            self.add_extension()
        self.analyze_content()
    
    def __scan_path(self):
        for x in listdir(self.path):
            xx=self.path+slash+x
            if isdir(xx):self.dirs.append(xx)
            elif isfile(xx):self.files.append(xx)

    def __analyze_arguments(self):
        for x in self.arguments:
            if x=="*":self.__AllFiles=True
            elif is_exception(x): # - args
                y=get_exception(x)
                xx=self.path+slash+y
                if is_extension(y):self.__No_extensions.append(xx)
                elif is_file_name(y):self.__No_files.append(xx)
                elif y!="":self.__No_folders.append(xx)
            else: # args
                xx=self.path+slash+x
                if is_extension(x):self.__extensions.append(xx)
                elif is_file_name(x):self.__files.append(xx)
                elif x!="":self.__folders.append(xx) 

    def analyze_content(self):
        self.__scan_path()
        self.__analyze_arguments()

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
    #  algorithm for push
    #
    
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

