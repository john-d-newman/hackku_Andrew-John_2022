'''
Creator: John Newman
Created: 4/9/2022
Modified: 4/9/2022 by John Newman
Desc:  This file parses a csv file of stream names and tags


'''
from os import link
import random
from flask import render_template, request
from flask import Flask
from datetime import datetime
import re
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    
    raw_tag = request.query_string.decode()
    tag = ''

    if raw_tag != '':
        tag = raw_tag[4:len(raw_tag)]
    

    if tag == '' or tag == None:

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

        for item in operating_list:
            tag_list.append(item[1:len(item)])
            stream_list.append(item[0])
    
        rand_list = []
        length = len(stream_list)
        
        for _ in range(4):
            rand_list.append(random.randint(0,length-1))



        stream_data.close()

        return render_template(
            'joe.html',
            link1 = stream_list[rand_list[0]],
            tag1 = tag_list[rand_list[0]][0],
            link2 = stream_list[rand_list[1]],
            tag2 = tag_list[rand_list[1]][0],
            link3 = stream_list[rand_list[2]],
            tag3 = tag_list[rand_list[2]][0],
            link4 = stream_list[rand_list[3]],
            tag4 = tag_list[rand_list[3]][0]
            )
    else:
        return redirect('/search?'+ raw_tag)

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





@app.route("/search")
def link_from_tag(tag = None):

    raw_tag = request.query_string.decode()
    if raw_tag != '':
        tag = raw_tag[4:len(raw_tag)]
    

    if tag == '' or tag == None:
        return render_template(
            'joe2.html',
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


    
    if len(tag_list) == 0:
        return render_template(
            'joe3.html',
            tag = tag,
            link = 'https://youtu.be/dQw4w9WgXcQ'
        )
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
        'joe2.html',
        tag=tag_list[0],
        link = return_stream_list[random.randint(0,len(return_stream_list)-1)]
        )
    else:
        return "Tag not in options, try retyping or clicking an image"
    
def search(tag):
    raw_tag = request.query_string.decode()
    if raw_tag != '':
        tag = raw_tag[4:len(raw_tag)]
    

    if tag == '' or tag == None:
        return render_template(
            'joe2.html',
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


    
    if len(tag_list) == 0:
        return render_template(
            'joe3.html',
            tag = tag,
            link = 'https://youtu.be/dQw4w9WgXcQ'
        )
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
        'joe2.html',
        tag=tag_list[0],
        link = return_stream_list[random.randint(0,len(return_stream_list)-1)]
        )
    else:
        return "Tag not in options, try retyping or clicking an image"


@app.route('/addstream')
def addstream(stream_link=None):
    raw_in = request.query_string.decode()

    if raw_in == '':
        return render_template(
            'joe4.html'

        )
    new_url = raw_in[4:len(raw_in)]
    stream_file = open('stream_database.csv','a')
    stream_file.write(new_url)
    stream_file.close()
    return redirect('/addtags')

    

@app.route('/addtags')
def addtags(csvtags = None):

    
    raw_in = request.query_string.decode()
    less_raw_in = raw_in.replace('%2C',',')
    csvtags = less_raw_in.replace('Tag=','')

    if csvtags == '' or csvtags == None:
        return render_template(
            'joe5.html'
        )
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

    
    
    

    tag_list = tagcleaner(tag_list)

    tag_list.pop()
    tag_list.append(new_tags)

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
    print(index)
    print(tag_list)
    return redirect('/home')
    
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

