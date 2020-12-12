import hashlib


def my_generator(file_path):
    with open(file_path) as file:
        line = file.readline()
        while line:
            md5_line = hashlib.md5(line.encode('utf-8')).hexdigest()
            yield md5_line
            line = file.readline()


if __name__ == '__main__':
    for i, item in enumerate(my_generator('countries.txt')):
        print(f'{i+1}.{item}')
