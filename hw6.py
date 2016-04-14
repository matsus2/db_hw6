import sys

if __name__ == '__main__':
	if(len(sys.argv) != 2):
		print("incorrect amount of arguments")
		return 0
	with open(sys.argv[1]) as r:
        ifile = r.readlines()

    input_list = []
    for line in ifile:
    	input_list.append(line.split(','))

    