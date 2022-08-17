#
# class filter
#
try:
    from .__class_path_obj import path_obj
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
        #----------------------
        self.__sort_information()


    def __sort_information(self):
        self.__sorting_files_in_origin()

    def __sorting_files_in_origin(self):
        

        pass


