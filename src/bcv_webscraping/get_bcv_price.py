
import requests
from bs4 import BeautifulSoup
import urllib3

# Monedas válidas: "dolar", "euro", "yuan", "lira", "rublo"

CURRENCY_TYPE = "dolar"

def get_currency_value_from_bcv(currency="dolar"):
    """
    Obtiene el precio de la moneda seleccionada CURRENCY_TYPE de la página del Banco Central de Venezuela.
    """
    try:
        url = "https://www.bcv.org.ve/"
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encuentra el div con el id de CURRENCY_TYPE y luego el 'strong' que contiene el precio
        currency_div = soup.find('div', id=currency)
        if currency_div:
            price_strong = currency_div.find('strong')
            if price_strong:
                price_text = price_strong.text.strip().replace(',', '.')
                return float(price_text)
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud HTTP: {e}")
        return None
    except (AttributeError, ValueError) as e:
        print(f"Error al parsear el contenido HTML: {e}")
        return None

if __name__ == "__main__":
    currency_value = get_currency_value_from_bcv(CURRENCY_TYPE)
    if currency_value:
        print(f"El precio del {CURRENCY_TYPE} es: {currency_value}")
    else:
        print(f"No se pudo obtener el precio del {CURRENCY_TYPE}.")

