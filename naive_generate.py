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
        return True

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
                    if naive_recursion(new_field_id, remaining_pieces, depth=depth+1, verbose=verbose):
                        return True

    return False


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

    print(f'Recursion time: {time.time() - start_time}')

    print(result)


