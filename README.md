Group 7: Jiaxin Luo, Zion Gassner, Tyler Nguyen

# Abstract

Using the internet, it’s very easy to find information about hiking trails throughout the United States, but there’s a problem: it’s a lot easier to browse through lists of trails available online, like on the website alltrails.com, and filtering by location. What are you supposed to do if you don’t know much about an area but still want to go hiking, or what if you want to do certain things on your hike but don’t know where to go? You could do lots of research online yourself, reading articles or sifting through different locations, but this process can be very difficult, especially if you want to go somewhere that you’ve never been.

Our project addresses finding new places to visit based upon what type of hiking trails the user wants to see (which the user would describe). For instance, if the user wants to hike near lakes, then we give the user cities in the United States in states such as Michigan with pretty lake hikes. This would be mainly for tourists visiting the United States or people who want to visit parts of the country they have not been to. 

# Planned Deliverables

Full Success:

We’ll make either a dynamic website or app where the user would enter information about the type of hike they’re interested in such as geographic features or recommendations based on previous hikes.
We’ll use web scraping to collect data from alltrails.com and other websites that contain information about hiking trails.
We’ll need to use advanced machine learning techniques to gain as much information as we can about the trails: interpreting reviews left by hikers to understand what a trail is like and to implement a recommendation system based on a user’s history.
We’ll use plotly geographical plots to showcase trail locations and perhaps other information.
The app/website would give explanations as to why it has recommended certain trails/places to the user.

Partial Success:

The program would at the very least be able to return the trails/locations that best match the user’s criteria in some sort of object such as a pandas DataFrame.
It would also be able to return the necessary information to quickly and easily create a plotly plot.
In other words, we should at least be able to let the user feasibly generate a lot of the information themselves that they would otherwise find in the “Full Success” results. The hard part of making the recommendation and such should be done by the program!

# Webscraping
There are two webscrapers. One is in the TripAdvisor folder

# Word Embedding
There is a file called national_parks.ipynb which contains instructions and functions on how to create and return dataframes and geogrpahical plots of similar trails! 
