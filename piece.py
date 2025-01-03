import numpy as np

import utils

class GeometricPiece:
    def __init__(self, arr, id_char='#', field_max_rows=7, field_max_cols=7, allow_flip=True, verbose=False):
        self.rows = len(arr)
        self.cols = len(arr[0])
        self.arr = np.array(arr)
        self.id_char = id_char
        if verbose:
            print(f'Processing piece {id_char}')
        self.rotations = {}
        self._generate_rotations(verbose=verbose, allow_flip=allow_flip)
        self.rot_row_col_list = []
        self._generate_row_col_rotations(field_max_rows, field_max_cols)

    def _generate_rotations(self, verbose=False, allow_flip=True):
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

        if allow_flip:
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
    
def return_all_city_pieces_default(verbose=False):
    pieces = []
    # generate cornrner piece 3x3
    piece = GeometricPiece([[True, False, False],
                            [True, True, False],
                            [True, True,  True]], id_char='A', allow_flip=False)
    pieces.append(piece)
    # generate I-shaped piece 5x1
    piece = GeometricPiece([[True],
                            [True],
                            [True],
                            [True],
                            [True]], id_char='I',allow_flip=False)
    pieces.append(piece)
    # generate !-shaped piece 1x2
    piece = GeometricPiece([[True, True]], id_char='!', allow_flip=False)
    pieces.append(piece)
    # generate M-shaped piece 3x3
    piece = GeometricPiece([[True, False, False],
                            [True, True,  False],
                            [False, True, True]], id_char='M', allow_flip=False)
    pieces.append(piece)
    # generate T-shaped piece 4x2
    piece = GeometricPiece([[True, False],
                            [True, True],
                            [True, True],
                            [True, False]], id_char='T',
                            allow_flip=False)
    pieces.append(piece)
    #generate Q-shaped piece 4x3
    piece = GeometricPiece([[False, True, False],
                            [True, True, True],
                            [True, True, True],
                            [True, False, False]], 
                            id_char='Q',
                            allow_flip=False,
                            verbose=False)
    pieces.append(piece)
    #generate P-shaped piece 4x2
    piece = GeometricPiece([[True, False],
                            [True, True],
                            [True, False],
                            [True, False]], id_char='P',
                            allow_flip=False)
    pieces.append(piece)
    #generate Y-shaped piece 3x2
    piece = GeometricPiece([[True, False],
                            [True, True],
                            [True, False]], 
                            id_char='Y',
                            allow_flip=False)
    pieces.append(piece)
    # generate E-shaped piece 3x3
    piece = GeometricPiece([[True, True, False],
                            [True, True, True],
                            [True, True, False]], 
                            id_char='E',
                            allow_flip=False)
    pieces.append(piece)
    return pieces

def return_all_calendar_pieces_default(verbose=False):
    pieces = []
    #generate rotations of L-shaped piece 3x3
    piece = GeometricPiece([[True, False, False],
                            [True, False, False],
                            [True, True,  True]], id_char='L')
    pieces.append(piece)
    #generate rotations of Z-shaped piece 3x3
    piece = GeometricPiece([[True,  True, False],
                            [False, True, False],
                            [False, True, True]], id_char='Z')
    pieces.append(piece)
    #generate rotations of J-shaped piece 4x2
    piece = GeometricPiece([[True, False],
                            [True, False],
                            [True, False],
                            [True, True]], id_char='J')
    pieces.append(piece)
    #generate rotations of T-shaped piece 2x4   
    piece = GeometricPiece([[True, True, True, True],
                            [False, True, False, False]], id_char='T')
    pieces.append(piece)
    #generate rotations of Q-shaped piece 2x4
    piece = GeometricPiece([[True, True, False, False],
                            [False, True, True, True]], id_char='Q')
    pieces.append(piece)
    #generate rotations of C-shaped piece 2x3
    piece = GeometricPiece([[True, True, True],
                            [True, False, True]], id_char='C')
    pieces.append(piece)
    #generate rotations of boot-shaped piece 3x2
    piece = GeometricPiece([[True, False],
                            [True, True],
                            [True, True]], id_char='B')
    pieces.append(piece)
    #generate rectangle O-shaped piece 3x2
    piece = GeometricPiece([[True, True],
                            [True, True],
                            [True, True]], id_char='O')
    pieces.append(piece)
    if verbose:
        for i, piece in enumerate(pieces):
            print(f'Piece {i+1}')
            print(piece)
            print()
    return pieces

if __name__ == '__main__':
    pieces = return_all_calendar_pieces_default()
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

    
