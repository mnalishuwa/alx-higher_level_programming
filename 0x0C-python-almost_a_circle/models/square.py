#!/usr/bin/python3


"""
Square module docs
Square class inherits from Rectangle
Rectangle class inherits from Base
"""


from rectangle import Rectangle


class Square(Rectangle):
    """
    Square class template:
        Square is a subclass of Rectangle

    Attributes:
        id (inherited)
        __width (inherited)
        __height (inherited)
        __x (inherited)
        __y (inherited)

    Methods:
        Base.__init__(self, id) - super
        Rectangle.__init__(self, width, height, x=0, y=0, id=None)
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
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square constructor method

        Arguments:
            id
            size
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
        super().__init__(size, size, x, y, id)

    # override builtin __str__ method
    def __str__(self):
        """
        Return string representation of rectangle object

        Arguments:

        Return:
            string - Rectangle object
        """
        string_representation = super().__str__()
        end_pos = -1
        for end_pos in range(-1, -len(string_representation), -1):
            if string_representation[end_pos] == "/":
                break
        return string_representation[:end_pos]

    @property
    def size(self):
        """
        Getter for size

        Arguments:

        Return:
            size - int
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size

        Arguments:
            value

        Return:
            None
        """
        self.width = value
        self.height = value

    # override to dictionary method
    def to_dictionary(self):
        """
        Return dictionary representation of Square

        Arguments:

        Return:
            dict
        """
        return {attr: value for attr, value
                in super().to_dictionary().items()
                if attr not in ("width", "height")}

    # override the update method
    def update(self, *args, **kwargs):
        """
        Update attributes using * arguments

        Arguments:
            *args(tuple)
            **kwargs(dict)

        Return:
            None
        """
        if args:
            self.id, self.size, self.x, self.y =\
                args + (self.id, self.size, self.x, self.y)[len(args):]
            return

        self.id = kwargs.get("id", self.id)
        self.size = kwargs.get("size", self.size)
        self.x = kwargs.get("x", self.x)
        self.y = kwargs.get("y", self.y)
