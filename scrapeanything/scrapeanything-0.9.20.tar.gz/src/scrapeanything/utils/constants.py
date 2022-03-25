class Integration:

    class Types:
        CSV = 'CSV'
        EXCEL = 'EXCEL'
        GOOGLESPREADSHEET = 'GOOGLE SPREADSHEET'

    class Modes:
        READ = 'READ'
        WRITE = 'WRITE'

class WebScraper:

    class Functions:
        SUBSTRING = 'substring'
        EXPLODE = 'explode'
        REPLACE = 'join'
        JOIN = 'join'

    class Types:
        PERCENTAGE = 'PERCENTAGE'
        BOOL = 'BOOL'
        MONEY = 'MONEY'
        NUMBER = 'NUMBER'
        INTEGER = 'INTEGER'
        GEO = 'GEO'
        CHAR = 'CHAR'
        URL = 'URL'
        LIST = 'LIST'
        DATE = 'DATE'
        JSON = 'JSON'
        STRING = 'STRING'

    class Properties:
        TEXT = 'text()'
        HTML = 'html()'

class Requests:

    class Types:
        POST = 'POST'
        GET = 'GET'
    
    class Responses:
        TEXT = 'TEXT'
        JSON = 'JSON'
