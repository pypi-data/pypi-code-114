class DelhiMetro:

    def __init__(self):
        super(DelhiMetro).__init__()
        self.keyword=None
        self.line_code=None
        self.station_code=None
        self.start_station_code=None
        self.final_station_code=None

    @classmethod
    def applicant_to_object(cls,db_ob):
        applicant = cls()
        applicant.keyword=db_ob.keyword
        applicant.line_code=db_ob.line_code
        applicant.station_code  = db_ob.station_code
        applicant.start_station_code = db_ob.start_station_code
        applicant.final_station_code = db_ob.final_station_code
        return applicant