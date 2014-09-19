from django.core.management.base import BaseCommand
from carter_scraper.carter_interface import CarterScrape

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        cs = CarterScrape()
        cs.fetch_page_for_campus()