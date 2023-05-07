import os
import json


def add_file_size_to_dict(files, dictionary, path):
    for i in files:
        try:
            file = os.stat(path)
            dictionary[i] = file.st_size
        except FileNotFoundError:
            return
    return dictionary


def minimum_file_size(list_of_files: dict):
    return min(list_of_files.values())


def maximum_file_size(list_of_files: dict):
    return max(list_of_files.values())


def add_files_to_list(files, list):
    for i in files:
        list.append(i)


def shortest_name(list_of_files):
    list_of_files = set(list_of_files)
    return min(list_of_files, key=len)


def longest_name(list_of_files):
    list_of_files = set(list_of_files)
    return max(list_of_files, key=len)


def check_if_path_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False


def scan_files_and_directories_in_path(empty_list_for_roots, path):
    if check_if_path_exists(path):
        with open('scanned_roots.txt', 'r+') as file:
            content = file.readline()
            try:
                for root, dirs, files in os.walk(path):
                    if root not in content:
                        empty_list_for_roots.append(root)
                        add_file_size_to_dict(files, value_bytes, root)
                        add_files_to_list(files, list_of_names)
            except KeyboardInterrupt:
                file.write(json.dumps(roots))
    else:
        path = 'C:/'
        scan_files_and_directories_in_path(empty_list_for_roots, path)


if __name__ == '__main__':
    value_bytes = {}
    list_of_names = []
    roots = []

    scan_files_and_directories_in_path(roots, 'A:/')

    print(f'Maximum file size is "{maximum_file_size(value_bytes)}" bites.')
    print(f'Minimum file size is "{minimum_file_size(value_bytes)}" bites.')
    print(f'The longest file name is "{longest_name(list_of_names)}".')
    print(f'The shortest file name is "{shortest_name(list_of_names)}".')
    print(f'the number of scanned roots: {len(roots)}')
    print(f'the number of scanned files: {len(list_of_names)}')
