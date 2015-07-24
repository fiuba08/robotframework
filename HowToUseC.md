
---


**NOTE:** This demo has moved to a separate project:
https://bitbucket.org/robotframework/cdemo


---




# Introduction #

This simple example demonstrates how to use C language from Robot
Framework test libraries. The example uses Python's standard
[ctypes module](http://docs.python.org/library/ctypes.html), which
requires that the C code is compiled into a shared library. This
version is implemented and tested on Linux, but adapting it to other
operating systems would require only changing compilation and name of
the produced shared library.


# Getting and running the example #

The example is available on the
[download page](http://code.google.com/p/robotframework/downloads/list)
as
`robotframework-c-example-<date>.zip`.
After downloading and unzipping the package, you should have all the
files in a directory `robotframework-c-example`.

To try out the example first run `make` in the directory that was
created when you unzipped the package. This will create library
`liblogin.so`, a shared library that is needed to use `ctypes` module.
The example tests can be executed using command `pybot LoginTests.tsv`.
All the test should pass.


# System under test #

The demo application is a very simple login system, implemented using
C, that validates the given user name and password and returns the
status. There are two valid username password combinations:
`demo/mode` and `john/long`.

```
#include <string.h>
#define NR_USERS 2

struct User {
    const char* name;
    const char* password;
};
const struct User VALID_USERS[NR_USERS] = { "john", "long", "demo", "mode" };

int validate_user(const char* name, const char* password) {
    int i;
    for (i = 0; i < NR_USERS; i++) {
        if (0 == strncmp(VALID_USERS[i].name, name, strlen(VALID_USERS[i].name)))
            if (0 == strncmp(VALID_USERS[i].password, password, strlen(VALID_USERS[i].password)))
                return 1;
    }    
    return 0;
}
```


# Test library #

A simple test library that can interact with the above program using
`ctypes` module. The library provides only one keyword `Check User`.

```
from ctypes import CDLL, c_char_p

LIBRARY = CDLL('./liblogin.so')  # On Windows we'd use '.dll'


def check_user(username, password):
    """Validates user name and password using imported shared C library."""
    if not LIBRARY.validate_user(c_char_p(username), c_char_p(password)):
        raise AssertionError('Wrong username/password combination')


if __name__ == '__main__':
    import sys
    try:
        check_user(*sys.argv[1:])
    except TypeError:
        print 'Usage:  %s username password' % sys.argv[0]
    except AssertionError, err:
        print err
    else:
        print 'Valid password'
```


The `if __name__ == '__main__'` block above is not used by the
executed tests, but it allows using the library code as a tool for
manual testing. You can test this handy behavior by running, for
example, `python LoginLibrary.py demo mode` or
`python LoginLibrary.py demo invalid` on the command line.


# Test cases #

| `*** Settings ***` | | | |
|:-------------------|:|:|:|
| `Library`          | `LoginLibrary.py` | | |
|                    | | | |
| `*** Test Case ***` | | | |
| `Validate Users`   | | | |
|                    | `Check Valid User` | `john` | `long` |
|                    | `Check Valid User` | `demo` | `mode` |
|                    | | | |
| `Login With Invalid User Should Fail` | | | |
|                    | `Check Invalid User` | `de` | `mo` |
|                    | `Check Invalid User` | `invalid` | `invalid` |
|                    | `Check Invalid User` | `long` | `invalid` |
|                    | `Check Invalid User` | `${EMPTY}` | `${EMPTY}` |
|                    | | | |
| `*** Keyword ***`  | | | |
| `Check Valid User` | `[Arguments]` | `${username}` | `${password}` |
|                    | `Check User` | `${username}` | `${password}` |
|                    | | | |
| `Check Invalid User` | `[Arguments]` | `${username}` | `${password}` |
|                    | `Run Keyword And Expect Error` | `Wrong username/password combination` | `Check User` |
|                    | `...`  | `${username}` | `${password}` |