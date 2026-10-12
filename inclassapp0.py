import requests
import streamlit as st

st.set_page_config(page_title="NASA Astronomy Picture of the Day")
st.title("NASA Astronomy Picture of the Day")

# API URL
url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"

# API call
response = requests.get(url).json()

dates = []

for i in response:
    dates.append(i["date"])

selected_date = st.sidebar.selectbox("Select a date", dates)

if selected_date:
    # Convert 2026-10-06 to 261006
    selected_date = selected_date[2:].replace("-", "")

    url2 = f"https://science.nasa.gov/wp-json/wp/v2/apod-basic/{selected_date}"

    response2 = requests.get(url2).json()

    st.header(response2["title"])
    with st.expander("Show explanation"):
        st.markdown(response2["explanation"], unsafe_allow_html=True)
    st.image(response2["hdurl"])