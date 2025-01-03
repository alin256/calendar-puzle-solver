import time
import naive_generate
import piece
import utils
import sys

# take two command line arguments and generate the answer
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python generate_single_city.py <x_post> <y_post> (coordinates of light post)')
        print('Using (0, 0) as default')
        x_post = 0
        y_post = 0
    else:
        x_post = int(sys.argv[1])
        y_post = int(sys.argv[2])
    start_time = time.time()

    field = naive_generate.generate_city_field(x_post, y_post)
    print(utils.field_to_str(field))
    field_id = utils.field_to_int64(field)
    result = naive_generate.naive_recursion(field_id, 
                                            piece.return_all_city_pieces_default(), 
                                            verbose=False)
    readable_result = naive_generate.readable_result(result)
    
    print(f'\nAnswer for light post in coordinates ({x_post}, {y_post}) \n[0-indexed]\n')
    print(readable_result)

    print(f'\nTotal time: {time.time() - start_time}')    

