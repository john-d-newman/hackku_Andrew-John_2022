'''
Creator: John Newman
Created: 4/9/2022
Modified: 4/9/2022 by John Newman
Desc:  This file parses a csv file of stream names and tags


'''
from os import link
import random

from flask import Flask
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route("/link_from_tag/<tag>")
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
    return str(return_stream_list)


#link_from_tag('elephant')

@app.route('/random_stream/')
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

    

