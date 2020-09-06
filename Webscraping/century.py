import requests
import pandas
from bs4 import BeautifulSoup


base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
l=[]
suf=0

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS",
 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c=r.content

soup=BeautifulSoup(c, "html.parser")
all=soup.find_all("div",{"class":"propertyRow"})
last_page=soup.find_all("a",{"class":"Page"})[-1].text
print(last_page)

for page in range(0,int(last_page)*10,10):
    print(base_url+str(page))

    r = requests.get(base_url+str(page)+".html",
     headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

    c=r.content

    soup=BeautifulSoup(c, "html.parser")

    all=soup.find_all("div",{"class":"propertyRow"})

    for house in all:
        d={}
        price=((house.find("h4",{"class":"propPrice"}).text).replace("\n","")).replace(" ","")
        d["price"]=price

        ad=house.find_all("span",{"class":"propAddressCollapse"})
        full_ad=[]
        for row in ad:
            full_ad.append(row.text)
        d["Address"]="{}, \n{}".format(full_ad[0],full_ad[1])

        try:
            beds=house.find("span",{"class":"infoBed"})
            d["beds:"]= beds.find("b").text
        except AttributeError:
            d["beds:"]=None
            pass

        try:
            beds=house.find("span",{"class":"infoValueHalfBath"})
            d["half bath:"]= beds.find("b").text
        except AttributeError:
            d["half bath:"]=None
            pass

        try:
            beds=house.find("span",{"class":"infoValueFullBath"})
            d["full bath:"]= beds.find("b").text
        except AttributeError:
            d["full bath:"]=None
            pass

        try:
            beds=house.find("span",{"class":"infoSqFt"})
            d["SqFt:"]= beds.find("b").text
        except AttributeError:
            d["SqFt:"]=None
            pass


        for column_group in house.find_all("div",{"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size:"]=feature_name.text
        l.append(d)

df=pandas.DataFrame(l)
print(df)
print(len(df))
df.to_csv("output.csv")
