# coding=gbk
import urllib, urllib2
import base64
import json
import sys
import ssl
import codecs

## get access token by api key & secret key
def get_token():
    apiKey = "LG7ZlOAvVy7p6pLk3LqGrEHC"
    secretKey = "IyFMxyKy6vd7wf7ge5LDrIFdPHqCdfUG"
    auth_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
    request = urllib2.Request(auth_url)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    json_data = response.read()    
    #if (json_data):
        #print(json_data)
    return json.loads(json_data)['access_token']

def dump_res(buf):
    print(buf)

def get_cloud(token):
    host = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer' + '?access_token=' + token
    fp = open("./Test.txt").read()
    s = fp
    print(s)
    data = {"text" : s }
    data = json.dumps(data)
    request = urllib2.Request(host,data)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    de_content = content.decode('gbk')
    if (de_content):
        print(de_content)
    out_fp = file("result.txt", "wr")
    out_fp.write(content.decode("gbk").encode("utf-8"))
    out_fp.close()

def judge_sen():
    fp = open('result.txt', 'r')
    match_fp = open("./QAWord.txt", 'r')
    while 1:
        line = match_fp.readline()
        print line
        if not line:
            break
        index = -1
        while 1:
            sub_line = fp.readline()
            if not sub_line:
                 break
            index = sub_line.find(line)
        if (index != -1):
            print("This is a question")
        else:
            print("This is a statement")
	


    
if __name__ == "__main__":
    token = get_token()
    print(token)
    get_cloud(token) 
    #judge_sen()

