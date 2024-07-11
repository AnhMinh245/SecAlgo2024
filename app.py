from flask import Flask, render_template_string, request, redirect, url_for
import os
import git
import subprocess
import hmac
import hashlib
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

# Đường dẫn tới thư mục chứa repo
REPO_DIR = '/home/ec2-user/SecAlgo2024'

# URL của repo trên GitHub
REPO_URL = 'https://github.com/AnhMinh245/SecAlgo2024.git'

# GitHub Webhook secret
GITHUB_SECRET = 'SecAlgo2024'

# Thư mục chứa các file .py cần hiển thị và thực thi
TARGET_DIR = os.path.join(REPO_DIR, 'python_version/complete')

def clone_or_pull_repo():
    if os.path.exists(REPO_DIR):
        # Nếu thư mục repo đã tồn tại, thực hiện pull
        repo = git.Repo(REPO_DIR)
        origin = repo.remotes.origin
        origin.pull()
    else:
        # Nếu chưa tồn tại, thực hiện clone
        git.Repo.clone_from(REPO_URL, REPO_DIR)

@app.route('/')
def home():
    clone_or_pull_repo()
    # Lấy danh sách các file .py trong thư mục TARGET_DIR
    files = [f for f in os.listdir(TARGET_DIR) if f.endswith('.py')]
    files.sort(key=lambda x: int(x.split('_')[0][2:]))
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SecAlgo24</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Roboto', sans-serif;
                    background-color: #f0f0f0;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    text-align: center;
                    color: #333;
                    margin-bottom: 30px;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                li {
                    margin: 10px 0;
                }
                a {
                    text-decoration: none;
                    color: #007BFF;
                    font-weight: bold;
                }
                a:hover {
                    text-decoration: underline;
                }
                .update-link {
                    display: block;
                    text-align: center;
                    margin-top: 20px;
                    color: #28a745;
                    font-weight: bold;
                }
                .update-link:hover {
                    text-decoration: underline;
                }
                .header, .footer {
                    text-align: center;
                    color: red;
                    font-weight: bold;
                }
                {{ formatter.get_style_defs('.highlight') }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h3>HỌC VIỆN KỸ THUẬT MẬT MÃ</h3>
                </div>
                <h1>Thuật toán trong An toàn thông tin 2024</h1>
                <ul>
                    {% for file in files %}
                        <li><a href="/view?filename={{ file }}">{{ file }}</a></li>
                    {% endfor %}
                </ul>
                <a class="update-link" href="/update">Cập nhật từ GitHub</a>
                <div class="footer">
                    <h2>Phạm Anh Minh - AT160148</h2>
                </div>
            </div>
        </body>
        </html>
    ''', files=files, formatter=HtmlFormatter())

@app.route('/view', methods=['GET', 'POST'])
def view_file():
    filename = request.args.get('filename')
    filepath = os.path.join(TARGET_DIR, filename)
    if not filename or not os.path.isfile(filepath):
        return "File không tồn tại", 404

    with open(filepath, 'r') as file:
        content = file.read()

    highlighted_code = highlight(content, PythonLexer(), HtmlFormatter())

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{{ filename }}</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Roboto', sans-serif;
                    background-color: #f0f0f0;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1, h2 {
                    text-align: center;
                    color: #333;
                }
                pre {
                    background-color: #272822;
                    color: #f8f8f2;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                    font-size: 16px; /* Tăng cỡ chữ của code */
                }
                code {
                    font-family: 'Source Code Pro', monospace;
                    font-size: 16px; /* Tăng cỡ chữ của code */
                }
                .terminal {
                    background-color: #000;
                    color: #0f0;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                    font-family: 'Source Code Pro', monospace;
                    font-size: 16px;
                }
                .hidden {
                    display: none;
                }
                form {
                    margin-top: 20px;
                    text-align: center;
                }
                textarea {
                    width: 100%;
                    max-width: 100%;
                    height: 100px;
                    border-radius: 5px;
                    border: 1px solid #ced4da;
                    padding: 10px;
                    font-size: 16px;
                    font-family: 'Roboto', sans-serif;
                }
                input[type="submit"], button {
                    background-color: #007BFF;
                    color: #fff;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                }
                input[type="submit"]:hover, button:hover {
                    background-color: #0056b3;
                }
                .back-link {
                    display: block;
                    text-align: center;
                    margin-top: 20px;
                    color: #007BFF;
                    font-weight: bold;
                }
                .back-link:hover {
                    text-decoration: underline;
                }
                {{ formatter.get_style_defs('.highlight') }}
            </style>
            <script>
                function showTerminal() {
                    document.getElementById('terminal').classList.remove('hidden');
                    document.getElementById('execute-button').classList.add('hidden');
                }

                function resetTerminal() {
                    document.getElementById('terminal-output').innerText = '';
                    document.getElementById('user-input').value = '';
                }

                function executeCode() {
                    const userInput = document.getElementById('user-input').value;
                    const xhr = new XMLHttpRequest();
                    xhr.open('POST', '{{ url_for("execute_code") }}', true);
                    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                    xhr.onreadystatechange = function() {
                        if (xhr.readyState == 4 && xhr.status == 200) {
                            document.getElementById('terminal-output').innerText = xhr.responseText;
                        }
                    };
                    xhr.send('filename={{ filename }}&user_input=' + encodeURIComponent(userInput));
                }
            </script>
        </head>
        <body>
            <div class="container">
                <h1>{{ filename }}</h1>
                <div class="highlight">{{ highlighted_code|safe }}</div>
                <button id="execute-button" onclick="showTerminal()">Thực thi</button>
                <div id="terminal" class="terminal hidden">
                    <div id="terminal-output"></div>
                    <textarea id="user-input" placeholder="Nhập đầu vào tại đây..."></textarea><br>
                    <button onclick="executeCode()">Thực thi</button>
                    <button onclick="resetTerminal()">Thực hiện lại</button>
                </div>
                <a class="back-link" href="/">Quay lại trang chủ</a>
            </div>
        </body>
        </html>
    ''', filename=filename, highlighted_code=highlighted_code, formatter=HtmlFormatter())

@app.route('/execute_code', methods=['POST'])
def execute_code():
    filename = request.form.get('filename')
    user_input = request.form.get('user_input', '')
    filepath = os.path.join(TARGET_DIR, filename)
    if not filename or not os.path.isfile(filepath):
        return "File không tồn tại", 404

    result = ''
    try:
        # Sử dụng subprocess để thực thi mã nguồn của file với đầu vào từ người dùng
        process = subprocess.Popen(['python3', filepath], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=user_input)
        result = stdout + stderr
    except Exception as e:
        result = str(e)

    return result

@app.route('/update')
def update_repo():
    clone_or_pull_repo()
    return redirect(url_for('home'))

@app.route('/webhook', methods=['POST'])
def webhook():
    # Xác thực Webhook từ GitHub
    signature = request.headers.get('X-Hub-Signature-256')
    if not is_valid_signature(request.data, signature):
        return 'Invalid signature', 403

    # Xử lý sự kiện push
    event = request.headers.get('X-GitHub-Event')
    if event == 'push':
        clone_or_pull_repo()
        return 'Repository updated', 200

    return 'Unhandled event', 400

def is_valid_signature(payload, signature):
    if signature is None:
        return False

    secret = GITHUB_SECRET.encode()
    mac = hmac.new(secret, msg=payload, digestmod=hashlib.sha256)
    expected_signature = 'sha256=' + mac.hexdigest()

    return hmac.compare_digest(expected_signature, signature)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
