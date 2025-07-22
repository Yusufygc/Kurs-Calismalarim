import json

person_string = '{"name": "John", "age": 30, "city": "New York"}'

result = json.loads(person_string)  # JSON string to Python dictionary

isim = result["name"]  # Accessing the value associated with the key "name"
print(isim)  # Output: John

# print(result)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Direkt json dosyasından okuma
with open("person.json") as file:
    person_data = json.load(file)  # JSON file to Python dictionary
print(person_data)


# Verimizi JSON formatında kaydetme
person_dict = {
    "name": "Jane",
    "age": 25,
    "city": "Los Angeles"
}

jsonKaydetmek = json.dumps(person_dict)  # Python dictionary to JSON string
print(jsonKaydetmek)

with open("person.json","w") as file:
    json.dump(person_dict, file)  # Python dictionary to JSON file
# Bu kod, person.json dosyasına person_dict içeriğini JSON formatında kaydeder.

# Okunabilirligi artırmak için JSON string'ini girintili hale getirme
# indent parametresi girintili hale getirmek için kullanılır
# sort_keys parametresi ise anahtarları alfabetik sıraya göre sıralar
person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True)  # JSON string with indentation for readability
print(result)