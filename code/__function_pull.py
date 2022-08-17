import __actions_file as af

try:
    from .__class_path_obj import path_obj
    from .__class_special_file import special_file
    from .__class_filter import filter_
except:
    from __class_path_obj import path_obj
    from __class_special_file import special_file
    from __class_filter import filter_


special_name_file=".filepull"

#==================================================
#
#      XXXXXX     X    X     X          X
#      X    X     X    X     X          X
#      X    X     X    X     X          X
#      XXXXXX     X    X     X          X
#      X          X    X     X          X
#      X          X    X     X          X
#      X          XXXXXX     XXXXXX     XXXXXX
#
#==================================================

def cicle(origin,destiny):
    f=filter_(origin,destiny,special_name_file)
    print("")
    print(origin)
    print(destiny)

#===================================================

def pull(path):
    #-----------------
    origin=path_obj(path,special_name_file)
    for subdir in origin.special_subdirs():
        pull(subdir)
    filepull=special_file(path,special_name_file)
    #-----------------
    for destiny in filepull.list():
        cicle(origin,destiny)

