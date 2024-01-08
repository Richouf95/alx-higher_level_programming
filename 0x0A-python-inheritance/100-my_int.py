#!/usr/bin/python3
"""
    My integer
"""


class MyInt(int):
    """
        MyInt rebel
    """
    def __eq__(self, v):
        """
            Invert equality
        """
        return self.real != v

    def __ne__(self, v):
        """
            Invert negation
        """
        return self.real == v
