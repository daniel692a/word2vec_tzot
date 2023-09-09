from pathlib import Path

import scrapy


class BibleSpider(scrapy.Spider):
    name = "bible"
    allowed_domains = ['bible.com']

    def start_requests(self):
        urls = [
            'https://www.bible.com/bible/279/MAT.1.TZOZ',
            'https://www.bible.com/bible/279/MAT.2.TZOZ',
            'https://www.bible.com/bible/279/MAT.3.TZOZ',
            'https://www.bible.com/bible/279/MAT.4.TZOZ',
            'https://www.bible.com/bible/279/MAT.5.TZOZ',
            'https://www.bible.com/bible/279/MAT.6.TZOZ'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        chapter = response.url.split("/")[-1].split(".")[1]
        file = f"chapter-{chapter}.txt"
        verses = ""
        for verse in response.xpath("//span[contains(@class, 'ChapterContent_content')]/text()").getall():
            if verse.strip()!='':
                verses += f'{verse}\n'
        Path(file).write_text(verses)
        self.log(f"Saved file")