import scrapy

class populationSpider(scrapy.Spider):
    name = 'population'
    start_urls = ['https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/search-recherche/lst/results-resultats.cfm?Lang=E&TABID=1&G=1&Geo1=&Code1=&Geo2=&Code2=&GEOCODE=35&type=0']

    def parse(self, response):
        for link in response.css("#details-elements li > a:nth-child(1)::attr(href)").extract():
            yield scrapy.Request(response.urljoin(link),callback=self.get_info)

    def get_info(self, response):
        item = {}
        region = response.css(".small::text").extract_first()
        item['region'] = ' '.join(region.split()) if region else None
        item['population'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[2]/td[1]//text()').extract()[0].strip(),
        item['male'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[10]/td[2]//text()').extract()[0].strip(),
        item['female'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[10]/td[3]//text()').extract()[0].strip(),
        item['0_to_14years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[11]/td[1]//text()').extract()[0].strip(),
        item['15_to_19years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[16]/td[1]//text()').extract()[0].strip(),
        item['20_to_24years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[17]/td[1]//text()').extract()[0].strip(),
        item['25_to_29years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[18]/td[1]//text()').extract()[0].strip(),
        item['30_to_34years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[19]/td[1]//text()').extract()[0].strip(),
        item['35_to_39years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[20]/td[1]//text()').extract()[0].strip(), 
        item['40_to_44years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[21]/td[1]//text()').extract()[0].strip(),
        item['45_to_49years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[22]/td[1]//text()').extract()[0].strip(), 
        item['50_to_54years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[23]/td[1]//text()').extract()[0].strip(), 
        item['55_to_59years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[24]/td[1]//text()').extract()[0].strip(), 
        item['60_to_64years'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[25]/td[1]//text()').extract()[0].strip(),
        item['65_years_and_over'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[26]/td[1]//text()').extract()[0].strip(),
        item['average_age'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[41]/td[1]//text()').extract()[0].strip(),
        item['Knowledge_of_English'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[108]/td[1]//text()').extract()[0].strip(),
        item['Knowledge_of_French'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[109]/td[1]//text()').extract()[0].strip(),
        item['English_and_French'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[110]/td[1]//text()').extract()[0].strip(),
        item['Arabic'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[222]/td[1]//text()').extract()[0].strip(),
        item['Hebrew'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[226]/td[1]//text()').extract()[0].strip(),
        item['Vietnamese'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[233]/td[1]//text()').extract()[0].strip(),
        item['Tagalog'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[245]/td[1]//text()').extract()[0].strip(),
        item['Tamil'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[255]/td[1]//text()').extract()[0].strip(),
        item['Albanian'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[260]/td[1]//text()').extract()[0].strip(),
        item['Polish'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[273]/td[1]//text()').extract()[0].strip(),
        item['Russian'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[274]/td[1]//text()').extract()[0].strip(),
        item['German'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[290]/td[1]//text()').extract()[0].strip(),
        item['Dutch'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[288]/td[1]//text()').extract()[0].strip(),
        item['Greek'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[297]/td[1]//text()').extract()[0].strip(),
        item['Punjabi'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[308]/td[1]//text()').extract()[0].strip(),
        item['Urdu'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[311]/td[1]//text()').extract()[0].strip(),
        item['Gujarati'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[301]/td[1]//text()').extract()[0].strip(),
        item['Persian'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[315]/td[1]//text()').extract()[0].strip(),
        item['Portuguese'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[320]/td[1]//text()').extract()[0].strip(),
        item['Spanish'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[322]/td[1]//text()').extract()[0].strip(),
        item['Japanese'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[324]/td[1]//text()').extract()[0].strip(),
        item['Korean'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[327]/td[1]//text()').extract()[0].strip(),
        item['Cantonese'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[356]/td[1]//text()').extract()[0].strip(),
        item['Mandarin'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[358]/td[1]//text()').extract()[0].strip(),
        item['Under_$10,000'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[358]/td[1]//text()').extract()[0].strip(),
        item['income under $10,000'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[724]/td[1]//text()').extract()[0].strip(),
        item['$10,000_to_19,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[725]/td[1]//text()').extract()[0].strip(),
        item['$20,000_to_29,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[726]/td[1]//text()').extract()[0].strip(),
        item['$30,000_to_39,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[727]/td[1]//text()').extract()[0].strip(),
        item['$40,000_to_49,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[728]/td[1]//text()').extract()[0].strip(),
        item['$50,000_to_59,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[729]/td[1]//text()').extract()[0].strip(),
        item['$60,000_to_69,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[730]/td[1]//text()').extract()[0].strip(),
        item['$70,000_to_79,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[731]/td[1]//text()').extract()[0].strip(),
        item['$80,000_to_89,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[733]/td[1]//text()').extract()[0].strip(),
        item['$90,000_to_99,999'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[734]/td[1]//text()').extract()[0].strip(),
        item['$100,000_and_over'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[735]/td[1]//text()').extract()[0].strip()
        item['average income'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[688]/td[1]//text()').extract()[0].strip()
        item['employed'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1898]/td[1]//text()').extract()[0].strip(),
        item['unemployed'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1899]/td[1]//text()').extract()[0].strip(),
        item['Business, finance and administration occupations'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1922]/td[1]//text()').extract()[0].strip(),
        item['Natural and applied sciences and related occupations'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1923]/td[1]//text()').extract()[0].strip(),
        item['Health occupations'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1924]/td[1]//text()').extract()[0].strip(),
        item['Occupations in education, law and social, community and government services'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1925]/td[1]//text()').extract()[0].strip(),
        item['Occupations in art, culture, recreation and sport'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1926]/td[1]//text()').extract()[0].strip(),
        item['Sales and service occupations'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1927]/td[1]//text()').extract()[0].strip(),
        item['Trades, transport and equipment operators and related occupations'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1928]/td[1]//text()').extract()[0].strip(),
        item['Natural resources, agriculture and related production occupations'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1929]/td[1]//text()').extract()[0].strip(),
        item['Occupations in manufacturing and utilities'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1930]/td[1]//text()').extract()[0].strip()
        item['no certificate, degree or diploma'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1712]/td[1]//text()').extract()[0].strip()
        item['Secondary School diploma'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1713]/td[1]//text()').extract()[0].strip()
        item['College diploma'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1718]/td[1]//text()').extract()[0].strip()
        item['Bachelors degree'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1721]/td[1]//text()').extract()[0].strip()
        item['Masters degree'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1724]/td[1]//text()').extract()[0].strip()
        item['PhD'] = response.xpath('//*[@id="tablehtml"]/tbody/tr[1725]/td[1]//text()').extract()[0].strip()
        
        
        yield item
        


