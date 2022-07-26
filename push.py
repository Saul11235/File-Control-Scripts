#
#  file  push - ESaul1135
#
#  minimum destination address length

minimun_address_length=6  

#--------------------
from os import getcwd,listdir,mkdir,makedirs
from os import remove
from os.path import isfile,isdir,basename
from platform import system  as platsys
from shutil import copy
#--------------------

slash="/"
if platsys()=="Windows":slash="\\"

def DELETE_FOLDER(folder):
    print("folder "+str(folder)+" eliminado")

def DELETE_FILE(filepath):
    try:
        remove(filepath)
        print("  deleted   : "+filepath)
    except:
        print("  ERROR del : "+filepath)


def COPY_FILE(path_origin_file,destination):
    try:
        copy(path_origin_file,destination)
        print("  copy file : "+path_origin_file)
    except:
        print("  ERROR copy:"+path_origin_file)

#--------------------
def intersection(list1,list2):
    response=[] 
    for x in list1:
        try: list2.index(x);response.append(x)
        except:pass
    return response

def diference(list1,list2):
    response=[]
    for x in list1:
        try: list2.index(x)
        except: response.append(x)
    return response

def list_subdirs(path):
    subdirs=[]
    for x in listdir(path):
        full_path=path+slash+x
        if isdir(full_path):subdirs.append(full_path)
    return subdirs

def list_special_subdirs(path):
    especial_subdirs=[]
    for x in list_subdirs(path):
        if is_special_path(x):especial_subdirs.append(x)
    return especial_subdirs    

def list_no_special_subdirs(path):
    normal_subdirs=[]
    for x in list_subdirs(path):
        if  not(is_special_path(x)):normal_subdirs.append(x)
    return normal_subdirs

def list_files(path):
    subfiles=[]
    for x in listdir(path):
        full_path=path+slash+x
        if isfile(full_path) and x!=".filepush" and x!=".filepull":
            subfiles.append(full_path)
    return subfiles



def concat_strings(*args):
    string=""; first=True
    for x in args:
        if  first: first=False;string=str(x)
        else: string+=" "+str(x)
    return string    
#--------------------
def is_end(string,end):
    if len(end)>len(string):return False
    nend=string[len(string)-len(end):len(string)]
    if nend==end:return True
    else: return False
#--------------------    
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
#--------------------
def is_special_path(path):
    path_file=path+slash+".filepush"
    if isfile(path_file):return True 
    else: return False
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
    def get_path(self): return self.path

    def add_extension(self,extension):
        if extension!=" "*len(extension):
            self.arguments.append(extension)

    def add_extension_list(self,list_extensions):
        for x in list_extensions:
            self.add_extension(x)
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

    def get_special_folders(self):
        response=[]
        for x in self.dirs:
            if is_special_path(x):response.append(x)
        return response

    def get_no_special_folders(self):
        response=[]
        print("----")
        print(self.dirs)
        print("-----")
        for x in self.dirs:
            if not(is_special_path(x)):response.append(x)
        return response

    def get_atributes_no_folder(self):
        response=[]
        for x in self.arguments:
            if not(is_file_name(x)):response.append(x)
        return response




#--------------------

class filepush_data:

    def __init__(self,location_path):
        self.data=[]
        try:
            file=open(location_path+slash+".filepush","r")
            self.data=file.read().split("\n")
            file.close()
        except:
            print(" no .filepush:\n"+location_path)
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
            if len(x[0])>minimun_address_length and len(x[1]):
                path_destiny=x[0]
                if not(isdir(path_destiny)):
                    makedirs(path_destiny)
                if isdir(path_destiny):
                    obj=object_arguments(path_destiny)
                    for extension in x[1]:
                        obj.add_extension(extension)
                    obj.analyze_content()
                    list_objects.append(obj)
        return list_objects
                
#--------------------

def push(path):
    # push in subdirs whith .filepush----
    for x in list_special_subdirs(path):push(x)
    # push  on current path
    cicle_pushfile(path)

   
def cicle_pushfile(path_origin):
    file_push=filepush_data(path_origin)
    for obj_destination in file_push.list():
        # vars genral
        path_destiny=obj_destination.get_path()
        if path_origin==path_destiny:
            print("Error autoref: "+path_destiny)
            exit()
        else:
            print("Origin  : "+path_origin)
            print("Destiny : "+path_destiny)
        move_all_files=obj_destination.get_is_all_files()
        #  origin vars
        dirs_origin  =list_no_special_subdirs(path_origin)
        files_origin =list_files(path_origin)
        dirs_destiny =list_subdirs(path_destiny)
        files_destiny=list_files(path_destiny)
        #----------------------------------
        FILES_TO_COPY=[]
        #----------------------------------
        if move_all_files:
            # case * copy all files
            FILES_TO_COPY=files_origin
        else:
            # case NO * no copy all files
            print("no alll  files")
            pass
        #copying files
        FILES_COPYED=[]
        for x in FILES_TO_COPY:
            COPY_FILE(x,path_destiny)
            new_file=path_destiny+slash+basename(x)
            FILES_COPYED.append(new_file)
        #cleaner path data
        FILES_TO_DESTROY=diference(files_destiny,FILES_COPYED)
        for x  in FILES_TO_DESTROY:DELETE_FILE(x)
        print("")

       

  

    #************************
    #  algorithm for push
    #************************
    


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

