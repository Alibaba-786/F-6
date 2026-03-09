#!/usr/bin/env python3
"""
Alibaba FB Auto-Reg v4.0 - Multi-platform (Kali/Termux/Pydroid3/Windows)
100% UID|pass|cookie|OTP|email capture | Nepal-optimized | ARM64 compatible
"""

import requests
import re
import time
import random
import threading
import os
import json
from datetime import datetime
from requests_html import HTMLSession
from concurrent.futures import ThreadPoolExecutor
import queue

# Nepal-optimized config
NEPAL_NAMES = [
    "Ram", "Shyam", "Hari", "Krishna", "Buddha", "Sita", "Gita", "Radha", "Laxmi", "Kamal",
    "Sharma", "Thapa", "Karki", "Magar", "Tamang", "Gurung", "Rai", "Limbu", "Sherpa", "Newar"
]
NEPAL_PASSWORDS = [
    "Np{rand}Himalaya!", "Nepal2026!", "Kathmandu99!", "EverestNp1!", "Pokhara2026!",
    "LumbiniNp!", "BhutaneseNp!", "Himalaya{num}!", "Nepal{rand}!", "Gorkha2026!"
]

# Fresh Nepal proxies (HNI 405 Ncell + others) - rotate every thread
PROXIES = [
    "http://38.54.71.67:80", "http://103.94.120.198:80", "http://202.166.195.202:8080",
    "http://103.105.49.67:80", "http://202.51.101.122:8080", "http://103.69.216.199:80",
    "http://14.161.33.66:8080", "http://103.123.17.155:80"
]

class MailTM:
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.domain = None
        self.email = None
        
    def get_domains(self):
        r = self.session.get("https://api.mail.tm/domains")
        return r.json()['hydra:member']
    
    def create_account(self, domain):
        email = f"nepal{random.randint(10000,99999)}@{domain['domain']}"
        passw = "NpTest123!"
        r = self.session.post("https://api.mail.tm/accounts", json={
            "address": email, "password": passw
        })
        if r.status_code == 201:
            self.email = email
            return True
        return False
    
    def get_token(self):
        r = self.session.post("https://api.mail.tm/token", json={
            "address": self.email, "password": "NpTest123!"
        })
        if r.status_code == 200:
            self.token = r.json()['token']
            self.session.headers['Authorization'] = f"Bearer {self.token}"
            return True
        return False
    
    def get_messages(self):
        r = self.session.get("https://api.mail.tm/messages", params={'limit': 5})
        if r.status_code == 200:
            return r.json()['hydra:member']
        return []
    
    def get_message_content(self, msg_id):
        r = self.session.get(f"https://api.mail.tm/messages/{msg_id}")
        if r.status_code == 200:
            return r.json()['text'] or r.json()['html']
        return ""

class FBRegistrar:
    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.proxy = random.choice(PROXIES)
        self.session = HTMLSession()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'ne-NP,ne;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        })
        if self.proxy:
            self.session.proxies = {'http': self.proxy, 'https': self.proxy}
        
    def register(self):
        print(f"[T{self.thread_id}] Starting registration w/ proxy: {self.proxy}")
        
        # Create temp mail
        mail = MailTM()
        domains = mail.get_domains()
        domain = random.choice([d for d in domains if 'free' not in d['domain']])
        
        if not mail.create_account(domain) or not mail.get_token():
            print(f"[T{self.thread_id}] MailTM setup failed")
            return False
        
        print(f"[T{self.thread_id}] Email created: {mail.email}")
        
        # Generate Nepal creds
        firstname = random.choice(NEPAL_NAMES[:10])
        lastname = random.choice(NEPAL_NAMES[10:])
        password = random.choice(NEPAL_PASSWORDS).format(
            rand=random.randint(1000,9999), num=random.randint(10,99)
        )
        birthday_day = random.randint(1,28)
        birthday_month = random.randint(1,12)
        birthday_year = random.randint(1985,2005)
        
        print(f"[T{self.thread_id}] Names: {firstname} {lastname} | Pass: {password}")
        
        try:
            # Hit registration page
            r = self.session.get("https://m.facebook.com/reg", timeout=30)
            r.html.render(timeout=20)  # JS render for dynamic content
            
            # Fill exact FB reg form fields
            data = {
                'firstname': firstname,
                'lastname': lastname,
                'reg_email': mail.email,
                'reg_email_confirmation': mail.email,
                'reg_passwd': password,
                'birthday_day': str(birthday_day),
                'birthday_month': str(birthday_month),
                'birthday_year': str(birthday_year),
                'sex': '1',  # Male (randomize later)
                'websubmit': '1',
                '__user': '0',
                '__a': '1',
                '__dyn': '',
                '__csr': '',
                '__req': 'z',
                '__hs': '',
                'lsd': re.search(r'"LSD",\[\],{"token":"([^"]+)"', r.html.html) or 'default',
                'jazoest': '25985'
            }
            
            # Submit registration
            reg_url = "https://m.facebook.com/reg/"
            r2 = self.session.post(reg_url, data=data, timeout=30)
            r2.html.render(timeout=20)
            
            print(f"[T{self.thread_id}] Reg submitted, polling OTP...")
            
            # Poll OTP (5s intervals, 300s timeout)
            otp = self.poll_otp(mail, 60)  # 5min max
            if not otp:
                print(f"[T{self.thread_id}] No OTP received")
                return False
            
            print(f"[T{self.thread_id}] OTP: {otp}")
            
            # Submit OTP
            otp_data = {'code': otp, 'submit': '1'}
            r3 = self.session.post("https://m.facebook.com/reg/confirm/", data=otp_data)
            r3.html.render(timeout=20)
            
            # Extract UID (multiple patterns)
            uid = self.extract_uid(r3)
            if not uid:
                # Fallback: check redirect/profile
                time.sleep(3)
                r4 = self.session.get("https://m.facebook.com/home.php")
                uid = self.extract_uid(r4)
            
            if not uid:
                print(f"[T{self.thread_id}] No UID found")
                return False
            
            # Get cookies as string
            cookies_str = "; ".join([f"{k}={v}" for k,v in self.session.cookies.items()])
            
            # Export
            self.export(uid, password, cookies_str, otp, mail.email)
            print(f"[T{self.thread_id}] SUCCESS: UID {uid}")
            return True
            
        except Exception as e:
            print(f"[T{self.thread_id}] Error: {e}")
            return False
    
    def poll_otp(self, mail, timeout=60):
        start = time.time()
        while time.time() - start < timeout:
            messages = mail.get_messages()
            for msg in messages:
                if 'facebook' in msg['subject'].lower() or 'code' in msg['subject'].lower():
                    content = mail.get_message_content(msg['id'])
                    otp_match = re.search(r'(?i)(?:code|otp|fb-)[:\s]*(\d{4,8})|(\d{6})', content)
                    if otp_match:
                        return otp_match.group(1) or otp_match.group(2)
            time.sleep(5)
        return None
    
    def extract_uid(self, response):
        patterns = [
            r'id=(\d+)', r'profile.php\?id=(\d+)', r'(\d{15,})',
            r'"userID":"(\d+)"', r'"entity_id":(\d+)', r'id&quot;:&quot;(\d+)'
        ]
        text = response.text + response.html.html if hasattr(response, 'html') else response.text
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(1)
        return None
    
    def export(self, uid, password, cookies, otp, email):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"/sdcard/AliV4-FULL_{ts}.txt" if os.path.exists('/sdcard') else f"AliV4-FULL_{ts}.txt"
        
        with open(filename, 'a') as f:
            f.write(f"{uid}|{password}|{cookies}|{otp}|{email}\n")
        print(f"[T{self.thread_id}] Exported to {filename}")

def worker(thread_id):
    reg = FBRegistrar(thread_id)
    reg.register()

if __name__ == "__main__":
    num_threads = 10  # Adjust 5-25
    print(f"Alibaba FB v4.0 - {num_threads} threads | Nepal-optimized")
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(worker, range(1, num_threads+1))