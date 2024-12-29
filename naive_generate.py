import numpy as np
import time

import utils
import piece
import calendar

def naive_recursion(field_id, remaining_pieces, depth=0, verbose=False, used_set=None):
    if verbose:
        print(f'Depth: {depth}')
        field = utils.decode_from_int64(field_id)
        utils.print_field(field)
        print(remaining_pieces)
    if len(remaining_pieces) == 0:
        char_array = np.full((8, 8), '.', dtype=str)
        return char_array
    if used_set is not None:
        if field_id in used_set:
            return None
        used_set.add(field_id)
        

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
                    recursion_reult = naive_recursion(new_field_id, remaining_pieces, 
                                                      depth=depth+1, 
                                                      verbose=verbose,
                                                      used_set=used_set)
                    if recursion_reult is not None:
                        bool_array = utils.decode_from_int64(piece_id)
                        # convert to array of chars using the id_char of the piece
                        char_array = recursion_reult
                        char_array[bool_array] = piece.id_char
                        return char_array
    return None

def generate_date_field(month_number, day_number):
    field_np = np.full((7, 7), False, dtype=bool)
    field_np[0:2, -1] = True
    field_np[-1, -4:7] = True

    month_line = (month_number - 1) // 6
    month_pos  = (month_number - 1) % 6

    day_line = (day_number - 1) // 7 + 2
    day_pos = (day_number - 1) % 7 

    field_np[month_line, month_pos] = True
    field_np[day_line, day_pos] = True

    return field_np

def readable_result(result):
    # convert 2d array from numpy to a single string with line breaks
    return '\n'.join([''.join(row) for row in result])

if __name__ == '__main__':
    start_time_year = time.time()

    #pre-generating pieces bit-masks
    pieces = piece.return_all_pieces_default(verbose=False)

    # iterate calendart days in 2024
    for month in range(1, 13):
        for day in range(1, calendar.monthrange(2024, month)[1] + 1):
            field_np = generate_date_field(month, day)
            field_id = utils.encode_nd_array_to_int64(field_np)
            
            start_time = time.time()

            used_set = None

            result = naive_recursion(field_id, pieces, verbose=False, used_set=used_set)
            
            result = readable_result(result)

            # print('\n\nChecking field\n')
            # print the text {Month} {day}
            print(f'{calendar.month_name[month]} {day}\n')
            utils.print_field(field_np)
            
            if used_set is not None:
                print(f"Used set size: {len(used_set)}")

            
            print(f'\nAnswer for {calendar.month_name[month]} {day}\n')
            print(result)

            with open('results.txt', 'a') as f:
                f.write(f'Answer for {calendar.month_name[month]} {day}\n')
                f.write(result)
                f.write('\n\n')
            print(f'\nRecursion time: {time.time() - start_time}')

    # print total time
    print(f'Total time: {time.time() - start_time_year}')


