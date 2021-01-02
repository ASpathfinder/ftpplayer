from app import ftp
from app import player
import time

if __name__ == '__main__':
    player.refresh_playlist(ftp.ls('/Music'))
    while True:
        player.play()
        time.sleep(5)
