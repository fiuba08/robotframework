#  Copyright 2008-2010 Nokia Siemens Networks Oyj
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


from ctypes import windll, Structure, c_short, c_ushort, byref

from robot import utils


class COORD(Structure):
  _fields_ = [
    ("X", c_short),
    ("Y", c_short)]

class SMALL_RECT(Structure):
  _fields_ = [
    ("Left", c_short),
    ("Top", c_short),
    ("Right", c_short),
    ("Bottom", c_short)]

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
  _fields_ = [
    ("dwSize", COORD),
    ("dwCursorPosition", COORD),
    ("wAttributes", c_ushort),
    ("srWindow", SMALL_RECT),
    ("dwMaximumWindowSize", COORD)]


class DosHiglighting:
    FOREGROUND_RED = 0x0004
    FOREGROUND_YELLOW = 0x0006
    FOREGROUND_GREEN = 0x0002
    FOREGROUND_INTENSITY = 0x0008
    FOREGROUND_GREY = 0x0007

    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12

    _highlight_colors = {'FAIL': FOREGROUND_RED,
                         'ERROR': FOREGROUND_RED,
                         'WARN': FOREGROUND_YELLOW,
                         'PASS': FOREGROUND_GREEN}

    def __init__(self, msg):
        self._msg = msg

    def _set_text_attr(self, color):
        windll.kernel32.SetConsoleTextAttribute(windll.kernel32.GetStdHandle(self.STD_OUTPUT_HANDLE), color)

    def _get_text_attr(self):
        csbi = CONSOLE_SCREEN_BUFFER_INFO()
        windll.kernel32.GetConsoleScreenBufferInfo(self.STD_OUTPUT_HANDLE, byref(csbi))
        return csbi.wAttributes

    def _write_encoded_with_tab_replacing(self, stream, message):
        stream.write(utils.encode_output(message).replace('\t', ' '*8))

    def start(self):
        self._default_colors = self._get_text_attr()
        self._set_text_attr(self._highlight_colors[self._msg] | self.FOREGROUND_INTENSITY)
        return ''

    def end(self):
        self._set_text_attr(self._default_colors | self.FOREGROUND_INTENSITY)
        return ''
