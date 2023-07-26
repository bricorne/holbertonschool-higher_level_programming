#!/usr/bin/python3
"""create class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    
    def display(self):
        """print the square"""
        for y in range(self.y):
            print()
        for i in range(self.size):
            print(' ' * self.x + '#' * self.size)

    def update(self, *args, **kwargs):
        """update the square"""
        if len(args) > 0:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """return dictionary"""
        return {
        'id': self.id,
        'x': self.x,
        'y': self.y,
        'size': self.size,
        }