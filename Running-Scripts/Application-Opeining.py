import os

def open_program(program_name):
    program_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\" + program_name + ".lnk"
    
    try:
        os.startfile(program_path)
        print(f"Successfully opened {program_path}")

    except:
        print("File doesn't exixt")

# Example usage
program_name = "Google Chrome"
open_program(program_name)