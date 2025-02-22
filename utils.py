import numpy as np

def encode_nd_array_to_int64(arr_in, extend_with=True):
    arr = np.full((8, 8), extend_with, dtype=bool)
    shape = arr_in.shape
    arr[:shape[0], :shape[1]] = arr_in
    return int(''.join([str(int(x)) for x in arr.flatten()]), 2)

def decode_from_int64(num, num_rows=8, num_cols=8, verbose=False):
    # todo stop assuming fixed size grid
    bin_str = bin(num)[2:]
    if verbose:
        print(bin_str)
    bin_str = '0' * (num_rows * num_cols - len(bin_str)) + bin_str
    if verbose:
        print(bin_str)
    flat_array = np.array([int(x) for x in bin_str], dtype=bool)
    if verbose:
        print(flat_array)
        print(flat_array.shape)
    grid = flat_array.reshape(num_rows, num_cols)
    return grid

def rotate(arr):
    return np.rot90(arr)

def flip(arr):
    return np.flip(arr, axis=0)

def field_to_int64(arr):
    return encode_nd_array_to_int64(arr)

def print_field(arr):
    for row in arr:
        print(''.join(['X' if cell else '.' for cell in row]))

def field_to_str(arr):
    return '\n'.join([''.join(['X' if cell else '.' for cell in row]) for row in arr])

def check_add(field_id, piece_id):
    return not (field_id & piece_id)

def bitwise_add(field_id, piece_id):
    return field_id | piece_id
