class Rectangle:

    def __init__(self, x, y, w, h):
        self.mX = x
        self.mY = y
        self.mWidth = w
        self.mHeight = h
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def setX(self, v):
        if v > 0:
            self.mX = v
            return True
        return False

    def setY(self, v):
        if v > 0:
            self.mY = v
            return True
        return False

    def setWidth(self, v):
        if v > 0:
            self.mWidth = v
            return True
        return False

    def setHeight(self, v):
        if v > 0:
            self.mHeight = v
            return True
        return False

    def getArea(self):
        return self.mWidth * self.mHeight

    def getPerimeter(self):
        return 2 * (self.mWidth + self.mHeight)