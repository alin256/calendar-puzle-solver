import numpy as np

import utils

class GeometricPiece:
    def __init__(self, arr: list):
        self.arr = arr
        self.rows = len(arr)
        self.cols = len(arr[0])
        self.rotations = {}

    def _generate_rotations(self):
        ind = 0

        rotation = self.arr.copy()
        for i in range(4):
            print(ind)
            utils.print_field(rotation)
            print()
            rotation = utils.rotate(rotation)
            ind += 1
        
        rotation = utils.flip(rotation)
        for i in range(4):
            print(ind)
            utils.print_field(rotation)
            print()
            rotation = utils.rotate(rotation)
            ind += 1

if __name__ == '__main__':
    piece = GeometricPiece([[True, False], 
                            [True, True],
                            [True, False],
                            [True, False],
                            [True, False]])
    piece._generate_rotations()

    
