import scrapy

class TripAdvisor2(scrapy.Spider):
    name = "trip_advisor2"
    def __init__(self, subdir=None, *args, **kwargs):
        self.start_urls = ["https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa0-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa30-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa60-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa90-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa120-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa150-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa180-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa210-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa240-United_States.html",
                           "https://www.tripadvisor.com/Attractions-g191-Activities-c61-t87-oa270-United_States.html"]

    def parse(self, response):
        next_page = response.xpath("//div[@class = 'alPVI eNNhq PgLKC tnGGX']//a[1]//@href").getall() #css command to redirect to the full cast page url
        for next in next_page:
            yield response.follow(next, callback = self.parse_trail) #redirects to the new url page and executes parse_full_credits 

    #def parse_full_credits(self, response):
        #trail_page = response.xpath("//div[@class = 'BYvbL A']//a[@class = 'BUupS _R w _Z y M0 B0 Gm wSSLS']//@href").getall()
        #for trail in trail_page: #for every trail in the trial page list url, execute the callback command parse_actor_page 
            #yield response.follow(trail, callback = self.parse_trail)

    def parse_trail(self, response):
        trail = response.xpath("//h1//text()").get()
        comment_title = response.xpath("//div[@class = 'LbPSX']//div[@class = 'biGQs _P fiohW qWPrE ncFvv fOtGX']//span//text()").getall()
        ratings = response.xpath("//div[@class = 'LbPSX']//svg[@class = 'UctUV d H0']//title//text()").getall()
        comment_text = response.xpath("//div[@class = 'LbPSX']//span[@class = 'JguWG']//span[@class = 'yCeTE']//text()[1]").getall()
        pictures = response.xpath("//div[@class = 'LbPSX']//span[@class = 'biGQs _P XWJSj Wb']//img//@srcset").getall()
        overall_rating = response.xpath("//div[@class = 'biGQs _P fiohW hzzSG uuBRH']//text()").get()
        #for ix in range(len(comment_title)):
            #yield {
              #  "trail":trail,
               # "overall_rating": overall_rating,
              #  "comment_title":comment_title[ix],
             #   "ratings":ratings[ix],
            #    "comment_text":comment_text[ix]
         #   }
        
        for picture in pictures:
            yield{
                "trail_name": trail,
                "picture": picture  
            }
