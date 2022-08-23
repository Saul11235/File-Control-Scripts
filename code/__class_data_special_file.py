#
# class data_special_file
#
try:
    from __slash import slash
except:
    from .__slash import slash

import __actions_str as ast
import __actions_path as ap

from os import listdir
from os.path import isdir,isfile

class data_special_file:

    def __init__(self,path,special_name):
        self.special_name=special_name
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

    def list(self): return self.arguments

    def is_file(self,namefile):
        get_name=ast.get_subname
        name=get_name(namefile)
        #-------------------
        extension=False
        for x in self.__extensions:
            if ast.is_name_extension(name,x):
                extension=True
        #-------------------
        noextension=False
        for x in self.__No_extensions:
            if ast.is_name_no_extension(name,x):
                noextension=True
        #--------------------        
        file_=False
        for x in self.__files:
            if name==get_name(x):file_=True
        #--------------------        
        nofile=False
        for x in self.__No_files:
            print(x)
            if name==get_name(x):nofile=True
        #--------------------        
        if self.__AllFiles:
            if noextension or nofile:
                return   False
            else: return True
        else:
            if extension or file_:
                return   True
            else: return False

    def is_folder(self,namefolder):
        get_name=ast.get_subname
        name=get_name(namefolder)
        #--------------------        
        folder=False
        for x in self.__folders:
            if name==get_name(x): folder=True
        #--------------------        
        nofolder=False
        for x in self.__No_folders:
            if name==get_name(x): nofolder=True
        #--------------------        
        if self.__AllFiles:
            if folder: return True
            else:      return False
        else:
            if nofolder: return True
            else:        return False


    def get_arg_positve(self):
        return self.__extensions+self.__files+self.__folders

    def get_arg_negative(self):
        return self.__No_extensions

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
            elif ast.is_exception(x): # - args
                y=ast.get_exception(x)
                xx=self.path+slash+y
                if ast.is_extension(y):
                    self.__No_extensions.append(x)
                elif ast.is_folder_name(y):
                    self.__No_files.append(xx)
                elif y!="":
                    self.__No_folders.append(xx)
            else: # args
                xx=self.path+slash+x
                xxx=self.path+slash+ast.get_exception(x)
                if ast.is_extension(x):
                    self.__extensions.append(x)
                elif ast.is_folder_name(x):
                    self.__files.append(xxx)
                elif x!="":
                    self.__folders.append(xx) 

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
        print(self.dirs)
        for x in self.dirs:
            if not(is_special_path(x)):response.append(x)
        return response

    def get_atributes_no_folder(self):
        response=[]
        for x in self.arguments:
            if not(is_file_name(x)):response.append(x)
        return response




