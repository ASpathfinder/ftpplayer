from . import platform
import ftplib

class FtpInstance:
    def __init__(self, **kwargs):
        self.tls = kwargs.get('tls')
        self.encoding = kwargs.get('encoding')
        self.ftp = ftplib.FTP_TLS(encoding=self.encoding) if self.tls else ftplib.FTP(encoding=self.encoding)
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')
        self.user = kwargs.get('user')
        self.passwd = kwargs.get('passwd')
        self.paths = []
        self.path_prefix = "{}://{}:{}".format('ftps' if self.tls else 'ftp', self.host, self.port)
        self.path_separate = '/' if platform == 'win32' else '/'
        self.extensions = []

    def connect(self):
        return self.ftp.connect(self.host, self.port)

    def login(self):
        return self.ftp.login(self.user, self.passwd)

    def read_extensions(self, path='audio_format.txt'):
        with open(path, 'r') as f:
            for line in f:
                self.extensions.append(line.replace('\n', ''))

    def ls(self, custom_path=''):
        root_path = custom_path if custom_path else self.path_separate
        self.recursion_path(root_path)
        return self.paths

    def recursion_path(self, path):
        for file_info in self.ftp.mlsd(path):
            if file_info[1]['type'] == 'dir':
                if path == self.path_separate:
                    self.recursion_path(path + file_info[0])
                else:
                    self.recursion_path(path + self.path_separate + file_info[0])
            else:
                if file_info[0].split('.')[-1].lower() in self.extensions:
                    if path == self.path_separate:
                        self.paths.append(self.path_prefix + path + file_info[0])
                    else:
                        self.paths.append(self.path_prefix + path + self.path_separate + file_info[0])
        return True