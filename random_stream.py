'''
Creator: John Newman
Created: 4/9/2022
Modified: 4/9/2022 by John Newman
Desc:  This file parses a csv file of stream names and tags


'''
from os import link
import random
from flask import render_template
from flask import Flask
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the main site, naivagate to other sites."

'''
@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
'''


@app.route("/link_from_tag/")
@app.route("/link_from_tag/<tag>")
def link_from_tag(tag = None):
    tag = tag
    if tag == None:
        return render_template(
            'rand_1.html',
            tag=tag,
            link = 'https://youtu.be/dQw4w9WgXcQ'
        )

    stream_data = open('stream_database.csv')

    return_stream_list = []
    tag_list = []
    operating_list = []

    for item in stream_data:
        operating_list.append(item.split(','))
    operating_list.pop(0)
    print(operating_list)
    for item in operating_list:
        if '\n' in item[len(item)-1]:
            item[len(item)-1]= item[len(item)-1][0:len(item[len(item)-1])-1]

    print(operating_list)
    
    for item in operating_list:
        if tag in item:
            tag_list.append(item[1:len(item)])
            return_stream_list.append(item[0])

    tag_list = tag_list[0]

    print(tag_list[0])
    print(return_stream_list)
    print(tag)
#    for item in return_stream_list:
#       return_stream.write(str(item)+'\n')
    for item in tag_list:
        if tag == item:
            print("WHYYYYYYYYYYYYY")

    stream_data.close()
#    return_stream.close()
    if tag in tag_list:
        return render_template(
        'rand_1.html',
        tag=tag_list[0],
        link = return_stream_list[random.randint(0,len(return_stream_list)-1)]
        )
    else:
        return "Tag not in options, try retyping or clicking an image"
    

    

