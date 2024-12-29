import numpy as np

import utils

class GeometricPiece:
    def __init__(self, arr, field_max_rows=7, field_max_cols=7):
        self.rows = len(arr)
        self.cols = len(arr[0])
        self.arr = np.array(arr)
        self.rotations = {}
        self._generate_rotations()
        self.rot_row_col_list = []
        self._generate_row_col_rotations(field_max_rows, field_max_cols)

    def _generate_rotations(self, verbose=False):
        ind = 0
        rotation = self.arr.copy()
        for i in range(4):
            if verbose:
                print(ind)
                utils.print_field(rotation)
                print()
            id = utils.encode_nd_array_to_int64(rotation, False)
            self.rotations[id] = rotation
            rotation = utils.rotate(rotation)
            ind += 1
        
        rotation = utils.flip(rotation)
        for i in range(4):
            if verbose:
                print(ind)
                utils.print_field(rotation)
                print()
            id = utils.encode_nd_array_to_int64(rotation, False)
            self.rotations[id] = rotation
            rotation = utils.rotate(rotation)
            ind += 1
        if verbose:
            print(f'Total rotations: {len(self.rotations)}\n')

    def _generate_row_col_rotations(self, rows_to_fill, cols_to_fill, verbose=False):
        for k, rot in enumerate(self.rotations):
            self.rot_row_col_list.append([])
            for i in range(rows_to_fill - self.rotations[rot].shape[0] + 1):
                self.rot_row_col_list[k].append([])
                for j in range(cols_to_fill - self.rotations[rot].shape[1] + 1):
                    result = np.full((rows_to_fill, cols_to_fill), False, dtype=bool)
                    result[i:i+self.rotations[rot].shape[0], j:j+self.rotations[rot].shape[1]] = self.rotations[rot]
                    if verbose:
                        print(f'Rotation {k} at ({i}, {j})')
                        utils.print_field(result)
                    self.rot_row_col_list[k][i].append(utils.encode_nd_array_to_int64(result, False))
    
    def __str__(self):
        return utils.field_to_str(self.arr)

def return_all_pieces_default(verbose=False):
    pieces = []
    #generate rotations of L-shaped piece 3x3
    piece = GeometricPiece([[True, False, False],
                            [True, False, False],
                            [True, True,  True]])
    pieces.append(piece)
    #generate rotations of Z-shaped piece 3x3
    piece = GeometricPiece([[True,  True, False],
                            [False, True, False],
                            [False, True, True]])
    pieces.append(piece)
    #generate rotations of L-shaped piece 4x2
    piece = GeometricPiece([[True, False],
                            [True, False],
                            [True, False],
                            [True, True]])
    pieces.append(piece)
    #generate rotations of T-shaped piece 2x4   
    piece = GeometricPiece([[True, True, True, True],
                            [False, True, False, False]])
    pieces.append(piece)
    #generate rotations of Z-shaped piece 2x4
    piece = GeometricPiece([[True, True, False, False],
                            [False, True, True, True]])
    pieces.append(piece)
    #generate rotations of Pi-shaped piece 2x3
    piece = GeometricPiece([[True, True, True],
                            [True, False, True]])
    pieces.append(piece)
    #generate rotations of boot-shaped piece 3x2
    piece = GeometricPiece([[True, False],
                            [True, True],
                            [True, True]])
    pieces.append(piece)
    #generate rectangle piece 3x2
    piece = GeometricPiece([[True, True],
                            [True, True],
                            [True, True]])
    pieces.append(piece)
    if verbose:
        for i, piece in enumerate(pieces):
            print(f'Piece {i+1}')
            print(piece)
            print()
    return pieces

if __name__ == '__main__':
    pieces = return_all_pieces_default()
    exit(0)

    piece = GeometricPiece([[True, False], 
                            [True, True],
                            [True, False],
                            [True, False],
                            [True, False]])

    #generate rotations of L-shaped-True piece 3x3
    piece = GeometricPiece([[True, False, False],
                            [True, False, False],
                            [True, True, True]])

    
