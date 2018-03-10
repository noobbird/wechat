#_*_coding: utf-8 _*_
#FileName: reqweb.py
#Author: yang
#History: 1#2017/8/24

import requests
import crypt
import json
import sys

def post(posturl, dictdata, proxies = None):
        headers = {'Host':'music.163.com',
                   'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 63.0.3239.132Safari / 5'}
        try:
            if proxies is None:
                r = requests.post(url=posturl, data=dictdata, headers = headers,timeout =2)
            else:
                r = requests.post(url=posturl, data=dictdata, proxies = proxies, headers = headers, timeout =2)
            return r
        except requests.exceptions.ConnectTimeout:
            sys.stderr.write('post ConnectTimeout except\n')
        except requests.exceptions.ProxyError,e:
            sys.stderr.write('post ProxyError\n')
        except requests.exceptions.ConnectionError,e:
            sys.stderr.write('post ConnectionError\n')
        except Exception,e:
            sys.stderr.write('post '+str(e))


def get(url, proxies = None):
        try:
            if proxies is None:
                r = requests.get(url=url, timeout = 2)
            else:
                r = requests.get(url=url, proxies = proxies, timeout = 2)
            return r
        except requests.exceptions.ConnectTimeout:
            sys.stderr.write('get ConnectTimeout except\n')
        except requests.exceptions.ProxyError, e:
            sys.stderr.write('get ProxyError\n')
        except requests.exceptions.ConnectionError, e:
            sys.stderr.write('get ConnectionError\n')
        except Exception, e:
            sys.stderr.write('get' + str(e))

if __name__ == "__main__":
    song_id = "4154790"
    song_url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token=" %song_id
    params = '{"rid":"R_SO_%s","offset":"0","total":"true","limit":"100","csrf_token":""}' %song_id
    proxies = {"http": "http://47.52.24.117:80"}
    data = crypt.get_postData(params)
    res = post(song_url, data)
    comment_json = json.loads(res.text)
    print comment_json["total"]
    for h in comment_json["hotComments"]:
        content = h['content']
        commentId = h['commentId']
        likedCount = h['likedCount']
        time = h['time']
        replied = h['beReplied']
        rep = ''
        user= h['user']
        user_name = user['nickname']
        user_id = user['userId']
        user_avatar = user['avatarUrl']
        if replied:
            rep = replied[0]['content']
        
        print '\trep: ' + rep +'\ncontent' + content
        print 'user: '+user_name+'\t'+str(user_id)+'\t'+user_avatar+str(likedCount)
        
    #for c in comment_json["hotcomments"]:
    #    print c["user"]["nickname"] + ': ' + c['content']
    print res.headers['X-From-Src'] 

