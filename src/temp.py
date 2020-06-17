import os
import platform

dir_path = os.path.dirname(os.path.realpath(__file__))


def search_for_file_with_ending(contains_a, contains_b):
    search_list = []
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if file.__contains__(contains_a) or file.__contains__(contains_b):
                path = root + '\\' + str(file)
                yield file, path


def get_creation_date(path_to_file, file):
    file_dict = {}
    if platform.system() == 'Windows':
        # file_dict={path_to_file:}
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            stat.st_mtime
            return stat.st_birthtime
        except AttributeError:
            # Linux OS
            return stat.st_mtime

file_dict=[]
for file, path in search_for_file_with_ending('XT.ec', 'AcGenral'):
    file_dict.append(file, path)

print('Files:' + str(file_dict))

