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

  get_total_positivity_score combines the overall rating of a review, the rating of the individual employees in a review, and the sentiment analysis positivity score from the nltk package (This is a pre-trained Nueual Network to analyze positive sentiment in a sentence). overall_rating is weighted the most, employee_rating the second, 
  and sentiment rating is the lowest weighted contributor. get_total_positivity_score weights them by by moving overall_rating into the 100s place, sentiment_rating into the ones place, and sentiment_rating stays in the decimanl places. 
  Then it normalizes it to be between zero and 1.

<h3>For example</h3>

overall_rating = 50 (out of 50)

employee_rating = 45 (out of 50)

sentiment_rating = .36 (out of 1)

=

total_positivity_score = 5045.36 / 10000 = 0.504536