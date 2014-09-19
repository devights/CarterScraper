import urllib2
from bs4 import BeautifulSoup
from StringIO import StringIO
from django.utils import timezone
import re
from carter_scraper.models import Car, Price, Feature

BALLARD = "cartersubaruballardsoa"
SHORELINE = "cartersubarusoa"


class CarterScrape():
    campus = None
    start_count = 0

    def __init__(self, start_count=0, campus=SHORELINE):
        self.campus = campus
        self.start_count = start_count

    def fetch_page_for_campus(self):
        url = "http://www.cartersubarushoreline.com/all-inventory/index.htm?start=%s&make=Subaru&accountId=%s&model=Outback&" % (self.start_count, self.campus)
        req = urllib2.Request(url)
        html = None
        try:
            html = urllib2.urlopen(req).read()
        except urllib2.URLError, e:
            if e.code == 404:
                raise
        except Exception as ex:
            print ex
            print url
            raise
        if html is not None:
            self._get_cars_from_html(html)


    def _get_cars_from_html(self, html):
        soup = BeautifulSoup(html)

        lists = soup.findAll("ul", class_="inventoryList")
        listings = []
        cars = []

        for list in lists:
            listings += list.findChildren("li", recursive=False)
        for item in listings:
            cars.append(self._car_from_html(item))
            # break
        Car.objects.bulk_create(cars)



    def _car_from_html(self, html):
        car = Car()

        try:
            title_block = html.find("h1", class_="fn h3")
            link = title_block.a["href"]
            title = title_block.a.getText()
            car.url = link
            car.trim = self._get_trim_word(title)
            car.number = self._get_number(title)
            car.year = self._get_year(title)
        except Exception as ex:
            print ex
            pass

        descriptions = html.find("div", class_="description").findChildren("dl")
        dl_litems = []
        for list in descriptions:
            for item in list.findChildren():
                dl_litems.append(item)
        dl_iter = iter(dl_litems)
        try:
            for item in dl_iter:
                if item.getText() == "Engine:":
                    car.engine = self._clean_string(next(dl_iter).getText())
                if item.getText() == "Transmission:":
                    car.transmission = self._clean_string(next(dl_iter).getText())
                if item.getText() == "Exterior Color:":
                    car.ex_color = self._clean_string(next(dl_iter).getText())
                if item.getText() == "Interior Color:":
                    car.in_color = self._clean_string(next(dl_iter).getText())
                if item.getText() == "Stock #:":
                    car.stock_number = self._clean_string(next(dl_iter).getText())
                if item.getText() == "Mileage:":
                    car.mileage = self._clean_string(next(dl_iter).getText())
                if item.getText() == "VIN:":
                    car.vin = self._clean_string(next(dl_iter).getText())
        except StopIteration:
            pass
        return car

    def _clean_string(self, string):
        clean_string = string.strip()
        clean_string = clean_string.strip(",")
        return clean_string

    def _get_trim_word(self, title):
        title = title.lower()
        if "premium" in title:
            return "premium"
        elif "limited" in title:
            return "limited"
        else:
            return "base"

    def _get_number(self, title):
        title = title.lower()
        if "2.5" in title:
            return "2.5i"
        elif "3.6" in title:
            return "3.6r"
        else:
            return "Wtf"

    def _get_year(self, title):
        return re.match(r'^[0-9]{4}', title)
