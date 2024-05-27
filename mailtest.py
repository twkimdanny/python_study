import smtplib
from email.mime.text import MIMEText

 # STMP 서버의 url과 port 번호
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

# # 1. SMTP 서버 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

EMAIL_ADDR = ''
EMAIL_PASSWORD = ''

# # 2. SMTP 서버에 로그인
# smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
reply_from_smtp = smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
print(reply_from_smtp)

#내용을 입력하는 MIMEText => 다른 라이브러리 사용 가능
msg = MIMEText('내용 : 본문 내용')
msg['Subject'] = '제목: 파이썬으로 gmail 보내기'

#이메일을 보내기 위한 설정(Cc도 가능)
smtp.sendmail('twkim@kyonggi.ac.kr', 'hihi00@kyonggi.ac.kr', msg.as_string())

#객체 닫기
smtp.quit()
