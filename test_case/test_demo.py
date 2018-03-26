import unittest
from comm.service.get_excel_case_data import GetCaseData

step = 0

class Test_demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.getExcelCaseData = GetCaseData()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        global step
        step+=1
        file_name = '../data/test_shop.xlsx'
        index = 0
        self.getExcelCaseData.get_excel_data(file_name, index, step)

    def tearDown(self):
        pass

    def test_one(self):
        exp_case_data, resp_case_data = self.getExcelCaseData.get_case_data()
        self.assertIn(exp_case_data, resp_case_data, msg=None)


