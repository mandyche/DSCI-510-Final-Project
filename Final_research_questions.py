import streamlit as st

st.title('Research Question #4-8')
#Answering questions on the rubric
st.write('4. What did you set out to study?')
st.write('I chose to study identifying relationship between financial news sentiment, weather patterns and stock performance by observing what financial news talks about corresponding to the weather pattern in California on a specific date and use that information to observe a trend to see if there is a significant influence on the SPY stock (Note that the changes between here and my mileston1 is that I decided to use BBC business/financial news content instead of US money news).')

st.write('5. What did you Discover/what were your conclusions?')
st.write('From my graphical analysis, I noticed there is a significant pattern between news title impact and stock performance. However, the relationship between weather and stock performance is not as significant as between news & stock. For example, I noticed that when the news titles are rated as positive, the closing prices tend to go up. When the news title is negative, the closing prices tend to go down. On the other side, sunny and rainy weather do not make significant difference on stock performance.')

st.write('6. What difficulties did you have in completing the project')
st.write('The first difficulty I had was that at first I could not scrpae US Money news, which is why I changed to scrape BBC news. The second difficulty I had was that establishing graph for comparing stock performance with different weather patterns. Because I had to create pandas data frame to merge the information together before start comparing, I personally thought some pandas language was hard to debug.')

st.write('7. What skills did you wish you had while you were doing the project?')
st.write('During my project work, I wish I had a fluent data engineering skill in data cleaning. I think data cleaning is essential for handling messy, real-world datasets efficiently. I was not able to handle/clean large missing data such as data imputation for missing closing price for one of the date throughout 2023 SPY stock performance.')

st.write('8. What would you do “next” to expand or augment the project?')
st.write('After I found out if weather has influences on stock, I would like to know if it is because weather has directly influence on stock or if it is because weather has influenced the news article, and stock is affected only because of news article content (difference in difference).')