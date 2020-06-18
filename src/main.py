from src.search import Search


def main():
    search_in_OS = Search()
    all_file_list =[]
    all_paths=('Find All' + str(
        search_in_OS.find_all(path='C:\\', file_a='XT.ec', file_b='AcGenral', dir_a='CSC', dir_b='ERRORREP')))
    for path in all_paths:
        all_file_list.append([path, search_in_OS.get_file_name(path)])
        for dt in search_in_OS.get_time_list(path):
            all_file_list.append(dt)
    # all_file_list.append(file_list)
    search_in_OS.export_to_csv(all_file_list)


if __name__ == "__main__":
    main()
