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

        with open("log", "w") as f:
            pass

        for i in range(2):
            for j in range(len(MODEL[i])):
                tmpURL = URL % (BRAND[i], SERIES[i], MODEL[i][j])
                self.log(tmpURL)
                yield scrapy.Request(url=tmpURL, callback=self.getPages)

    def getPages(self, response):
        pages = response.css(".pageList > a.page")
        for i in range(len(pages.extract()) + 1):
            tmpSubURL = response.url + "&Order=&Page=" + str(i + 1)
            self.log(tmpSubURL)
            yield scrapy.Request(url=tmpSubURL, callback=self.parse)

    def parse(self, response):
        subSite = response.css("li.clearFix")

        with open("log", "a") as f:
            for sub in subSite:
                car_photo = sub.css("div > a > img").xpath("@src")[0].extract()   # image
                subElement = sub.css("div > div > span")
                car_oil = subElement[0].extract()[6:-7]
                car_tran = subElement[1].extract()[6:-7]
                car_color = subElement[2].extract()[6:-7]
                car_number = subElement[3].extract()[6:-7]
                car_model = sub.css("div > div").xpath("@title")[0].extract()
                car_mile = sub.css('div[class="mile"]::text')[0].extract().strip()
                car_year = sub.css('div[class="year"]::text')[0].extract().strip()
                car_price = sub.css("div > span[class='num']::text")[0].extract().strip()
                car_link = sub.css("div > div > a").xpath("@href")[0].extract()[1:]
                f.write("%s|%s|%s|%s|%s|%s|%s|%s|%s|%s\n" % (car_model, car_oil, car_year, car_mile, car_price, car_tran, car_color, car_number, car_photo, "http://auto.danawa.com/usedcar/" + car_link))
