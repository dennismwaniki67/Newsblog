import unittest
from models import news

News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test the behaviour of the News class
    '''

    def setUp(self):
      '''
      method that runs before every test
      '''
      self.new_news = News("aftenposten", "Aftenposten","Norges ledende nettavis med alltid oppdaterte nyheter innenfor innenriks, utenriks, sport og kultur","https://www.aftenposten.no","general","no")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main() 
