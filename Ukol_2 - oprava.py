import requests

#Část 1
ico = input("Zadejte IČO subjektu: ").strip()

if not ico.isdigit() or len(ico) != 8:
    print("Neplatné IČO. Musí obsahovat 8 číslic.")
else: 
    try:
        response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}", timeout=10)
        if not response.ok:
            print(f"Chyba při získávání dat (HTTP {response.status_code}).")
        else:
            data = response.json()
            obchodni_jmeno = data.get("obchodniJmeno")
            adresa = data.get("sidlo", {}).get("textovaAdresa")

            if not obchodni_jmeno:
                print("Subjekt s tímto IČO neexistuje.")
            else:
                print(obchodni_jmeno)
                print(adresa)
    except requests.exceptions.Timeout:
        print("Požadavek na server vypršel (timeout).")

    except requests.exceptions.ConnectionError:
        print("Nepodařilo se připojit k serveru.")

    except ValueError:
        print("Server vrátil neplatná data (neplatný JSON).")

    except requests.exceptions.RequestException as e:
        print(f"Nastala chyba při komunikaci se serverem: {e}")

#Část 2
nazev = input("Zadejte název subjektu: ").strip()

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = {"obchodniJmeno": nazev}

try:
    response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, json=data, timeout=10)
    if not response.ok:
        print(f"Chyba při získávání dat (HTTP {response.status_code}).")
    else:
        data_json = response.json()
        pocet = data_json.get("pocetCelkem", 0)
        subjekty = data_json.get("ekonomickeSubjekty", [])
        print (f"Nalezeno subjektů: {pocet}")
        for subjekt in subjekty:
            jmeno = subjekt.get("obchodniJmeno")
            ico = subjekt.get("ico")
            print(f"{jmeno}, {ico}")
except requests.exceptions.Timeout:
    print("Požadavek na server vypršel (timeout).")

except requests.exceptions.ConnectionError:
    print("Nepodařilo se připojit k serveru.")

except ValueError:
    print("Server vrátil neplatná data (neplatný JSON).")

except requests.exceptions.RequestException as e:
    print(f"Nastala chyba při komunikaci se serverem: {e}")

