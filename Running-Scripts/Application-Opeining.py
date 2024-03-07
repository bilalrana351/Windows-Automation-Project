import os

def open_program(program_name):
    #Utilize the start menu folder to open the program
    program_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\" + program_name + ".lnk"
    
    try:
        os.startfile(program_path)
        print(f"Successfully opened {program_path}")

    #Need to put failure code
    except:
        print("File doesn't exixt")

if __name__ == "__main__":
    open_program("Google Chrome")