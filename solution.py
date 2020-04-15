def exist(list, name):  # function return boolean for whether a function name exists in some list
    for tuples in list:
        if tuples[0] == name:
            return True
    return False


def find_index(list, name):  # find index of some function name in some list, if not found, return -1 and report error
    for tuples in list:
        if tuples[0] == name:
            return list.index(tuples)
    print("Error: the order of function call has error")
    return -1


def cvt_sec_2_usec(second):  # convert second to usec
    second = float(second)
    usec = second * 1000000
    usec = "%.9f" % usec
    return usec


with open("log.txt") as f:
    content = f.readlines()

enter = []  # a list that maintains unfinished functions in the form of tuple: (function name, start time, if nested)
finished_list = []  # a list maintains the function that's already exited. Ready for print at anytime
time_inside_nested = 0  # the time inside the nested function.
# General idea: exit_time(A) - start_time(A) - time_inside_nested == time spent on function A


for line in content:
    str = line.split()
    if str[1] == "enters":  # if enter a function
        start_time = str[0]
        start_time = start_time[:-1]
        start_time = cvt_sec_2_usec(start_time)

        if len(enter) >= 1:     # change dirty bit to 1 to indicate the function is nested
            temp_name, temp_startTime, temp_dirtyBit = enter.pop()
            enter.append((temp_name, temp_startTime, 1))
        enter.append((str[-1], start_time, 0))  # append new entered function as dirty bit = 0

    elif str[1] == "exits":     # if some function exits
        end_time = str[0]
        end_time = end_time[:-1]
        end_time = cvt_sec_2_usec(end_time)
        function_name = str[-1]

        if enter[-1][2] == 0:   # if the function is not nested (exit right after it enters)
            duration = float(end_time) - float(enter[-1][1])    # calculate duration and add to "finished_list"
            if exist(finished_list, function_name):
                index = find_index(finished_list, function_name)
                function_name, old_count, old_duration = finished_list.pop(index)
                finished_list.insert(index, (function_name, old_count + 1, old_duration + duration))
            else:
                finished_list.append((function_name, 1, duration))
            time_inside_nested += duration
            enter.pop()
        elif enter[-1][2] == 1: # if the function is nested
            duration = float(end_time) - float(enter[-1][1]) - time_inside_nested
            # calculate the duration by exit time - enter time - total nested function time
            # also add the finished function into "finished_list"

            if exist(finished_list, function_name):
                index = find_index(finished_list, function_name)
                function_name, old_count, old_duration = finished_list.pop(index)
                finished_list.insert(index, (function_name, old_count + 1, old_duration + duration))
            else:
                finished_list.append((function_name, 1, duration))
            time_inside_nested = float(end_time) - float(enter[-1][1])
            enter.pop()

print("Function" + "\t" + "Times-called" + "\t" + "Time-spent")     # giving report
for tuples in finished_list:
    function_name = tuples[0]
    print(function_name[:-2], end='\t', flush=True)
    print(tuples[1], end='\t', flush=True)
    print("{} {}".format((tuples[2]), "us"))
