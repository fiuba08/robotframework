from __future__ import with_statement

import os
from os.path import abspath, dirname, join
from subprocess import call, STDOUT
import tempfile

from robot.utils.asserts import assert_equals
from robot.utils import decode_output


ROBOT_SRC = join(dirname(abspath(__file__)), '..', '..', '..', 'src')
DATA_DIR = join(dirname(abspath(__file__)), '..', '..', 'testdata', 'tidy')
TEMP_FILE = join(os.getenv('TEMPDIR'), 'tidy-test-dir', 'tidy-test-file')


class TidyLib(object):

    def __init__(self, interpreter):
        self._tidy = [interpreter, '-m', 'robot.tidy']
        self._interpreter = interpreter

    def run_tidy(self, options, input, output=None, tidy=None):
        """Runs tidy in the operating system and returns output."""
        command = (tidy or self._tidy)[:]
        if options:
            command.extend(options.split(' '))
        command.append(self._path(input))
        if output:
            command.append(output)
        print ' '.join(command)
        with tempfile.TemporaryFile() as stdout:
            rc = call(command, stdout=stdout, stderr=STDOUT,
                      cwd=ROBOT_SRC, shell=os.sep=='\\')
            stdout.seek(0)
            content = decode_output(stdout.read().strip())
            if rc:
                raise RuntimeError(content)
            return content

    def run_tidy_and_check_result(self, options, input, output=TEMP_FILE,
                                  expected=None):
        """Runs tidy and checks that output matches content of file `expected`."""
        result = self.run_tidy(options, input, output)
        self.compare_tidy_results(output or result, expected or input)

    def run_tidy_as_a_script_and_check_result(self, options, input,
                                              output=TEMP_FILE, expected=None):
        """Runs tidy and checks that output matches content of file `expected`."""
        tidy = [self._interpreter, join(ROBOT_SRC, 'robot', 'tidy.py')]
        result = self.run_tidy(options, input, output, tidy)
        self.compare_tidy_results(output or result, expected or input)

    def compare_tidy_results(self, result, expected):
        if os.path.isfile(result):
            result = self._read(result)
        expected = self._read(expected)
        result_lines = result.splitlines()
        expected_lines = expected.splitlines()
        msg = "Actual:\n%s\n\nExpected:\n%s\n\n" % (repr(result), repr(expected))
        assert_equals(len(result_lines), len(expected_lines), msg)
        for line1, line2 in zip(result_lines, expected_lines):
            assert_equals(repr(unicode(line1)), repr(unicode(line2)), msg)

    def _path(self, path):
        return abspath(join(DATA_DIR, path.replace('/', os.sep)))

    def _read(self, path):
        with open(self._path(path)) as f:
            return f.read().decode('UTF-8')
