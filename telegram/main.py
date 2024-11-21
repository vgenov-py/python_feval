# import requests as req

# res = req.get("http://ckan.juntaex.es/storage/f/2023-02-15T10%3A16%3A05.828Z/emisorasext.csv")

# with open("emisoras.csv", "w") as file:
#     file.write(res.content.decode("utf-8"))

import requests as req
TOKEN = ""
chat_id = ""
message = "Hola desde Python"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(url)
req.get(url)