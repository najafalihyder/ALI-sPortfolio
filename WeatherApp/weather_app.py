import streamlit as st
import requests

# 🌐 API Info
API_KEY = "65e571c7163de44f2dc3ac7f2e4ebb74"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 🖥️ Streamlit Page Config
st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")
st.title("🌤️ Simple Weather Forecast")
st.markdown("Enter a city name below to get the current weather conditions.")

# 🧾 User Input
city = st.text_input("Enter City:")

# 🚀 On Button Click
if st.button("Get Weather"):
    if city.strip() == "":
        st.warning("Please enter a valid city name.")
    else:
        # 🛰️ Prepare API call
        params = {
            "q": city,
            "units": "metric",
            "appid": API_KEY
        }

        # ⏳ Show loading spinner
        with st.spinner("Fetching weather data..."):
            response = requests.get(BASE_URL, params=params)

            # ✅ If response is successful
            if response.status_code == 200:
                data = response.json()

                # 🎯 Extract data
                temp = data["main"]["temp"]
                condition = data["weather"][0]["description"].title()
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]
                icon = data["weather"][0]["icon"]
                icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"

                # 📊 Display Results
                st.image(icon_url)
                st.subheader(f"Weather in {city.title()}")
                st.write(f"**Condition:** {condition}")
                st.write(f"**Temperature:** {temp} °C")
                st.write(f"**Humidity:** {humidity}%")
                st.write(f"**Wind Speed:** {wind} m/s")
            else:
                st.error("City not found or API error.")
