import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

senderEmail = "realduckduckhoe@gmail.com"
empfangsEmail = "jeremiegless23@gmail.com"
msg = MIMEMultipart()
msg['From'] = senderEmail
msg['To'] = empfangsEmail
msg['Subject'] = "Test"

emailText = "Hallo David, <br><br>ich wünsche dir eine angenehme Woche!<br><br>Mit freundlichen Grüßen,<br>Nix"
msg.attach(MIMEText(emailText, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, "cJObMDl3XPb!")
text = msg.as_string()
server.sendmail(senderEmail, empfangsEmail, text)
server.quit()