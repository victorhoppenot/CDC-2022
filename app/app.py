import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.title('Climate Related Tweet Sentiment by State over Time')

fig, ax = plt.subplots()

df = pd.read_csv('minor2.csv')
    

slider = st.slider("Week", datetime.strptime("2017-09-21", r"%Y-%m-%d"), datetime.strptime("2019-01-03", r"%Y-%m-%d"), step=timedelta(days=7))



if (slider >= datetime.strptime("2017-10-08", r"%Y-%m-%d") and slider <= datetime.strptime("2018-01-12", r"%Y-%m-%d")):
    st.write("Initial damages alone of 18 billion USD. The total economic cost, including fire suppression, insurance, etc. totalled to 180 billion USD.")
if (slider >= datetime.strptime("2018-09-10", r"%Y-%m-%d") and slider <= datetime.strptime("2018-09-18", r"%Y-%m-%d")):
    st.write("Became a category 4 major storm, and caused massive damage in the Carolinas. The damage totalled 24 billion dollars.")
if (slider >= datetime.strptime("2018-10-07", r"%Y-%m-%d") and slider <= datetime.strptime("2018-10-16", r"%Y-%m-%d")):
    st.write("First category 5 hurricane to make landfall on US since Andrew in 1992. Caused an estimated 25 billion USD in damages.")
if (slider >= datetime.strptime("2018-11-01", r"%Y-%m-%d") and slider <= datetime.strptime("2018-11-30", r"%Y-%m-%d")):
    st.write("Woosley Fire and Camp Fire in California. Camp Fire by itself was the most deadly and destructive wild fire in California history, causing the deaths of 85 people and damage costs totalling 16 billion USD.")

graph = sb.swarmplot(data=df, x='region', y=df[slider.strftime(r"%Y-%m-%d")], hue='political', palette={'Republican': "RED", 'Democrat': "BLUE"})
st.pyplot(fig)

