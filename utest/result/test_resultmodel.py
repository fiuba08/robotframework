import unittest
from robot.utils.asserts import assert_equal, assert_true, assert_raises

from robot.result.model import *


class TestSuiteStats(unittest.TestCase):

    def test_stats(self):
        suite = self._create_suite_with_tests()
        assert_equal(suite.critical_stats.passed, 2)
        assert_equal(suite.critical_stats.failed, 1)
        assert_equal(suite.all_stats.passed, 3)
        assert_equal(suite.all_stats.failed, 2)

    def test_nested_suite_stats(self):
        suite = self._create_nested_suite_with_tests()
        assert_equal(suite.critical_stats.passed, 4)
        assert_equal(suite.critical_stats.failed, 2)
        assert_equal(suite.all_stats.passed, 6)
        assert_equal(suite.all_stats.failed, 4)

    def test_test_count(self):
        suite = self._create_nested_suite_with_tests()
        assert_equal(suite.test_count, 10)
        assert_equal(suite.suites[0].test_count, 5)
        suite.suites.append(self._create_suite_with_tests())
        assert_equal(suite.test_count, 15)
        suite.suites[-1].tests.create()
        assert_equal(suite.test_count, 16)
        assert_equal(suite.suites[-1].test_count, 6)

    def _create_nested_suite_with_tests(self):
        suite = TestSuite()
        suite.suites = [self._create_suite_with_tests(),
                        self._create_suite_with_tests()]
        return suite

    def _create_suite_with_tests(self):
        suite = TestSuite()
        suite.set_criticality([], ['nc'])
        suite.tests = [TestCase(status='PASS'),
                       TestCase(status='PASS', tags='nc'),
                       TestCase(status='PASS'),
                       TestCase(status='FAIL'),
                       TestCase(status='FAIL', tags='nc')]
        return suite


class TestSuiteStatus(unittest.TestCase):

    def test_suite_status_is_passed_by_default(self):
        assert_equal(TestSuite().status, 'PASS')

    def test_suite_status_is_failed_if_critical_failed_test(self):
        suite = TestSuite()
        suite.tests.create(status='PASS')
        assert_equal(suite.status, 'PASS')
        suite.tests.create(status='FAIL')
        assert_equal(suite.status, 'FAIL')
        suite.tests.create(status='PASS')
        assert_equal(suite.status, 'FAIL')

    def test_suite_status_is_passed_if_only_passed_tests(self):
        suite = TestSuite()
        for i in range(10):
            suite.tests.create(status='PASS')
        assert_equal(TestSuite().status, 'PASS')

    def test_suite_status_is_failed_if_failed_subsuite(self):
        suite = TestSuite()
        suite.suites.create().tests.create(status='FAIL')
        assert_equal(suite.status, 'FAIL')


class TestElapsedTime(unittest.TestCase):

    def test_suite_elapsed_time_when_start_and_end_given(self):
        suite = TestSuite()
        suite.starttime = '20010101 10:00:00.000'
        suite.endtime = '20010101 10:00:01.234'
        assert_equal(suite.elapsedtime, 1234)

    def test_suite_elapsed_time_is_zero_by_default(self):
        suite = TestSuite()
        assert_equal(suite.elapsedtime, 0)

    def _test_suite_elapsed_time_is_test_time(self):
        suite = TestSuite()
        suite.tests.create(starttime='19991212 12:00:00.010',
                           endtime='19991212 13:00:01.010')
        assert_equal(suite.elapsedtime, 3610000)


if __name__ == '__main__':
    unittest.main()