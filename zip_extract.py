import zipfile

def unzip_archive(file_path, dest):
    with zipfile.ZipFile(file_path, 'r') as file:
        file.extractall(dest)


if __name__ == "__main__":
    unzip_archive('/Users/mac/PycharmProjects/file_unarchiver/005 compressed.zip',
                  "/Users/mac/PycharmProjects/file_unarchiver/new")
