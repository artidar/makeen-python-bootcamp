city_list = ["Tehran","LosAngeles","London","Paris","Berlin",
"LasVegas","Nashville","NewYork","SanDiego","SanFrancisco","Dixie"]

import requests

def show():
    for item in city_list :
        print(item)
    city =input(f"Enter your City : ")

    while city not in city_list:
        print("Not in Options")
        city =input(f"Enter your City : ")

    try:
     response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0469f816b067dbbbabb77247630de354")
     temp = response.json().get('main').get('temp')
     return temp
    except Exception as exc: 
        print(exc)
       



    
    


temp_1 =show()
print(temp_1)








