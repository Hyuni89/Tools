import scrapy

class UsedCarSpider(scrapy.Spider):

    name = "usedcar"

    def start_requests(self):
        URL = "http://auto.danawa.com/usedcar/?Tab=classic&Brand=%s&Series=%s&Model=%s"
        BRAND = ["307", "312"]           # KIA, CHEVOLET
        SERIES = ["2735", "3163"]         # MORNING, SPARK
        MORNING_MODEL = ["3333", "3239", "2132", "2029", "1910"]    # lastest order
        SPARK_MODEL = ["3255", "2138"]
        MODEL = [MORNING_MODEL, SPARK_MODEL]

        for i in range(2):
            for j in range(len(MODEL[i])):
                tmpURL = URL % (BRAND[i], SERIES[i], MODEL[i][j])
                self.log(tmpURL)
                yield scrapy.Request(url=tmpURL, callback=self.parse)

    def parse(self, response):
        subSite = response.css("li.clearFix")

        for sub in subSite:
            print(sub.css("img").xpath("@src").extract())   # image

                # car_name
                # car_photo
                # car_model
                # car_mile
                # car_oil
                # car_price
                # car_year
                # car_color
                # car_number
                # car_tran