import unittest
import web_scraper
from bs4 import BeautifulSoup
import heapq


"""
This class is designed to test the functions in web_scraper.py
"""
class TestWebScraper(unittest.TestCase):

    def test_get_star_rating(self):
        # Create sample div and turn it into a BeautifulSoup object
        test_div = BeautifulSoup('<div class="rating-static rating-43 margin-top-none pull-left"></div>', 'html.parser')
        # Turn the div into a BeautifulSoup tag object
        star_div_info = test_div.find("div", {"class": "rating-static"})
        # Send to the get_star_rating() function and assert the correct answer
        rating = web_scraper.get_star_rating(star_div_info)
        self.assertEqual(rating, 43)

        # Repeat process for a second test
        test_div_2 = BeautifulSoup('<div class="rating-static visible-xs pad-none margin-none rating-21 pull-right"></div>', 'html.parser')
        star_div_info_2 = test_div_2.find("div", {"class": "rating-static"})
        rating_2 = web_scraper.get_star_rating(star_div_info_2)
        self.assertEqual(rating_2, 21)

    def test_get_employee_rating(self):
        # Create sample div and turn it into a BeautifulSoup object
        test_div = BeautifulSoup('<div class="rating-static rating-40 margin-top-none pull-left"></div>', 'html.parser')
        # Turn the div into a BeautifulSoup tag object
        star_div_info = test_div.find("div", {"class": "rating-static"})
        
        # Repeat for 2nd test
        test_div_2 = BeautifulSoup('<div class="rating-static rating-10 margin-top-none pull-left"></div>', 'html.parser')
        star_div_info_2 = test_div_2.find("div", {"class": "rating-static"})

        arr = []
        arr.append(star_div_info)
        arr.append(star_div_info_2)

        rating = web_scraper.get_employee_rating(arr)
        self.assertEqual(rating, 25)

        # Test an empty array for scenarios when there are no employee ratings
        rating_2 = web_scraper.get_employee_rating([])
        self.assertEqual(rating_2, 49)
    
    def test_get_total_positivity_score(self):
        score = web_scraper.get_total_positivity_score(50, 45, 0.9)
        self.assertEqual(score, 0.50459)

    def test_get_review_info(self):
        # Load test_page.txt which consists of HTML that contains a whole page of reviews
        with open('test_page.txt', 'r') as file:
            data = file.read()
            doc = BeautifulSoup(data, "html.parser")

        top_reviews = []
        heapq.heapify(top_reviews)

        # Populate the top_reviews max-heap
        top_reviews = web_scraper.get_review_info(doc, top_reviews)

        # Get the top two results for testing
        first_review = heapq.heappop(top_reviews)
        second_review = heapq.heappop(top_reviews)

        # The top two most positive reviews should be by SavannaH and Abygail respectively
        self.assertEqual(first_review.name, "- SavannaH")
        self.assertEqual(second_review.name, "- Abygail ")

    def test_print_solution(self):
        # Create top_reviews max-heap with two entries that are created below
        top_reviews = []
        heapq.heapify(top_reviews)

        review = web_scraper.Review("- nathan clark", "best car ever!!!", .505077)
        heapq.heappush(top_reviews, review)

        review = web_scraper.Review("- frodo baggins", "its da best Sam", .485075)
        heapq.heappush(top_reviews, review)
        
        web_scraper.print_solution(top_reviews)
        """
        The following should print to the console:

            best car ever!!!
            - nathan clark
            its da best Sam
            - frodo baggins
        """


if __name__ == '__main__':
    unittest.main()