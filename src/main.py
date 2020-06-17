from src.search import Search


def main():
    search_in_OS = Search()
    all_files_list = []
    for path_to_file in search_in_OS.search_for_file_with_ending('XT.ec', 'AcGenral', 'CSC', 'ERRORREP'):
        file_list = []
        file_list.append([path_to_file, search_in_OS.get_file_name(path_to_file)])
        for dt in search_in_OS.get_time_list(path_to_file):
            file_list.append(dt)
        all_files_list.append(file_list)
    search_in_OS.export_to_csv(all_files_list)


if __name__ == "__main__":
    main()
