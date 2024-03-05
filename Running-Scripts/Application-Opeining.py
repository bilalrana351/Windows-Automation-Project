import subprocess
import os.path

def open_program(program_name):
    program_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/' + program_name
    
    try:
        subprocess.Popen(program_path)
        print(f"Successfully opened {program_path}")

    except:
        print("File doesn't exixt")

# Example usage
program_name = "C:/Program Files/ExampleProgram.exe"
open_program(program_name)