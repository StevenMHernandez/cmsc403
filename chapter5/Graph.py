from tkinter import *

import math


class Graph(Canvas):
    data = []

    def __init__(self, data, width, height):
        self.window = Tk()
        self.window.title("Graphing: " + str(type(self)))

        super().__init__(self.window, width=width, height=height, bg="white")
        self.pack()

        self.data = data
        self.width = width
        self.height = height

        self.graph()

        self.display_wind()

    def display_wind(self):
        self.window.mainloop()

    def get_data_height_max(self):
        data_max_height = self.data[0][0]
        for d in self.data:
            if d[0] > data_max_height:
                data_max_height = d[0]
        return data_max_height

    def get_data_height_sum(self):
        height_sum = 0
        for d in self.data:
            height_sum += d[0]
        return height_sum


class GraphBar(Graph):
    PADDING = 10
    MIN_BAR_HEIGHT = 10

    def graph(self):
        bar_width = (self.width - (2 * self.PADDING)) / len(self.data)

        data_max_height = self.get_data_height_max()

        bar_height_range = (self.height - (2 * self.PADDING)) / (data_max_height)

        for index, d in enumerate(self.data):
            self.create_rectangle(self.PADDING + (bar_width * index),
                                  self.height - self.PADDING,
                                  self.PADDING + (bar_width * (index + 1)),
                                  self.height - (bar_height_range * d[0]),
                                  tags="rect",
                                  fill=d[2])

            self.create_text(self.PADDING + (bar_width * (index + 0.5)),
                             self.height, text=d[1],
                             font="Times 10 bold underline", tags="string")


class GraphPie(Graph):
    PADDING = 10

    def graph(self):
        height_sum = self.get_data_height_sum()

        degree_ratio = 360 / height_sum

        degree_offset = 0

        for index, d in enumerate(self.data):
            degree_calculated = degree_ratio * d[0]
            self.create_arc(self.PADDING, self.PADDING, self.width - self.PADDING, self.height - self.PADDING,
                            start=degree_offset, extent=degree_calculated, width=0, fill=d[2], tags="arc")

            radius_width = ((self.width - (2 * self.PADDING)) / 2) - self.PADDING
            radius_height = ((self.height - (2 * self.PADDING)) / 2) - self.PADDING
            angle_radians = -degrees_to_radians((degree_calculated / 2) + degree_offset)

            text_color = "black" if d[2] != "black" else "gray"

            self.create_text((math.cos(angle_radians) * radius_width) + (self.width / 2),
                             (math.sin(angle_radians) * radius_height) + (self.height / 2),
                             text=d[1], font="Times 10 bold underline", tags="string", fill=text_color)

            degree_offset += degree_calculated


def degrees_to_radians(degree):
    return degree * (math.pi / 180)


def main():
    infile = open("graphData.txt", "r")
    line = infile.readline()
    while line != '':
        chart_type, data, width, height = line.split('\t')
        print(data)
        if chart_type == "bar":
            GraphBar(eval(data), int(width), int(height))
        else:  # we can assume perfect input, so this is pie
            GraphPie(eval(data), int(width), int(height))

        line = infile.readline()


if __name__ == "__main__":
    main()
