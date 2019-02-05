import scrapy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Region, Cyclone, TrackingInfo


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://rammb.cira.colostate.edu/products/tc_realtime/index.asp']

    def __init__(self):
        engine = create_engine('postgresql+psycopg2://postgres:integra@localhost:5432/postgres')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def parse(self, response):
        for title in response.css('.basin_storms'):
            region_name = str(title.css('h3 ::text').extract_first()).strip()
            cyclone_name = title.css('ul>li>a ::text').extract_first()
            if cyclone_name:
                region = self.get_or_create(Region, {'name': region_name})
                cyclone = self.get_or_create(
                    Cyclone, {'name': cyclone_name.strip()})
                tracking_info = TrackingInfo(region=region, cyclone=cyclone)
                self.save_data(tracking_info)

    def save_data(self, obj):
        self.session.add(obj)
        self.session.commit()

    def get_or_create(self, model, kwargs):
        obj = self.session.query(model).filter_by(**kwargs).first()
        if not obj:
            obj = model(**kwargs)
            self.save_data(obj)
        return obj
