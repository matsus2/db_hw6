import sys
import csv

def method1_same_movie_idx(input_list):
    return 0

def method1_range_movie_idx(input_list):
    return 0

def method1_actor_idx(actor_list):
    return 0


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("incorrect amount of arguments")
        sys.exit(0)

    with open(sys.argv[1]) as r:
        ifile = r.readlines()

    for line in ifile:
        input_list = []
        input_list = line.split(',')

        if(input_list[0] == input_list[1]):
            method1_same_movie_idx(input_list)
        else:
            method1_range_movie_idx(input_list)


