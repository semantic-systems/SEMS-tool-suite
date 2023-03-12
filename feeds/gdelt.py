import re
from datetime import datetime, timedelta
from gdeltdoc import GdeltDoc, Filters


class GdeltFunctions:
    def __init__(self):
        self.api = GdeltDoc()

    def get_feed(self, query: str, lang: str = "English") -> str:
        '''Searches for feeds with the given query and returns one randomly'''
        if query == '':
            return ''
        today = datetime.today().strftime('%Y-%m-%d')
        yesterday = datetime.today() - timedelta(1)
        f = Filters(
            keyword=query,
            start_date=yesterday.strftime('%Y-%m-%d'),
            end_date=today,
            num_records=20,
            country=["UK", "US"]
        )

        # Search for articles matching the filters
        articles = self.api.article_search(f)

        try:
            english_articles = articles[articles['language'] == lang]
            title = english_articles.sample()["title"].values[0]
        except:
            title = ""
        return self.clean_feed(title)

    def get_feed_batch(self, query: str, lang: str = "English") -> Tuple[List, str]:
        '''Searches for feeds with the given query and returns one randomly'''
        if query == '':
            query = "Germany"

        today = datetime.today().strftime('%Y-%m-%d')
        yesterday = datetime.today() - timedelta(1)
        f = Filters(
            keyword=query,
            start_date=yesterday.strftime('%Y-%m-%d'),
            end_date=today,
            num_records=250,
            country=["UK", "US"]
        )

        # Search for articles matching the filters
        articles = self.api.article_search(f)
        english_articles = articles[articles['language'] == lang]
        description = f"{len(articles)} articles found with the keyword {query}, among which {len(english_articles)} articles are in English.\n"
        return [self.clean_feed(title) for title in list(set(english_articles['title'].values))], description

    # stolen from previous code ;)
    @staticmethod
    def clean_feed(feed: str):
        '''
        Utility function to clean feed text by removing links, special characters
        using simple regex statements.
        '''
        if feed.startswith("RT @") :
            feed = feed.replace("RT ", "")
        feed = re.sub(" . ",".", feed)
        feed = re.sub(" : ",":", feed)
        feed = re.sub(" / ","/", feed)
        feed = re.sub(" , ",", ", feed)
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", feed).split())


if __name__ == "__main__":
    api = GdeltFunctions()
    print(api.get_feed("earthquake"))