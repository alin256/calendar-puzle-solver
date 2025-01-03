import naive_generate
import piece
import utils
import sys
import time
import calendar

# take two command line arguments and generate the answer
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python generate_single.py <month_number> <day_number>')
        print('Using December 25th as default')
        month_number = 12
        day_number = 25
    else:
        month_number = int(sys.argv[1])
        day_number = int(sys.argv[2])
    
    start_time = time.time()

    print(f'\nAnswer for {calendar.month_name[month_number]} {day_number}\n')

    field = naive_generate.generate_date_field(month_number, day_number)
    field_id = utils.field_to_int64(field)
    result = naive_generate.naive_recursion(field_id, 
                                            piece.return_all_calendar_pieces_default(), 
                                            verbose=False)
    readable_result = naive_generate.readable_result(result)
    print(readable_result)    

    print(f'\nTotal time: {time.time() - start_time}')    

