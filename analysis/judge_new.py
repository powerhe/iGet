# coding=utf8
import base64
import json
import sys
import ssl
import codecs
import string
import xlrd
import os

def judge_sen():
    q_fp = open("./QSen.txt", 'a')
    s_fp = open("./SSen.txt", 'a')
    fname = "../weixin/example.xls"
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    sh = bk.sheet_by_name("A Test Sheet")
    nrows = sh.nrows
    ncols = sh.ncols
    print ("nrows %d, ncols %d" % (nrows,ncols))
    #cell_value = sh.cell_value(1,3)
    #print(cell_value)
    index = -1
    flag = 0
    string = ["?", "什么", "哪", "吗", "吧", "可否", "行不行"]
    for i in range(1, nrows):
            flag = 0
            for str in string:
                cell_value = sh.cell_value(i, 3)
                index = cell_value.find(str)
                if (index != -1):
                    print(i)
                    print("This is a question")
                    index = -1
                    flag = 1
                    q_fp.write(cell_value + '\n') 
                    break
            if(flag == 0):
                print("This is a statement")
                s_fp.write(cell_value)

def judge_me():
    myname = "HeLi"
    fname = "../weixin/example.xls"
    me_fp = open("./Atme.txt",'a')
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    sh = bk.sheet_by_name("A Test Sheet")
    nrows = sh.nrows
    ncols = sh.ncols
    index = -1
    flag = 0
    for i in range(1, nrows):
        cell_value = sh.cell_value(i, 3)
        index = cell_value.find("@"+myname)
        if (index != -1):
            print(cell_value)
            me_fp.write(cell_value)
            

def judge_iyouhe(filename):
    fp = open("./Atme.txt",'r')
    i_fp = open("./i.txt", "a")
    y_fp = open('./you.txt', 'a')
    h_fp = open('./he.txt', 'a')
    i_string = ["我", "我们", "咱", "咱们"]
    y_string = ["你", "你们", "您"]
    h_string = ["他", "她", "他们", "她们"]
    index = -1
    line = fp.readlines()
    for i in range(0, len(line)):
        for str in i_string:
            print(line[i])
            index = line[i].find(str)
            if (index != -1):
                i_fp.write(line[i])
                break 
    for i in range(0, len(line)):
        for str in y_string:
            print(line[i])
            index = line[i].find(str)
            if (index != -1):
                y_fp.write(line[i])
                break        
    for i in range(0, len(line)):
        for str in h_string:
            print(line[i])
            index = line[i].find(str)
            if (index != -1):
                h_fp.write(line[i])
                break

def judge_time(sen):
    fp = open("result.txt", 'r')
    time_fp = open("time.txt", 'a')
    line = fp.readlines()
    print(line[0])
    index = line[0].find("TIME")
    if (index != -1 ):
        time_fp.write(sen)
	

def judge_location(sen):
    fp = open("result.txt", 'r')
    time_fp = open("time.txt", 'a')
    line = fp.readlines()
    print(line[0])
    index = line[0].find("LOC")
    if (index != -1 ):
        time_fp.write(sen)

#def judge_action():

if __name__ == "__main__":
    q_file = "./QSen.txt"
    s_file = "./SSen.txt"
    if os.path.exists(q_file):
        os.remove(q_file)
    if os.path.exists(s_file):
        os.remove(s_file)
    judge_sen()
    #judge_me()
    #judge_iyouhe("Atme.txt")
    #judge_time("下午2点吃饭")
