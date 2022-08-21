
try:
    from .__slash import slash
    from .__class_data_special_file import data_special_file
except:
    from __slash import slash
    from __class_data_special_file import data_special_file


from platform import system
from os.path import isdir
from os import makedirs


import __actions_str as ast

# IMPORTANT this var is for security
minimun_address_length=4


class special_file:


    def __init__(self,path,name_file):
        self.special_name=name_file
        self.data=[]
        try:
            f=open(path+slash+name_file,"r")
            self.data=f.read().split("\n")
            f.close()
        except:
            print(" no "+name_file+":\n"+path)

        #-------operating in sublist---------
        a=self.sorting_arguments_filepush()
        self.list_objects=self.generate_objects_arguments(a)
        #-------------------------------------


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
            destination_path=ast.concat_strings(*tuple(split[1:len(split)]))
            extension=ast.concat_strings(*tuple(split[0:len(split)]))
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
                    try:
                        makedirs(path_destiny)
                    except:
                        print("not valid path "+str(path_destiny))
                        exit()
                if isdir(path_destiny):
                    # make a new object -----------------
                    obj=data_special_file(path_destiny,self.special_name)
                    # -----------------------------------
                    for extension in x[1]:
                        obj.add_extension(extension)
                    obj.analyze_content()
                    list_objects.append(obj)
        return list_objects
        



