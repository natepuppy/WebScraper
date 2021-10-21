"""
pip install requests
pip install beautifulsoup4
pip install nltk

python 3 required
python practice.py > output.txt   # if you want to output to a file
"""

import re
import heapq
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer





"""
This class models a review, and sets the less than comparator to compare by the positivity_score
"""
class Review:
    def __init__(self, name, text, positivity_score):
        self.name = name
        self.text = text
        self.positivity_score = positivity_score

    def __lt__(self, other):
        return self.positivity_score > other.positivity_score

"""
This function parses the class info of the divs that contain the information for a specific 
star rating. The number of stars depends on what class the div is. For example:
        <div class="rating-static visible-xs pad-none margin-none rating-48 pull-right"></div>
This would be a 4.8 out of 5 stars because the "rating-48" in the class info. 
"""
def get_star_rating(star_div_info):
    print(type(star_div_info))
    # this gives you all of the class information
    classes = star_div_info['class']
    for i in range(len(classes)):
        # find the rating in the form rating-{number} and get the number at the end
        if re.search("rating-\d", classes[i]):
            _, rating_string = classes[i].split('-')
            return int(rating_string)
    return 0


"""
This function takes the raw divs that contain the number of stars given to the employees in the 
"EMPLOYEES WORKED WITH" section of each review
"""
def get_employee_rating(employee_reviews):
    # If there wasn't an employee review
    if not employee_reviews:
        # This will give priority to positive reviews of employees, but prefer no reviews over reviews 
        # that arent completely positive (essentially a 4.9 rating)
        return 49 

    # Get the average rating of the employees that the reviewer interacted with
    total_employee_rating = 0
    for i in range(len(employee_reviews)):
        rating = get_star_rating(employee_reviews[i])
        total_employee_rating += rating
    return total_employee_rating / len(employee_reviews)

"""
This combines the ratings with overall_rating being weighted the most, employee_rating the second, 
and sentiment rating as the lowest weighted contributor. It does this by moving overall_rating into 
the 100s place, sentiment_rating into the ones place, and sentiment_rating stays in the decimanl places. 
Then it normalizes it to be between zero and 1.

For example:
   overall_rating = 50 (out of 50)
   employee_rating = 45 (out of 50)
   sentiment_rating = .36 (out of 1)
   =
   total_positivity_score = 0.504536
"""
def get_total_positivity_score(overall_rating, sentiment_rating, employee_rating=0):
    return ((overall_rating * 100) + employee_rating + sentiment_rating) / 10000

"""
Parse the information in page of reviews
"""
def get_review_info(doc, top_reviews):
    # Get each review section
    reviews = doc.find_all("div", {"class": "review-entry"})

    for i in range(len(reviews)):
        # Get the p tag that contains the actual written review
        review_text = reviews[i].find("p", {"class": "review-content"}).text

        # Use the nltk (natural language tool kit) library to analyze how positive the review is 
        # based on the built in SentimentIntensityAnalyzer machine learning network
        sentiment_rating = sia.polarity_scores(review_text)['pos']

        reviewer_name = reviews[i].find("span", {"class": "italic font-18 black notranslate"}).text

        # Get all of the divs with "rating-static" in the class name. The first two are connected to the 
        # overall rating. The 3rd and on contains how many stars were given to each of the "employees worked with"
        star_div_infos = reviews[i].find_all("div", {"class": "rating-static"})
        overall_rating = get_star_rating(star_div_infos[0])
        employee_avg_rating = get_employee_rating(star_div_infos[2:])
        total_positivity_score = get_total_positivity_score(overall_rating, sentiment_rating, employee_avg_rating)
        
        # Create a review to stor in the top_reviews max-heap
        review = Review(reviewer_name, review_text, total_positivity_score)
        heapq.heappush(top_reviews, review)

"""
This is where each page is requested and loaded
"""
def main_workflow(url, num_pages_to_scrape):
    # create a max-heap to store reviews
    top_reviews = []
    heapq.heapify(top_reviews)

    for i in range(1, num_pages_to_scrape + 1):
        # This determines what page to get
        url = re.sub("page\d", "page" + str(i), url)
        result = requests.get(url)

        # Use BeautifulSoup to store and parse the web pages
        doc = BeautifulSoup(result.text, "html.parser")
        get_review_info(doc, top_reviews)
    # print_solution(top_reviews)


"""
Print top three on the max-heap
"""
def print_solution(top_reviews):
    for _ in range(3):
        review = heapq.heappop(top_reviews)
        print(review.text)
        print(review.name)

"""
This program
    1 scrapes the first five pages of reviews
    2 identifies the top three most “overly positive” endorsements (criteria documented in the README)
    3 outputs these three reviews to the console, in order of severity
"""
if __name__=="__main__":
    # Download nltk sentiment analysis neural network
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()

    # Hyperparameters
    url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page1/?filter=ONLY_POSITIVE#link"
    num_pages_to_scrape = 5

    main_workflow(url, num_pages_to_scrape)
    
    
