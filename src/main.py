import subprocess

# Run spider.py first
subprocess.run(["python", "src/spider.py"], check=True)

# Then run email_push.py
subprocess.run(["python", "src/email_push.py"], check=True)
