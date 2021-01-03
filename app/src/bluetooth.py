from . exception import BlueToothCheckError, BlueToothConnectError
import subprocess
import re

class BlueTooth:
    def __init__(self, device_address):
        self.device_address = device_address
        self.connected_flag_pt = re.compile(r'\s*Connected: ([^\s]*)\s*')
        self.status = 'disconnected'

    def connected(self):
        complete = subprocess.run(['bluetoothctl', 'info', self.device_address], capture_output=True)
        try:
            complete.check_returncode()
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            print(e.stdout)
            raise BlueToothCheckError
        else:
            device_info = complete.stdout.decode('utf-8')
            connected = self.connected_flag_pt.search(device_info).group(1)
            if connected == 'yes':
                self.status = 'connected'
                return True
            else:
                self.status = 'disconnected'
                return False

    def reconnect_bluetooth(self):
        complete = subprocess.run(['bluetoothctl', 'connect', self.device_address], capture_output=True)
        try:
            complete.check_returncode()
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            print(e.stdout)
        else:
            self.status = 'connected'
