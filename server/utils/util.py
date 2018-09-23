import tempfile
import os

def temppath(filename):
    return os.path.join(tempfile.gettempdir(), filename)
    
