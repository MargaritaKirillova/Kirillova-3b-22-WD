class GeometricFigure:
    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def figure_info(self):
        print(self.square, "- Площадь", ",", self.perimeter, "- Периметр")


GeometricFigure = GeometricFigure(40, 24)
GeometricFigure.figure_info()