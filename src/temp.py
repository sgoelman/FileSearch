import os
import platform

dir_path = os.path.dirname(os.path.realpath(__file__))


def search_for_file_with_ending(contains_a, contains_b):
    search_list = []
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if file.__contains__(contains_a) or file.__contains__(contains_b):
                search_list.append(root + '\\' + str(file))
    return search_list


def get_creation_date(path_to_file,file):
    file_dict={}
    if platform.system() == 'Windows':
        file_dict={path_to_file:}
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            stat.st_mtime
            return stat.st_birthtime
        except AttributeError:
            # Linux OS
            return stat.st_mtime


file_paths_list = search_for_file_with_ending('XT.ec', 'AcGenral')
creation_date = []
for path in file_paths_list:
    creation_date.append(creation_date)

print('Files:' + str(file_paths_list))
print('Dates:' + (str(creation_date)))
