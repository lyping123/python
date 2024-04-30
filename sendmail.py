import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "synergycollegenet@gmail.com"
receiver_email = ["lyping0526@gmail.com"]
subject = "loonkng for application web development internship"
body=f"i comming from synergy college"
                            
                            
try:
    file_path="resume3.pdf"
    for email in receiver_email:
        message=MIMEMultipart()
        message["From"]=sender_email
        message["To"]=email
        message["Subject"] = subject
        message.attach(MIMEText(body,"plain"))
        attachment=open(file_path,"rb")
        part=MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename= " + file_path)     
        message.attach(part)
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(sender_email,"zhvskykulmxzfcgg")
            server.sendmail(sender_email,email,message.as_string())
        
    print("mail successfully send")
except Exception as e:
    print(f"An error occured:{e}")


    
