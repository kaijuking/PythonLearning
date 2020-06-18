import sys
import os
sys.path.append(os.pardir)
sys.path.append(os.path.join(os.pardir, os.pardir))

from src.common import helpers as h

def print_hello_world():
    h.hello_world()

if __name__ == "__main__":
    print_hello_world()