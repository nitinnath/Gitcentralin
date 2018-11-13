from connection import connection
import datetime


class PersonalLink:
    priority = ''
    websiteurl = ''
    websitename = ''
    purpose = ''
    tags = ''
    type = ''
    market = ''
    visualize = ''
    createddate = ''

    def __init__(self, priority, websiteurl, websitename, purpose, tags, type, market, visualize, createddate):
        self.priority = priority
        self.websiteurl = websiteurl
        self.websitename = websitename
        self.purpose = purpose
        self.tags = tags
        self.type = type
        self.market = market
        self.visualize = visualize
        self.createddate = createddate

    def getAllData(self):
        with connection.cursor() as cur:
            cur.execute("select * from personallink")
            data = cur.fetchall()
            cur.close()
            return data

    def insertPersonalLink(self):
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "INSERT INTO personallink ( priority,websiteurl,websitename,purpose,tags,type,market,visualize,createddate) VALUES (%s, %s,%s, %s,%s, %s,%s, %s, %s)"
                cursor.execute(sql, (
                self.priority, self.websiteurl, self.websitename, self.purpose, self.tags, self.type, self.market,
                self.visualize, self.createddate))
                connection.commit()
                cursor.close()
        finally:
            return "Saved successfully."
