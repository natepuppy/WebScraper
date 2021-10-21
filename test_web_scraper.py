import unittest
import web_scraper
from bs4 import BeautifulSoup
# from web_scraper import get_total_positivity_score


class TestWebScraper(unittest.TestCase):


    def test_get_total_positivity_score(self):
        score = web_scraper.get_total_positivity_score(50, 45, 0.9)
        self.assertEqual(score, 0.50459)

    

    def test_get_star_rating(self):
        test_div = BeautifulSoup('<div class="rating-static rating-43 margin-top-none pull-left"></div>', 'html.parser')
        star_div_info = test_div.find("div", {"class": "rating-static"})
        rating = web_scraper.get_star_rating(star_div_info)
        self.assertEqual(rating, 43)

        test_div_2 = BeautifulSoup('<div class="rating-static visible-xs pad-none margin-none rating-21 pull-right"></div>', 'html.parser')
        star_div_info_2 = test_div_2.find("div", {"class": "rating-static"})
        rating_2 = web_scraper.get_star_rating(star_div_info_2)
        self.assertEqual(rating_2, 21)

    def test_get_employee_rating(self):
        test_div = BeautifulSoup('<div class="rating-static rating-40 margin-top-none pull-left"></div>', 'html.parser')
        star_div_info = test_div.find("div", {"class": "rating-static"})
        test_div_2 = BeautifulSoup('<div class="rating-static rating-10 margin-top-none pull-left"></div>', 'html.parser')
        star_div_info_2 = test_div_2.find("div", {"class": "rating-static"})

        arr = []
        arr.append(star_div_info)
        arr.append(star_div_info_2)

        rating = web_scraper.get_employee_rating(arr)
        self.assertEqual(rating, 25)

        rating_2 = web_scraper.get_employee_rating([])
        self.assertEqual(rating_2, 49)


    # <div class="rating-static rating-50 margin-top-none pull-left"></div>
    # <div class="rating-static visible-xs pad-none margin-none rating-50 pull-right"></div>

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()