'''
Creator: John Newman
Created: 4/9/2022
Modified: 4/9/2022 by John Newman
Desc:  This file parses a csv file of stream names and tags


'''
import random


def link_from_tag(tag):
    stream_data = open('stream_database.csv')

    return_stream = open('desired_stream.txt','w')
    return_stream_list = []

    operating_list = []
    for item in stream_data:
        operating_list.append(item.split(','))
    operating_list.pop(0)
    for item in operating_list:
        if '\n' in item[1]:
            item[1]= item[1][0:len(item[1])-1]

    print(operating_list)
    
    for item in operating_list:
        if tag in item:
            return_stream_list.append(item[1])

    for item in return_stream_list:
        return_stream.write(str(item)+'\n')

    stream_data.close()
    return_stream.close()

#link_from_tag('elephant')

def choose_rand_stream(stream_data_filename):
    stream_option = []
    file_object = open(str(stream_data_filename),'r')

    for line in file_object:
        stream_option.append(line[0:len(line)-1])

    print(stream_option)
    length = len(stream_option)-1
    print(length)

    file_object.close()

    return stream_option[random.randint(0,length)]

    

print(choose_rand_stream('desired_stream.txt'))