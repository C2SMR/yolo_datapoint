import matplotlib.pyplot as plt


class Display:

    def __init__(self, big_data):
        self.big_data = big_data
        self.colors_possibility = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'black', 'white']
        self.display2D()
        self.display3D()

    def display2D(self):
        x = []
        y = []
        colors = []
        index = 0
        for tag in self.big_data:
            index += 1
            print(f"{tag}: {self.colors_possibility[index]}")
            for i in range(len(self.big_data[tag])):
                colors.append(self.colors_possibility[index])
                x.append(i)
                y.append(self.big_data[tag][i])
        plt.scatter(x, y, c=colors)
        print(self.big_data.keys())
        plt.legend(self.big_data.keys(), [self.colors_possibility[i] for i in range(len(self.big_data.keys()))])
        plt.show()

    def display3D(self):
        x = []
        y = []
        z = []
        colors = []
        index = 0
        for tag in self.big_data:
            index += 1
            print(f"{tag}: {self.colors_possibility[index]}")
            for i in range(len(self.big_data[tag])):
                colors.append(self.colors_possibility[index])
                x.append(i)
                y.append(i)
                z.append(self.big_data[tag][i])
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, c=colors)
        plt.show()
