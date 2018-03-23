from comm.utils.unittest_util import Unittest_Utils


class RunTest():

    def runTest(self, suites_name, file, title=None, description=None):
        suites = Unittest_Utils()
        suites_list = []
        for suite_name in suites_name:
            suite = suites.add_Cases(suite_name)
            suites_list.append(suite)
        suites.make_suite(suites_list)
        suites.run_suite(report=True, file=file, title=title, description=description)


if __name__ == '__main__':
    from test_case.test_demo import Test_demo
    suites_name = (Test_demo,)
    tests = RunTest()
    file = 'a.html'
    tests.runTest(suites_name,file)
