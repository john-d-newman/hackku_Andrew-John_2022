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

@app.route("/<hold>")
def home():
    stream_data = open('stream_database.csv','r')
    
    stream_list = []
    tag_list = []
    operating_list = []

    for item in stream_data:
        operating_list.append(item.split(','))
    
    print(operating_list)
    for item in operating_list:
        if '\n' in item[len(item)-1]:
            item[len(item)-1]= item[len(item)-1][0:len(item[len(item)-1])-1]

    print(operating_list)
    
    rand_list = []
    for _ in range(4):
        rand_list.append(random.randint(0,len(stream_list)-1))



    tag_list = tag_list[0]
    stream_data.close()

    return render_template(
        'main.html',
        link1 = stream_data[rand_list[0]],
        link2 = stream_data[rand_list[1]],
        link3 = stream_data[rand_list[2]],
        link4 = stream_data[rand_list[3]]

    )

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

    stream_data = open('stream_database.csv','r')

    return_stream_list = []
    tag_list = []
    operating_list = []

    for item in stream_data:
        operating_list.append(item.split(','))
    
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
    



#@app.route('/addstream/')
def addstream(stream_link,csvtags):
    stream_file = open('stream_database.csv','a')
    stream_file.write(str(stream_link) +',' + csvtags)
    stream_file.close()

#@app.route('/addtags/')
def addtags(stream_link, csvtags):
    stream_file = open('stream_database.csv','r')

    index = 0
    operating_list = []
    tag_list = []
    stream_list = []
    
    new_tags = csvtags.split(',')

    for item in stream_file:
        operating_list.append(item.split(','))
    

    for item in operating_list:
        if '\n' in item[len(item)-1]:
            item[len(item)-1]= item[len(item)-1][0:len(item[len(item)-1])-1]

    for item in operating_list:
        tag_list.append(item[1:len(item)])
        stream_list.append(item[0])

    
    
    print(stream_list)

    if stream_link in stream_list:
        for item in stream_list:
            if stream_link != item:
                index += 1
            else:
                findex = index
    else:
        print("THIS WILL BE A RETURN FUNCITON WITH AN ERROR")
        return("Link not defined, try the add streams link")

    tag_list = tagcleaner(tag_list)

    for item in new_tags:
        tag_list[findex].append(item)

    stream_file.close()
    stream_file = open('stream_database.csv','w')
    index = 0

    for item in stream_list:
        stream_file.write(item+',')
        for item in tag_list[index]:
            stream_file.write(item+',')
        index += 1
        stream_file.write('\n')


    stream_file.close()
    print(index)
    print(findex)
    print(tag_list)
    
def tagcleaner(tag_list):
    cleaned_tags = []
    doublec_tags = []
    for item in tag_list:
        while '' in item:
            item.remove('')
        cleaned_tags.append(item)
    for item in cleaned_tags:
        for tag in item:
            while item.count(tag)>1:
                item.remove(tag)
        doublec_tags.append(item)
    return doublec_tags

addtags('https://zoo.sandiegozoo.org/cams/polar-cam','bear,arctic,paws,pol,pola')