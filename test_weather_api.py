import requests, json

city_name = input("Enter the city_name 1.Baddi 2. Noide")
mapping = {'Baddi':7279742, 'Noida': 7279746}

url = "https://openweathermap.org/data/2.5/weather?id={}&appid=b6907d289e10d714a6e88b30761fae22".format(mapping[city_name])

response = requests.get(url)
details_dict = response.json()

if details_dict['cod'] != 404:
	for i,j in details_dict.items():
		print(i,j)
	
	res= requests.get(url)
    output= res.json()

    res= requests.get(url)
    output= res.json()

    weather_status=output['weather'][0]['description']