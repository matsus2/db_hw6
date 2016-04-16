import sys
import csv

def method1_same_movie_idx(input_list):
    movie_id = input_list[1]
    actor_low = input_list[2]
    if actor_low == "*":
        test_low = 0
    else:
        test_low = int(actor_low)
    #print actor_low
    actor_high = input_list[3]
    prev_id = 0
    next_file = ""
    leaf_node = ""
    page_count = 0
    list_actors_leaves = []
    # list of page numbers
    list_actors = []
    # set of actor ids
    node_dir = "movieroles_ma_idx\\"
    found  = False
    with open("movieroles_ma_idx\\root.txt", 'r') as root:
        root_node = csv.DictReader(root, delimiter = "," ,fieldnames = ["movieid","actorid","pageid"])
        page_count+=1
        for row in root_node:
            if(row["movieid"] != "internal"):
                if (int(movie_id) <= int(row["movieid"]) and int(movie_id) > prev_id) :
                   # print next_node
                    next_file = node_dir + row["pageid"]
                    #print next_file
                prev_id = int(row["movieid"])
    with open(next_file, 'r') as stem:
        stem_node = csv.DictReader(stem,delimiter = ",", fieldnames = ["movieid","actorid","pageid"])
        page_count +=1
        for row in stem_node:
            if row["movieid"] != "internal" and row["movieid"] != "int2.txt" :
                if (int(movie_id) <= int(row["movieid"]) and int(movie_id) > prev_id ):
                    next_file = node_dir + row["pageid"]
                    #print next_file
                prev_id = int(row["movieid"])
    with open(next_file, 'r') as leaf:
        leaf_node = csv.DictReader(leaf, delimiter = ",", fieldnames = ["movieid","actorid", "pageid"])
        page_count +=1
        for row in leaf_node:
            if(row["movieid"] != "leaf"):
                if not (row["movieid"].isdigit()) :
                    next_file = node_dir + row["movieid"]
                else:
                    if int(movie_id) == int(row["movieid"]):
                        found = True
                        if  actor_high == "*":
                            if  int(row["actorid"]) >= int(test_low):
                                list_actors.append(row["actorid"])
                                list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                        else:
                            if  int(row["actorid"]) >= int(test_low) and int(row["actorid"] <= int(actor_high)) :
                                list_actors.append(row["actorid"])
                                list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                    else:
                        found = False

    if found:
        with open(next_file, 'r') as leaf:
            leaf_node = csv.DictReader(leaf, delimiter = ",", fieldnames = ["movieid","actorid", "pageid"])
            page_count +=1
            for row in leaf_node:
                if(row["movieid"] != "leaf"):
                    if not (row["movieid"].isdigit()) :
                        next_file = node_dir + row["movieid"]
                    else:
                        if int(movie_id) == int(row["movieid"]):
                            if  actor_high == "*":
                                if  int(row["actorid"]) >= int(test_low):
                                    list_actors.append(row["actorid"])
                                    list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                            else:
                                if  int(row["actorid"]) >= int(test_low) and int(row["actorid"] <= int(actor_high)) :
                                    list_actors.append(row["actorid"])
                                    list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                                    
    
    print list_actors,page_count
    return [list_actors,page_count]

def method1_range_movie_idx(input_list):
    return 0

def method1_actor_idx(actor_list):
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


    idx_page_count = 0
    tb_page_count = 0

    for actor in  actor_list:
        with open("actors_id_idx\\root.txt") as fin:
            reader = csv.DictReader(fin, delimiter=",",fieldnames = ['id', 'pageid'])
            next_file = ' '
            prev_id = 0
            for row in reader:
                if(row['id'] != 'internal'):
                    if(int(actor) <= int(row['id']) and int(actor) > prev_id):
                        next_file = row['pageid']
                        print next_file
                    prev_id = int(row['id'])

        idx_page_count+=1

        next_file = "actors_id_idx\\" + next_file
        with open(next_file) as fin:
            reader = csv.DictReader(fin, delimiter=",",fieldnames = ['id', 'pageid'])
            for row in reader:
                if(row['id']!='leaf'):
                    if(row['id'] == actor_list[0]):
                        actor_page_id.append([row['id'], row['pageid']])

        idx_page_count+=1



    for idx, pages in enumerate(actor_page_id):
        tb_page_count+=1
        next_file = "actors_table\\page" + pages[1]+ '.txt'
        with open(next_file) as fin:
            reader = csv.DictReader(fin, delimiter=",",fieldnames = ['atype', 'id', 'name', 'surname'])
            for row in reader:
                if(row['id'] == actor_page_id[idx][0]):
                    output.append(row)


    #print output, idx_page_count, tb_page_count
    return output, idx_page_count, tb_page_count


def print_output(method_number,num_movieroles_idx,num_movieroles_table,num_actor_id_idx,num_actors_table):
    print "Method "+ str(method_number) +" total cost " + str(num_actors_table + num_movieroles_table +num_actor_id_idx + num_movieroles_idx) + " Pages" 
    if num_movieroles_idx >=1:
        print "    " + str(num_movieroles_idx) + " pages movieroles_ma_idx"
    if num_movieroles_table >=1:
        print "    " + str(num_movieroles_table) + " pages movieroles_table"
    if num_actor_id_idx >=1:
        print "    " + str(num_actor_id_idx) + " pages actor_id_idx"
    if num_actors_table >=1:
        print "    " + str(num_actors_table) + " pages actors_table"

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
    print_output(1,1,1,1,1)



