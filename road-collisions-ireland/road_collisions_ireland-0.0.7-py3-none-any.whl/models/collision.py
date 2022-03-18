import os
import tarfile
import glob
import hashlib

import pandas as pd

from road_collisions_base import logger
from road_collisions_base.utils import epsg_900913_to_4326
from road_collisions_base.models.generic import (
    GenericObjects,
    GenericObject
)
from road_collisions_base.models.raw_collision import RawCollision

from road_collisions_ireland.constants import (
    SEVERITY_MAP_VALS,
    SEVERITY_MAP,
    COUNTY_MAP_VALS,
    COUNTY_MAP,
    CIRCUMSTANCS_MAP_VALS,
    CIRCUMSTANCS_MAP,
    HOUR_MAP,
    HOUR_MAP_VALS,
    VEHICLE_TYPE_MAP_VALS,
    VEHICLE_TYPE_MAP,
    GENDER_MAP_VALS,
    GENDER_MAP,
    WEEKDAY_MAP_VALS,
    WEEKDAY_MAP

)

def isnan(num):
    return num != num


class Collisions(GenericObjects):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('child_class', RawCollision)
        super().__init__(*args, **kwargs)

    @staticmethod
    def from_file(filepath):
        data = None

        ext = os.path.splitext(filepath)[-1]
        if ext == '.tgz':
            tar = tarfile.open(filepath, "r:gz")
            tar.extractall(path=os.path.dirname(filepath))
            tar.close()

            data = []
            for sub_file in glob.iglob(os.path.dirname(filepath) + '/**', recursive=True):
                ext = os.path.splitext(sub_file)[-1]
                if ext == '.csv':
                    csv_data = pd.read_csv(
                        sub_file.replace('.csv.tgz', '.csv')
                    ).to_dict(orient='records')
                    data.extend(csv_data)
        else:
            raise Exception()

        collisions = Collisions()
        for collision_dict in data:
            obj = Collision.parse(
                collision_dict
            )

            # TODO: filter the object out here by whatever prop params
            # and save some mem

            collisions.append(obj)

        return collisions

    @staticmethod
    def from_dir(dirpath, region=None):
        collisions = Collisions()
        if region is None:
            search_dir = f'{dirpath}/**'
        else:
            search_dir = f'{dirpath}/{region}/**'
        for filename in glob.iglob(search_dir, recursive=True):
            if os.path.splitext(filename)[-1] not in {'.tgz'}:
                continue
            collisions.extend(
                Collisions.from_file(
                    filename
                )._data
            )

        return collisions

    def filter(self, **kwargs):
        '''
        By whatever props that exist
        '''
        logger.debug('Filtering from %s' % (len(self)))

        filtered = [
            d for d in self if all(
                [
                    getattr(d, attr) == kwargs[attr] for attr in kwargs.keys()
                ]
            )
        ]

        return Collisions(
            data=filtered
        )

    @staticmethod
    def load_all():
        import road_collisions_ireland
        return Collisions.from_dir(
            os.path.join(road_collisions_ireland.__path__[0], 'resources'),
            region='ireland'
        )


class Collision(GenericObject, RawCollision):

    __slots__ = [
        '_lat',
        '_lng',
        '_year',
        '_weekday',
        '_gender',
        '_age',
        '_vehicle_type',
        '_vehicle',
        '_hour',
        '_circumstances',
        '_num_fatal',
        '_num_minor',
        '_num_notinjured',
        '_num_serious',
        '_num_unknown',
        '_speed_limit',
        '_severity',
        '_county',
        '_carrf',
        '_carri',
        '_class2',
        '_goodsrf',
        '_goodsri',
        '_mcycrf',
        '_mcycri',
        '_otherrf',
        '_otherri',
        '_pcycrf',
        '_pcycri',
        '_pedrf',
        '_pedri',
        '_psvrf',
        '_psvri',
        '_unknrf',
        '_unknri',
    ]

    def __init__(self, **kwargs):
        super().__init__()

        self._lat = kwargs['lat']
        self._lng = kwargs['lng']
        self._year = kwargs['year']
        self._weekday = kwargs['weekday']
        self._gender = kwargs['gender']
        self._age = kwargs['age']
        self._vehicle_type = kwargs['vehicle_type']
        self._vehicle = kwargs['vehicle']
        self._hour = kwargs['hour']
        self._circumstances = kwargs['circumstances']
        self._num_fatal = kwargs['num_fatal']
        self._num_minor = kwargs['num_minor']
        self._num_notinjured = kwargs['num_notinjured']
        self._num_serious = kwargs['num_serious']
        self._num_unknown = kwargs['num_unknown']
        self._speed_limit = kwargs['speed_limit']
        self._severity = kwargs['severity']
        self._county = kwargs['county']
        self._carrf = kwargs['carrf']
        self._carri = kwargs['carri']
        self._class2 = kwargs['class2']
        self._goodsrf = kwargs['goodsrf']
        self._goodsri = kwargs['goodsri']
        self._mcycrf = kwargs['mcycrf']
        self._mcycri = kwargs['mcycri']
        self._otherrf = kwargs['otherrf']
        self._otherri = kwargs['otherri']
        self._pcycrf = kwargs['pcycrf']
        self._pcycri = kwargs['pcycri']
        self._pedrf = kwargs['pedrf']
        self._pedri = kwargs['pedri']
        self._psvrf = kwargs['psvrf']
        self._psvri = kwargs['psvri']
        self._unknrf = kwargs['unknrf']
        self._unknri = kwargs['unknri']

    @staticmethod
    def parse(data):
        if isinstance(data, Collision):
            return data

        return Collision(
            **data
        )

    @property
    def id(self):
        return hashlib.md5(
            str(
                '%s_%s_%s' % (self.lat, self.lng, self.weekday)
            ).encode()
        ).hexdigest()

    @property
    def data(self):
        return {
            'lat': self.geo[0],
            'lng': self.geo[1],
            'year': self.year,
            'weekday': self.weekday,
            'gender': self.gender,
            'age': self.age,
            'vehicle_type': self.vehicle_type,
            'vehicle': self.vehicle,
            'hour': self.hour,
            'circumstances': self.circumstances,
            'num_fatal': self.num_fatal,
            'num_minor': self.num_minor,
            'num_notinjured': self.num_notinjured,
            'num_serious': self.num_serious,
            'num_unknown': self.num_unknown,
            'speed_limit': self.speed_limit,
            'severity': self.severity,
            'county': self.county,
            'carrf': self.carrf,
            'carri': self.carri,
            'class2': self.class2,
            'goodsrf': self.goodsrf,
            'goodsri': self.goodsri,
            'mcycrf': self.mcycrf,
            'mcycri': self.mcycri,
            'otherrf': self.otherrf,
            'otherri': self.otherri,
            'pcycrf': self.pcycrf,
            'pcycri': self.pcycri,
            'pedrf': self.pedrf,
            'pedri': self.pedri,
            'psvrf': self.psvrf,
            'psvri': self.psvri,
            'unknrf': self.unknrf,
            'unknri': self.unknri
        }

    def serialize(self):
        return {
            'lat': self.geo[0],
            'lng': self.geo[1],
            'year': self.year,
            'weekday': self.weekday,
            'gender': self.gender,
            'age': self.age,
            'vehicle_type': self.vehicle_type,
            'vehicle': self.vehicle,
            'hour': self.hour,
            'circumstances': self.circumstances,
            'num_fatal': self.num_fatal,
            'num_minor': self.num_minor,
            'num_notinjured': self.num_notinjured,
            'num_serious': self.num_serious,
            'num_unknown': self.num_unknown,
            'speed_limit': self.speed_limit,
            'severity': self.severity,
            'county': self.county,
            'carrf': self.carrf,
            'carri': self.carri,
            'class2': self.class2,
            'goodsrf': self.goodsrf,
            'goodsri': self.goodsri,
            'mcycrf': self.mcycrf,
            'mcycri': self.mcycri,
            'otherrf': self.otherrf,
            'otherri': self.otherri,
            'pcycrf': self.pcycrf,
            'pcycri': self.pcycri,
            'pedrf': self.pedrf,
            'pedri': self.pedri,
            'psvrf': self.psvrf,
            'psvri': self.psvri,
            'unknrf': self.unknrf,
            'unknri': self.unknri
        }

    @property
    def geo(self):
        return [self._lat, self._lng]

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng

    @property
    def year(self):
        if isinstance(self._year, int):
            if self._year > 2000:
                return self._year
        return int(f'20{str(self._year).zfill(2)}')

    @property
    def weekday(self):
        if self._weekday in WEEKDAY_MAP_VALS:
            return self._weekday

        return WEEKDAY_MAP[
            int(self._weekday)
        ]

    @property
    def gender(self):
        gender = None

        if isnan(self._gender):
            return None

        if self._gender in GENDER_MAP_VALS:
            return self._gender

        try:
            gender = GENDER_MAP[
                self._gender.lower()
            ]
        except KeyError:
            logger.debug('Can not parse gender: %s', self._gender)
            gender = self._gender

        return gender

    @property
    def age(self):
        age = None

        if isinstance(self._age, int):
            if self._age % 10 == 0:
                return self._age

        if self._age is None:
            return None

        try:
            age = int(self._age) * 10
        except ValueError:
            logger.debug('Can not parse age: %s', self._age)

        return age

    @property
    def vehicle_type(self):
        if self._vehicle_type in VEHICLE_TYPE_MAP_VALS:
            return self._vehicle_type

        return VEHICLE_TYPE_MAP.get(
            int(self._vehicle_type),
            self._vehicle_type
        )

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def hour(self):
        if self._hour in HOUR_MAP_VALS:
            return self._hour

        hour = None
        try:
            hour = HOUR_MAP.get(
                int(self._hour),
                self._hour
            )
        except ValueError:
            hour = self._hour

        return hour

    @property
    def circumstances(self):
        if self._circumstances in CIRCUMSTANCS_MAP_VALS:
            return self._circumstances

        circumstances = None
        try:
            circumstances = CIRCUMSTANCS_MAP.get(
                int(self._circumstances),
                self._circumstances
            )
        except ValueError:
            circumstances = self._circumstances

        return circumstances

    @property
    def num_fatal(self):
        return int(self._num_fatal)

    @property
    def num_minor(self):
        return int(self._num_minor)

    @property
    def num_notinjured(self):
        return int(self._num_notinjured)

    @property
    def num_serious(self):
        return int(self._num_serious)

    @property
    def num_unknown(self):
        return int(self._num_unknown)

    @property
    def speed_limit(self):
        if isinstance(self._speed_limit, int):
            return self._speed_limit

        if self._speed_limit is None:
            return None

        speed_limit = None
        try:
            speed_limit = int(self._speed_limit)
        except ValueError:
            logger.debug(
                'Could not parse speed limit: %s',
                self._speed_limit
            )

        return speed_limit

    @property
    def severity(self):
        if self._severity in SEVERITY_MAP_VALS:
            return self._severity

        return SEVERITY_MAP[
            int(self._severity)
        ]

    @property
    def county(self):
        county_lower = self._county.lower()
        if county_lower in COUNTY_MAP_VALS:
            return county_lower

        return COUNTY_MAP[
            int(self._county)
        ]

    # NOT SURE WHAT THE BELOW DO

    @property
    def carrf(self):
        return int(self._carrf)

    @property
    def carri(self):
        return int(self._carri)

    @property
    def class2(self):
        # TODO: looks interesting
        return int(self._class2)

    @property
    def goodsrf(self):
        return int(self._goodsrf)

    @property
    def goodsri(self):
        return int(self._goodsri)

    @property
    def mcycrf(self):
        return int(self._mcycrf)

    @property
    def mcycri(self):
        return int(self._mcycrf)

    @property
    def otherrf(self):
        return int(self._otherrf)

    @property
    def otherri(self):
        return int(self._otherri)

    @property
    def pcycrf(self):
        return int(self._pcycrf)

    @property
    def pcycri(self):
        return int(self._pcycri)

    @property
    def pedrf(self):
        return int(self._pedrf)

    @property
    def pedri(self):
        return int(self._pedri)

    @property
    def psvrf(self):
        return int(self._psvrf)

    @property
    def psvri(self):
        return int(self._psvri)

    @property
    def unknrf(self):
        return int(self._unknrf)

    @property
    def unknri(self):
        return int(self._unknri)
