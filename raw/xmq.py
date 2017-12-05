#-*-coding:utf-8-*- 
import re
import os
import json
import time
import requests
import urllib
import sys
import traceback
reload(sys)
sys.setdefaultencoding('utf-8')

token = '' # Your access_token
name = '' # Your name
user_id = '' # Your user_id
avatar_url = '' # Your avatar_url
ddd = 'D:\\test\\kkk\\ko\\'#your dir

headers = {
    'Host': 'wapi.xiaomiquan.com',
    'Origin': 'https://wx.xiaomiquan.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'authorization': token,
    'Accept': '*/*',
    'Referer': 'https://wx.xiaomiquan.com/dweb/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.'+str(time.strftime('%S',time.localtime(time.time()))),
    'Connection': 'keep-alive',
    'x-request-id': '92c35538-be75-3029-4d8a-e338e6'+str(time.strftime('%H%M%S',time.localtime(time.time())))
}

cookies = {
    'access_token': token,
    'name': name,
    'user_id': user_id,
    'PHPSESSID': '42g23c6ss7140joq3mmsb114t2',
    'UM_distinctid': '15d59be81a811b-0e2bd99982822d8-7f682331-1fa400-15d59be81a930f',
    'ws_address': 'ws_address=wss%3A//ws.xiaomiquan.com%3A443/ws%3Fversion%3Dv1.6%26access_token%3D'+token,
    'avatar_url': avatar_url
}


api = 'https://wapi.xiaomiquan.com/v1.6/'


def saveTopics(groupId):
    o = getAllTopics(groupId,getTimeNow())
    for i in range(len(o)):
        ty_1 = que_tak(o[i])
        comm = []
        reut = hv_comt(o[i],comm)
        file_name = file(o[i])
        wrt_fie(reut,ty_1,ddd,file_name)
    print 'down'
	
def file(p):
    file_name = ''
    try:
        for i in range(len(p['talk']['files'])):
            name = p['talk']['files'][i]['name']
            file_name = file_name+name+'\n'
        return '**file : **\n'+file_name
    except:
        return file_name

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return True
    else:
        return False
		
def hash_tag(text):
    ll = re.search('<e type="hashtag.+?/>',text)
    if ll is not None:
        lll = re.search('title=.+?"',ll.group())
        llll = lll.group().lstrip('title="').lstrip('%').lstrip('23').rstrip('23"').rstrip('%')
        return llll
    else:
        return  '%E6%9C%AA%E5%88%86%E7%B1%BB'
		
def link(kk): 
    z0 = kk
    pp = re.findall('<e type=.?"web.?" .+/>',kk)
    if len(pp) == 0:
        return kk
    else:
        for i in range(len(pp)):
            oo = re.search('href=.?".+?"',pp[i])
            jj = oo.group().lstrip('href=').lstrip('"').rstrip('title').rstrip().rstrip('"')
            nn = '[link]'+'('+urllib.unquote(jj).decode('utf-8', 'replace').encode('gbk', 'replace')+')'
            zz = 'zx = z'+str(i)+'.replace(pp[i],nn)'
            exec(zz)
            ex = 'z'+str(i+1)+'=zx'
            exec(ex)
        ex1 = 're =  z'+str(len(pp))
        exec(ex1)
        return re
        
def chek_text(p):
    ll = re.sub('\n#','\n',p)
    pp = re.sub('\s#','',ll)
    return pp	
		

		
#talk
def que_tak(p):
    try:
        author1 = p['talk']['owner']['name']
        talk_text1 = chek_text(link(p['talk']['text']))
        imgs = retr_imgs(p['talk'])		
        ty1_1 = '**'+author1+'**\n\n'+talk_text1+imgs
        ty1 = who(ty1_1)
        return ty1

    except:
        try:
            question1 = chek_text(link(p['question']['text']))
            question_user1 = chek_text(p['question']['owner']['name'])
            author2 = p['answer']['owner']['name']
            talk_text2 = link(p['answer']['text'])
            imgs = retr_imgs(p['answer'])
            ty2_2 = '**'+author2+'**'+' reply **'+ question_user1 +'** : \n'+'>'+question1+'\n\n'+talk_text2+imgs
            ty2 = who(ty2_2)
            return ty2
        except:
            question2 = chek_text(link(p['question']['text']))
            question_user2 = 'Anonymous'
            author3 = p['answer']['owner']['name']
            talk_text3 = chek_text(link(p['answer']['text']))
            imgs = retr_imgs(p['answer'])
            ty3_3 = '**'+author3+'**'+' reply **'+ question_user2 +'** : \n'+'>'+question2+'\n\n'+talk_text3+imgs
            ty3 = who(ty3_3)
            return ty3

#@who			
def who(ty):
    z0 = ty
    ll = re.findall('<e type=.?"mention.?".+?/>',ty)
    if len(ll) == 0:
        return ty
    else:
        for i in range(len(ll)):
            kk = re.search('title=.?".+?"',ll[i])
            jj = kk.group().lstrip('title=').lstrip('"').lstrip('@').rstrip().rstrip('"')
            nn = str(urllib.unquote(str(jj)).decode('utf-8', 'replace').encode('utf-8', 'replace')) 
            ex = 'mm = z'+str(i)
            exec(ex)			
            ww = re.sub('<e type=.?"mention.?".+?/>','@'+nn,mm)
            ex1 = 'z'+str(i+1)+'=ww'
            exec(ex1)
        ex2 = 're =  z'+str(len(ll))
        exec(ex2)
        return re        
     	

#commen
def talk_recv(p):
    try:
        recv_name = p['repliee']['name']
        to_name = p['owner']['name']
        text_chat = link(p['text'])
        images = retr_imgs2(p)
        msg_1 = to_name + ' reply '+ recv_name + ' : '+ text_chat+ images +'\n'
        msg = who(msg_1)
    except:
        talk_name = p['owner']['name']
        text_chat = link(p['text'])
        images = retr_imgs2(p)
        msg_1 = talk_name + ' : '+text_chat+images+'\n'
        msg = who(msg_1)
    return msg

#have or not comment
def hv_comt(p,comm):
    try:
        for r in range(len(p['show_comments'])):
            comm.append(talk_recv(p['show_comments'][r]))
        chat = ''
        for i in range(len(comm)):
            chat = chat + comm[i]
        re = '**comment:**\n\n'+chat
        return re
    except:
        re = ''
        return re
#write file
def wrt_fie(reut,ty_1,ddd,file_name):
    txt = 'txt.md'
    question = re.search('\sreply\s',ty_1)
    if question is not None:
        dir_q = urllib.unquote('%E6%8F%90%E9%97%AE').decode('utf-8', 'replace').encode('gbk', 'replace')
        dir3_q = ddd+dir_q+'\\'
        mkdir(dir3_q)
        with open(ddd+dir_q+'\\'+txt,'a') as oo:
            pass
        with open(ddd+dir_q+'\\'+txt,'r') as check:
            che = check.read()
            if drop(ty_1) in che:
                pass
            else:
                with open(ddd+dir_q+'\\'+txt,'a') as j:
                    news = '***\n'+drop(ty_1)+'\n***\n'+reut+file_name+'***\n'
                    j.write(news)
    else:
        dir = urllib.unquote(str(hash_tag(ty_1))).decode('utf-8', 'replace').encode('gbk', 'replace')
        dir3 = ddd+dir+'\\'
        mkdir(dir3)
        with open(ddd+dir+'\\'+txt,'a') as oo:
            pass
        with open(ddd+dir+'\\'+txt,'r') as check:
            che = check.read()
            if drop(ty_1) in che:
                pass
            else:
                with open(ddd+dir+'\\'+txt,'a') as j:
                    news = '***\n'+drop(ty_1)+'\n***\n'+reut+file_name+'***\n'
                    j.write(news)
			
def drop(ty_1):
    ll = re.sub('<e type="hashtag.+?/>','',ty_1)
    return ll
			
#get images	
def get_img(p):
    img_url = ''
    for img in range(len(p['images'])):
        url0 = p['images'][img]['large']['url']
        url1 = '<img src="'+url0+'" alt="kkk" align=center style="zoom:50%"/>'
        img_url = img_url+url1+' '
    return img_url

#have or not images
def retr_imgs(p):
    try:
        imgs = get_img(p)
        rel = '\n'+imgs
        return rel
    except:	
        rel = ''
        return rel
		
#get images	
def get_img2(p):
    img_url = ''
    for img in range(len(p['images'])):
        url0 = p['images'][img]['large']['url']
        url1 = '<img src="'+url0+'" alt="kkk" align=center style="zoom:20%"/>'
        img_url = img_url+url1+' '
    return img_url

#have or not images
def retr_imgs2(p):
    try:
        imgs = get_img2(p)
        rel = '\n'+imgs
        return rel
    except:	
        rel = ''
        return rel
	
	
	
	
def getTopicsByTime(groupId,t):
    time.sleep(1)
    return requests.get(api + 'groups/' + str(groupId) + '/topics?count=20&end_time=' + urllib.quote(t), headers=headers , cookies=cookies)

def getEndTime(o):
    return o['resp_data']['topics'][len(o['resp_data']['topics'])-1]['create_time']

def getTimeNow():
    return str(time.strftime('%Y-%m-%dT%H:%M:%S.6%S+0800',time.localtime(time.time())))

def getAllTopics(groupId,t):
    d = []
    n = (getTopicsNums(groupId)/20+1)
    for x in range(n):
        c = getTopicsByTime(groupId, t)
        t = getEndTime(json.loads(c.content))
        d.extend(json.loads(c.content)['resp_data']['topics'])
    return d

def getTopicsNums(groupId):
    kkk = json.loads(requests.get(api + 'groups/' + str(groupId) + '/details', headers=headers , cookies=cookies).content)['resp_data']['group']['statistics']['topics']['topics_count']
    return kkk

saveTopics(481818518558) # set bakup group id
