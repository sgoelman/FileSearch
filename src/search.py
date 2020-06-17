import datetime
import ntpath
import platform
import pandas as pd
import os, fnmatch

# https://stackoverflow.com/questions/1724693/find-a-file-in-python
class Search:

    def find(self, path, **patterns):
        result = []
        for type,value in patterns:
            for root, dirs, files in os.walk(path):
                for name in files:
                    if type.__contains__('file_'):
                        if fnmatch.fnmatch(name, patterns.items()):
                            result.append(os.path.join(root, name))
                for name in dirs:
                    if value.__contains__('dir_'):
                        if fnmatch.fnmatch(name, patterns.keys()):
                            result.append(os.path.join(root, name))
        return result

    def find_all(self, path, file_a, file_b, dir_a, dir_b):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if files.__contains__(file_a) or files.__contains__(file_b):
                    result.append(os.path.join(root, name))
            for dir in dirs:
                if dirs == dir_a or dirs == dir_b:
                    result.append(os.path.join(root, dir))
        return result

    def search_for_file_with_ending(self, path,file_a, file_b, dir_a, dir_b):
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if files.__contains__(file_a) or files.__contains__(file_b):
                    file_path = root + '\\' + str(file_name)
                    yield file_path
            # for folder in dirs:
            #     if folder == dir_a or folder == dir_b:
            #         folder_path = os.path.join(root, folder)
            #         yield folder_path

    def get_time_list(self, path_to_file):
        """

        :param path_to_file:
        :param file_name:
        :return:list :[file name,full path,creation date,modified date,date accessed,attributes]
        """
        file_time_list = [path_to_file]
        if platform.system() == 'Windows':
            # creation date
            file_time_list.append(os.path.getctime(path_to_file))
            # modified date
            file_time_list.append(os.path.getmtime(path_to_file))
            # date accessed
            file_time_list.append(os.path.getatime(path_to_file))
        else:
            # MAC OS
            stat = os.stat(path_to_file)
            try:
                # creation date
                file_time_list.append(stat.st_birthtime)
                # modified date
                file_time_list.append(stat.st_mtime)
                # date accessed
                file_time_list.append(stat.st_atime)
            except AttributeError as ae:
                # Linux OS
                print(ae)
        for ts in file_time_list:
            if isinstance(ts, float):
                yield self.get_date(ts)

    def get_date(self, time_stamp):
        value = datetime.datetime.fromtimestamp(time_stamp)
        return f"{value:%Y-%m-%d %H:%M:%S}"

    def get_file_name(self, path_to_file):
        return ntpath.basename(path_to_file)

    # todo:add attributes
    def export_to_csv(self, file_list):
        df = pd.DataFrame(file_list,
                          columns=["Folder Path", "File Name", "Creation Date", "Modified date", "Date Accessed"])
        df.to_csv('file_list.csv', index=False)


search_in_OS = Search()
print('Find All'+str(search_in_OS.find_all(path='C:\\', file_a='XT.ec', file_b='AcGenral', dir_a='CSC', dir_b='ERRORREP')))
print('Find: '+str(search_in_OS.find(path='C:\\', file_a='XT.ec', file_b='AcGenral', dir_a='CSC', dir_b='ERRORREP')))
