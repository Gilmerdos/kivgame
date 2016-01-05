class Rect(object):
    def __init__(self, texture):
        self.height = texture.height
        self.width = texture.width
        self.x = 0
        self.y = 0
        self.top = 0
        self.left = 0
        self.right = self.width
        self.bottom = self.height

    def move(self, x, y=None):
        copy = self

        if y == None:
            copy.x += x[0]
            copy.y += x[1]
        else:
            copy.x += x
            copy.y += y

        copy.top = copy.y
        copy.left = copy.x
        copy.right = copy.x + copy.width
        copy.bottom = copy.y + copy.height
        return copy

    def __repr__(self):
        return (self.x, self.y)

