import datetime
import ntpath
import platform
import pandas as pd
import os, fnmatch


class Search:

    def search_by_criteria(self, path, file_a, file_b, dir_a, dir_b):
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
        creation, modified, accessed = None, None, None
        file_time_list = [path_to_file]
        if platform.system() == 'Windows':
            # creation date
            creation = self.get_date(os.path.getctime(path_to_file))
            # modified date
            modified = self.get_date(os.path.getmtime(path_to_file))
            # date accessed
            accessed = self.get_date(os.path.getatime(path_to_file))
        else:
            # MAC OS
            stat = os.stat(path_to_file)
            try:
                # creation date
                creation = self.get_date(stat.st_birthtime)
                # modified date
                modified = self.get_date(stat.st_mtime)
                # date accessed
                accessed = self.get_date(stat.st_atime)
            except AttributeError as ae:
                # Linux OS
                print(ae)
        return creation, modified, accessed

    def get_date(self, time_stamp):
        value = datetime.datetime.fromtimestamp(time_stamp)
        return f"{value:%Y-%m-%d %H:%M:%S}"

    def get_file_name(self, path_to_file):
        return ntpath.basename(path_to_file)


    def export_to_csv(self, file_list):
        df = pd.DataFrame(file_list,
                          columns=["Folder Path", "File Name", "Creation Date", "Modified date", "Date Accessed"])
        df.to_csv('file_list.csv', index=False)