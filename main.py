from flask import Flask,render_template,request,redirect,url_for
from PIL import Image,ImageFont,ImageDraw
import textwrap
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart




def encrypt(text):
    AtoZ=[chr(i) for i in range(97,97+26)]

    text=text.lower()
    result=''
    for i in text:
        if i in AtoZ:
            result+=AtoZ[(AtoZ.index(i)+3)%26]
        else:
            result+=i
            
    return result



def sendmail(to_addr,secret):
    with open('secret.png', 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'Secret message from Someone'
    msg['From'] = os.environ.get('EMAIL')
    msg['To'] = to_addr

    text = MIMEText("You got a secret message from someone...\n")
    msg.attach(text)
    
    image = MIMEImage(img_data, name=os.path.basename('secret message'))
    msg.attach(image)
    server='smtp.gmail.com'
    
    text=MIMEText('\nTo decode the message click the link:\nhttps://caesarcipher.net/')
    msg.attach(text)
    text=MIMEText('\n\n\nCopy and Paste this:-\n\n'+secret+'\n\nPut key = 3 and decode \n\nYour memory from Trinity 2k24:-\n')
    msg.attach(text)

        
    with smtplib.SMTP(server) as connection:
        connection.starttls()
        connection.login(msg['From'],os.environ.get('PASS_KEY'))
        connection.sendmail(msg['From'],msg['To'],msg.as_string())




def put_text(text):
    img=Image.open('Secret Message.png')

    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype("Manjari-Bold.woff",80)


    wrapped_text=textwrap.wrap(text,width=50)
    height=700

    if len(wrapped_text)==2:
        height-=50
        for i in range(2):
            text=wrapped_text[i]
            lg=font.getlength(text)
            draw.text(((img.width-lg)//2,height),text,(255,255,255),font)
            height+=100
    else:
        lg=font.getlength(text)
        draw.text(((img.width-lg)//2,height+50),text,(255,255,255),font)


    img.save('secret.png')
    



app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        email=request.form.get('email')
        msg=request.form.get('message')
        text=encrypt(msg)
        put_text(text)
        sendmail(email,text)
        return redirect(url_for('home'))
        
    return render_template('index.html')


app.run(debug=False,port=5001,host='0.0.0.0')

