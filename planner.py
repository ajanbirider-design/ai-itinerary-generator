import os
import requests
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))
WEATHER_API_KEY = os.getenv("06baf489e4f3e79ab8cd9d779e4b1fc2")


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        return f"{temp}°C, {desc}"
    return "Weather data not available"


def generate_plan(destination, budget, days, mode):
    weather = get_weather(destination)

    # Special logic for your niche locations
    if destination.lower() in ["ladakh", "spiti", "zanskar"]:
        region_context = f"""
        Focus on high-altitude travel in {destination}.
        Include:
        - Acclimatization tips
        - Fuel stops
        - Dangerous roads
        - Rider safety tips
        """
    else:
        region_context = "Plan a general travel itinerary within India."

    prompt = f"""
    Create a detailed travel plan for {destination} in India.

    Budget: {budget} INR
    Days: {days}
    Mode: {mode}
    Weather: {weather}

    {region_context}

    Include:
    - Day-wise itinerary
    - Route suggestions
    - Weather-based travel advice
    - Packing checklist
    - Budget breakdown
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content, weather
