paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

# OUTPUT = Final destination: Sao Paulo

def solution(paths):
    # create a dictionary to store the paths
    path_dict = {}
    # iterate through the paths
    for path in paths:
        # if the path[0] is not in the dictionary
        if path[0] not in path_dict:
            # add the path to the dictionary
            path_dict[path[0]] = path[1]
    # iterate through the paths
    for path in paths:
        # if the path[1] is not in the dictionary
        if path[1] not in path_dict:
            # return the path[1]
            print(path[1])

solution(paths)
