#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Function inherit from class Rectangle
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloading string return [Square] (<id>)
        <x>/<y> - <size>
        """
        return (
                f"[Square] ({self.id})"
                f"{self.x}/{self.y} - {self.width}"
                )

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        Int: the size of the sqaure, which is equal to the width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Sets the size of the square by assigning the given value to both
        the width and height attributes.
        This ensures that the square maintains equal width and height

        Args:
        Value (int): The new size of a sqaure

        Raises:
        ValueError: If the value is not a position integer
        """
        self.width = value
        self.height = value

        def update(self, *args, **kwargs):
            """
            Updates the attributes of the Square.

            Args:
            *args: List of arguments. The first argument should
            be the id attribute. The second argument should be
            the size attribute.The third argument should be the
            x attribute. The fourth argument should be the y attribute.

            **kwargs: Keyworded arguments. each key represents
            an attribute of the instance.

            Raises:
            ValueError: If there are more than
            four arguments provided in *args.
            """
            if args:
                if len(args) > 4:
                    raise ValueError("Too many arguments provided.")
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            else:
                if 'id' in kwargs:
                    self.id = kwargs['id']
                if 'size' in kwargs:
                    self.size = kwargs['size']
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']

        def to_dictionary(self):
            """
            Returns a dictionary representation of the Square.

            Returns:
            dict: A dictionary containing the attributes of the Square
            the keys are 'id','size', 'x', 'y'
            """
            return {
                    'id': self.id,
                    'size': self.size,
                    'x': self.x,
                    'y': self.y
                    }
