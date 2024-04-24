from PIL import Image
from tqdm import tqdm


class LoadDataset:
    def __init__(self, path):
        self.data = None
        self.path = path
        self.load_file()
        self.add_path_in_data()

    def load_file(self):
        file = open(self.path, 'r')
        list_of_lines = file.readlines()
        self.data = list_of_lines
        file.close()

    def add_path_in_data(self):
        for i in tqdm(range(len(self.data))):
            temp = self.path.split('train.txt')[0] + self.data[i]
            self.data[i] = temp

    def get_data_from_picture(self):
        big_data = {}
        for i in tqdm(range(len(self.data))):
            if '.png' in self.data[i]:
                text_file = open(self.data[i].split('.png')[0] + '.txt', 'r')
            elif '.jpg' in self.data[i]:
                text_file = open(self.data[i].split('.jpg')[0] + '.txt', 'r')
            elif '.jpeg' in self.data[i]:
                text_file = open(self.data[i].split('.jpeg')[0] + '.txt', 'r')
            else:
                print('File format not supported')
                continue
            for line in text_file:
                tag = line.split(' ')[0]
                if tag in big_data:
                    big_data[tag].append(self.get_tensor_from_line(line, self.data[i]))
                else:
                    big_data[tag] = [self.get_tensor_from_line(line, self.data[i])]

        return big_data

    @staticmethod
    def get_tensor_from_line(line, picture_file):
        w = float(line.split(' ')[1])
        h = float(line.split(' ')[2])
        x = float(line.split(' ')[3])
        y = float(line.split(' ')[4])
        picture = Image.open(picture_file.split('\n')[0])
        picture_width, picture_height = picture.size
        x = int(x * picture_width)
        y = int(y * picture_height)
        w = int(w * picture_width)
        h = int(h * picture_height)
        picture = picture.crop((x, y, x + w, y + h))
        picture = picture.resize((224, 224))
        picture_pixels_sum = 0
        for pixel in picture.getdata():
            picture_pixels_sum += sum(pixel)
        picture = picture_pixels_sum
        return picture
