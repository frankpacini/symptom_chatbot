from unittest.mock import Mock

import main
# testing function locally

def test_print_name():
    race = ['white']
    age = ['18', '20']
    data = {'race': race}
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    res = main.sort_data(req) 
    print("result is ", res)
    assert(1==2)
# def test_cors():
#     name = 'white'
#     data = {'race': name}
#     req = Mock(get_json=Mock(return_value=data), args=data)

#     # Call tested function
#     res = main.cors_enabled(req) 
#     print("result is ", res)
#     assert(1==2)

