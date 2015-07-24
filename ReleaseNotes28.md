

# Robot Framework 2.8 #

Robot Framework 2.8 is a new major release with loads of bigger
and smaller enhancements and bug fixes. It was released on Tuesday 11th June 2013.

Questions and comments related to the release can be sent to the
[mailing lists](MailingLists.md) and possible bugs submitted to
the [issue tracker](http://code.google.com/p/robotframework/issues).

## Downloads and installation ##

Installers and other packages are available on the
[download page](http://code.google.com/p/robotframework/downloads/list).

Installation instructions can be found at the
[wiki page](https://code.google.com/p/robotframework/wiki/Installation).

## Compatibility with RIDE and Mabot ##

Latest [RIDE](https://github.com/robotframework/RIDE) versions
are not dependent on the installed Robot Framework version. It
is thus safe to install any Robot Framework release alongside RIDE.

[Mabot](https://code.google.com/p/robotframework-mabot/), as of version 0.9,
is not compatible with Robot Framework 2.8. This will be fixed in the future Mabot
releases.

## Most important enhancements ##

### Public API for generating and executing tests ###

A completely new API is introduced for creating executable test suites
programmatically on fly ([issue 825](https://code.google.com/p/robotframework/issues/detail?id=825)). Practically this means that tests can be now
created using Python programming language using based on external models or otherwise.

Robot Framework now provides [TestSuite](http://robot-framework.readthedocs.org/en/latest/autodoc/robot.running.html#robot.running.model.TestSuite) API for creating an executable
test suite structure. This structure includes test cases, keywords,
variables, imports and so on - basically everything that can be done in the
test case files is also possible via the API.

Additionally, these executable TestSuite objects can be built based on the
existing test case files and directories using [TestSuiteBuilder API](http://robot-framework.readthedocs.org/en/latest/autodoc/robot.running.html#robot.running.builder.TestSuiteBuilder).

Please take a look at [Robot Framework API documentation](http://robot-framework.readthedocs.org/en/latest/autodoc/robot.running.html) for practical examples.

### New `Process` test library ###

[Process](ProcessLibrary.md) library is a completely new test library which introduces new keywords for running processes ([issue 485](https://code.google.com/p/robotframework/issues/detail?id=485)).

The main enhancements compared to the process execution keywords in [OperatingSystem](OperatingSystemLibrary.md) library are better configuration and possibility to terminate started processes. See the [documentation of the library](ProcessLibrary.md) for more information.

### Named arguments changes ###

There are several bigger and smaller enhancements to the named argument syntax:

  * All arguments can be [named](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#named-arguments) now, not just the arguments with default values ([issue 1324](https://code.google.com/p/robotframework/issues/detail?id=1324)).
  * Named arguments are [supported by dynamic libraries](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#named-argument-syntax-with-dynamic-libraries), e.g. [SwingLibrary](https://github.com/robotframework/SwingLibrary) ([issue 1115](https://code.google.com/p/robotframework/issues/detail?id=1115)).
  * If a positional argument is used after named arguments, this now results to a clear error ([issue 1325](https://code.google.com/p/robotframework/issues/detail?id=1325)).
  * Named arguments work when importing a library using [Import Library](http://robotframework.googlecode.com/hg/doc/libraries/BuiltIn.html#Import%20Library) keyword ([issue 1424](https://code.google.com/p/robotframework/issues/detail?id=1424)).

### Support for Python's keyword arguments ###

Python has a so-called keyword argument syntax (`**kwargs`) which is now supported by
[Robot Framework as well](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#free-keyword-arguments) ([issue 1383](https://code.google.com/p/robotframework/issues/detail?id=1383)).

For example, if we have a keyword like below (like we have in the new [Process](ProcessLibrary.md) library):

```
def run_process(command, *arguments, **configuration):
   # ...
```

and call it as follows:

```
    Run Process    ls    -h    cwd=/tmp
```

the parameter `configuration` got by the keyword now contains a dictionary `{'cwd': '/tmp'}`.

### Support for re-executing failed test cases ###

New command line option `--runfailed` allows executing tests that have failed again ([issue 702](https://code.google.com/p/robotframework/issues/detail?id=702)).

### Creating reports and xUnit outputs is possible without processing output.xml ###

Reports and xUnit outputs can now be created as part of test execution without processing output.xml ([issue 1432](https://code.google.com/p/robotframework/issues/detail?id=1432)). If logs files are not needed, disabling them with `--log NONE` can thus save time and memory considerably.

### Variable related enhancements ###

  * It is possible to use imported variables in the variable table ([issue 561](https://code.google.com/p/robotframework/issues/detail?id=561)).
  * It is possible to use scalar variables as list variables ([issue 483](https://code.google.com/p/robotframework/issues/detail?id=483)).

### New control keywords in BuiltIn test library ###

New control flow related keywords have been added to the [BuiltIn](BuiltInLibrary.md) library:

  * `Pass Execution` and `Pass Execution If`, which make the test pass immediately and skip executing any further steps of the test ([issue 174](https://code.google.com/p/robotframework/issues/detail?id=174)).
  * `Return From Keyword` and `Return From Keyword If`, which return the control to the calling keyword with the user specified return values ([issue 996](https://code.google.com/p/robotframework/issues/detail?id=996)).
  * `Continue For Loop` and `Continue For Loop If`, which work like `continue` statement in popular programming languages ([issue 1125](https://code.google.com/p/robotframework/issues/detail?id=1125)).
  * `Exit For Loop If`, as a conditional variant for the existing `Exit For Loop` ([issue 1411](https://code.google.com/p/robotframework/issues/detail?id=1411)).


## Backwards incompatible changes ##

### The old runner entry point removed ###

Deprecated `robot/runner.py` entry point was removed ([issue 1439](https://code.google.com/p/robotframework/issues/detail?id=1439)).
Please use `robot/run.py` instead.

### Deprecated Screenshot library keywords removed ###

Deprecated keywords `Save Screenshot`, `Save Screenshot To` and
`Log Screenshot` were removed from [Screenshot](ScreenshotLibrary.md) library ([issue 1093](https://code.google.com/p/robotframework/issues/detail?id=1093)).

### Unused utility functions removed ###

Following utility functions were removed ([issue 1457](https://code.google.com/p/robotframework/issues/detail?id=1457)):

  * `matches` and `matches_any`: use `Matcher` and `MultiMatcher` instead
  * `normalize_tags`: functionality moved to `model.Tags` which tests use internally
  * `html_attr_escape`: use `attribute_escape` instead

`utils.matches` was unfortunately used by [SSHLibrary 1.1](http://code.google.com/p/robotframework-sshlibrary/) which is thus not compatible with RF 2.8. This utility will be added back temporarily in RF 2.8.1 ([issue 1472](https://code.google.com/p/robotframework/issues/detail?id=1472)), and !SSHLibrary 1.2 will be changed not to use `utils.matches` anymore.

### Creating scalar list in variable table is not possible ###

Creating a scalar variable with a list as it's value
is not allowed in the variable table anymore ([issue 939](https://code.google.com/p/robotframework/issues/detail?id=939)).  This was already deprecated
in Robot Framework 2.5. If there still is data that uses this functionality,
updating it is nearly trivial. All that is needed is changing `$` to `@`
in the variable name in the variable table.

### Using test suite init files as resources is not allowed ###

Using test suite init files (e.g. `__init__.txt`) as resources is not allowed anymore ([issue 1276](https://code.google.com/p/robotframework/issues/detail?id=1276)).

### Report (and log) generated if tests run `--output NONE` ###

Earlier using `--output NONE` disabled creating a log and a report in addition to the XML output file.
Now that the report can be generated also without the output file ([issue 1432](https://code.google.com/p/robotframework/issues/detail?id=1432)) this behavior was changed.

If just `--output NONE` is used with RF 2.8, the report is generated and there is an error about log generation failing ([issue 1444](https://code.google.com/p/robotframework/issues/detail?id=1444)).
Use `--output NONE --report NONE --log NONE` to disable all outputs.

### Empty timeout attributes in output XML ###

Empty timeout attributes are not written to the output XML anymore ([issue 1438](https://code.google.com/p/robotframework/issues/detail?id=1438)).
Using timeouts is pretty rare, so most of the time test cases and keywords just
had `timeout=""`. This increased XML size without any real benefits.

The change is backwards incompatible because external XML readers cannot anymore expect timeout
attribute to exist. In those rare cases that some external tool is actually interested in the timeout value,
updating it to handle this situation should not be a problem.

### Command line option errors are now fatal ###

All command line option errors are now handled as fatal errors preventing test execution ([issue 1447](https://code.google.com/p/robotframework/issues/detail?id=1447)).
Earlier some errors were fatal, but with `--reportbackground`, `--tagstatlink` and
`--suitestatlevel` there was just a warning.

### Traceback removed from xUnit outputs ###

Previously if test were run on DEBUG level, the xUnit output contained
a traceback of a failure (as well as all other debug messages). Now that xUnit output can be
generated without reading the output.xml to memory, the tracebacks are
never written ([issue 1456](https://code.google.com/p/robotframework/issues/detail?id=1456)).

### Non-existing variables in tags fail the test ###

Using a non-existing variable tests's tags fails the test ([issue 1469](https://code.google.com/p/robotframework/issues/detail?id=1469)).

## Deprecated features ##

### Attribute ROBOT\_EXIT\_FOR\_LOOP is deprecated ###

Using special `ROBOT_EXIT_FOR_LOOP` attribute with exceptions to exit for loops is deprecated ([issue 1436](https://code.google.com/p/robotframework/issues/detail?id=1436)).

### Command line option `--runmode` is deprecated ###

Command line option `--runmode` is now deprecated ([issue 1445](https://code.google.com/p/robotframework/issues/detail?id=1445)).
Please use the new, individual command line options `--dryrun`, `--randomize`,
`--exitonfailure` and `--skipteardownonexit` instead.

### Option --xunitfile changed to --xunit ###

The option `--xunitfile` has been deprecated in favor of the shorter
`--xunit` ([issue 1465](https://code.google.com/p/robotframework/issues/detail?id=1465)).

## Full list of fixes and enhancements in 2.8 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 825](https://code.google.com/p/robotframework/issues/detail?id=825) | Enhancement | Critical     | Public API for generating and executing test cases |
| [Issue 561](https://code.google.com/p/robotframework/issues/detail?id=561) | Defect   | High         | It's now possible to use imported variables in variable table |
| [Issue 483](https://code.google.com/p/robotframework/issues/detail?id=483) | Enhancement | High         | Using scalar variables as list variables is allowed |
| [Issue 485](https://code.google.com/p/robotframework/issues/detail?id=485) | Enhancement | High         | Separate library for running processes |
| [Issue 702](https://code.google.com/p/robotframework/issues/detail?id=702) | Enhancement | High         | Failed tests can be re-executed with `--runfailed` option |
| [Issue 939](https://code.google.com/p/robotframework/issues/detail?id=939) | Enhancement | High         | Creating scalar variables with list values in variable table is not allowed |
| [Issue 1115](https://code.google.com/p/robotframework/issues/detail?id=1115) | Enhancement | High         | Named arguments can be used with dynamic libraries |
| [Issue 1324](https://code.google.com/p/robotframework/issues/detail?id=1324) | Enhancement | High         | Named argument syntax can be used also with arguments not having default values |
| [Issue 1383](https://code.google.com/p/robotframework/issues/detail?id=1383) | Enhancement | High         | Python's keyword argument syntax is supported |
| [Issue 1432](https://code.google.com/p/robotframework/issues/detail?id=1432) | Enhancement | High         | Report and XUnit are generated without reading the output.xml |
| [Issue 1468](https://code.google.com/p/robotframework/issues/detail?id=1468) | Documentation | High         | Enhancement to public API documentation |
| [Issue 1379](https://code.google.com/p/robotframework/issues/detail?id=1379) | Defect   | Medium       | Settings and variable tables: Three dots are handled correctly |
| [Issue 1395](https://code.google.com/p/robotframework/issues/detail?id=1395) | Defect   | Medium       | Dialogs library documentation improved |
| [Issue 1453](https://code.google.com/p/robotframework/issues/detail?id=1453) | Defect   | Medium       | Wrong encoding detection for HTML5 document |
| [Issue 1466](https://code.google.com/p/robotframework/issues/detail?id=1466) | Defect   | Medium       | Dialog boxes don't properly close with Python on Linux |
| [Issue 174](https://code.google.com/p/robotframework/issues/detail?id=174) | Enhancement | Medium       | New BuiltIn keyword to stop text execution with PASS status |
| [Issue 996](https://code.google.com/p/robotframework/issues/detail?id=996) | Enhancement | Medium       | New BuiltIn keywords for returning from user keywords |
| [Issue 1125](https://code.google.com/p/robotframework/issues/detail?id=1125) | Enhancement | Medium       | New BuiltIn keyword for continuing for loop execution |
| [Issue 1325](https://code.google.com/p/robotframework/issues/detail?id=1325) | Enhancement | Medium       | Explicit error if positional arguments are used after named arguments |
| [Issue 1378](https://code.google.com/p/robotframework/issues/detail?id=1378) | Enhancement | Medium       | HTML can be used in error messages by prefixing message with `*HTML*` |
| [Issue 1381](https://code.google.com/p/robotframework/issues/detail?id=1381) | Enhancement | Medium       | New automatic variable: ${LOG\_LEVEL} |
| [Issue 1394](https://code.google.com/p/robotframework/issues/detail?id=1394) | Enhancement | Medium       | New Collection library keyword: `Dictionary Should Contain Item` |
| [Issue 1408](https://code.google.com/p/robotframework/issues/detail?id=1408) | Enhancement | Medium       | Support skipping non-critical tests in xUnit outputs |
| [Issue 1409](https://code.google.com/p/robotframework/issues/detail?id=1409) | Enhancement | Medium       | OperatingSystem library: Resolve `~` and `~user` in paths |
| [Issue 1411](https://code.google.com/p/robotframework/issues/detail?id=1411) | Enhancement | Medium       | New BuiltIn keyword for exiting for loop conditionally |
| [Issue 1444](https://code.google.com/p/robotframework/issues/detail?id=1444) | Enhancement | Medium       | Generate report by default when running tests with `--output NONE` |
| [Issue 1448](https://code.google.com/p/robotframework/issues/detail?id=1448) | Enhancement | Medium       | Setting teardown dynamically with variable is possible |
| [Issue 1276](https://code.google.com/p/robotframework/issues/detail?id=1276) | Defect   | Low          | Using init files as resources is not allowed |
| [Issue 1404](https://code.google.com/p/robotframework/issues/detail?id=1404) | Defect   | Low          | Better error message when dynamic library returns invalid argument spec |
| [Issue 1428](https://code.google.com/p/robotframework/issues/detail?id=1428) | Defect   | Low          | User guide: Screenshot library can be used with other interpreters than Jython |
| [Issue 1434](https://code.google.com/p/robotframework/issues/detail?id=1434) | Defect   | Low          | Tidy: Support Windows line separators with HTML files |
| [Issue 1435](https://code.google.com/p/robotframework/issues/detail?id=1435) | Defect   | Low          | Libdoc and Testdoc: Correct line separators on Windows in outputs |
| [Issue 1443](https://code.google.com/p/robotframework/issues/detail?id=1443) | Defect   | Low          | Listeners: `end_suite` has now the missing attributes |
| [Issue 1093](https://code.google.com/p/robotframework/issues/detail?id=1093) | Enhancement | Low          | Screenshot library: Deprecated `Save Screenshot`, `Save Screenshot To` and `Log Screenshot` keywords were removed |
| [Issue 1389](https://code.google.com/p/robotframework/issues/detail?id=1389) | Enhancement | Low          | Report and log: Smaller font size for section titles |
| [Issue 1405](https://code.google.com/p/robotframework/issues/detail?id=1405) | Enhancement | Low          | Dialogs library: Automatically wrap long text |
| [Issue 1424](https://code.google.com/p/robotframework/issues/detail?id=1424) | Enhancement | Low          | Named arguments are supported with `Import Library` keyword |
| [Issue 1436](https://code.google.com/p/robotframework/issues/detail?id=1436) | Enhancement | Low          | BuiltIn library: `ROBOT_EXIT_FOR_LOOP` attribute is now deprecated |
| [Issue 1438](https://code.google.com/p/robotframework/issues/detail?id=1438) | Enhancement | Low          | Output: Empty timeout attributes are not written to XML |
| [Issue 1439](https://code.google.com/p/robotframework/issues/detail?id=1439) | Enhancement | Low          | Deprecated `robot/runner.py` entry point is now removed |
| [Issue 1445](https://code.google.com/p/robotframework/issues/detail?id=1445) | Enhancement | Low          | Command line options: `--runmode` is now deprecated. Separate command line options `--dryrun`, `--randomize`, `--exitonfailure' and `--skipteardownonexit` introduced |
| [Issue 1447](https://code.google.com/p/robotframework/issues/detail?id=1447) | Enhancement | Low          | Command line options: All errors are now handled as fatal |
| [Issue 1449](https://code.google.com/p/robotframework/issues/detail?id=1449) | Enhancement | Low          | BuiltIn library: `Should Be True` and its dependents should automatically import Python's `os`- and `sys`-modules |
| [Issue 1456](https://code.google.com/p/robotframework/issues/detail?id=1456) | Enhancement | Low          | Remove failure traceback from xUnit outputs |
| [Issue 1457](https://code.google.com/p/robotframework/issues/detail?id=1457) | Enhancement | Low          | Remove deprecated utility functions |
| [Issue 1465](https://code.google.com/p/robotframework/issues/detail?id=1465) | Enhancement | Low          | Deprecate `--xunitfile` option in favor of shorter `--xunit` option |
| [Issue 1469](https://code.google.com/p/robotframework/issues/detail?id=1469) | Enhancement | Low          | Non-existing variables in tags should fail the test |
| [Issue 1470](https://code.google.com/p/robotframework/issues/detail?id=1470) | Enhancement | Low          | Libdoc should allow linking to all headers in the introduction |
| [Issue 1167](https://code.google.com/p/robotframework/issues/detail?id=1167) | Refactoring | Low          | File reading and writing code is unified |

Altogether 49 issues.

# Robot Framework 2.8.1 #

Robot Framework 2.8.1 is a minor release which adds back a deprecated internal utility method that unfortunately has been used in several external libraries ([issue 1472](https://code.google.com/p/robotframework/issues/detail?id=1472) and [issue 1474](https://code.google.com/p/robotframework/issues/detail?id=1474)). Now SSHLibrary and Selenium2Library should again work. This release also fixes some issues with new process library ([issue 1475](https://code.google.com/p/robotframework/issues/detail?id=1475) and [issue 1476](https://code.google.com/p/robotframework/issues/detail?id=1476)) and takes the new `**kwargs` functionality into use in Collections library ([issue 1473](https://code.google.com/p/robotframework/issues/detail?id=1473)). It was released on Friday 14th June 2013.

## Full list of fixes and enhancements in 2.8.1 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1472](https://code.google.com/p/robotframework/issues/detail?id=1472) | Defect   | High         | Removed utility functions broke SSHLibrary and SeleniumLibrary and need to be added back |
| [Issue 1474](https://code.google.com/p/robotframework/issues/detail?id=1474) | Defect   | High         | `ConnectionCache.current_index` should be assignable for compatibility reasons |
| [Issue 1475](https://code.google.com/p/robotframework/issues/detail?id=1475) | Defect   | Medium       | `Process.Terminate All Processes` does not terminate last started process if it is not active |
| [Issue 1476](https://code.google.com/p/robotframework/issues/detail?id=1476) | Defect   | Medium       | `Process.Terminate All Processes` does not clear resources |
| [Issue 1473](https://code.google.com/p/robotframework/issues/detail?id=1473) | Enhancement | Medium       | Collections: `Create Dictionary` and `Set To Dictionary` should accept `**items` |

Altogether 5 issues.

# Robot Framework 2.8.2 #

Robot Framework 2.8.2 is a minor release with major enhancements. The most important features are explained in the next section and a full list of features/fixes is a little further below.

Robot Framework 2.8.2 should be backwards-compatible with older 2.8 releases and thus safe to upgrade to. It was released on Tuesday 26th of November, 2013.

**NOTE:** Due to Google Code [deprecating downloads](http://google-opensource.blogspot.fi/2013/05/a-change-to-google-code-download-service.html), installers have been moved to https://pypi.python.org/pypi/robotframework/. Running `pip install robotframework` or `pip install --upgrade robotframework` works exactly like earlier.

## Most important enhancements in 2.8.2 ##

### New plain text reStructuredText parser ###

It is now possible to define test date in reStructuredText format in
`robotframework` code blocks using the plain text format ([issue 1495](https://code.google.com/p/robotframework/issues/detail?id=1495)). This new data
format combines many of the benefits of plain text and HTML formats.

Old support for parsing reST files as HTML was not affected.

### `**kwargs` support for dynamic test libraries ###

Normal Python libraries got support for free keyword arguments (`**kwargs`)
in Robot Framework 2.8 and now also dynamic libraries support them ([issue 1500](https://code.google.com/p/robotframework/issues/detail?id=1500)).
The support works both with Python and Java based dynamic libraries.

### Support for creating characters using `\xhh`, `\uhhhh` and `\Uhhhhhhhh` escapes ###

These escapes allow creating characters that are hard to create and
show in the test data ([issue 1524](https://code.google.com/p/robotframework/issues/detail?id=1524)). The main usages are:

  * Create "invisible" characters such as the null byte `\x00`.
  * Create Unicode characters that cannot be shown, for example, due to correct glyph being missing from the environment.
  * Using non-ASCII test data but keeping source files in ASCII.

### Removing and flattening named keywords ###

Old command line option `--RemoveKeywords` was enhanced to allow
removing named keywords from logs and XML output ([issue 1480](https://code.google.com/p/robotframework/issues/detail?id=1480)). This
helps reducing size of the generated output files if there are
certain keywords with big and/or many log messages.

New command line option `--FlattenKeywords` was added to allow
flattening keywords so that their internal nested keyword structure is
removed but all log messages preserved ([issue 1480](https://code.google.com/p/robotframework/issues/detail?id=1480)). This can
considerably reduce the size of the generated output files if there
are deep keyword structures. Because log messages are not removed,
most of the information is still there after flattening. Unlike removing keywords,
flattening is done already when XML output is parsed, before creating
an internal model based on it, and thus it can also save a
considerable amount of memory.

### `Run Keyword And Return` and `Run Keyword And Return If` keywords ###

These new [BuiltIn](BuiltInLibrary.md) keywords allow executing a certain keyword and returning from the enclosing user keyword ([issue 1588](https://code.google.com/p/robotframework/issues/detail?id=1588)).

For example,

```
Example keyword
    Run Keyword And Return    My Keyword    arg1    arg2
```

is equivalent to

```
Example keyword
   ${return} =    My Keyword    arg1    arg2
   [Return]    ${return}
```

### Possibility to use keyword with embedded arguments as template ###

This enhancement ([issue 1454](https://code.google.com/p/robotframework/issues/detail?id=1454)) is best explained with an example:

```
*** Test Cases ***
Example
    [Template]    The result of ${calculation} should be ${expected}
    1 + 1    2
    1 + 2    3

*** Keywords ***
The result of ${calculation} should be ${expected}
    ${result} =    Calculate    ${calculation}
    Should Be Equal    ${result}    ${expected}
```

### Enhancements to `Process` library ###

  * `Get Process Result` keyword to support getting results over remote interface ([issue 1490](https://code.google.com/p/robotframework/issues/detail?id=1490))
  * Add timeout and option to terminate process to `Wait For Process` keyword ([issue 1481](https://code.google.com/p/robotframework/issues/detail?id=1481))
  * `Send Signal To Process` keyword ([issue 1515](https://code.google.com/p/robotframework/issues/detail?id=1515))
  * `Terminate Process` should automatically kill process that does not terminate ([issue 1541](https://code.google.com/p/robotframework/issues/detail?id=1541))
  * `Terminate All Processes` should terminate, not kill, processes by default ([issue 1542](https://code.google.com/p/robotframework/issues/detail?id=1542))
  * `Terminate Process` should return result object ([issue 1543](https://code.google.com/p/robotframework/issues/detail?id=1543))
  * Consider string 'false' as Boolean False ([issue 1560](https://code.google.com/p/robotframework/issues/detail?id=1560))

### Enhancements to `Telnet` library ###

  * Terminal emulation support ([issue 1574](https://code.google.com/p/robotframework/issues/detail?id=1574))
  * Negotiate window size ([issue 1571](https://code.google.com/p/robotframework/issues/detail?id=1571))
  * Negotiate terminal type ([issue 1572](https://code.google.com/p/robotframework/issues/detail?id=1572))
  * Define USER environment variable ([issue 1573](https://code.google.com/p/robotframework/issues/detail?id=1573))
  * Include output in error message if no match found ([issue 1523](https://code.google.com/p/robotframework/issues/detail?id=1523))

## Backwards incompatible changes in 2.8.2 ##

Following three issues can potentially cause backwards-compatibility
issues, but the risk is extremely low:

  * String: Keyword `Split String From Right` reverses string but not separator ([issue 1553](https://code.google.com/p/robotframework/issues/detail?id=1553))
  * Process: `Terminate Process` should automatically kill process that does not terminate ([issue 1541](https://code.google.com/p/robotframework/issues/detail?id=1541))
  * Invalid values for `--RemoveKeywords` option should fail execution and not be skipped ([issue 1520](https://code.google.com/p/robotframework/issues/detail?id=1520))

## Acknowledgements in 2.8.2 ##

Big thanks for the following contributors for really nice
enhancements. Thanks also everyone else who has reported issues or
otherwise helped with the project.

  * Asko Soukka and Vivek Kumar Verma:  New plain text reStructuredText parser ([issue 1495](https://code.google.com/p/robotframework/issues/detail?id=1495))
  * Stefan Zimmermann: `**kwargs` support for dynamic test libraries ([issue 1500](https://code.google.com/p/robotframework/issues/detail?id=1500))
  * Mirel Pehadzic and Diogo Sa-Chaves De Oliveira:  Terminal emulation support for Telnet library ([issue 1574](https://code.google.com/p/robotframework/issues/detail?id=1574))

These and earlier contributors are also listed in
[AUTHORS.txt](http://code.google.com/p/robotframework/source/browse/AUTHORS.txt) file
added to the project repository ([issue 1585](https://code.google.com/p/robotframework/issues/detail?id=1585)). Please let us know if
contributors are missing from the file.

## Full list of fixes and enhancements in 2.8.2 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1505](https://code.google.com/p/robotframework/issues/detail?id=1505) | Defect   | High         | Logging callable that returns non-string corrupts output file |
| [Issue 1511](https://code.google.com/p/robotframework/issues/detail?id=1511) | Defect   | High         | Dryrun mode does not validate named args or kwargs correctly |
| [Issue 1549](https://code.google.com/p/robotframework/issues/detail?id=1549) | Defect   | High         | Log and report break if `</script>` is logged as HTML |
| [Issue 1454](https://code.google.com/p/robotframework/issues/detail?id=1454) | Enhancement | High         | Possibility to use keyword with embedded arguments as template |
| [Issue 1480](https://code.google.com/p/robotframework/issues/detail?id=1480) | Enhancement | High         | Support removing named keywords with `--RemoveKeywords` |
| [Issue 1490](https://code.google.com/p/robotframework/issues/detail?id=1490) | Enhancement | High         | Process: `Get Process Result` keyword to support getting results over remote interface |
| [Issue 1495](https://code.google.com/p/robotframework/issues/detail?id=1495) | Enhancement | High         | Add plain text syntax support into reStructuredText parser |
| [Issue 1500](https://code.google.com/p/robotframework/issues/detail?id=1500) | Enhancement | High         | `**kwargs` support for dynamic test libraries |
| [Issue 1524](https://code.google.com/p/robotframework/issues/detail?id=1524) | Enhancement | High         | Support for creating characters using `\xhh`, `\uhhhh` and `\Uhhhhhhhh` escapes in test data |
| [Issue 1551](https://code.google.com/p/robotframework/issues/detail?id=1551) | Enhancement | High         | Support flattening deeply nested keyword structures memory efficiently with `--FlattenKeywords` |
| [Issue 1574](https://code.google.com/p/robotframework/issues/detail?id=1574) | Enhancement | High         | Telnet: Terminal emulation support |
| [Issue 1588](https://code.google.com/p/robotframework/issues/detail?id=1588) | Enhancement | High         | BuiltIn: New `Run Keyword And Return` and `Run Keyword And Return If` keywords |
| [Issue 1585](https://code.google.com/p/robotframework/issues/detail?id=1585) | Documentation | High         | Add AUTHORS.txt file with contributor names to repository |
| [Issue 1479](https://code.google.com/p/robotframework/issues/detail?id=1479) | Defect   | Medium       | Collections: Should not use `has_key` because generic mappings do not have it |
| [Issue 1488](https://code.google.com/p/robotframework/issues/detail?id=1488) | Defect   | Medium       | Support variables in library name given using WITH NAME syntax |
| [Issue 1494](https://code.google.com/p/robotframework/issues/detail?id=1494) | Defect   | Medium       | Ampersand is escaped in tag stat link |
| [Issue 1502](https://code.google.com/p/robotframework/issues/detail?id=1502) | Defect   | Medium       | `OperatingSystem.Copy File` sometimes fails when destination is removed during operation |
| [Issue 1504](https://code.google.com/p/robotframework/issues/detail?id=1504) | Defect   | Medium       | Links to log do not work correctly when there are many and/or big errors |
| [Issue 1513](https://code.google.com/p/robotframework/issues/detail?id=1513) | Defect   | Medium       | Suite related automatic variables (`${SUITE NAME}`, etc.) are not available at import time anymore |
| [Issue 1525](https://code.google.com/p/robotframework/issues/detail?id=1525) | Defect   | Medium       | Confusing error message when same argument passed to keyword as positional and named argument |
| [Issue 1538](https://code.google.com/p/robotframework/issues/detail?id=1538) | Defect   | Medium       | `Set Test Message` does not override test message on failed test |
| [Issue 1553](https://code.google.com/p/robotframework/issues/detail?id=1553) | Defect   | Medium       | String: Keyword `Split String From Right` reverses string but not separator |
| [Issue 1562](https://code.google.com/p/robotframework/issues/detail?id=1562) | Defect   | Medium       | `OperatingSystem.Grep File` should not read whole file into memory |
| [Issue 1568](https://code.google.com/p/robotframework/issues/detail?id=1568) | Defect   | Medium       | Logging non-ASCII to STDERR fails |
| [Issue 1403](https://code.google.com/p/robotframework/issues/detail?id=1403) | Enhancement | Medium       | Logs: Permalinks to a suite, test, or keyword |
| [Issue 1481](https://code.google.com/p/robotframework/issues/detail?id=1481) | Enhancement | Medium       | Process: Add timeout and option to terminate process to `Wait For Process` keyword |
| [Issue 1491](https://code.google.com/p/robotframework/issues/detail?id=1491) | Enhancement | Medium       | Add `Remove String` and `Remove String Using Regexp` keywords to `String` library |
| [Issue 1515](https://code.google.com/p/robotframework/issues/detail?id=1515) | Enhancement | Medium       | Process: `Send Signal To Process` keyword |
| [Issue 1523](https://code.google.com/p/robotframework/issues/detail?id=1523) | Enhancement | Medium       | Telnet: Include output in error message if no match found |
| [Issue 1530](https://code.google.com/p/robotframework/issues/detail?id=1530) | Enhancement | Medium       | Add timestamps to debugfile |
| [Issue 1534](https://code.google.com/p/robotframework/issues/detail?id=1534) | Enhancement | Medium       | `BuiltIn`: Support logging to console using `Log` and new `Log To Console` keywords |
| [Issue 1541](https://code.google.com/p/robotframework/issues/detail?id=1541) | Enhancement | Medium       | Process: `Terminate Process` should automatically kill process that does not terminate |
| [Issue 1542](https://code.google.com/p/robotframework/issues/detail?id=1542) | Enhancement | Medium       | Process: `Terminate All Processes` should terminate, not kill, processes by default |
| [Issue 1547](https://code.google.com/p/robotframework/issues/detail?id=1547) | Enhancement | Medium       | Support table headers cells (`<th>`) in documentation syntax |
| [Issue 1564](https://code.google.com/p/robotframework/issues/detail?id=1564) | Enhancement | Medium       | `OperatingSystem.Move File/Directory` should not use `Copy File/Directory` internally for performance reasons |
| [Issue 1566](https://code.google.com/p/robotframework/issues/detail?id=1566) | Enhancement | Medium       | `ROBOT_OPTIONS` and `REBOT_OPTIONS` environment variables for setting default command line options |
| [Issue 1571](https://code.google.com/p/robotframework/issues/detail?id=1571) | Enhancement | Medium       | Telnet library: Negotiate window size |
| [Issue 1572](https://code.google.com/p/robotframework/issues/detail?id=1572) | Enhancement | Medium       | Telnet library: Negotiate terminal type |
| [Issue 1573](https://code.google.com/p/robotframework/issues/detail?id=1573) | Enhancement | Medium       | Telnet library: Define USER environment variable |
| [Issue 1579](https://code.google.com/p/robotframework/issues/detail?id=1579) | Enhancement | Medium       | Better encoding detection on Windows |
| [Issue 1581](https://code.google.com/p/robotframework/issues/detail?id=1581) | Enhancement | Medium       | `Convert To Bytes` keyword for creating byte strings from text, integers, etc. |
| [Issue 1401](https://code.google.com/p/robotframework/issues/detail?id=1401) | Defect   | Low          | Variable files from command line not searched from PYTHONPATH |
| [Issue 1526](https://code.google.com/p/robotframework/issues/detail?id=1526) | Defect   | Low          | Characters outside the Unicode Basic Multilingual Plane are not shown correctly in outputs |
| [Issue 1575](https://code.google.com/p/robotframework/issues/detail?id=1575) | Defect   | Low          | Messages printed in Java are lost if keyword prints also in Python |
| [Issue 1576](https://code.google.com/p/robotframework/issues/detail?id=1576) | Defect   | Low          | `Run Keywords` does not handle `Pass Execution` correctly |
| [Issue 1580](https://code.google.com/p/robotframework/issues/detail?id=1580) | Defect   | Low          | On IronPython opening argument files starting with BOM and containing non-ASCII characters fails |
| [Issue 1484](https://code.google.com/p/robotframework/issues/detail?id=1484) | Enhancement | Low          | Add support for `setuptools` development mode |
| [Issue 1520](https://code.google.com/p/robotframework/issues/detail?id=1520) | Enhancement | Low          | Invalid values for `--RemoveKeywords` option should fail execution and not be skipped |
| [Issue 1543](https://code.google.com/p/robotframework/issues/detail?id=1543) | Enhancement | Low          | Process: `Terminate Process` should return result object |
| [Issue 1552](https://code.google.com/p/robotframework/issues/detail?id=1552) | Enhancement | Low          | `BuiltIn.Log`: Support logging messages as HTML regardless the log level |
| [Issue 1554](https://code.google.com/p/robotframework/issues/detail?id=1554) | Enhancement | Low          | `Libdoc`: Make it easier to find correct shortcut by highlighting their first letter |
| [Issue 1555](https://code.google.com/p/robotframework/issues/detail?id=1555) | Enhancement | Low          | Support writing to `stderr` with `robot.api.logger.console` method |
| [Issue 1560](https://code.google.com/p/robotframework/issues/detail?id=1560) | Enhancement | Low          | `Process` library: Consider string 'false' as Boolean False |
| [Issue 1584](https://code.google.com/p/robotframework/issues/detail?id=1584) | Enhancement | Low          | `BuiltIn.Log`: Support logging `repr` of the given item |
| [Issue 1483](https://code.google.com/p/robotframework/issues/detail?id=1483) | Documentation | Low          | Enhance visitor interface documentation in the Robot API doc |
| [Issue 1489](https://code.google.com/p/robotframework/issues/detail?id=1489) | Documentation | Low          | Document that remote library interface supports only standard XML-RPC and no extensions |
| [Issue 1507](https://code.google.com/p/robotframework/issues/detail?id=1507) | Documentation | Low          | Libdoc tool documentation should contain example and notes about javalibrary with package |
| [Issue 1508](https://code.google.com/p/robotframework/issues/detail?id=1508) | Documentation | Low          | Document that test libraries with global scope imported with different arguments do not share a same instance |
| [Issue 1531](https://code.google.com/p/robotframework/issues/detail?id=1531) | Documentation | Low          | Document that running acceptance tests requires Python 2.6 or newer |
| [Issue 1544](https://code.google.com/p/robotframework/issues/detail?id=1544) | Documentation | Low          | User Guide: Syntax highlight plain text test data examples |

Altogether 60 issues.

# Robot Framework 2.8.3 #

Robot Framework 2.8.3 fixes several nasty regressions in the
[2.8.2 release](#Robot_Framework_2.8.2.md).
Its main enhancement is extending `**kwargs` support to static
Java libraries ([issue 1583](https://code.google.com/p/robotframework/issues/detail?id=1583)) and to the
[remote library interface](RemoteLibrary.md) ([issue 1596](https://code.google.com/p/robotframework/issues/detail?id=1596)).

Robot Framework 2.8.3 was released on Tuesday 3rd of December, 2013.

**NOTE:** Due to Google Code [deprecating downloads](http://google-opensource.blogspot.fi/2013/05/a-change-to-google-code-download-service.html), installers have been moved to https://pypi.python.org/pypi/robotframework/. Running `pip install robotframework` or `pip install --upgrade robotframework` works exactly like earlier.

## Acknowledgements in 2.8.3 ##

Thanks Stefan Zimmermann for contributing `**kwargs` support for Java
libraries ([issue 1583](https://code.google.com/p/robotframework/issues/detail?id=1583)) and `*varargs` support using `java.util.List`
([issue 1586](https://code.google.com/p/robotframework/issues/detail?id=1586)). Big thanks also for everyone reporting issues in RF
2.8.2 and enabling us to create a bug fix release soon.

## Full list of fixes and enhancements in 2.8.3 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1591](https://code.google.com/p/robotframework/issues/detail?id=1591) | Defect   | Critical     | robotframework-2.8.2.jar is totally broken |
| [Issue 1589](https://code.google.com/p/robotframework/issues/detail?id=1589) | Defect   | High         | Dry-run mode does not work with Java libraries |
| [Issue 1600](https://code.google.com/p/robotframework/issues/detail?id=1600) | Defect   | High         | `OperatingSystem.Copy File` fails if destination is directory and it contains file with same name |
| [Issue 1583](https://code.google.com/p/robotframework/issues/detail?id=1583) | Enhancement | High         | `**kwargs` support for static Java test libraries |
| [Issue 1596](https://code.google.com/p/robotframework/issues/detail?id=1596) | Enhancement | High         | `**kwargs` support for remote library interface |
| [Issue 1592](https://code.google.com/p/robotframework/issues/detail?id=1592) | Defect   | Medium       | Java keyword argument coercion should be disabled in dry-run when arguments contain variables |
| [Issue 1597](https://code.google.com/p/robotframework/issues/detail?id=1597) | Defect   | Medium       | Remote library does not support generic mappings or lists |
| [Issue 1586](https://code.google.com/p/robotframework/issues/detail?id=1586) | Enhancement | Medium       | Support `java.util.List` arguments for `*varargs` |
| [Issue 1598](https://code.google.com/p/robotframework/issues/detail?id=1598) | Defect   | Low          | Dynamic variable files cannot return variables in generic mapping |
| [Issue 1601](https://code.google.com/p/robotframework/issues/detail?id=1601) | Defect   | Low          | Libdoc marks all Java arrays as `*varargs` |

Altogether 10 issues.

# Robot Framework 2.8.4 #

Robot Framework 2.8.4 is yet another not-so-minor minor release. The
most visible change is the new search functionality in reports ([issue 1634](https://code.google.com/p/robotframework/issues/detail?id=1634))
that allows complex search operations based on tags as well as
suite and test names. See the full list of issues below for other
higher and lower priority fixes and enhancements.

Robot Framework 2.8.4 was released on Friday 7th of February, 2014.

**NOTE:** Due to Google Code
[deprecating downloads](http://google-opensource.blogspot.fi/2013/05/a-change-to-google-code-download-service.html),
installers have been moved to https://pypi.python.org/pypi/robotframework/. Running `pip install robotframework` or `pip install --upgrade robotframework` works exactly like earlier.
Also [User Guide](UserGuide.md) version 2.8.4 must be downloaded from a [temporary location](http://bit.ly/RF_UG_284).

## Backwards incompatible changes in 2.8.4 ##

Following changes may cause backwards compatibility problems.  Study
the linked issues more closely if you suspect that the changes affect
you.

  * Changes to configuring console output with `TestSuite.run` method ([issue 1605](https://code.google.com/p/robotframework/issues/detail?id=1605)).
  * New argument to Python remote server ([issue 1627](https://code.google.com/p/robotframework/issues/detail?id=1627)).
  * Changes to importing classes from sub modules as libraries ([issue 1614](https://code.google.com/p/robotframework/issues/detail?id=1614)).
  * New `OR` operator in tag patterns ([issue 1558](https://code.google.com/p/robotframework/issues/detail?id=1558)) changes meaning of, for example, `--include CORE`. This can be avoided by using lower-case patterns like `--include core`.

## Full list of fixes and enhancements in 2.8.4 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1634](https://code.google.com/p/robotframework/issues/detail?id=1634) | Enhancement | Critical     | Possibility to search tests by tag and suite names in report |
| [Issue 1614](https://code.google.com/p/robotframework/issues/detail?id=1614) | Defect   | High         | Dropping class name from library imports does not work with submodules |
| [Issue 1632](https://code.google.com/p/robotframework/issues/detail?id=1632) | Defect   | High         | --suite option doesn't work when dot in filename and running folder |
| [Issue 1615](https://code.google.com/p/robotframework/issues/detail?id=1615) | Enhancement | High         | Support merging re-run results with Rebot |
| [Issue 1628](https://code.google.com/p/robotframework/issues/detail?id=1628) | Enhancement | High         | Remote interface does not support reporting continuable and fatal errors |
| [Issue 1605](https://code.google.com/p/robotframework/issues/detail?id=1605) | Defect   | Medium       | Not possible to configure console output when using `TestSuite.run` method |
| [Issue 1606](https://code.google.com/p/robotframework/issues/detail?id=1606) | Defect   | Medium       | Remote interface does not support binary data |
| [Issue 1607](https://code.google.com/p/robotframework/issues/detail?id=1607) | Defect   | Medium       | Remote library should use `127.0.0.1`, not `localhost`, as default address to avoid potentially slow name resolution |
| [Issue 1617](https://code.google.com/p/robotframework/issues/detail?id=1617) | Defect   | Medium       | Original signal handlers should be reset after test execution |
| [Issue 1626](https://code.google.com/p/robotframework/issues/detail?id=1626) | Defect   | Medium       | Processing logged output fails if both Unicode and non-ASCII bytes are logged |
| [Issue 1627](https://code.google.com/p/robotframework/issues/detail?id=1627) | Defect   | Medium       | Various fixes and enhancements to Python remote server |
| [Issue 1631](https://code.google.com/p/robotframework/issues/detail?id=1631) | Defect   | Medium       | `Continue/Exit For Loop` silences continuable failures |
| [Issue 1638](https://code.google.com/p/robotframework/issues/detail?id=1638) | Defect   | Medium       | Process library does not support non-ASCII arguments or output with Jython |
| [Issue 1640](https://code.google.com/p/robotframework/issues/detail?id=1640) | Defect   | Medium       | Process: Reading output from custom streams sometimes fails with Jython on Windows |
| [Issue 1650](https://code.google.com/p/robotframework/issues/detail?id=1650) | Defect   | Medium       | Log message timestamps are wrong in debug file |
| [Issue 1558](https://code.google.com/p/robotframework/issues/detail?id=1558) | Enhancement | Medium       | Support `OR` operator with tag patterns |
| [Issue 1613](https://code.google.com/p/robotframework/issues/detail?id=1613) | Enhancement | Medium       | `OperatingSystem`: New `Move/Copy Files` keywords for moving/copying multiple files (incl. wildcard support) |
| [Issue 1620](https://code.google.com/p/robotframework/issues/detail?id=1620) | Enhancement | Medium       | `Dialogs.Get Value From User`: Extend to allow secret input |
| [Issue 1622](https://code.google.com/p/robotframework/issues/detail?id=1622) | Enhancement | Medium       | `BuiltIn.Evaluate`: Support for custom namespace |
| [Issue 1637](https://code.google.com/p/robotframework/issues/detail?id=1637) | Enhancement | Medium       | Process: Add timeout support for `Run Process` keyword |
| [Issue 1639](https://code.google.com/p/robotframework/issues/detail?id=1639) | Enhancement | Medium       | `OperatingSystem`: Add wildcard support to `Move/Copy File` keywords to move/copy a file without knowing its full name |
| [Issue 1643](https://code.google.com/p/robotframework/issues/detail?id=1643) | Enhancement | Medium       | Faster finding of failed tests with `--rerunfailed` |
| [Issue 1646](https://code.google.com/p/robotframework/issues/detail?id=1646) | Defect   | Low          | Report background color sometimes leaks through tables |
| [Issue 1652](https://code.google.com/p/robotframework/issues/detail?id=1652) | Defect   | Low          | String library: Typo in `Remove String` example |
| [Issue 1618](https://code.google.com/p/robotframework/issues/detail?id=1618) | Enhancement | Low          | `ArgumentParser` enhancements to improve programmatic RF execution |
| [Issue 1636](https://code.google.com/p/robotframework/issues/detail?id=1636) | Enhancement | Low          | `OperatingSystem`: New `Append To Environment Variable` keyword |
| [Issue 1641](https://code.google.com/p/robotframework/issues/detail?id=1641) | Enhancement | Low          | Rename `--runfailed` to `--rerunfailed` |

Altogether 27 issues.

# Robot Framework 2.8.5 #

Robot Framework 2.8.5 is again not-so-minor minor release. Hopefully the last one
before we start 2.9 and move the project away from Google Code.

The most important new features are the new library for date/time conversion
([issue 415](https://code.google.com/p/robotframework/issues/detail?id=415)) and the possibility for libraries to automatically register a
listener ([issue 811](https://code.google.com/p/robotframework/issues/detail?id=811)). The logs now allow the user to select messages
fully to ease copying them ([issue 1689](https://code.google.com/p/robotframework/issues/detail?id=1689)), XMLLibrary also has better xpath support
via [lxml](http://lxml.de) ([issue 1623](https://code.google.com/p/robotframework/issues/detail?id=1623)), and `--randomize` option allows
reproducing earlier execution orders ([issue 1673](https://code.google.com/p/robotframework/issues/detail?id=1673)).

Many thanks to Lionel Perrin for contributing giving custom seed to --randomize
([issue 1673](https://code.google.com/p/robotframework/issues/detail?id=1673)) and Michael Walle for providing Write Control Character keyword to
Telnet library ([issue 1729](https://code.google.com/p/robotframework/issues/detail?id=1729)).

Robot Framework 2.8.5 was released on Tuesday 17th of June, 2014.

**NOTE:** Due to Google Code
[deprecating downloads](http://google-opensource.blogspot.fi/2013/05/a-change-to-google-code-download-service.html),
installers have been moved to https://pypi.python.org/pypi/robotframework/. Running `pip install robotframework` or `pip install --upgrade robotframework` works exactly like earlier.
Also [User Guide](UserGuide.md) version 2.8.5 must be downloaded from a [temporary location](http://bit.ly/RF_UG_285).

## Full list of fixes and enhancements in 2.8.5 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 415](https://code.google.com/p/robotframework/issues/detail?id=415) | Enhancement | Critical     | Library for date/time conversion and calculation |
| [Issue 811](https://code.google.com/p/robotframework/issues/detail?id=811) | Enhancement | Critical     | Libraries should get notification when suites/tests/keywords start/end and when library is out of scope |
| [Issue 1665](https://code.google.com/p/robotframework/issues/detail?id=1665) | Defect   | High         | `Grep File` does not work with UTF-16 since RF 2.8.2 |
| [Issue 1675](https://code.google.com/p/robotframework/issues/detail?id=1675) | Defect   | High         | Process: `Terminate Process` and `Send Signal To Process` ignore child processes and processes running in shell |
| [Issue 1686](https://code.google.com/p/robotframework/issues/detail?id=1686) | Defect   | High         | Telnet terminal emulation is broken with pyte 0.4.8 |
| [Issue 1623](https://code.google.com/p/robotframework/issues/detail?id=1623) | Enhancement | High         | XML library: Support using lxml module to get better xpath support |
| [Issue 1673](https://code.google.com/p/robotframework/issues/detail?id=1673) | Enhancement | High         | `--randomize` option should give a way to reproduce the random execution order |
| [Issue 1689](https://code.google.com/p/robotframework/issues/detail?id=1689) | Enhancement | High         | Log: Allow selecting logged messages fully to ease copying them |
| [Issue 1656](https://code.google.com/p/robotframework/issues/detail?id=1656) | Defect   | Medium       | `Pass Execution` in suite teardown causes tests to be reported failed on console |
| [Issue 1661](https://code.google.com/p/robotframework/issues/detail?id=1661) | Defect   | Medium       | reST support: Too old docutils versions incorrectly reported as not being installed at all |
| [Issue 1670](https://code.google.com/p/robotframework/issues/detail?id=1670) | Defect   | Medium       | Executing `Run Keyword` variants in dry-run mode can fail if keyword name contains variable |
| [Issue 1678](https://code.google.com/p/robotframework/issues/detail?id=1678) | Defect   | Medium       | Libdoc: Links to keywords not percent encoded |
| [Issue 1684](https://code.google.com/p/robotframework/issues/detail?id=1684) | Defect   | Medium       | `Run Keyword And Return` does not escape return values correctly |
| [Issue 1688](https://code.google.com/p/robotframework/issues/detail?id=1688) | Defect   | Medium       | `Set Library Search Order` does not work in dry-run mode |
| [Issue 1700](https://code.google.com/p/robotframework/issues/detail?id=1700) | Defect   | Medium       | Process: Executed processes leave file handles open |
| [Issue 1704](https://code.google.com/p/robotframework/issues/detail?id=1704) | Defect   | Medium       | Libdoc: Creating documentation based on JavaDocs fails on Java 8 |
| [Issue 1655](https://code.google.com/p/robotframework/issues/detail?id=1655) | Enhancement | Medium       | OperatingSystem: Add encoding error handler to `Get File`, `Grep File' and `Log File` keywords |
| [Issue 1674](https://code.google.com/p/robotframework/issues/detail?id=1674) | Enhancement | Medium       | Support for creating `wheel` distributions |
| [Issue 1680](https://code.google.com/p/robotframework/issues/detail?id=1680) | Enhancement | Medium       | Python remote server: Include enhancements and fixes in 1.0.1 version |
| [Issue 1694](https://code.google.com/p/robotframework/issues/detail?id=1694) | Enhancement | Medium       | OperatingSystem: Support for creating binary files |
| [Issue 1715](https://code.google.com/p/robotframework/issues/detail?id=1715) | Enhancement | Medium       | Time format: Support 'timer' format 'hh:mm:ss.mil' |
| [Issue 1725](https://code.google.com/p/robotframework/issues/detail?id=1725) | Enhancement | Medium       | Add suite and test id to attributes passed to listeners |
| [Issue 1729](https://code.google.com/p/robotframework/issues/detail?id=1729) | Enhancement | Medium       | Add support for telnet commands in telnet library (esp break command) |
| [Issue 1730](https://code.google.com/p/robotframework/issues/detail?id=1730) | Enhancement | Medium       | Test with Jython 2.7 betas and fix/workaround possible problems |
| [Issue 1733](https://code.google.com/p/robotframework/issues/detail?id=1733) | Enhancement | Medium       | Support flattening for loops in generated outputs |
| [Issue 1679](https://code.google.com/p/robotframework/issues/detail?id=1679) | Documentation | Medium       | Process: Document that possible equal signs in process arguments need to be escaped |
| [Issue 1681](https://code.google.com/p/robotframework/issues/detail?id=1681) | Documentation | Medium       | Update remote library interface documentation to mention independent remote server projects |
| [Issue 1658](https://code.google.com/p/robotframework/issues/detail?id=1658) | Defect   | Low          | Report: Search using `&` and `%` fails on Firefox |
| [Issue 1720](https://code.google.com/p/robotframework/issues/detail?id=1720) | Defect   | Low          | Full suite and test names shown in log and report pop-ups are escaped |
| [Issue 1667](https://code.google.com/p/robotframework/issues/detail?id=1667) | Enhancement | Low          | Improve error message when BuiltIn keywords are called outside an execution |
| [Issue 1671](https://code.google.com/p/robotframework/issues/detail?id=1671) | Enhancement | Low          | Process: `Send Signal To Process` should log signal it sends |
| [Issue 1690](https://code.google.com/p/robotframework/issues/detail?id=1690) | Enhancement | Low          | XML library: Document that sources given as strings are not modified in place |
| [Issue 1677](https://code.google.com/p/robotframework/issues/detail?id=1677) | Documentation | Low          | Document that `Wait Until Keyword Succeeds` returns return value of executed keyword on success |
| [Issue 1682](https://code.google.com/p/robotframework/issues/detail?id=1682) | Documentation | Low          | Remote interface: Document that `stop_remote_server` should return True/False depending was server stopped or not |
| [Issue 1693](https://code.google.com/p/robotframework/issues/detail?id=1693) | Documentation | Low          | Remote: Document that URI without path gets '/RPC2' appended |
| [Issue 1695](https://code.google.com/p/robotframework/issues/detail?id=1695) | Documentation | Low          | Remove information about already removed keywords from Screenshot library documentation |
| [Issue 1719](https://code.google.com/p/robotframework/issues/detail?id=1719) | Documentation | Low          | User Guide: Explain settings variables using return values better |
| [Issue 1722](https://code.google.com/p/robotframework/issues/detail?id=1722) | Documentation | Low          | User Guide: Explain that variables in variables from variable files are not resolved |

Altogether 38 issues.