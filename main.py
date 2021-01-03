from app import ftp
from app import player
from app.src import threads
from app.src.bluetooth import BlueTooth
from app import bluetooth_address
import time
import pyautogui
import sys

if __name__ == '__main__':
    player.refresh_playlist(ftp.ls('/'))
    play_thread = threads.PlayThread(name='play_thread_1', threadID=1, player=player)
    bt = BlueTooth(bluetooth_address)

    play_thread.start()

    if sys.platform == 'linux':
        #keypress_thread = threads.KeyPressThread(name='keypress_thread_1', threadID=1)
        #keypress_thread.start()
        bt.reconnect_bluetooth()
        bt_last_status = bt.status
        print(bt_last_status)
        while True:
            if not bt.connected():
                print('not connected: ' + bt_last_status + ' -- ' + bt.status)
                if bt_last_status == 'connected' and bt.status == 'disconnected':
                    pyautogui.press('space')
                bt_last_status = bt.status
                bt.reconnect_bluetooth()
            else:
                print('connected: ' + bt_last_status + ' -- ' + bt.status)
                if bt_last_status == 'disconnected' and bt.status == 'connected':
                    pyautogui.press('space')
                bt_last_status = bt.status
            time.sleep(1)




