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
    }}
    .st-bb {{
        font-size: 18px;
        color: #FF5733;
    }}
    .news-item {{
        display: flex;
        flex-direction: row;
        align-items: center;
        margin: 10px 0;
    }}
    .news-item img {{
        max-width: 100px;
        max-height: 80px;
        margin-right: 10px;
    }}
    .news-item a {{
        color: #3498db;
        text-decoration: none;
    }}
    .article-title {{
        color: blue;
    }}
    .sidebar {{
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }}
    .sidebar-header {{
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }}
    .sidebar-nav {{
        margin-top: 20px;
    }}
    .sidebar-nav a {{
        display: block;
        padding: 10px 0;
        color: #343a40;
        text-decoration: none;
    }}
    .sidebar-nav a:hover {{
        background-color: #f0f3f5;
        border-radius: 5px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Choose the country
countries = ['IN','US', 'GB', 'CA', 'AU', 'FR', 'DE', 'JP', 'CN', 'RU', 'BR', 'MX', 'IT', 'ES', 'KR']# add more countries as needed
selected_country = st.sidebar.selectbox('Select a country', countries)

# Choose the category
categories = ['All','Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology']
selected_category = st.sidebar.selectbox('Select a category (optional)', categories)

# Fetch the news
if selected_category == 'All':
    news = fetch_news(selected_country)
else:
    news = fetch_news(selected_country, category=selected_category)

# Fetch the news with search query
search_query = st.text_input("Search for news:")
if search_query:
    search_news = fetch_news(selected_country, q=search_query)
else:
    search_news = {'articles': []}

col1, col2, col3 = st.columns(3)
# Display the news articles based on the selected category
for i, article in enumerate(news['articles']):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
        if article['urlToImage']:
            st.markdown(f'<a href="{article["url"]}" class="news-item" target="_blank">', unsafe_allow_html=True)
            st.image(article['urlToImage'], use_column_width=True)
            st.markdown('</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{article["url"]}" class="article-title" target="_blank">{article["title"]}</a>', unsafe_allow_html=True)

# Display the news articles based on the search query

if search_query:
    if not search_news['articles']:
        st.write("No results found.")
    else:
        st.write('## Search Results')
        for i, article in enumerate(search_news['articles']):
            with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
                if article['urlToImage']:
                    st.markdown(f'<a href="{article["url"]}" class="news-item" target="_blank">', unsafe_allow_html=True)
                    st.image(article['urlToImage'], use_column_width=True)
                    st.markdown('</a>', unsafe_allow_html=True)
                st.markdown(f'<a href="{article["url"]}" class="article-title" target="_blank">{article["title"]}</a>', unsafe_allow_html=True)
