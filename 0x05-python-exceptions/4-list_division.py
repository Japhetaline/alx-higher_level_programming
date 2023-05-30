#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Takes two lists and creates a new list with result of
    division operstion
    """

    current_list = []
    outcome = 0
    for k in range(0, list_length):
        try:
            outcome = (my_list_1[k] / my_list_2[k])
        except TypeError:
            outcome = 0
            print("wrong type")
        except ZeroDivisionError:
            outcome = 0
            print("division by 0")
        except IndexError:
            outcome = 0
            print("out of range")
        finally:
            current_list.append(outcome)
            return current_list
