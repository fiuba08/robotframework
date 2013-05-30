#  Copyright 2008-2012 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import with_statement

from contextlib import contextmanager

from robot.errors import DataError
from robot.variables import GLOBAL_VARIABLES


class ExecutionContexts(object):

    def __init__(self):
        self._contexts = []

    @property
    def current(self):
        return self._contexts[-1] if self._contexts else None

    @property
    def top(self):
        return self._contexts[0] if self._contexts else None

    def __iter__(self):
        return iter(self._contexts)

    @property
    def namespaces(self):
        return (context.namespace for context in self)

    def start_suite(self, namespace, output, dry_run=False):
        self._contexts.append(_ExecutionContext(namespace, output, dry_run))
        return self.current

    def end_suite(self):
        self._contexts.pop()


# This is ugly but currently needed e.g. by BuiltIn
EXECUTION_CONTEXTS = ExecutionContexts()


class _ExecutionContext(object):
    _started_keywords_threshold = 42  # Jython on Windows don't work with higher

    def __init__(self, namespace, output, dry_run=False):
        self.namespace = namespace
        self.output = output
        self.dry_run = dry_run
        self.suite_teardown = False
        self._in_keyword_teardown = 0
        self._started_keywords = 0

    # TODO: Clean-up needed here ....

    @property
    @contextmanager
    def in_suite_teardown(self):
        self.suite_teardown = True
        try:
            yield
        finally:
            self.suite_teardown = False

    @property
    def teardown(self):
        if self.suite_teardown or self._in_keyword_teardown:
            return True
        test = self.namespace.test
        return test and test.status != 'RUNNING'

    @property
    def variables(self):
        return self.namespace.variables

    # TODO: Remove
    def get_current_vars(self):
        return self.variables

    def start_keyword_teardown(self, error):
        self.variables['${KEYWORD_STATUS}'] = 'FAIL' if error else 'PASS'
        self.variables['${KEYWORD_MESSAGE}'] = unicode(error or '')
        self._in_keyword_teardown += 1

    def end_keyword_teardown(self):
        self._in_keyword_teardown -= 1

    def end_test(self, test):
        self.output.end_test(test)
        self.namespace.end_test()
        self.set_prev_test_variables(test)

    def end_suite(self, suite):
        self.copy_prev_test_vars_to_global()
        self.output.end_suite(suite)
        self.namespace.end_suite()
        EXECUTION_CONTEXTS.end_suite()

    def replace_vars_from_setting(self, name, value, errors):
        return self.namespace.variables.replace_meta(name, value, errors)

    def set_suite_variables(self, suite):
        self.variables['${SUITE_NAME}'] = suite.longname
        self.variables['${SUITE_SOURCE}'] = suite.source
        self.variables['${SUITE_DOCUMENTATION}'] = suite.doc
        self.variables['${SUITE_METADATA}'] = suite.metadata.copy()

    def set_prev_test_variables(self, test):
        self.variables['${PREV_TEST_NAME}'] = test.name
        self.variables['${PREV_TEST_STATUS}'] = test.status
        self.variables['${PREV_TEST_MESSAGE}'] = test.message

    def copy_prev_test_vars_to_global(self):
        for var in ['${PREV_TEST_NAME}',
                    '${PREV_TEST_STATUS}',
                    '${PREV_TEST_MESSAGE}']:
            GLOBAL_VARIABLES[var] = self.variables[var]

    def report_suite_status(self, status, message):
        self.variables['${SUITE_STATUS}'] = status
        self.variables['${SUITE_MESSAGE}'] = message

    def start_test(self, test):
        self.namespace.start_test(test)
        self.output.start_test(test)

    def set_test_status_before_teardown(self, message, status):
        self.namespace.set_test_status_before_teardown(message, status)

    def get_handler(self, name):
        return self.namespace.get_handler(name)

    def start_keyword(self, keyword):
        self._started_keywords += 1
        if self._started_keywords > self._started_keywords_threshold:
            raise DataError('Maximum limit of started keywords exceeded.')
        self.output.start_keyword(keyword)

    def end_keyword(self, keyword):
        self.output.end_keyword(keyword)
        self._started_keywords -= 1

    def start_user_keyword(self, kw):
        self.namespace.start_user_keyword(kw)

    def end_user_keyword(self):
        self.namespace.end_user_keyword()

    def warn(self, message):
        self.output.warn(message)

    def trace(self, message):
        self.output.trace(message)
