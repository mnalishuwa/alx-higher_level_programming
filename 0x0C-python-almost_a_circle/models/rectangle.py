#!/usr/bin/python3


"""
Rectangle module docs
Rectangle class inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class template:
        Rectangle is subclass of Base

    Attributes:
        id - inherited

    Methods:
        Base.__init__(self, id) - super
        __init__(self, width, height, x=0, y=0, id=None)
        __str__(self)
        area(self)
        display(self)
        height(self)
        height(self, value)
        width(self)
        width(self, value)
        x(self)
        x(self, value)
        y(self)
        y(self, value)
        integer_validator(self, name, value)
        position_validator(self, name, value)
        update(self, *args, **kwargs)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle constructor method

        Arguments:
            id
            width
            height
            x
            y

        Attributes:
            id
            __width
            __height
            __x
            __y

        Return:
            object
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    # override builtin __str__ method
    def __str__(self):
        """
        Return string representation of rectangle object

        Arguments:

        Return:
            string - Rectangle object representation
        """
        class_name = self.__class__.__name__
        return str("[{}] ({}) {}/{} - {}/{}".format(class_name,
                                                    self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height))

    # Getter and Setters
    @property
    def height(self):
        """
        getter method for height

        Args:

        Return:
            int - rectangle object height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter  method for height

        Arguments:
            value - int

        Return:
            None
        """
        self.integer_validator("height", value)
        self.__height = value

    @property
    def width(self):
        """
        Getter method for width

        Arguments:

        Return:
            int - rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width

        Arguments:

        Return:
            None
        """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def x(self):
        """
        Getter method for x

        Arguments:

        Return:
            int - x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method  for x

        Arguments:
            value(int)

        Return:
            None
        """
        self.position_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y

        Arguments:

        Return:
            y - int
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter methdo for y

        Arguments:
            value - int

        Return:
            None
        """
        self.position_validator("y", value)
        self.__y = value

    # utility methods
    def area(self):
        """
        Area method

        Args:

        Return:
            area(int) - width * height
        """
        return self.width * self.height

    def display(self):
        """
        Visually display Rectangle representation
        by printing to stdout with # symbol

        Arguments:

        Return:
            None
        """
        rows = self.height
        columns = self.width
        string_rectangle = ""
        symbol = "#"
        for y_pos in range(self.y):
            print()
        for row in range(rows):
            string_rectangle += (" " * self.x) + (symbol * columns)
            if row != rows - 1 and columns != 0:
                string_rectangle += "\n"
        print(string_rectangle)

    def integer_validator(self, name, value):
        """
        Integer validator function

        Args:
            name
            value
        Return:
            None
        """
        if not isinstance(value, int) or type(value) not in (int,):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def position_validator(self, name, value):
        """
        Position validator function

        Args:
            name
            value
        Return:
            None
        """
        if not isinstance(value, int) or type(value) not in (int,):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def to_dictionary(self):
        """
        Return dictionary representation of Rectangle

        Arguments:

        Return:
            dict
        """
        return {attr: getattr(self, attr)
                for attr in dir(self)
                if not attr.startswith("_")
                and not callable(getattr(self, attr))}

    def update(self, *args, **kwargs):
        """
        Update attributes using * arguments

        Arguments:
            *args(tuple)

        Return:
            None
        """
        if args:
            self.id, self.width, self.height, self.x, self.y =\
                args + (self.id, self.width,
                        self.height, self.x, self.y)[len(args):]
            return

        self.id = kwargs.get("id", self.id)
        self.width = kwargs.get("width", self.width)
        self.height = kwargs.get("height", self.height)
        self.x = kwargs.get("x", self.x)
        self.y = kwargs.get("y", self.y)
