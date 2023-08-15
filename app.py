import streamlit as st
import requests

NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
NEWS_API_KEY = '10bf4a47cf6e48069821a23ff15fce50'  

def fetch_news(country, category=None, q=None):
    params = {
        'country': country,
        'apiKey': NEWS_API_KEY,
        'q': q
    }
    if category:
        params['category'] = category
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    return response.json()
st.set_page_config(page_title='News Aggregator')
st.title('News Aggregator')
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1585241645927-c7a8e5840c42?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Nnx8fGVufDB8fHx8&w=1000&q=80");
             background-attachment: fixed;
             background-size: cover;
             text-color:yellow;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
# Choose the country
countries = ['US', 'GB', 'IN', 'CA', 'AU', 'FR', 'DE', 'JP', 'CN', 'RU', 'BR', 'MX', 'IT', 'ES', 'KR']# add more countries as needed
selected_country = st.sidebar.selectbox('Select a country', countries)

# Choose the category
categories = ['All','Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology']
selected_category = st.sidebar.selectbox('Select a category (optional)', categories)

# Fetch the news
if selected_category == 'All':
    news = fetch_news(selected_country)
else:
    news = fetch_news(selected_country, category=selected_category)


# Search bar
search_query = st.text_input("Search for news:")
# Fetch the news with search query
if search_query:
    search_news = fetch_news(selected_country, q=search_query)
else:
    search_news = {'articles': []} 

# Display the news articles based on the selected category
for article in news['articles']:
    st.write('###', article['title'])
    if article['urlToImage']:
        st.image(article['urlToImage'], use_column_width=True)
    st.write(article['url'])

# Display the news articles based on the search query
if search_query:
    st.write('## Search Results')
    for article in search_news['articles']:
        st.write('###', article['title'])
        if article['urlToImage']:
            st.image(article['urlToImage'], use_column_width=True)
        st.write(article['url'])
        

  
