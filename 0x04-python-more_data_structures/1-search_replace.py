#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replacing all occurances of search with replace
    """
    return (
            [jcode if jcode != search else replace for jcode in my_list]
            )
