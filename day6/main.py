#!/usr/bin/env python3


path_mapping = {}

def get_orbit_count(parent):
    count = 0
    for child in path_mapping.get(parent, []): # memoize doesnt benefit much here
        count += get_orbit_count(child)
        count += 1

    return count

def traverse_up(child):
    path = []

    parent = [k for (k, v) in path_mapping.items() if child in v]
    path += parent

    if 'COM' in parent:
        return path
    else:
        return path + traverse_up(parent[0])


def main():
    with open('input', 'r') as f:
    # with open('sample2', 'r') as f:
        for line in f.readlines():
            parent, child = line.replace('\n', '').split(')')
            if not parent in path_mapping:
                path_mapping[parent] = []
            path_mapping[parent].append(child)
            

    count = 0
    for key in path_mapping:
        count += get_orbit_count(key)

    #part 1 
    print(f'Part 1: {count}' )

    path_up = []
    count_to_common_ancestor = -1
    for key, value in path_mapping.items():
        if 'YOU' in value or 'SAN' in value:
            if len(path_up) == 0:
                path_up = traverse_up(key) # path for source (you / santa)
            else:
                t = traverse_up(key) # path for target
                s = set(path_up) # convert source to set 
                for item in (item for item in t if item in s and count_to_common_ancestor == -1):
                    count_to_common_ancestor = path_up.index(item) + t.index(item) # count step to common ancestor

    print(f'Part 2: {count_to_common_ancestor+2}') # +2 since it excludes first & last step

if __name__ == "__main__":
    main()