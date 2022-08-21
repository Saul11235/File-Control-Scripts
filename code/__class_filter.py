#
# class filter
#
try:
    from __class_path_obj import path_obj
except:
    from .__class_path_obj import path_obj


import __actions_list as al

class filter_:

    def __init__(self,origin,destiny,specialn):
        # origin  __class_path_obj.py
        # destiny __class_data_special_file.py 
        #----------------------
        self.special_name=specialn
        #----------------------
        self.arguments_destiny=destiny
        #----------------------
        self.path_origin=origin
        self.path_destiny=path_obj(destiny.get_path(),specialn)
        #----------------------
        self.files_origin=[]
        self.files_destiny=[]
        self.folders_origin=[]
        self.folders_destiny=[]
        #----------------------
        self.__sort_information()


    def __sort_information(self):
        self.files_origin=self.path_origin.all_files()
        self.files_destiny=self.path_destiny.all_files()
        self.folders_origin=self.path_origin.no_special_dirs()
        self.folders_destiny=self.path_destiny.no_special_dirs()
        #------------------
        

    def PUSH_files_to_copy(self):
        print("---")
        print(self.files_origin)

        print("---")
        files=[]
        for x in self.files_origin:
            if self.arguments_destiny.is_file(x):
                files.append(x)
        return files

    def PUSH_files_to_delete(self):
        files=[]
        for x in self.files_origin:
            if self.arguments_destiny.is_file(x):
                files.append(x)
        return files

    def PUSH_subfolders_to_push(self):
        folders=[]
        for x in self.folders_origin:
            if self.arguments_destiny.is_folder(x):
                folders_destiny.append(x)
        return folders



    


