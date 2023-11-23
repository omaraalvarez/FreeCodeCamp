class Rectangle:

  def __init__(self, width, height):

    self.w = width
    self.h = height

  def __str__(self):

    return f'Rectangle(width={self.w}, height={self.h})'

  def set_width(self, width):

    self.w = width

  def set_height(self, height):

    self.h = height

  def get_area(self):

    return self.w * self.h

  def get_perimeter(self):

    return 2 * self.w + 2 * self.h

  def get_diagonal(self):

    return (self.w**2 + self.h**2)**0.5

  def get_picture(self):

    if self.h > 50 or self.w > 50:

      return 'Too big for picture.'

    else:

      pic = ''

      for _ in range(self.h):

        pic += self.w * '*' + '\n'

      return pic

  def get_amount_inside(self, fig):

    A1 = self.get_area()
    A2 = fig.get_area()

    return A1 // A2


class Square(Rectangle):

  def __init__(self, width):

    self.w = width
    self.h = self.w

  def __str__(self):

    return f'Square(side={self.w})'

  def set_side(self, s):

    self.w = s
    self.h = s

  def set_width(self, s):

    self.w = s
    self.h = s

  def set_height(self, s):

    self.w = s
    self.h = s
