class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        pass

    def set_height(self, height):
        self.height = height
        pass

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
        pass

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        s = ''
        for i in range(self.height):
            for j in range(self.width):
                s += '*'
            s += '\n'
        return s

    def get_amount_inside(self, obj):
        return self.get_area() // obj.get_area()


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.width = side
        self.height = side

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

    def set_width(self, side):
        self.width = side
        self.width = side

    def set_height(self, side):
        self.width = side
        self.height = side
