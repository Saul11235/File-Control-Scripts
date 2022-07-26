import __actions_file as af

try:
    from .__class_path_obj import path_obj
    from .__class_special_file import special_file
    from .__class_filter import filter_
except:
    from __class_path_obj import path_obj
    from __class_special_file import special_file
    from __class_filter import filter_


special_name_file=".filepush"

#==================================================
#
#      XXXXXX     X    X     XXXXXX     X    X
#      X    X     X    X     X          X    X
#      X    X     X    X     X          X    X
#      XXXXXX     X    X     XXXXXX     XXXXXX
#      X          X    X          X     X    X
#      X          X    X          X     X    X
#      X          XXXXXX     XXXXXX     X    X
#
#==================================================

def cicle(origin,destiny):
    f=filter_(origin,destiny,special_name_file)
    #----------------------------------
    files_to_copy=f.PUSH_files_to_copy()
    print("")
    print("COPY")
    for fl in files_to_copy:
        print(fl)
    files_to_delete=f.PUSH_files_to_delete()
    print("")
    print("DELETE")
    for fl in files_to_delete:
        print(fl)
    folders_to_push=f.PUSH_subfolders_to_push()
    print("")
    print("push")
    for fl in folders_to_push:
        print(fl)


def cicle_subdir(origin,destiny):
    pass
    




#===================================================

def push(path):
    #-----------------
    origin=path_obj(path,special_name_file)
    for subdir in origin.special_subdirs():
        push(subdir)
    filepush=special_file(path,special_name_file)
    #-----------------
    for destiny in filepush.list():
        cicle(origin,destiny)

    #filepush=special_file(path,".filepush")
