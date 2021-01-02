from .src.ftp_method import FtpInstance
from .src.player import Player
from dotenv import load_dotenv
from os import getenv

load_dotenv()

ftp_params = {
    'host': getenv('HOST', '127.0.0.1'),
    'port': int(getenv('PORT', 21)),
    'user': getenv('FTP_USER', 'anonymous'),
    'passwd': getenv('PASSWD', ''),
    'tls': bool(getenv('TLS', False)),
    'encoding': getenv('ENCODING', 'utf-8'),
}

ftp = FtpInstance(**ftp_params)
ftp.read_extensions()
ftp.connect()
ftp.login()

player = Player()
