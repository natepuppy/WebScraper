<h1>Dependencies</h1>

<h3>Python 3.8 or higher</h3>

<h3>BeautifulSoup</h3>

pip3 install beautifulsoup4

<h3>Requests</h3>

pip3 install requests

<h3>NLTK</h3>

pip3 install nltk



<h1>How to Run</h1>

<h3>Main Program</h3>

python3 web_scraper.py

<h3>Unit Tests</h3>

python3 test_web_scraper.py


<h1>Review Positivity Calculation</h1>

  get_total_positivity_score combines the overall rating of a review, the rating of the individual employees in a review, and the sentiment analysis positivity score from the nltk package. overall_rating comes from the number of stars given for the whole review. It is scraped from the page for each review. employee_rating also is scraped from each review, and it is the average rating given to the "employees worked with". If no employee rating is given, a default value of 49 (4.9 stars) is given. This is used so that 5 star employee reviews will be ranked over no employee reviews, however, no reviews will be higher than negative reviews. Lastly, nltk is a pre-trained neural network to analyze positive sentiment in a sentence. Documentation for it can be found here: https://www.nltk.org/ and https://www.nltk.org/api/nltk.sentiment.html.
  

  overall_rating is weighted the most, employee_rating the second, and sentiment rating is the lowest weighted contributor. get_total_positivity_score weights them by by moving overall_rating into the 100s place, sentiment_rating into the ones place, and sentiment_rating stays in the decimanl places. 
  Then it normalizes it to be between zero and 1. 

<h3>For example</h3>

overall_rating = 50 (out of 50)

employee_rating = 45 (out of 50)

sentiment_rating = .36 (out of 1)

=

total_positivity_score = 5045.36 / 10000 = 0.504536