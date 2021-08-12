path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'


def get_file_name(path):
    index = path.rindex('\\')
    return path[index + 1:]


def get_file_name2(path):
    return path.split('\\')[-1]


print(get_file_name(path))
print(get_file_name2(path))
