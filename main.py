import os
import platform
import time
import getpass

def open_file(file_path):

    if platform.system() == "Windows":

        os.startfile(file_path)

    elif platform.system() == "Darwin":

        os.system(f"open '{file_path}'")

    else:

        os.system(f"xdg-open '{file_path}'")

def searchBeatmaps(directory, extension, num_files=10):

    while True:
        empty = True
        for filename in os.listdir(directory):

            if filename.endswith(extension):
                empty = False

                file_path = os.path.join(directory, filename)

                print(f"Opening beatmap in osu!: {file_path}")
                open_file(file_path)

        if empty == False:
            time.sleep(5)
        else:
            time.sleep(0.5)

if __name__ == "__main__":
    print("--------------------------------------")
    print(" Ankpudding's automatic beatmap adder")
    print("--------------------------------------\n")

    USERNAME = getpass.getuser()

    downloads = "C:\\Users\\" + USERNAME +"\\Downloads"
    file_extension = ".osz"

    print("Search path: " + downloads)
    print("File extension: " + file_extension + "\n")

    searchBeatmaps(downloads, file_extension)

