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

    prev_id = 0
    #print "stem " + next_file
    with open(next_file, 'r') as stem:
        stem_node = csv.DictReader(stem,delimiter = ",", fieldnames = ["movieid","actorid","pageid"])
        page_count +=1
        for row in stem_node:
            if row["movieid"] != "internal" and row["movieid"] != "int2.txt" :
                if (int(movie_id) <= int(row["movieid"]) and int(movie_id) > prev_id ):
                    next_file = node_dir + row["pageid"]
                    print "changed stem to leaf"
                prev_id = int(row["movieid"])

    #print "leaf " + next_file 
    with open(next_file, 'r') as leaf:
        leaf_node = csv.DictReader(leaf, delimiter = ",", fieldnames = ["movieid","actorid", "pageid"])
        page_count +=1
        for row in leaf_node:
            if(row["movieid"] != "leaf"):
                if not (row["movieid"].isdigit()) :
                    print "changed next file"
                    next_file = node_dir + row["movieid"]
                else:
                    if int(movie_id) == int(row["movieid"]):
                        found = True
                        if  actor_high == "*":
                            if  int(row["actorid"]) >= int(test_low):
                                list_actors.append(row["actorid"])
                                list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                        else:
                            if  int(row["actorid"]) >= int(test_low) and int(row["actorid"]) <= int(actor_high):
                                list_actors.append(row["actorid"])
                                list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                    else:
                        found = False

    print next_file
    if found:
        print "opening next file"
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
                                if  int(row["actorid"]) >= int(test_low) and int(row["actorid"]) <= int(actor_high) :
                                    list_actors.append(row["actorid"])
                                    list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                                    

    print list_actors
    return list(set(list_actors)),page_count


def method1_range_movie_idx(input_list):
    movie_low = input_list[0]
    if movie_low == "*":
        movie_test_low = 0;
    else:
        movie_test_low = int(movie_low)
    movie_high = input_list[1]
    if movie_high == "*":
        movie_test_high = 3619455;
    else:
        movie_test_high = int(movie_high)
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
                if movie_low == "*":
                    next_file = node_dir + row["pageid"]
                    break
                elif (int(movie_low) <= int(row["movieid"]) and int(movie_low) > prev_id) :
                   # print next_node
                    next_file = node_dir + row["pageid"]
                    #print next_file
                prev_id = int(row["movieid"])

    prev_id = 0
    #print "stem " + next_file
    with open(next_file, 'r') as stem:
        stem_node = csv.DictReader(stem,delimiter = ",", fieldnames = ["movieid","actorid","pageid"])
        page_count +=1
        for row in stem_node:
            if row["movieid"] != "internal" and row["movieid"] != "int2.txt" :
                if movie_low == "*":
                    next_file = node_dir + row["pageid"]
                    break
                if (int(movie_low) <= int(row["movieid"]) and int(movie_low) > prev_id ):
                    next_file = node_dir + row["pageid"]
                    #print next_file
                prev_id = int(row["movieid"])


    #print "leaf " + next_file 
    with open(next_file, 'r') as leaf:
        leaf_node = csv.DictReader(leaf, delimiter = ",", fieldnames = ["movieid","actorid", "pageid"])
        page_count +=1
        for row in leaf_node:
            if(row["movieid"] != "leaf"):
                if not (row["movieid"].isdigit()) :
                    next_file = node_dir + row["movieid"]
                else:
                    if int(row["movieid"]) in range(int(movie_test_low),int(movie_test_high) +1):
                        found = True
                        if  actor_high == "*":
                            if  int(row["actorid"]) >= int(test_low):
                                list_actors.append(row["actorid"])
                                list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                        else:
                            if  int(row["actorid"]) >= int(test_low) and int(row["actorid"]) <= int(actor_high) :
                                list_actors.append(row["actorid"])
                                list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                    else:
                        found = False

    while found:
        with open(next_file, 'r') as leaf:
            leaf_node = csv.DictReader(leaf, delimiter = ",", fieldnames = ["movieid","actorid", "pageid"])
            page_count +=1
            next_found = False
            for row in leaf_node:
                if(row["movieid"] != "leaf"):
                    if not (row["movieid"].isdigit()):
                        next_found = True
                        next_file = node_dir + row["movieid"]
                    else:
                        if int(row["movieid"]) in range(int(movie_test_low),int(movie_test_high) +1):
                            found = True
                            if  actor_high == "*":
                                if  int(row["actorid"]) >= int(test_low):
                                    list_actors.append(row["actorid"])
                                    list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                            else:
                                if  int(row["actorid"]) >= int(test_low) and int(row["actorid"]) <= int(actor_high):
                                    list_actors.append(row["actorid"])
                                    list_actors_leaves.append([row["movieid"],row["actorid"], row["pageid"]])
                        else:
                            found = False
            if not next_found:
                found = False
    #print list_actors,page_count

    return list(set(list_actors)),page_count

def method1_actor_idx(actor_list):
    output = []
    actor_page_id = []
    idx_page_count = 0
    tb_page_count = 0

    if(len(actor_list) != 0):
        with open("actors_id_idx\\root.txt") as fin:
            reader = csv.DictReader(fin, delimiter=",",fieldnames = ['id', 'pageid'])
            next_file = ' '
            prev_id = 0
            for row in reader:
                if(row['id'] != 'internal'):
                    if(int(actor_list[0]) <= int(row['id']) and int(actor_list[0]) > prev_id):
                        next_file = row['pageid']
                        #print next_file
                    prev_id = int(row['id'])




        for idx, actor in  enumerate(actor_list):
            with open("actors_id_idx\\root.txt") as fin:
                reader = csv.DictReader(fin, delimiter=",",fieldnames = ['id', 'pageid'])
                next_file = ' '
                prev_id = 0
                for row in reader:
                    if(row['id'] != 'internal'):
                        if(int(actor) <= int(row['id']) and int(actor) > prev_id):
                            next_file = row['pageid']
                            #print next_file
                        prev_id = int(row['id'])

            idx_page_count+=1

            next_file = "actors_id_idx\\" + next_file
            with open(next_file) as fin:
                reader = csv.DictReader(fin, delimiter=",",fieldnames = ['id', 'pageid'])
                for row in reader:
                    if(row['id']!='leaf'):
                        if(row['id'] == actor_list[idx]):
                            actor_page_id.append([row['id'], row['pageid']])

            idx_page_count+=1


        #print actor_page_id
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

def method2_actor_table(actor_list):
    page_count = 0
    for i in range(1, 2105):
        if len(actor_list) == 0:
            break
        page_count +=1
        filename = "actors_table\\page" + str(i) + ".txt"
        with open(filename) as fin:
            reader = csv.DictReader(fin, delimiter=",",fieldnames = ['atype', 'id', 'name', 'surname'])
            for row in reader:
                if(row['id'] in actor_list):
                    actor_list.remove(row['id'])

    return page_count

def method3_movie_table(input_list):
    list_actors = []
    movie_low = input_list[0]
    if movie_low == "*":
        movie_test_low = 0;
    else:
        movie_test_low = int(movie_low)
    movie_high = input_list[1]
    if movie_high == "*":
        movie_test_high = 3619455;
    else:
        movie_test_high = int(movie_high)
    actor_low = input_list[2]
    if actor_low == "*":
        actor_test_low = 0
    else:
        actor_test_low = int(actor_low)
    actor_high = input_list[3]
    if actor_high == "*":
        actor_test_high = 149374
    else:
        actor_test_high = int(actor_high)

    keep_going = 1
    page_count = 0
    for i in range(1, 4018):
        page_count+=1
        filename = "movieroles_table\\page" + str(i) + ".txt"
        with open(filename) as fin:
            reader = csv.DictReader(fin, delimiter=",",fieldnames = ['actorid', 'info_1', 'info_2', 'movieid', 'role'])
            for row in reader:
                if(int(row['movieid']) in range(movie_test_low, movie_test_high+1)):
                    if(int(row['actorid']) in range(actor_test_low, actor_test_high+1)):
                        list_actors.append(row['actorid'])


    return page_count



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
    print



if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("incorrect amount of arguments")
        sys.exit(0)
    with open(sys.argv[1]) as r:
        ifile = r.readlines()

    for line in ifile:
        a_idx_page = 0
        a_table_page = 0
        m_idx_page = 0
        m_table_page = 0
        actor_list = []
        actor_info_list = []
        input_list = []
        input_list = line.split(',')

        #deletes the \n string at the end
        input_list[-1] = input_list[-1][:-1]
        
        if(input_list[0] == input_list[1] and input_list[0] != '*'):
            actor_list, m_idx_page = method1_same_movie_idx(input_list)
        else:
            actor_list, m_idx_page =  method1_range_movie_idx(input_list)

        actor_info_list, a_idx_page, a_table_page = method1_actor_idx(actor_list)

        print "Query: " + line
        print "Results (" + str(len(actor_info_list))  +  " total):\n"
        for actor in actor_info_list:
            print actor['name'] + " " + actor['surname'] + "(" + actor['atype'] + ")"
        print
        print_output(1,m_idx_page,m_table_page,a_idx_page,a_table_page)
        a_table_page = 0
        temp_actor_page = method2_actor_table(actor_list)
        print_output(2,m_idx_page,m_table_page,0,temp_actor_page)
        #print_output(3,0, method3_movie_table(input_list), 0, temp_actor_page)
        




