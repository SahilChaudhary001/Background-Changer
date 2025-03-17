from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Get current IST time
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    ist_time_str = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    # Get top output
    try:
        top_output = subprocess.check_output("top -bn1 | head -10", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    return f"""
    <h1>System Information</h1>
    <p><b>Name:</b> Sahil Chaudhary</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time_str}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=8080, debug=True)