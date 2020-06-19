from src.search import Search


def main(file_a, file_b, dir_a, dir_b, path='C:\\'):
    search_in_OS = Search()
    all_file_list = []
    try:
        all_paths = (
            search_in_OS.find_all(path, file_a=file_a, file_b=file_b, dir_a=dir_a, dir_b=dir_b))
        for path in all_paths:
            creation, modified, accessed = search_in_OS.get_time_list(path)
            all_file_list.append([path, search_in_OS.get_file_name(path), creation, modified, accessed])
        search_in_OS.export_to_csv(all_file_list)
    except Exception as e:
        print('Exception' + str(e))
        print(all_file_list)


if __name__ == "__main__":
    main(path='C:\\', file_a='XT.ec', file_b='AcGenral', dir_a='CSC', dir_b='ERRORREP')
