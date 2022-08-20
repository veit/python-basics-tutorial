class EmptyFileError(Exception):
    pass
filenames = ["myFile1.py", "nonExistent.py", "emptyFile.py", "myFile2.py"]
for file in filenames:
    try:
        f = open(file, 'r')
        line = f.readline()
        if line == "":
            f.close()
            raise EmptyFileError(f"{file} is empty")
    except IOError as error:
        print(f"Cannot open file {file}: {error.strerror}")
    except EmptyFileError as error:
        print(error)
    else:
        print(f"{file}: {f.readline()}")
    finally:
        print("File", file, "processed")
