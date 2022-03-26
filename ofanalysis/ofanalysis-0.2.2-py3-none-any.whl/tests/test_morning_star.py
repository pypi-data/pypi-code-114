from unittest import TestCase

from ofanalysis.morningstar.morning_star import MorningStar


class TestMorningStar(TestCase):
    def setUp(self) -> None:
        self.morning_star = MorningStar(
            web_driver_path='./drivers/chromedriver',
            assets_path='./assets',
            cookie_str='ASP.NET_SessionId=2ryt2tuxvearx0ek5j4y11md; Hm_lvt_eca85e284f8b74d1200a42c9faa85464=1648263052; MSCC=p4i0G02/Of8=; user=username=laye0619@gmail.com&nickname=laye0619&status=Free&memberId=458975&password=trWMrjKv97VkUvhSrVRdJw==; authWeb=2EA92C9858F4D79C3B056777F08106CE589F02651BB2A97F3D5554A9A8368A831F1D83970DEDC326B1F62AFB96906D1CB5C83F865DAB05D58E437678DA1C291D7034D149D90891D0872CAC23F807F4D8EDF478FAB2C93E13DA530FB38D377E3BD18013947DC46C914A284ED5378488ABAD53BE3B; MS_LocalEmailAddr=laye0619@gmail.com=; Hm_lpvt_eca85e284f8b74d1200a42c9faa85464=1648263096; AWSALB=8+toOYS3OvJ8AxQXRq3/Kt7HbvYXj82bE6GtKpdQqY+ChSblZFKyZ0cFV+xSD00JglOa40xvW86XuUkSXMNV+0ydtB22IPZ51KcTPMM5BVnpoRjdD2TNS4Zjq8tA; AWSALBCORS=8+toOYS3OvJ8AxQXRq3/Kt7HbvYXj82bE6GtKpdQqY+ChSblZFKyZ0cFV+xSD00JglOa40xvW86XuUkSXMNV+0ydtB22IPZ51KcTPMM5BVnpoRjdD2TNS4Zjq8tA'
        )

    def test_get_fund_list(self):
        self.morning_star.get_fund_list()

    def test_write_to_db(self):
        # self.morning_star.write_to_db()
        pass
