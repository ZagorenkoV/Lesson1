city_temp = {"city": "Москва", "temperature": "20"}
    
print(city_temp["city"])
city_temp["temperature"] = int(city_temp["temperature"]) - 5
print(city_temp)

print(city_temp.get("country"))
print(city_temp.get("country", "Россия"))

city_temp["date"] = "27.05.2019"
print(len(city_temp))