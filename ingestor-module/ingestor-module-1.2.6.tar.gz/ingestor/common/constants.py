LABEL = "label"
PROPERTIES = "properties"
RELATIONSHIP = "relationship_name"
LEFT = 'left'

'''for user-content network generation'''
USER_CONTENT_RELATIONSHIP_LABEL = 'VIEWED'

'''for CONTENT label'''
CONTENT = "content"
CONTENT_ID = "content_id"
TITLE = "title"
YEAR = "year"
STATUS = "status"
DURATION_MINUTE = "duration_minute"
IS_GEO_BLOCK = "is_geo_block"
IS_FREE = "is_free"
IS_ORIGINAL = "is_original"
IS_BRANDED = "is_branded"
IS_EXCLUSIVE = "is_exclusive"
SYNOPSIS = "synopsis"
SYNOPSIS_EN = "synopsis_en"
START_DATE = "start_date"
END_DATE = "end_date"
MODIFIED_ON = "modified_on"
TYPE = "type"

'''for RATING label'''
RATING = 'rating'

'''for CATEGORY label'''
CATEGORY = "category"
CATEGORY_ID = "category_id"
CATEGORY_EN = 'category_en'

'''for SUBCATEGORY label'''
SUBCATEGORY = "subcategory"
SUBCATEGORY_ID = "subcategory_id"
SUBCATEGORY_EN = 'subcategory_en'

'''for COUNTRY label'''
COUNTRY = "country"
COUNTRY_ID = 'country_id'
COUNTRY_NAME = "country_name"
COUNTRY_DESCRIPTION = "country_description"

'''for TAG label'''
TAGS = "tags"
TAGS_ID = "tags_id"
TAGS_NAME = "tags_name"

'''for ACTOR label'''
ACTOR = "actor"
ACTORS = "actors"
ACTOR_NAME = "actor_name"
ACTOR_ID = "actor_id"

'''for Director label'''
DIRECTORS = 'directors'
DIRECTOR_NAME = 'director_name'
DIRECTOR_ID = 'director_id'

'''for SEASON label'''
SEASON_ID = 'season_id'
SEASON_NAME = "season_name"
SEASON = 'season'

'''for CONTENT_CORE label'''
CONTENT_CORE = "content_core"
CONTENT_CORE_ID = "content_core_id"
CONTENT_CORE_SYNOPSIS = 'content_core_synopsis'
CONTENT_CORE_SYNOPSIS_EN = 'content_core_synopsis_en'
CONTENT_CORE_TITLE = 'content_core_title'
CONTENT_CORE_EPISODE = 'content_core_episode'

'''for PACKAGE label'''
PACKAGE = "package"
PACKAGES = "packages"
PACKAGE_ID = "package_id"
PACKAGE_NAME = "package_name"
PACKAGE_NAME_EN = "package_name_en"

'''for PRODUCT label'''
PRODUCT = "product"
PRODUCTS = "products"
PRODUCT_ID = "product_id"
PRODUCT_NAME = "product_name"
PRODUCT_NAME_EN = "product_name_en"

'''for Paytv provider label'''
PAYTV_PROVIDER = "paytv_provider"
PAYTVPROVIDER_ID = "paytvprovider_id"
PAYTVPROVIDER_NAME= "paytvprovider_name"

'''for HOMEPAGE label'''
HOMEPAGE = "homepage"
HOMEPAGE_ID = "homepage_id"
HOMEPAGE_TITLE = "homepage_title"
HOMEPAGE_TITLE_EN = "homepage_title_en"
HOMEPAGE_STATUS = "homepage_status"
HOMEPAGE_TYPE = "homepage_type"

'''for preprocessing_utils'''
WHITESPACE_REGEX = '\s+'
SINGLE_SPACE = ' '

'''for merge df : content profile'''
CONTENT_BUNDLE_ID = "content_bundle_id"

''' for user labels '''
CREATED_ON = 'created_on'
CUSTOMER_ID = "customer_id"
CUSTOMER_CREATED_ON = "customer_created_on"
CUSTOMER_MODIFIED_ON = "customer_modified_on"
USER_LABEL = "user"
USER_DEMOGRAPHY = "user_demography"
DURATION = "duration"
BIRTHDAY = "birthday"
GENDER = "gender"
UD_KEY = "UserDetail_UDKey"
REGION_NAME = "region_name"
DEVOPS = "devops"
VIDEO_ID1 = "video_id1"
ATTRIBUTE1 = "attribute1"
CATEGORY1 = "category1"
CATEGORY2 = "category2"
CHANNEL_LIVE = 'channel_live'
CATCHUP = 'catchup'
VOD = 'vod'
DEFAULT_DATE = "1970-10-10"
AGE = "age"
MEDIAN_AGE = 52
AGE_UPPER_BOUND = 100
DEFAULT_NUM = '-1'
DEFAULT_NAN = 'nan'
UNKNOWN_LABEL = 'unknown'
GENDER_VALUES = {'male': 'm', 'female': 'f', 'gender': 'na'}
ABSURD_VALUE = "\\N"
DUMMY_ATTRIBUTE_SPLIT_ON = "_"
DEFAULT_FEATURE_VALUES = {
    COUNTRY_ID: DEFAULT_NAN, REGION_NAME: UNKNOWN_LABEL,
    DEVOPS: UNKNOWN_LABEL, ATTRIBUTE1: DEFAULT_NAN,
    RATING: DEFAULT_NAN,
}
LOCAL_CONNECTION_URI = "ws://localhost:8182/gremlin"
CSV_EXTENSION = ".csv"
FINAL_MERGED_DF = 'final_merged_df'
SOLO_FEATURE_LIST = [RATING, ATTRIBUTE1]
FEATURE_DICT = {
    CATEGORY: CATEGORY_ID, SUBCATEGORY: SUBCATEGORY_ID,
    ACTORS: ACTOR_ID, DIRECTORS: DIRECTOR_ID, TAGS: TAGS_ID
}