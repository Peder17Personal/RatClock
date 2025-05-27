import subprocess

def play_sound(filename):
    subprocess.run(["ffplay", "-nodisp", "-autoexit", filename])


