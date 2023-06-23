import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
from datetime import datetime
import time
import pandas
import requests

api = 'https://api.telegram.org/bot5665543233:AAHKfv8CMBo1xP01ruZ6FsM_aPMVzunuMIg/'
send_command = 'sendMessage'

gayboi = '1702020451'
ahbeng = '319504714'
suechi= '751526176'
kx='1032882671'

def send(message):
    requests.post(api+send_command, {'chat_id': gayboi, 'text': message})
    requests.post(api+send_command, {'chat_id': ahbeng, 'text': message})
    requests.post(api+send_command, {'chat_id': suechi, 'text': message})
    requests.post(api+send_command, {'chat_id': kx, 'text': message})

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)

#br.open("https://op.responsive.net/lt/jackson/entry.html") #Replace this url with yours
#br.select_form(nr=0)
#br.form['id'] = 'kastam' # Replace this id with yours 
#br.form['password'] = 'fano123' # Replace this password with yours
#br.submit()

url_list = ["CASH","JOBIN","JOBQ","S1Q","S2Q","S3Q","S1UTIL","S2UTIL","S3UTIL"]
url_list_4col = ["JOBT","JOBREV","JOBOUT"]
LF_DATA = {}


while True:
    br.open("https://op.responsive.net/lt/jackson/entry.html") #Replace this url with yours
    br.select_form(nr=0)
    br.form['id'] = 'kastam' # Replace this id with yours 
    br.form['password'] = 'fano123' # Replace this password with yours
    br.submit()
    lf_url = "https://op.responsive.net/Littlefield/Plot?data=INV&x=all"
    soup = BeautifulSoup(br.open(lf_url), "lxml")

    data = soup.findAll("script")[6].string
    data = data.split("\n")[4].split("'")[3].split()

    counter = 1
    LF_DATA = {}

    for i in data:
     if counter % 2 == 1:
      counter += 1
      day = float(i)
      LF_DATA[day] = []
     elif counter % 2 == 0:
      row_data = [float(i)]
      LF_DATA[day].extend(row_data)
      counter += 1

    for url in url_list:
     lf_url = "http://op.responsive.net/Littlefield/Plot?data=%s&x=all" % url
     soup = BeautifulSoup(br.open(lf_url), "lxml")
     data = soup.findAll("script")[6].string
     data = data.split("\n")[4].split("'")[3].split()
     counter = 1
     for i in data:
      if counter % 2 == 0:
       day = counter/2
       LF_DATA[day].append(float(i))
       counter += 1
      else:
       counter +=1

    for url in url_list_4col:
     lf_url = "http://op.responsive.net/Littlefield/Plot?data=%s&x=all" % url
     soup = BeautifulSoup(br.open(lf_url), "lxml")
     data = soup.findAll("script")[6].string
     data0 = data.split("\n")[4].split("'")[5].split()
     data1 = data.split("\n")[5].split("'")[5].split()
     data2 = data.split("\n")[6].split("'")[5].split()

     counter = 1

     for i in data0:
      if counter % 2 == 0:
       day = counter/2
       LF_DATA[day].append(float(i))
       counter += 1
      else:
       counter +=1

     counter = 1

     for i in data1:
      if counter % 2 == 0:
       day = counter/2
       LF_DATA[day].append(float(i))
       counter += 1
      else:
       counter +=1

     counter = 1

     for i in data2:
      if counter % 2 == 0:
       day = counter/2
       LF_DATA[day].append(float(i))
       counter += 1
      else:
       counter +=1

    dummy_data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for key, value in LF_DATA.items():
     if len(value) < 19:
      value.extend(dummy_data)

    headers = ["INV","CASH","JOBIN","JOBQ","S1Q","S2Q","S3Q","S1UTIL","S2UTIL","S3UTIL","JOBTC1","JOBTC2","JOBTC3","JOBREVC1","JOBREVC2","JOBREVC3","JOBOUTC1","JOBOUTC2","JOBOUTC3"]

    df = pandas.DataFrame.from_dict(LF_DATA, orient="index")
    df.columns = headers
    df.sort_index(inplace=True)
    df["Backlog"] = df["JOBIN"].cumsum() - df["JOBOUTC1"].cumsum() - df["JOBOUTC2"].cumsum() - df["JOBOUTC3"].cumsum()
    
    df.index.rename('DAY', inplace=True)
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    df.index = df.index.astype(int)
    df= df[~df.index.duplicated(keep='first')]
    df1=df.tail(1)
    update=df1.iloc[0]
    leadc3= update["JOBTC3"]
    leadc2=update["JOBTC2"]
    s3Q=update["S3Q"]

    if leadc3 >0.48:
     send("LEAD TIME CONTRACT 3")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 3")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 3")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 3")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 3")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 3")
    if leadc2 >1.2:
     send("LEAD TIME CONTRACT 2")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 2")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 2")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 2")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 2")
     time.sleep(0.2)
     send("LEAD TIME CONTRACT 2")
    if s3Q >=90:
     send("QUEUE S3 ")
     time.sleep(0.2)
     send("QUEUE S3")
     time.sleep(0.2)
     send("QUEUE S3")
     time.sleep(0.2)
     send("QUEUE S3")
     time.sleep(0.2)
     send("QUEUE S3")
     time.sleep(0.2)
     send("QUEUE S3")
    send('%s'%(update))
    LF_DATA = {}
    soup=None
    data=None
    time.sleep(42*60)