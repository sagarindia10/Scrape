from requests_html import HTML,HTMLSession
import csv

session=HTMLSession()
source=session.get("https://www.us-cert.gov/ncas/alerts?page=1")
print(source)

ht=source.html
match=ht.find("div")
match1=match[1].find("ul")
match2=match1[2].find("li")

with open(r"C:\Users\sagar\Desktop\prote.csv","w") as wf:
    wcsv=csv.writer(wf)
    wcsv.writerow(["ID","Alerts","URLs"])
    for i in match2:
        tex=i.text
        nt=tex.split(":")
        ID=nt[0]
        Alerts=nt[1]
        link=str(i.absolute_links)
        links=link[2:-2]
        wcsv.writerow([ID,Alerts,links])
    
    



    

