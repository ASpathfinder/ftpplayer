import threading
import time

class PlayThread(threading.Thread):
    def __init__(self, name, threadID, player):
        threading.Thread.__init__(self)
        self.name = name
        self.threadID = threadID
        self.player = player

    def run(self):
        while True:
            self.player.play()
            time.sleep(5)

