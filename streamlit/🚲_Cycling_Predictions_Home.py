import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Heart Rate Predictions by Adriana Machado",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("# Welcome to Adriana Machado's Cycling Predictions Project!")

st.markdown('### Please use the sidebar to explore the model and Tableau Dashboards for all predictions.')

st.markdown('For full project repo and README visit Adriana\'s [GitHub Repo](https://github.com/ajmachado42/Predicting-Cycling-Metrics#Predictions).')

st.markdown('![image](https://upload.wikimedia.org/wikipedia/en/thumb/0/0a/Johnson-london.jpg/660px-Johnson-london.jpg)')

st.markdown('Humans have been bicycling for hundreds of years. The earliest verified bicycle was the German draisine, or velocipede, dating back to 1817 and invented by Baron Karl von Drais. The name "bicycle" was coined in 1860s France. Earlier unverified and debatable accounts go as far as 1500 AD to a sketch by Gian Giacomo Caprotti, a pupil of Leonardo da Vinci ([source](https://en.wikipedia.org/wiki/History_of_the_bicycle)).')

st.markdown('The estimated size of the US bicycle market from 2004-2005 was 6.2bn USD. There were an estimated 52.73m cyclists aged 6+ in 2020. And the growing e-bike market is projected to be 53.53bn USD by 2027 ([source](https://www.statista.com/topics/1686/cycling/#topicHeader__wrapper)).')

st.markdown('Whether you are cycling for enjoyment, sport, or as a commuter, predicting the uncertainty of a route can be useful. How much exertion is it going to take riding to work? Is the headwind going to suck? Am I in shape enough to take that route on my bicycle or should I invest in an e-bike?')

st.markdown('Earlier this year, in the late Winter and Spring, I was training to complete my first century for later in August, the Marin Century Classic in Marin County, California. I had been cycling around 100+ miles (161+ km) a week on road and gravel trails with varying elevation changes. I had a training coach app and was cycling far above average. According to my Garmin watch stats, I had been in the 95th percentiles for distance and time spent cycling out of all female Garmin users.')

st.markdown('In May I started the full-time Data Science Immersive with General Assembly and the time I spent training had to be compromised with the time I would invest in my professional development. Giving up on a goal did not feel great but I knew it was necessary and only a set back that I could return to. I kept up cycling as regular exercise completing < 30 miles (<48 km) per week. However, I still was curious about how I would have done in the Marin Century at my peak (high) training period compared to if I had participated in my current average performance period.')

st.markdown('Heart rate, heart rate zones (intensity), and power output are good measures of how much a cyclist is exerting. Weather can also make a huge impact on the difficulty of a route, outside of the expected elevation changes. Using the resources I had, I decided to predict heart rate, which would be translated into intensity zones based on previous activity data (trackpoints) from Garmin .gpx files and weather data from each trackpoint. Here\'s some more on intensity zones and how they inform about stress on your body ([source](https://www.garmin.com/en-US/blog/general/get-zone-train-using-heart-rate/)).')

st.markdown('**Cycling is a widely popular sport and can accommodate a range of experiences. Being able to predict how much stress a route may put on your body can be really useful and offer a lot of insight for goal-making or reality-checking. Given past periods of cycling performance, how will I perform on a given route, based on heart rate intensity zones? Is that trail going to be too difficult or am I capable of riding it without feeling like I\'m going to die?**')