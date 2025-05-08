import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

data_folder = 'data'
bfsu_file = os.path.join(data_folder, 'bfsu_project.json')
last_file = os.path.join(data_folder, 'last_data.json')

# Load current data
with open(bfsu_file, 'r', encoding='utf-8')as f:
    current_data = json.load(f)

# Load previous data
if os.path.exists(last_file):
    with open(last_file, 'r', encoding='utf-8')as f:
        last_data = json.load(f)
else:
    last_data = []

# If no update, exit the script
if current_data == last_data:
    print('没有更新，不发送邮件')
    exit()

content = ''
for item in current_data:
    content += f"{item['title']}\n{item['date']}\n{item['link']}\n\n"

# Email sender information
smtp_server = 'smtp.qq.com'
smtp_port = 587  
sender_email = '1625433463@qq.com'
auth_code = os.environ.get("QQ邮箱SMTP授权码")  # 授权码

receiver_email = ['1625433463@qq.com'] 

# Create message container
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = ', '.join(receiver_email)
message['Subject'] = '北外海外实习实践项目信息更新'

# Attach content to the email
message.attach(MIMEText(content, 'plain', 'utf-8'))

# Connect to SMTP server and send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port) # creates SMTP session
    server.starttls()  # 启用 TLS 加密
    server.login(sender_email, auth_code) # Authentication
    server.sendmail(sender_email, receiver_email, message.as_string()) 
    server.quit()
    print("邮件发送成功！")

    # Save the latest data to overwrite the old one
    with open (last_file, 'w', encoding='utf-8') as f :
        json.dump(current_data, f, ensure_ascii=False, indent=2)

except Exception as e:
    print("邮件发送失败:", e)
    


