import sys
import csv

def method1_same_movie_idx(input_list):
    return 0

def method1_range_movie_idx(input_list):
    return 0

def method1_actor_idx(actor_list, page_count):
    output = []
    actor_page_id = []

    with open("actors_id_idx\\root.txt") as fin:
        reader = csv.DictReader(fin, delimiter=",",fieldnames = ['id', 'pageid'])
        next_file = ' '
        prev_id = 0
        for row in reader:
            if(row['id'] != 'internal'):
                if(int(actor_list[0]) <= int(row['id']) and int(actor_list[0]) > prev_id):
                    next_file = row['pageid']
                    print next_file
                prev_id = int(row['id'])

    page_count+=1

    next_file = "actors_id_idx\\" + next_file
    with open(next_file) as fin:
        reader = csv.DictReader(fin, delimiter=",",fieldnames = ['id', 'pageid'])
        for row in reader:
            if(row['id']!='leaf'):
                if(row['id'] == actor_list[0]):
                    actor_page_id.append([row['id'], row['pageid']])

    page_count+=1

    print actor_page_id


    for idx, pages in enumerate(actor_page_id):
        page_count+=1
        next_file = "actors_table\\page" + pages[1]+ '.txt'
        with open(next_file) as fin:
            reader = csv.DictReader(fin, delimiter=",",fieldnames = ['atype', 'id', 'name', 'surname'])
            for row in reader:
                if(row['id'] == actor_page_id[idx][0]):
                    output.append(row)

    print output

    return output, page_count


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

        method1_actor_idx([input_list[2]])




