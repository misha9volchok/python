# PROGRAMMER MICHAEL VOLCHOK
import os


def trace_route(site_user_input):
    '''
    Traceroute function from syster
    :param site_user_input: the site input from user (without https)
    :return: route value as 'str' type
    '''
    # trace defined from main
    trace = site_user_input
    # trace system operation
    route = os.popen(f"ping {trace}").read()
    print(route)
    return route
