import requests

#Část 1
ico = input("Zadejte IČO subjektu: ")
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")


data = response.json()
obchodni_jmeno = data.get("obchodniJmeno")
adresa = data.get("sidlo", {}).get("textovaAdresa")
if not obchodni_jmeno:
    print("Subjekt s týmto IČO neexistuje.")
else:
    print(obchodni_jmeno)
    print(adresa)

#Část 2
nazev = input("Zadejte název subjektu: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = {"obchodniJmeno": nazev}

response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, json=data)
data_json = response.json()

pocet = data_json.get("pocetCelkem", 0)
subjekty = data_json.get("ekonomickeSubjekty", [])
print (f"Nalezeno subjektů: {pocet}")
for subjekt in subjekty:
    jmeno = subjekt.get("obchodniJmeno")
    ico = subjekt.get("ico")
    print(f"{jmeno}, {ico}")


