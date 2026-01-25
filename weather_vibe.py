import requests

def get_weather(lat, lon):
    try:
        # Используем текущие параметры: температура, влажность, скорость ветра
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json().get("current")
    except Exception:
        return None

def get_emoji(code):
    mapping = {
        0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️",
        45: "🌫️", 48: "🌫️",
        51: "🌧️", 53: "🌧️", 55: "🌧️",
        61: "🌧️", 63: "🌧️", 65: "🌧️",
        71: "❄️", 73: "❄️", 75: "❄️",
        80: "🌦️", 81: "🌦️", 82: "🌦️",
        95: "⛈️",
    }
    return mapping.get(code, "🌡️")

def main():
    city = "Saint Petersburg"
    lat, lon = 59.93, 30.31
    
    weather = get_weather(lat, lon)

    if weather:
        temp = weather.get("temperature_2m")
        hum = weather.get("relative_humidity_2m")
        wind = weather.get("wind_speed_10m")
        code = weather.get("weather_code")
        emoji = get_emoji(code)
        
        print(f"📍 {city}: {temp}°C {emoji}")
        print(f"💨 Ветер: {wind} км/ч | 💧 Влажность: {hum}%")
    else:
        print("❌ Не удалось получить данные о погоде.")

if __name__ == "__main__":
    main()
