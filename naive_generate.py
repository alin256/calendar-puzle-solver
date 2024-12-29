import numpy as np
import time

import utils
import piece

def naive_recursion(field_id, remaining_pieces, depth=0, verbose=False):
    if verbose:
        print(f'Depth: {depth}')
        field = utils.decode_from_int64(field_id)
        utils.print_field(field)
        print(remaining_pieces)
    if len(remaining_pieces) == 0:
        char_array = np.full((8, 8), '.', dtype=str)
        return char_array

    piece = remaining_pieces[0]
    remaining_pieces = remaining_pieces[1:]

    for k, row_translation_list in enumerate(piece.rot_row_col_list):
        # print(f'k: {k}')
        for i, col_translation_list in enumerate(row_translation_list):
            # print(f'i: {i}')
            for j, piece_id in enumerate(col_translation_list):
                # print(f'j: {j}')
                if utils.check_add(field_id, piece_id):
                    new_field_id = utils.bitwise_add(field_id, piece_id)
                    recursion_reult = naive_recursion(new_field_id, remaining_pieces, depth=depth+1, verbose=verbose)
                    if recursion_reult is not None:
                        bool_array = utils.decode_from_int64(piece_id)
                        # convert to array of chars using the id_char of the piece
                        char_array = recursion_reult
                        char_array[bool_array] = piece.id_char
                        return char_array
    return None


if __name__ == '__main__':
    field_np = np.full((7, 7), False, dtype=bool)
    field_np[0:2, -1] = True
    field_np[-1, -4:7] = True

    field_np[1, 5] = True
    field_np[6, 0] = True

    utils.print_field(field_np)

    field_id = utils.encode_nd_array_to_int64(field_np)

    start_time = time.time()

    print('\n\ngenerating pieces\n\n')

    pieces = piece.return_all_pieces_default(verbose=False)
    print(f'Pre-compute time time: {time.time() - start_time}')

    start_time = time.time()

    print('\n\nstarting recursion\n\n')

    result = naive_recursion(field_id, pieces, verbose=False)
    # convert 2d array from numpy to a single string with line breaks
    result = '\n'.join([''.join(row) for row in result])

    print(f'Recursion time: {time.time() - start_time}')

    print(result)


