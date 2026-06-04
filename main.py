import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import run_app

if __name__ == "__main__":
    sys.exit(run_app())
