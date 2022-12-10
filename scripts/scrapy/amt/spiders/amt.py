import scrapy
from ..items import AmtItem


class AmtSpider(scrapy.Spider):
    name = 'amt'
    allowed_domains = ['www.piano-midi.de']
    start_urls = ['http://www.piano-midi.de/midi_files.htm']

    def parse(self, response):
        yield from response.follow_all(css='td.midi a', callback=self.parse_composer)

    def parse_composer(self, response):
        item = AmtItem()
        item['file_urls'] = []
        for mid in response.css('a[href*=mid]::attr(href)').getall():
            if mid[-4:] == '.mid' and 'format' not in mid:
                item['file_urls'].append(response.urljoin(mid))
        for mp3 in response.css('a[href*=mp3]::attr(href)').getall():
            item['file_urls'].append(response.urljoin(mp3))
        return item
