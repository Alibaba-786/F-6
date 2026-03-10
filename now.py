#!/usr/bin/env python3
import requests
import json
import re
import time
import random
import string
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

print("🚀🔥 Sahil bhai! 11000% CRASH-PROOF FB OTP script loading... 😎")

# Super safe session with retries
session = requests.Session()
retry_strategy = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://api.mail.tm", HTTPAdapter(max_retries=retry_strategy))
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
})

def safe_json_loads(data):
    """Handle all JSON edge cases - escaped /, hydra, lists, dicts"""
    try:
        if isinstance(data, str):
            # Fix escaped slashes first
            data = data.replace('\\/', '/')
            return json.loads(data)
        return data
    except json.JSONDecodeError:
        print("❌ JSON parse fail, raw preview:")
        print(str(data)[:500])
        return None

def get_domains():
    try:
        r = session.get('https://api.mail.tm/domains?page=1')
        print(f"🌐 Domains status: {r.status_code}")
        data = safe_json_loads(r.text)
        if not data: return None
        
        # Handle hydra or direct list
        domains = []
        if 'hydra:member' in data:
            domains = data['hydra:member']
        elif isinstance(data, list):
            domains = data
        elif 'domain' in data:
            domains = [data]
            
        active = [d for d in domains if d.get('isActive', False)]
        if active:
            domain = active[0]['domain']
            domain_id = active[0]['id']
            print(f"✅ Active domain: {domain} (ID: {domain_id})")
            return domain, domain_id
        return None, None
    except Exception as e:
        print(f"❌ Domain fetch error: {e}")
        return None, None

def create_account(domain):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    email = f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=10))}@{domain}"
    
    try:
        r = session.post('https://api.mail.tm/accounts', json={
            'address': email,
            'password': password
        })
        print(f"📧 Account status: {r.status_code}, Email: {email}")
        
        data = safe_json_loads(r.text)
        if data and 'id' in data:
            account_id = data['id']
            print(f"✅ Account created! ID: {account_id[:8]}... Pass: {password}")
            return email, account_id, password
        print("❌ Account creation failed, raw:", r.text[:200])
        return None, None, None
    except Exception as e:
        print(f"❌ Account error: {e}")
        return None, None, None

def get_token(email, password):
    try:
        r = session.post('https://api.mail.tm/token', json={
            'address': email,
            'password': password
        })
        print(f"🔑 Token status: {r.status_code}")
        
        data = safe_json_loads(r.text)
        if data and 'token' in data:
            token = data['token']
            session.headers['Authorization'] = f'Bearer {token}'
            print("✅ Token grabbed! Ready to poll 🔥")
            return True
        print("❌ Token fail, raw:", r.text[:200])
        return False
    except Exception as e:
        print(f"❌ Token error: {e}")
        return False

def extract_code_from_source(source):
    """Extract 4-8 digit codes from HTML source - multiple patterns"""
    patterns = [
        r'\b\d{4,8}\b',  # Any 4-8 digits
        r'code["\']?\s*[:=]\s*["\']?(\d{4,8})',  # code="12345"
        r'(\d{4,8})["\']?\s*</?code>',  # </code>12345
        r'Your code is[:\s]*(\d{4,8})',  # FB specific
        r'(\d{5,6})\s*is your code',  # Common OTP format
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, source, re.IGNORECASE | re.DOTALL)
        if matches:
            return matches[0]  # Return first match
    return None

def poll_messages(account_id, max_polls=200):  # 10min total
    print("\n⏳ ENTER FB VERIFICATION CODE SCREEN NOW!")
    print("📱 Manual FB signup → paste email → submit → then wait here...")
    input("🎯 Press ENTER after FB submits email (script starts polling)...")
    
    fb_patterns = ['facebook', 'fb', 'meta', 'instagram', 'confirm', 'verify', 'code']
    poll_count = 0
    
    while poll_count < max_polls:
        try:
            r = session.get(f'https://api.mail.tm/messages?accountId={account_id}&page=1')
            data = safe_json_loads(r.text)
            
            if not data or ('hydra:member' not in data and 'messages' not in data):
                time.sleep(3)
                poll_count += 1
                continue
                
            # Handle hydra or direct
            messages = data.get('hydra:member', data.get('messages', []))
            recent_msgs = messages[:10]  # Check last 10
            
            print(f"\n🔍 Poll #{poll_count+1}/200 ({len(recent_msgs)} msgs)")
            
            for msg in recent_msgs:
                subject = msg.get('subject', '').lower()
                sender = msg.get('from', {}).get('address', '').lower()
                
                # Print ALL recent senders for debug
                print(f"  📥 {sender[:30]}... | {subject[:40]}...")
                
                # FB detection
                if any(p in subject or p in sender for p in fb_patterns):
                    print(f"🎉 FB HIT! Fetching source...")
                    msg_id = msg['id']
                    
                    # Get full message source
                    r_source = session.get(f'https://api.mail.tm/messages/{msg_id}/source')
                    source_data = safe_json_loads(r_source.text)
                    
                    if source_data and 'source' in source_data:
                        source = source_data['source']
                        print(f"📄 Source preview: {source[:300]}...")
                        
                        code = extract_code_from_source(source)
                        if code:
                            print(f"\n🎊🎊 Sahil bhai! FB OTP FOUND: {code} 🎊🎊")
                            print("🔥 Copy-paste this NOW in FB!")
                            return code
                        else:
                            print("❌ No OTP regex match in source")
                    else:
                        print("❌ Source fetch failed")
            
            time.sleep(3)  # 3s poll
            poll_count += 1
            
        except Exception as e:
            print(f"⚠️ Poll error: {e}")
            time.sleep(3)
    
    print("\n😢 No FB email after 10min. Try: resend/another domain/VPN/SMS")
    return None

# 🔥 MAIN EXECUTION - 100% CRASH PROOF
print("🚀 Step 1: Fetching domains...")
domain, domain_id = get_domains()
if not domain:
    print("❌ No active domains. Try VPN?")
    exit(1)

print("🚀 Step 2: Creating temp email...")
email, account_id, password = create_account(domain)
if not email:
    print("❌ Account creation failed")
    exit(1)

print("🚀 Step 3: Grabbing token...")
if not get_token(email, password):
    print("❌ Token failed")
    exit(1)

print(f"\n💎 YOUR TEMP EMAIL: {email}")
print("📋 Copy this EXACTLY for FB signup!")
print("=" * 50)

# Poll for FB OTP
code = poll_messages(account_id)

if code:
    print(f"\n✅✅ MISSION COMPLETE Sahil bhai! Code: {code}")
    print("🚀 Script terminated successfully!")
else:
    print("\n💡 Next tries: FB resend → VPN → SMS fallback")
