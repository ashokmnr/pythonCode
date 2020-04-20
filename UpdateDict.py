import os, sys

try:
    dir_path = sys.argv[1]
    prodForce = sys.argv[2].lower()

    if prodForce == "prod":
        value = True
        if os.path.exists(dir_path):
            for (dirpath, dirnames, filenames) in os.walk(dir_path):
                os.chdir(dir_path)
                packFile = open("ValueFile.txt", "r")
                packFileContents = packFile.readlines()
                for i in range(0, len(packFileContents)):
                    if value != False:
                        splitAllapp = packFileContents[i].split("=")
                        importDict(
                            dir_path + "/" + splitAllapp[0],
                            splitAllapp[1].replace("\n", ""),
                            value,
                        )
                        packFile.close()
                    else:
                        print("Value is False")
        else:
            print("path does not exists")
    else:
        if os.path.exists(dir_path):
            for (dirpath, dirnames, filenames) in os.walk(dir_path):
                os.chdir(dir_path)
                packFile = open("ValueFile.txt", "r")
                packFileContents = packFile.readlines()
                for i in range(0, len(packFileContents)):
                    splitAllapp = packFileContents[i].split("=")
                    findProd = "PROD" not in splitAllapp[0].upper()
                    importDict(
                        dir_path + "/" + splitAllapp[0],
                        splitAllapp[1].replace("\n", ""),
                        findProd,
                    )
                    packFile.close()
        else:
            print("path does not exists")

except IndexError:
    print("Please provide dictionaries path as a input")
