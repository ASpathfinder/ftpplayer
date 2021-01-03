from . exception import EmptyPlayListError
from . import platform
import random
import subprocess

class Player:
    def __init__(self):
        self.playlist = []

    def refresh_playlist(self, paths):
        self.playlist = paths

    def play(self):
        random.seed()
        length = len(self.playlist)
        if length == 0:
            raise EmptyPlayListError
        playitem_index = random.randint(0, length-1)
        command = ['mplayer'] if platform == 'win32' else ['mplayer']
        command.append(self.playlist[playitem_index])
        print(command)
        complete = subprocess.run(command)#, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            complete.check_returncode()
        except subprocess.CalledProcessError as e:
            print(e.stdout)
            print(e.stderr)
        else:
            print(complete.stdout)

