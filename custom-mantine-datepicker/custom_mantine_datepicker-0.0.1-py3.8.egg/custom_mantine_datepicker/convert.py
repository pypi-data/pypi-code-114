import os


def main():
    for dirpath, dirnames, filenames in os.walk("custom_mantine_datepicker"):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "r", encoding="cp1252") as src:
                    filedata = src.read()
                    print("done1")
                with open(filepath, "w", encoding="utf8") as dest:
                    dest.write(filedata)
                    print("done2")

if __name__ == '__main__':
    main()
