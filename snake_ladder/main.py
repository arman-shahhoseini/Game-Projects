import os
from userInterface import *

def main():
    master = Tk()
    master.title("Snake and Ladder")
    master.geometry("850x600")
    
    # Construct the full file path
    file_path = os.path.join(os.path.dirname(__file__), "main_image.jpg")
    img = PhotoImage(file=file_path)
    x = Display(master, img)
    master.mainloop()

main()