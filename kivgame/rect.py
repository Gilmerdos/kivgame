class Rect(object):
    def __init__(self, left, top=None, width=None, height=None):
        if height != None:
            self.height = height
        else:
            self.height = left.height

        if width != None:
            self.width = width
        else:
            self.width = left.width

        if width != None:
            self.width = width
        else:
            self.width = left.width

        if top != None:
            self.y = top
            self.top = top
        else:
            self.y = 0
            self.top = 0

        if top != None and width != None and height != None:
            self.x = left
            self.left = left
        else:
            self.x = 0
            self.left = 0

        self.right = self.width
        self.bottom = self.height

    def collidepoint(self, x, y=None):
        if y == None: x, y = x

        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            return True
        else:
            return False

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

