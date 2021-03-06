# README

Name: Leo Shang (Student ID: 301280479)

School: SFU

## Development Environment:

    Language: Python
    Version: Python 3.6.4
    OS: Windows 10
    IDE: PyCharm (Community Edition)

## High level description of the algorithm:

    Keep two lists named "finished_list" and "enter":
        1. "enter" keeps the record of running (not exit yet) function names and their starting time with a dirty bit detecting the existence of nested function call. 
        2. "finished_list" is the list of tuples storing functions with their count and accumulated running time.

    Also, the program keeps the time consumed for the nested functions, called time_inside_nested. Therefore,for any given function, it is either nested or not nested:
        1. not nested: calculate as finish time - start time
        2. nested: calculate as finish time - start time - time_inside_nested

    At the end of program, report the tuples in "finished_list"

## Note:

    The program is built on the assumption that the function enters and exits naturally:
        i.e.: If A() calls B(), then B() must exit before A() does. Otherwise,
        the program triggers error report(see detail at line 12 of solution.py)
