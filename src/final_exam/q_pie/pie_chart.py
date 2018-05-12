class PieChart():

    def __init__(self, list1):

        self.pie_arcs = list1

    def draw(self):
        for i in self.pie_arcs:
            i.draw()
