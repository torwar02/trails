import scrapy

class TripAdvisor(scrapy.Spider):
    name = "trip_advisor"
    def __init__(self, subdir=None, *args, **kwargs):
        self.start_urls = ["https://www.tripadvisor.com/Tourism-g143010-Acadia_National_Park_Mount_Desert_Island_Maine-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g60665-American_Samoa-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143011-Arches_National_Park_Utah-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143012-Badlands_National_Park_South_Dakota-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g60733-Big_Bend_National_Park_Texas-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143013-Biscayne_National_Park_Florida-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143014-Black_Canyon_Of_The_Gunnison_National_Park_Colorado-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143015-Bryce_Canyon_National_Park_Utah-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143016-Canyonlands_National_Park_Utah-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143017-Capitol_Reef_National_Park_Utah-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143018-Carlsbad_Caverns_National_Park_New_Mexico-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143019-Channel_Islands_National_Park_California-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143020-Crater_Lake_National_Park_Oregon-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143021-Death_Valley_National_Park_Inyo_County_California-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143022-Denali_National_Park_and_Preserve_Alaska-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143023-Dry_Tortugas_National_Park_Florida_Keys_Florida-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143024-Everglades_National_Park_Florida-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143025-Gates_Of_The_Arctic_National_Park_and_Preserve_Alaska-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143026-Glacier_National_Park_Montana-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143027-Glacier_Bay_National_Park_and_Preserve_Alaska-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143028-Grand_Canyon_National_Park_Arizona-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143029-Grand_Teton_National_Park_Wyoming-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143030-Great_Basin_National_Park_Nevada-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g1511447-Great_Sand_Dunes_National_Park_Preserve_Colorado-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143031-Great_Smoky_Mountains_National_Park_Tennessee-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143032-Guadalupe_Mountains_National_Park_Texas-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143033-Haleakala_National_Park_Maui_Hawaii-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143034-Hawaii_Volcanoes_National_Park_Island_of_Hawaii_Hawaii-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143036-Isle_Royale_National_Park_Michigan-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g32544-Joshua_Tree_California-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143038-Katmai_National_Park_and_Preserve_Alaska-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143039-Kenai_Fjords_National_Park_Alaska-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143040-Kobuk_Valley_National_Park_Alaska-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143041-Lake_Clark_National_Park_and_Preserve_Alaska-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143042-Lassen_Volcanic_National_Park_California-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143043-Mammoth_Cave_National_Park_Kentucky-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g60900-Mesa_Verde_National_Park_Colorado-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143044-Mount_Rainier_National_Park_Washington-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143046-North_Cascades_National_Park_Washington-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143047-Olympic_National_Park_Washington-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g60932-Petrified_Forest_National_Park_Arizona-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g2193168-Redwood_National_Park_California-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143048-Rocky_Mountain_National_Park_Colorado-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143050-Sequoia_and_Kings_Canyon_National_Park_California-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143051-Shenandoah_National_Park_Virginia-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143052-Theodore_Roosevelt_National_Park_North_Dakota-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g147411-Virgin_Islands_National_Park_St_John_U_S_Virgin_Islands-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143054-Voyageurs_National_Park_Minnesota-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143055-Wind_Cave_National_Park_South_Dakota-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143056-Wrangell_St_Elias_National_Park_and_Preserve_Alaska-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g60999-Yellowstone_National_Park_Wyoming-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g61000-Yosemite_National_Park_California-Vacations.html",
                           "https://www.tripadvisor.com/Tourism-g143057-Zion_National_Park_Utah-Vacations.html"]

    def parse(self, response):
        next_page = response.xpath("//div//a[contains(@href, 'Attraction')]//@href").get() #css command to redirect to the full cast page url
        yield response.follow(next_page, callback = self.parse_full_credits) #redirects to the new url page and executes parse_full_credits 
    
    def parse_full_credits(self, response):
        trail_page = response.xpath("//div[@class = 'BYvbL A']//a[@class = 'BUupS _R w _Z y M0 B0 Gm wSSLS']//@href").getall()
        for trail in trail_page: #for every trail in the trial page list url, execute the callback command parse_actor_page 
            yield response.follow(trail, callback = self.parse_trail)

    def parse_trail(self, response):
        national_park = response.xpath("//span[@class = 'fxMOE']//text()").get()
        state = response.xpath("//span[@class = 'n q']//span[@class = 'biGQs _P pZUbB avBIb osNWb']//text()").getall()[1]
        trail = response.xpath("//h1//text()").get()
        comment_title = response.xpath("//div[@class = 'LbPSX']//div[@class = 'biGQs _P fiohW qWPrE ncFvv fOtGX']//span//text()").getall()
        ratings = response.xpath("//div[@class = 'LbPSX']//svg[@class = 'UctUV d H0']//title//text()").getall()
        comment_text = response.xpath("//div[@class = 'LbPSX']//span[@class = 'JguWG']//span[@class = 'yCeTE']//text()[1]").getall()
        pictures = response.xpath("//div[@class = 'LbPSX']//span[@class = 'biGQs _P XWJSj Wb']//img//@srcset").getall()
        overall_rating = response.xpath("//div[@class = 'biGQs _P fiohW hzzSG uuBRH']//text()").get()
        trail_type = response.xpath("//div[@class = 'biGQs _P pZUbB alXOW oCpZu GzNcM nvOhm UTQMg ZTpaU W KxBGd']//span//text()").get()
        for ix in range(len(comment_title)):
            yield {
                "national_park" : national_park,
                "state" : state,
                "trail":trail,
                "activity": trail_type,
                "overall_rating": overall_rating,
                "comment_title":comment_title[ix],
                "comment_ratings":ratings[ix],
                "comment_text":comment_text[ix]
            }
        
        #for picture in pictures:
            #yield{
              #  "trail_name": trail,
              #  "picture": picture  
           # }
