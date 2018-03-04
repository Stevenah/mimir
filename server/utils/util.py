import tempfile
from argparse import ArgumentParser
import os

def temppath(filename):
    return os.path.join(tempfile.gettempdir(), filename)
    
def server_arg_parser():
    ap = ArgumentParser()

    ap.add_argument('-p', '--port', help='set the port used by the server', type=int, default=5000)
    ap.add_argument('--host', help='set the host used by the server', default='0.0.0.0')
    ap.add_argument('-d', '--debug', help='set the debug option', default=False)

    return ap.parse_args()
