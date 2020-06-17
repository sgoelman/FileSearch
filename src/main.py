import datetime
import ntpath
import os
import platform
import pandas as pd

# for file in files:
#     if file.__contains__(contains_a) or file.__contains__(contains_b):
#         path = root + '\\' + str(file)
#         yield file, path


def search_for_file_with_ending(file_a, file_b, dir_a, dir_b):
    for root, dirs, files in os.walk('C:\\'):
        for folder in dirs:
            if folder == dir_a or folder == dir_b:
                folder_path = os.path.join(root, folder)
                yield folder_path
        for file in files:
            if files.__contains__(file_a):
                # if files.__contains__(file_a) or folder.__contains__(file_b):
                file_path = root + '\\' + str(file)
                yield file_path


def get_time_list(path_to_file):
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
            yield get_date(ts)


def get_date(time_stamp):
    value = datetime.datetime.fromtimestamp(time_stamp)
    return f"{value:%Y-%m-%d %H:%M:%S}"


def get_file_name(path_to_file):
    return ntpath.basename(path_to_file)


def main():
    all_files_list = []
    for path_to_file in search_for_file_with_ending('XT.ec', 'AcGenral', 'CSC', 'ERRORREP'):
        # for path_to_file in search_for_file_with_ending('XT.ec'):
        file_list = [path_to_file, get_file_name(path_to_file)]
        for dt in get_time_list(path_to_file):
            file_list.append(dt)
        all_files_list.append(file_list)
    export_to_csv(all_files_list)


# todo:add attributes
def export_to_csv(file_list):
    df = pd.DataFrame(file_list,
                      columns=["Folder Path", "File Name", "Creation Date", "Modified date", "Date Accessed"])
    df.to_csv('file_list.csv', index=False)


if __name__ == "__main__":
    main()
