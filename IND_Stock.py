
from  bs4 import BeautifulSoup
import requests
import pandas as pd

Comp=['ABBOTINDIA',
 'ASIANPAINT',
 'BAJFINANCE',
 'BERGEPAINT',
 'DIVISLAB',
 'HDFCBANK',
 'ITC',
 'KOTAKBANK',
 'MARICO',
 'NESTLEIND',
 'PAGEIND',
 'PIDILITIND',
 'RELAXO',
 'RELIANCE',
 'HINDUNILVR'
     ]
   
d=[]
for comp_name in Comp:
    r=requests.get("https://www.screener.in/company/{}/".format(comp_name))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("section")
    
    h=all[0].find_all("li",{"class":"four columns"})
    d.append({" {} ".format(comp_name): h[2].text.strip().replace("\n","").replace("    ","").replace("52 weeks High / Low ","")})

F={}
for i in range(14):
    F.update(d[i])
   
df=pd.DataFrame(data=F.keys(),columns=["Company Name"])
#df["52 weeks High / Low"]=pd.DataFrame(data=F.values())

H=[]
L=[]
for i in F.values():
    
    x=i[0 : i.index("/")].strip()
    y=i[i.index("/")+1 : ].strip()
    H.append(x)
    L.append(y)
#print("High= ",H)
#print("Low= ",L)

df["52 Week High"]=pd.DataFrame(data=H)
df["52 Week Low"]=pd.DataFrame(data=L)
df["20% low"]=df["52 Week High"].astype(float)*0.8
df["30% low"]=df["52 Week High"].astype(float)*0.7
df["40% low"]=df["52 Week High"].astype(float)*0.6
df["50% low"]=df["52 Week High"].astype(float)*0.5
print(df)


#CONVERT FILE INTO EXCEL
df.to_excel("Company_stock.xlsx")

