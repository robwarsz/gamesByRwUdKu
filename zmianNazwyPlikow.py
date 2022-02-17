import os

def main():
    path = "E://KURS PY//file-rename"
    for count, filename in enumerate(os.listdir(path)):
        if filename != 'new':
            print(filename)
            src = f'{path}/{filename}'
            dst = f'{path}/new/District9-{filename}'
            os.rename(src, dst)

if __name__ == '__main__':
    main()

