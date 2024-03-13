import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="select the number of forecasted days")


if place:
    try:
        data_list = get_data(place, days)
        option = st.selectbox("select data to view",
                              ("Temperature", "Sky"))
        st.subheader(f"{option} for the next {days} days in {place}")

        date = [date_value["dt_txt"] for date_value in data_list]

        if option == "Temperature":
            temperature = [int(temp_value["main"]["temp"])/10 for temp_value in data_list]
            figure = px.line(x = date, y = temperature, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_type = [sky_value["weather"][0]["main"] for sky_value in data_list]
            image_path ={
                "Clear": "Images/clear.png",
                "Cloud": "Images/cloud.png",
                "Rain": "Images/rain.png",
                "Snow": "Images/snow.png"
            }
            sky_image = [image_path[sky_value] for sky_value in sky_type]
            st.image(sky_image, width=115)
    except KeyError:
        st.info("This place does not exits")
