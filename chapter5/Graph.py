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
        sum = 0
        for d in self.data:
            sum += d[0]
        return sum

    def graph(self):
        print("Cannot graph type 'Graph'")


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
        sum = self.get_data_height_sum()

        degree_ratio = 360 / sum

        degree_offset = 0

        for index, d in enumerate(self.data):
            degree_calculated = degree_ratio * d[0]
            self.create_arc(self.PADDING, self.PADDING, self.width - self.PADDING, self.height - self.PADDING,
                            start=degree_offset, extent=degree_calculated, width=0, fill=d[2], tags="arc")

            radius_width = ((self.width - (2 * self.PADDING)) / 2) - self.PADDING
            radius_height = ((self.height - (2 * self.PADDING)) / 2) - self.PADDING

            self.create_text(
                (math.cos(- degrees_to_radians((degree_calculated / 2) + degree_offset)) * radius_width) + (
                    self.width / 2),
                (math.sin(- degrees_to_radians((degree_calculated / 2) + degree_offset)) * radius_height) + (
                    self.height / 2),
                text=d[1], font="Times 10 bold underline", tags="string")

            degree_offset += degree_calculated


def degrees_to_radians(degree):
    return degree * (math.pi / 180)


def main():
    GraphBar([[6, "A’s", "blue"], [7, "B’s", "yellow"], [4, "C’s", "green"], [2, "F’s", "red"]], 312, 223)
    GraphBar([[140, "Freshman", "red"], [130, "Sophomore", "blue"], [150, "Junior", "yellow"], [80, "Senior", "green"]],
             312, 223)
    GraphPie([[6, "A’s", "blue"], [7, "B’s", "yellow"], [4, "C’s", "green"], [2, "F’s", "red"]], 222, 222)
    GraphPie([[6, "A’s", "blue"], [6, "B’s", "yellow"], [6, "C’s", "green"], [6, "F’s", "red"]], 222, 222)


if __name__ == "__main__":
    main()
