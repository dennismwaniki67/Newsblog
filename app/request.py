from app import app
import urllib.request,json
from .models import news

News = news.News
NewsArticle = news.NewsArticle

# Getting API key
api_key = app.config['NEWS_API_KEY']

# Getting the NEWS base url
base_url = app.config["NEWS_API_BASE_URL"]
news_article_url = app.config['NEWS_ARTICLE_URL']

#Getting news sources:
def get_news():
    """
  Function that gets the json response to our url request
  """
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_source = None

        if get_news_response["sources"]:
            news_source_list = get_news_response["sources"]
            news_source = process_source(news_source_list)

    return news_source