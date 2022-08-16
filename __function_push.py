
try:
    from .__class_path_obj import path_obj
    from .__class_special_file import special_file
except:
    from __class_path_obj import path_obj
    from __class_special_file import special_file

def push(path):
    path_origin=path_obj(path)

    filepush=special_file(path,".filepush")


    print(str(path))


