import os


def my_path():
    path = r'E:\tg_bot_parsing_to\data'

    files = os.listdir(path)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)
    latest_file = (files[0])
    return str(latest_file)
    #print("Останній змінений файл:", latest_file)


if __name__ == '__main__':
    my_path()
