import unittest
from comm.utils.HtmlTestRunner import HTMLTestRunner


class Unittest_Utils():

    def add_Cases(self, testModule_name):
        __suite = unittest.TestSuite()
        cases = unittest.TestLoader().loadTestsFromTestCase(testModule_name)
        __suite.addTests(cases)
        return __suite

    def make_suite(self, suites):
        #将suite元组加到容器里
        self.__suite = unittest.TestSuite(suites)
        return self.__suite

    def run_suite(self, file, report=False,title=None, description=None):
        if report==False:
            with open('UnittestTextReport.txt', 'wb') as f:
                runner = unittest.TextTestRunner(stream=f, verbosity=2)
                runner.run(suite)
        elif report:
            with open(file, 'wb') as f:
                runner = HTMLTestRunner(stream=f,
                                        title=title,
                                        description=description,
                                        verbosity=2
                                        )
                runner.run(self.__suite)

if __name__ == '__main__':
    from test_case.test_demo import Test_demo
    suites_name = (Test_demo,)
    suites_list = []
    suites = Unittest_Utils()
    for suite_name in suites_name:
        suite = suites.add_Cases(suite_name)
        suites_list.append(suite)
    print(suites_list)
    suites.make_suite(suites_list)
    suites.run_suite(report=True)


