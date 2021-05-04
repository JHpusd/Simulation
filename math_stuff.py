import math

def calc_right_riemann(func, start, end, step_size):
    points = []
    counter = start + step_size
    while counter <= end:
        points.append(counter)
        counter += step_size
    
    points = [func(point) for point in points]
    return sum(points) * step_size

def cross_product(v1, v2):
    assert len(v1) == len(v2) == 3
    negative = False
    tracker = [0, 1, 2]
    result = []
    for i in range(len(v1)):
        tracker_copy = list(tracker)
        tracker_copy.remove(i)
        term = (v1[tracker_copy[0]]*v2[tracker_copy[1]]) - (v1[tracker_copy[1]]*v2[tracker_copy[0]])
        if negative:
            term *= -1
        negative = not negative
        result.append(term)
    return result

def len_of_vector(vector):
    return math.sqrt(sum([term**2 for term in list(vector)]))

def cycle_string_to_lists(cycle_string):
    cycles = []
    for i in range(len(cycle_string)):
        char = cycle_string[i]
        if char == '(':
            sample = cycle_string[i+1:]
            end_index = sample.index(')')
            sample = sample[:end_index].split(',')
            cycles.append([int(term) for term in sample])
    return cycles

def next_cycle_term(target_term, cycle_list):
    for cycle in cycle_list:
        if target_term in cycle:
            index = cycle.index(target_term)
            try:
                return cycle[index+1]
            except IndexError:
                return cycle[0]
    return target_term

def print_cycle(cycle_string):
    cycles = cycle_string_to_lists(cycle_string)

    largest_num = max([item for cycle in cycles for item in cycle])
    for i in range(1, int(largest_num)+1):
        print(str(i) + ' -> ' + str(next_cycle_term(i, cycles)))
    return None

def cycle_multiply(c1, c2, print_steps=False):
    c1 = cycle_string_to_lists(c1)
    c2 = cycle_string_to_lists(c2)
    result = []
    
    largest_num = max([i for c in c1 for i in c] + [i for c in c2 for i in c])
    for i in range(1, int(largest_num)+1):
        start = i
        mid = next_cycle_term(i, c2)
        end = next_cycle_term(mid, c1)
        for cycle in result:
            if start in cycle and end not in cycle:
                start_index = cycle.index(start)
                cycle.insert(start_index+1, end)
            if end in cycle and start not in cycle:
                end_index = cycle.index(end)
                cycle.insert(end_index, start)
        if start not in [i for c in result for i in c] and start != end:
            result.append([start, end])
        elif start == end:
            result.append([start])
        if print_steps:
            print(str(start) + ' -> ' + str(mid) + ' -> ' + str(end))
            print(result,'\n')
    return result

def cycle_list_to_string(cycle_list):
    result = ''
    for cycle in cycle_list:
        result += '('
        for item in cycle[:-1]:
            result += str(item) + ','
        result += str(cycle[-1]) + ')'
    return result
        
def integral(function, start, end, step_size):
    result = 0
    while start <= end:
        result += function(start) * step_size
        start += step_size
    return result
        
func = lambda x: 1 / (x - 1)**(1/3)

result = cycle_multiply('(1,5)(2,4)', '(1,5)', True)
print(cycle_list_to_string(result))