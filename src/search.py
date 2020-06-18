import datetime
import ntpath
import platform
import pandas as pd
import os, fnmatch

# https://stackoverflow.com/questions/1724693/find-a-file-in-python
class Search:

    # def find(self, path, **patterns):
    #     result = []
    #     for type,value in patterns:
    #         for root, dirs, files in os.walk(path):
    #             for f_name,d_name in files,dirs:
    #                 if type.__contains__('file_'):
    #                     if fnmatch.fnmatch(f_name, value):
    #                         result.append(os.path.join(root, f_name))
    #                 if value.__contains__('dir_'):
    #                     if fnmatch.fnmatch(d_name, value):
    #                         result.append(os.path.join(root, d_name))
    #     return result

    def find_all(self, path, file_a, file_b, dir_a, dir_b):
        result = []
        for root, dirs, files in os.walk(path):
            for f_name in files:
                if f_name.__contains__(file_a) or f_name.__contains__(file_b):
                    file_path = root + '\\' + str(f_name)
                    result.append(file_path)
            for d_name in dirs:
                if d_name == dir_a or d_name == dir_b:
                    dir_path = root + '\\' + str(d_name)
                    result.append(dir_path)
        return result


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
        for time in file_time_list:
            if isinstance(time, float):
                yield self.get_date(time)

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


# search_in_OS = Search()
# print('Find All'+str(search_in_OS.find_all(path='C:\\', file_a='XT.ec', file_b='AcGenral', dir_a='CSC', dir_b='ERRORREP')))
# print('Find: '+str(search_in_OS.find(path='C:\\', file_a='XT.ec', file_b='AcGenral', dir_a='CSC', dir_b='ERRORREP')))
