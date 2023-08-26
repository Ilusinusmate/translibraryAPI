import requests as rq

try:
    for i in range(1, 3):
        params = {
            "id" : i,
            "lang" : "pt-br"
        }
        response = rq.get(url=f"http://localhost:8000/books", params=params)
        print(response.json())

except Exception as e:
    print("An exception has ocurred", e)

input() #Teste por terminal, evita que feche