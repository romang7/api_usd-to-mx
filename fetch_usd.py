import requests

def get_usd_to_mxn():
    """Obtiene el valor del dólar a MXN desde una API externa junto con la fecha."""
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        rate = data.get("rates", {}).get("MXN")
        date = data.get("date")  # La API incluye la fecha 'YYYY-MM-DD'
        if rate is not None and date:
            formatted_rate = f"{rate:.2f}"  # Formatear a 2 decimales
            return {"rate": float(formatted_rate), "date": date}
        return None
    except Exception as e:
        print(f"Error fetching USD to MXN rate: {e}")
        return None

