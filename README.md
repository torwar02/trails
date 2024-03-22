Group 7: Jiaxin Luo, Zion Gassner, Tyler Nguyen

Check our [Colab tutorial](https://colab.research.google.com/drive/1nqJLP57fWBSJXRDAukjobWJQScYNlV4n?usp=chrome_ntp)!

# Abstract

Using the internet, it’s very easy to find information about hiking trails throughout the United States, but there’s a problem: it’s a lot easier to browse through lists of trails available online, like on the website alltrails.com, and filtering by location. What are you supposed to do if you don’t know much about an area but still want to go hiking, or what if you want to do certain things on your hike but don’t know where to go? You could do lots of research online yourself, reading articles or sifting through different locations, but this process can be very difficult, especially if you want to go somewhere that you’ve never been.

Our project addresses finding new places to visit based upon what type of hiking trails the user has previously visited. For instance, if the user previously visited Half Dome Trail in Yosemite National Park, then we give the user cities and National Park Trials in the United States most similar to Half Dome Trail. This would be mainly for tourists visiting the United States or people who want to visit parts of the country they have not been to. 

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

# Image Matting

Image matting, also known as foreground/background separation, is a computer vision technique used to accurately extract the foreground object or region of interest from an image while preserving fine details and transparency information around object boundaries. This process generates an alpha matte representing opacity values for each pixel, enabling seamless composition of the foreground onto a new background.

With image matting, you can merge your selfies with pictures of any US national parks in the background provided, or upload your own choice. At this time, we used a pre-trained model called MODNet.

Reference: https://github.com/ZHKKKe/MODNet

MODNet(Modulator-Decoupled Network) is a deep learning architecture specifically designed for image matting tasks, introduced in a 2022 research paper by Zhanghan Ke, Jingyu Zhang, Kaihao Zhang, Qiong Yan, and Kaiqi Huang. MODNet distinguishes itself with unique features: Decoupled Modulation, Effective Feature Fusion, Lightweight Architecture, and Improved Generalization. The key innovation of MODNet lies in its decoupled modulation approach, effectively disentangling foreground and background features for superior performance in capturing intricate object boundaries and transparency information. This architectural design, along with effective feature fusion and a lightweight structure, positions MODNet as a notable advancement in image matting technology.

Feel free to click the Colab link at the begining since you need GPU to run it. You might also need to download the `mergePicture.py` file, which contains the function that is needed to show the merged images and you can see the final output right after.

# Web Development

Make sure you have all the files needed: `trails_backend-main` and `trails_frontend-main`

**Step 1: Prepare the Node Environment**

1. Visit the official Node.js website at [https://nodejs.org](https://nodejs.org) and download the installer suitable for your operating system (Windows, macOS, or Linux). Once downloaded, locate the installer file and execute it, following the on-screen instructions for installation.

2. To ensure that Node.js has been installed correctly, open a terminal and execute the command `node -v`. This command will display the installed version of Node.js on your system.

**Step 2: Start the Backend Server**

Navigate to the `/backend-main` folder in a terminal session.

1. Create a `.env` file within this directory containing the MongoDB USERNAME and PASSWORD required for database connectivity.
```
USERNAME=jamieluo
PASSWORD=oFWMJnNpsd9i0Gvp
```
2. Execute the command `npm install` to install the project dependencies.

3. Run the command `npm run dev` to start the backend server, establishing a connection to the MongoDB server and enabling it to listen for incoming requests from the frontend.

**Step 3: Start the Frontend Server**

Navigate to the `/frontend-main` folder in another terminal session.

1. Execute the command `npm install` to install the project dependencies.

2. Run the command `npm run dev` to initiate the frontend server.

3. Note: As the frontend and backend servers typically run on different ports locally, and due to browser security policies that may block cross-origin requests, we utilize a middleware to circumvent this limitation. If your frontend project is not running on port 5174, please adjust the port number in line 13 of the `/backend-main/server.js` file accordingly.

4. Upon successful execution, a link will appear in your terminal indicating the URL for accessing the frontend. Click on this link to interact with the website.

By following these steps, you can set up the Node.js environment, start the backend server, initiate the frontend server and play with our website.


