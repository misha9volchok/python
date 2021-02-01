# PROGRAMMER MICHAEL VOLCHOK
from urllib import request, error

from client import *

file_path = "C:/Users/user/PycharmProjects/Socket Final Project/trace_route.txt"


def site_check(site_user_input):
    '''
    check the URL input from user.
    :return:
    The URL code after check
    '''
    # create new URL with added https://
    full_site_address = "https://" + site_user_input

    try:
        return request.urlopen(full_site_address).getcode()
    except error.HTTPError as err:
        print(err)
    except ValueError:
        # user input is not DNS name
        print(" Wrong input valid internet address only!")
    except error.URLError:
        print(" Wrong URL input! ")
    except OSError:
        print(" Wrong input valid internet address only!")
