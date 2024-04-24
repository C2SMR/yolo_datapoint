import sys

from display import Display
from load_dataset import LoadDataset


class Main:
    def __init__(self):
        self.file_path = sys.argv[1]

    def run(self):
        big_data = LoadDataset(self.file_path).get_data_from_picture()
        Display(big_data)


if __name__ == '__main__':
    Main().run()
