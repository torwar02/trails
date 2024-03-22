Group 7: Jiaxin Luo, Zion Gassner, Tyler Nguyen

# Abstract

Using the internet, it’s very easy to find information about hiking trails throughout the United States, but there’s a problem: it’s a lot easier to browse through lists of trails available online, like on the website alltrails.com, and filtering by location. What are you supposed to do if you don’t know much about an area but still want to go hiking, or what if you want to do certain things on your hike but don’t know where to go? You could do lots of research online yourself, reading articles or sifting through different locations, but this process can be very difficult, especially if you want to go somewhere that you’ve never been.

Our project addresses finding new places to visit based upon what type of hiking trails the user wants to see (which the user would describe). For instance, if the user wants to hike near lakes, then we give the user cities in the United States in states such as Michigan with pretty lake hikes. This would be mainly for tourists visiting the United States or people who want to visit parts of the country they have not been to. 

# Planned Deliverables

Full Success:

We planned on making either a dynamic website or app where the user would enter information about the type of hike they’re interested in such as geographic features or recommendations based on previous hikes.
We’ll use web scraping to collect data from alltrails.com and other websites that contain information about hiking trails.
We’ll need to use advanced machine learning techniques to gain as much information as we can about the trails: interpreting reviews left by hikers to understand what a trail is like and to implement a recommendation system based on a user’s history.
We’ll use plotly geographical plots to showcase trail locations and perhaps other information.
The app/website would give explanations as to why it has recommended certain trails/places to the user.

Partial Success:

However, we only acheived Partial Success as the deployment of our functions into a dynamic website or app was not fully realized.
The program would at the very least returned the trails/locations that best matched our user’s criteria in a pandas DataFrame.
It would returned the necessary information to quickly and easily create a plotly plot such that user's could visualize where in the United States these similar trails are.
In other words, we should at least be able to let the user feasibly generate a lot of the information themselves that they would otherwise find in the “Full Success” results. The hard part of making the recommendation and such should be done by the program!

# Webscraping
There are two webscrapers. One is the Trip Advisor webscraper. In order to get the csv file containing reviews of all National Parks Trail, open up the command prompt. From there, navigate to the folder which contains the spider and run `scrapy crawl trip_advisor -o national_parks.csv`. In addition, there is a file in the folder called `coords.xlsx`. We need this csv file later in order to plot geographical plots of where our recommended trails are. Great, now we can analyze our reviews! 

# Word Embedding
Our model uses a technique called `word embedding` such that we can return reviews with the highest similarity score. Word embedding in NLP is an important technique that is used for representing words for text analysis in the form of real-valued vectors. In this approach, words and documents are represented in the form of numeric vectors allowing similar words to have similar vector representations. The extracted features are fed into a machine learning model so as to work with text data and preserve the semantic and syntactic information. This information once received in its converted form is used by NLP algorithms that easily digest these learned representations and process textual information.

There is a file called `national_parks.ipynb` which contains instructions on how to utilize the written functions which return the most similar trails to the one's you previously hiked, in addition to constructing geographical plots to visualize where in the United States these trails are! To start, make sure to download the `spacy` and `gensim` packages which utilizes Word2Vec for accurate word embeeding. Word2Vec is a two-layer neural network that processes text by taking in batches of raw textual data, processing them and producing a vector space of several hundred dimensions. Each unique word in the data is assigned a corresponding vector in the space. The positioning of these vectors in the space is determined by the words’ semantic meanings and proximity to other words.
Therefore detecting similarities mathematically. We will use a pre-trained word embedding model using the SpaCy package. To take advantage of built-in word vectors we’ll need a larger library. En_core_web_lg is 560 MB and has 514 thousand unique word vectors and reduces these vectors down to 300 dimensions for predictability. 

Pay attention to the the code that contains the line `!python -m spacy download en_core_web_lg`, as this will download the 560 MB model! Also pay attention to, the `plotting_parks` function, as this is the function which returns a Plotly geographical plot of similar National Park Trails. This function calls the `total_similarity` function which calls the `comment_similarity` function. These functions return the most similar trails and reviews in the form of a dataframe. Also make sure to run the preprocessing regular expression code in order to have a csv file which these functions take as a parameter. 
