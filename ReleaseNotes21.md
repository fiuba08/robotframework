

# Robot Framework 2.1 #

Robot Framework 2.1 was released on Monday 2009-04-20 and it is the
first major release after the framework was open sourced in June
2008. It has plenty of new functionality, like a possibility to have
test data in [reStructuredText](http://docutils.sourceforge.net/rst.html)
format, and it also has three new standard libraries
[Remote](RemoteLibrary.md), [String](StringLibrary.md) and [Dialogs](DialogsLibrary.md).
Especially the Remote library is really interesting because
it provides possibilities for distributed testing and creating test
libraries using other languages than the natively supported Python and
Java. A full list of new features and fixed bugs can be found below.

Installers and other packages can be downloaded from the
[download page](http://code.google.com/p/robotframework/downloads/list).
See [installation instructions](Installation.md) for installation
and upgrading information. Questions and comments related to the
release can be sent to the [mailing lists](MailingLists.md) and possible
bugs submitted to
the [issue tracker](http://code.google.com/p/robotframework/issues).

## Backwards incompatible changes in 2.1 ##

Robot Framework 2.1 has some external changes and plenty of internal
refactorings. For example earlier RobotIDE and Mabot releases are not
compatible with RF 2.1, but compatible releases are in development.

[RIDE 0.14](http://code.google.com/p/robotframework-ride/) and [Mabot 0.6](http://code.google.com/p/robotframework-mabot/) and later are compatible with RF 2.1

Changes possibly affecting external tools or how test case are executed:

  * Information about critical tags is not stored in output XML ([issue 146](https://code.google.com/p/robotframework/issues/detail?id=146))
  * Tags are not normalized ([issue 182](https://code.google.com/p/robotframework/issues/detail?id=182))
  * Internal logging is changed ([issue 254](https://code.google.com/p/robotframework/issues/detail?id=254))
  * Helper classes in `BuiltIn` module renamed (e.g. `Converter` -> `_Converter`) ([issue 281](https://code.google.com/p/robotframework/issues/detail?id=281))
  * `mediumname` attribute removed from internal `TestCase` and `TestSuite` objects ([issue 279](https://code.google.com/p/robotframework/issues/detail?id=279))
  * Using test data with URLs is not possible anymore ([issue 123](https://code.google.com/p/robotframework/issues/detail?id=123))

Deprecated keywords and arguments to keywords:

  * `mode` argument of `Create File` keyword ([issue 217](https://code.google.com/p/robotframework/issues/detail?id=217))
  * `pattern_type` argument of `Grep File` and `List Directory` keywords ([issue 257](https://code.google.com/p/robotframework/issues/detail?id=257), [issue 259](https://code.google.com/p/robotframework/issues/detail?id=259))
  * `Set Variable` keyword with more/less than one value ([issue 262](https://code.google.com/p/robotframework/issues/detail?id=262)) - this was reverted in RF 2.1.2 ([issue 422](https://code.google.com/p/robotframework/issues/detail?id=422))
  * `Syslog` keyword ([issue 270](https://code.google.com/p/robotframework/issues/detail?id=270))
  * `return_mode` argument of `Run` keyword ([issue 282](https://code.google.com/p/robotframework/issues/detail?id=282))
  * `Grep` keyword ([issue 285](https://code.google.com/p/robotframework/issues/detail?id=285))

## Acknowledgements ##

Big thanks for everyone who have submitted bugs and enhancement requests to
the [issue tracker](http://code.google.com/p/robotframework/issues) and also for
those who tested the beta release. Special thanks go to Chirs Prinos
for initial implementation and documentation for reStructuredText
support ([issue 231](https://code.google.com/p/robotframework/issues/detail?id=231)) and to Marcin Michalak who was the driving force
behind the String library ([issue 18](https://code.google.com/p/robotframework/issues/detail?id=18)).

## List of fixes and enhancements in 2.1 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 241](https://code.google.com/p/robotframework/issues/detail?id=241) | Defect   | Critical     | Numerical Unicode character references in HTML data are ignored |
| [Issue 18](https://code.google.com/p/robotframework/issues/detail?id=18) | Library  | Critical     | New standard library `String` for different string operations |
| [Issue 118](https://code.google.com/p/robotframework/issues/detail?id=118) | Library  | Critical     | Remote library |
| [Issue 254](https://code.google.com/p/robotframework/issues/detail?id=254) | Refactoring | Critical     | Centralized internal logger (no more passing `syslog` around) |
| [Issue 28](https://code.google.com/p/robotframework/issues/detail?id=28) | Defect   | High         | Tests and suites don't have unique link targets in log files |
| [Issue 275](https://code.google.com/p/robotframework/issues/detail?id=275) | Defect   | High         | Using varargs in Java keywords fails with libraries imported using `WITH NAME` syntax |
| [Issue 2](https://code.google.com/p/robotframework/issues/detail?id=2) | Enhancement | High         | Show source where test suite data originated in log |
| [Issue 146](https://code.google.com/p/robotframework/issues/detail?id=146) | Enhancement | High         | Don't store information related to critical tags and filtered tests to XML outputs |
| [Issue 182](https://code.google.com/p/robotframework/issues/detail?id=182) | Enhancement | High         | Tags should not be normalized |
| [Issue 200](https://code.google.com/p/robotframework/issues/detail?id=200) | Enhancement | High         | Log messages with WARN level should be automatically shown in 'Execution Errors' section in log files |
| [Issue 203](https://code.google.com/p/robotframework/issues/detail?id=203) | Enhancement | High         | New keyword `Set Library Search Order` to ease handling keywords with same names |
| [Issue 231](https://code.google.com/p/robotframework/issues/detail?id=231) | Enhancement | High         | Support for test data in reStructuredText format |
| [Issue 245](https://code.google.com/p/robotframework/issues/detail?id=245) | Enhancement | High         | Automatic type conversion for Java keywords |
| [Issue 274](https://code.google.com/p/robotframework/issues/detail?id=274) | Enhancement | High         | Enhancements to how test and suite names are written in report (no more x.y.z.Name format) |
| [Issue 253](https://code.google.com/p/robotframework/issues/detail?id=253) | Library  | High         | New standard library for interactive dialogs |
| [Issue 213](https://code.google.com/p/robotframework/issues/detail?id=213) | Defect   | Medium       | Telnet library does not properly handle received control characters |
| [Issue 224](https://code.google.com/p/robotframework/issues/detail?id=224) | Defect   | Medium       | `libdoc.py` does not work with Unicode characters |
| [Issue 230](https://code.google.com/p/robotframework/issues/detail?id=230) | Defect   | Medium       | --argumentfile option should be accepted multiple times |
| [Issue 234](https://code.google.com/p/robotframework/issues/detail?id=234) | Defect   | Medium       | Installation using install.py fails if Python is installed into a path with spaces |
| [Issue 244](https://code.google.com/p/robotframework/issues/detail?id=244) | Defect   | Medium       | Test case criticality is not updated after using `Set Tags` or `Remove Tags` keywords |
| [Issue 250](https://code.google.com/p/robotframework/issues/detail?id=250) | Defect   | Medium       | libdoc.py and testdoc.py should not evaluate ${CURDIR} variable |
| [Issue 252](https://code.google.com/p/robotframework/issues/detail?id=252) | Defect   | Medium       | Library implemented as a module cannot have a function or other attribute with the same name as the module |
| [Issue 267](https://code.google.com/p/robotframework/issues/detail?id=267) | Defect   | Medium       | robotidy.py recursive mode does not work with directories containing other than html and tsv files |
| [Issue 88](https://code.google.com/p/robotframework/issues/detail?id=88) | Enhancement | Medium       | Listener interface methods need more information about suites, tests and keywords |
| [Issue 89](https://code.google.com/p/robotframework/issues/detail?id=89) | Enhancement | Medium       | Possibility to specify test suite execution order with non-visible prefixes |
| [Issue 123](https://code.google.com/p/robotframework/issues/detail?id=123) | Enhancement | Medium       | Remove code related to using test data with URLs |
| [Issue 214](https://code.google.com/p/robotframework/issues/detail?id=214) | Enhancement | Medium       | New builtin variable ${EXECDIR} |
| [Issue 217](https://code.google.com/p/robotframework/issues/detail?id=217) | Enhancement | Medium       | Deprecate `Create File` keyword's `mode` argument in favor of `encoding` |
| [Issue 239](https://code.google.com/p/robotframework/issues/detail?id=239) | Enhancement | Medium       | All `OperatingSystem` keywords handling paths should create links to affected files/dirs in the log file |
| [Issue 248](https://code.google.com/p/robotframework/issues/detail?id=248) | Enhancement | Medium       | Top level documentation in resource files |
| [Issue 257](https://code.google.com/p/robotframework/issues/detail?id=257) | Enhancement | Medium       | Deprecate `pattern_type` argument of `Grep File` keyword |
| [Issue 259](https://code.google.com/p/robotframework/issues/detail?id=259) | Enhancement | Medium       | Deprecate `pattern_type` argument of `List Directory` keywords |
| [Issue 262](https://code.google.com/p/robotframework/issues/detail?id=262) | Enhancement | Medium       | Deprecate using Set Variable keyword with more/less than one value |
| [Issue 264](https://code.google.com/p/robotframework/issues/detail?id=264) | Enhancement | Medium       | Keyword `Comment` should not resolve variables |
| [Issue 268](https://code.google.com/p/robotframework/issues/detail?id=268) | Enhancement | Medium       | Non-existing variables in suite, test and keyword documentations should not cause errors |
| [Issue 277](https://code.google.com/p/robotframework/issues/detail?id=277) | Enhancement | Medium       | New keywords `Get Count` and `Should Contain X Times` to `BuiltIn` library  |
| [Issue 284](https://code.google.com/p/robotframework/issues/detail?id=284) | Enhancement | Medium       | New `List Should Not Contain Duplicates` keyword to `Collections` library |
| [Issue 211](https://code.google.com/p/robotframework/issues/detail?id=211) | Documentation | Medium       | Need to document that TSV files are expected to have UTF-8 encoding |
| [Issue 52](https://code.google.com/p/robotframework/issues/detail?id=52) | Defect   | Low          | Running tests fails if a suite has name ending with a dot |
| [Issue 249](https://code.google.com/p/robotframework/issues/detail?id=249) | Defect   | Low          | libdoc.py requires double \n is resource files |
| [Issue 280](https://code.google.com/p/robotframework/issues/detail?id=280) | Defect   | Low          | It is not possible to set test/suite/global variable using an empty list variable as a value |
| [Issue 133](https://code.google.com/p/robotframework/issues/detail?id=133) | Enhancement | Low          | Change parsing time warning about having having tests with same name multiple times in a suite to run time warning |
| [Issue 197](https://code.google.com/p/robotframework/issues/detail?id=197) | Enhancement | Low          | Update `robotidy.py` tool to replace deprecated keyword repeating syntax with `Repeat Keyword` |
| [Issue 216](https://code.google.com/p/robotframework/issues/detail?id=216) | Enhancement | Low          | Remove the warning for empty init.html in directory suites |
| [Issue 240](https://code.google.com/p/robotframework/issues/detail?id=240) | Enhancement | Low          | `Evaluate` keyword should take an optional list of modules to add into the namespace of the evaluated expression |
| [Issue 255](https://code.google.com/p/robotframework/issues/detail?id=255) | Enhancement | Low          | New keyword `Append To File` to `OperatingSystem` library |
| [Issue 263](https://code.google.com/p/robotframework/issues/detail?id=263) | Enhancement | Low          | `Log Variables` keyword should log variable names using their original format |
| [Issue 270](https://code.google.com/p/robotframework/issues/detail?id=270) | Enhancement | Low          | Deprecate `Syslog` keyword |
| [Issue 278](https://code.google.com/p/robotframework/issues/detail?id=278) | Enhancement | Low          | `Set Test/Suite/Global Variable` and `Variable Should (Not) Exist` keywords work also when the variable name is given in normal format |
| [Issue 282](https://code.google.com/p/robotframework/issues/detail?id=282) | Enhancement | Low          | Deprecate `return_mode` argument of `Run` keyword |
| [Issue 285](https://code.google.com/p/robotframework/issues/detail?id=285) | Enhancement | Low          | Deprecate `BuiltIn` keyword `Grep` in favour of better keywords in `String` library |
| [Issue 167](https://code.google.com/p/robotframework/issues/detail?id=167) | Documentation | Low          | Document using `BuiltIn.replace_variables` as a public API for getting variables and settings to test libraries |
| [Issue 226](https://code.google.com/p/robotframework/issues/detail?id=226) | Documentation | Low          | Better explanation on how to install RF when using Jython |
| [Issue 283](https://code.google.com/p/robotframework/issues/detail?id=283) | Documentation | Low          | Enhancements to libraries' general documentation |
| [Issue 279](https://code.google.com/p/robotframework/issues/detail?id=279) | Refactoring | Low          | Remove `mediumname` attribute from internal `TestSuite` and `TestCase` objects |
| [Issue 281](https://code.google.com/p/robotframework/issues/detail?id=281) | Refactoring | Low          | Helper classes inside `BuiltIn` module renamed (e.g. `Converter` -> `_Converter`) because they are not part of the public API |

Altogether 56 issues.

# Robot Framework 2.1.1 #

Robot Framework 2.1.1 is a bug fix release with some smaller and bigger enhancements. Both of the major new features, embedding arguments to keyword names ([issue 370](https://code.google.com/p/robotframework/issues/detail?id=370)) and the plain text test data format ([issue 375](https://code.google.com/p/robotframework/issues/detail?id=375)), ease creating requirement-like test cases with sentence-like keywords such as `Given user selects book from list`. The biggest documentation enhancement is the new [Python Tutorial for Robot Framework Test Library Developers](PythonTutorial.md) ([issue 381](https://code.google.com/p/robotframework/issues/detail?id=381)).

Robot Framework 2.1.1 was released on Monday  2009-08-17. [Installation](Installation.md) packages can be found from the [download page](http://code.google.com/p/robotframework/downloads/list).

## Backwards incompatible changes in 2.1.1 ##

There should be no backwards incompatible changes in this release.

## List of fixes and enhancements in 2.1.1 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 300](https://code.google.com/p/robotframework/issues/detail?id=300) | Defect   | High         | `robotidy.py` cannot save to HTML and `libdoc.py` to XML |
| [Issue 306](https://code.google.com/p/robotframework/issues/detail?id=306) | Defect   | High         | `LOGGER.disable_automatic_console_logger` method raises exception |
| [Issue 311](https://code.google.com/p/robotframework/issues/detail?id=311) | Defect   | High         | Selecting test suites prefixed with execution order using `--suite` option fails |
| [Issue 314](https://code.google.com/p/robotframework/issues/detail?id=314) | Defect   | High         | Malformed test data crashes the whole test execution |
| [Issue 335](https://code.google.com/p/robotframework/issues/detail?id=335) | Defect   | High         | Top level suite name not included in lower level suite name in report/log when combining outputs |
| [Issue 348](https://code.google.com/p/robotframework/issues/detail?id=348) | Defect   | High         | `Set Test/Suite/Global Variable` and `Variable Should (Not) Exist` cannot be used in user keyword if variable is given as argument |
| [Issue 310](https://code.google.com/p/robotframework/issues/detail?id=310) | Enhancement | High         | `libdoc.py` should write library initialization and version information to XML |
| [Issue 370](https://code.google.com/p/robotframework/issues/detail?id=370) | Enhancement | High         | Possibility to embed arguments into keyword names (e.g. `When user selects ${item} from list`) |
| [Issue 375](https://code.google.com/p/robotframework/issues/detail?id=375) | Enhancement | High         | New plain text test data format |
| [Issue 305](https://code.google.com/p/robotframework/issues/detail?id=305) | Documentation | High         | Document that Python 3 is not supported |
| [Issue 261](https://code.google.com/p/robotframework/issues/detail?id=261) | Defect   | Medium       | Dialogs library cannot be used with Java Swing applications |
| [Issue 304](https://code.google.com/p/robotframework/issues/detail?id=304) | Defect   | Medium       | `robotidy.py` should change extension when format is changed and files edited inplace |
| [Issue 312](https://code.google.com/p/robotframework/issues/detail?id=312) | Defect   | Medium       | Executing a directory not containing tests fails for AttributeError |
| [Issue 315](https://code.google.com/p/robotframework/issues/detail?id=315) | Defect   | Medium       | `Set Global Variable` keyword does not update variables of parent suites |
| [Issue 320](https://code.google.com/p/robotframework/issues/detail?id=320) | Defect   | Medium       | `libdoc.py` doesn't unescape `\n` and `\t` in resource files' top-level documentation |
| [Issue 325](https://code.google.com/p/robotframework/issues/detail?id=325) | Defect   | Medium       | `libdoc.py` doesn't escape special characters in keyword name and documentation correctly |
| [Issue 333](https://code.google.com/p/robotframework/issues/detail?id=333) | Defect   | Medium       | Not removing XmlLogger from the global LOGGER after closing it causes an attempt to write to a closed file |
| [Issue 338](https://code.google.com/p/robotframework/issues/detail?id=338) | Defect   | Medium       | `--debugfile` option crashes pybot if test contains non-ASCII character |
| [Issue 347](https://code.google.com/p/robotframework/issues/detail?id=347) | Defect   | Medium       | Option `--TagStatLink` does not work with tags containing capital letters |
| [Issue 359](https://code.google.com/p/robotframework/issues/detail?id=359) | Defect   | Medium       | Using mutable objects (like lists and dictionaries) as arguments to test libraries fails |
| [Issue 372](https://code.google.com/p/robotframework/issues/detail?id=372) | Defect   | Medium       | Importing libraries fail if second last argument is not a string |
| [Issue 354](https://code.google.com/p/robotframework/issues/detail?id=354) | Enhancement | Medium       | `OperatingSystem.Set Environment Variable` should convert given values to strings automatically |
| [Issue 383](https://code.google.com/p/robotframework/issues/detail?id=383) | Enhancement | Medium       | Possibility to get also other than the current time with `Get Time` keyword |
| [Issue 299](https://code.google.com/p/robotframework/issues/detail?id=299) | Documentation | Medium       | Document that the One Click Installer works only on Windows XP |
| [Issue 303](https://code.google.com/p/robotframework/issues/detail?id=303) | Documentation | Medium       | Enhancements to Windows installation instructions |
| [Issue 381](https://code.google.com/p/robotframework/issues/detail?id=381) | Documentation | Medium       | Python basics tutorial |
| [Issue 382](https://code.google.com/p/robotframework/issues/detail?id=382) | Documentation | Medium       | Change content license to Creative Commons Attribution 3.0 Unported |
| [Issue 313](https://code.google.com/p/robotframework/issues/detail?id=313) | Defect   | Low          | Possible `"` in links created from URLs are not escaped |
| [Issue 328](https://code.google.com/p/robotframework/issues/detail?id=328) | Defect   | Low          | 'RUNNING' indication should be set before start\_suite and start\_test methods |
| [Issue 302](https://code.google.com/p/robotframework/issues/detail?id=302) | Documentation | Low          | Document that on Vista installers should be run with admin rights |
| [Issue 355](https://code.google.com/p/robotframework/issues/detail?id=355) | Documentation | Low          | Document that Python should be installed for 'All Users' on Windows |
| [Issue 373](https://code.google.com/p/robotframework/issues/detail?id=373) | Documentation | Low          | Document that reST format is converted to HTML first and errors in conversion are fatal |

Altogether 32 issues.


# Robot Framework 2.1.2 #

Robot Framework 2.1.2 contains mainly smallish bug fixes and
enhancements.  The most important new feature is making
[Given/When/Then/And prefixes optional in keyword names](http://robotframework.googlecode.com/svn/tags/robotframework-2.1.2/doc/userguide/RobotFrameworkUserGuide.html#behavior-driven-style) ([issue 409](https://code.google.com/p/robotframework/issues/detail?id=409))
to ease creating BDD style test cases, and the biggest documentation
enhancement is [an example of using the C language from test libraries](HowToUseC.md)
([issue 394](https://code.google.com/p/robotframework/issues/detail?id=394)).

Robot Framework 2.1.2 was released on Friday 2009-10-23.
[Installation](Installation.md) packages can be found from the
[download page](http://code.google.com/p/robotframework/downloads/list).

## Backwards incompatible changes in 2.1.2 ##

There should be no backwards incompatible changes in this release.

## List of fixes and enhancements in 2.1.2 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 413](https://code.google.com/p/robotframework/issues/detail?id=413) | Defect   | High         | When multiple variable files with the same name are used, extra variables might be imported |
| [Issue 409](https://code.google.com/p/robotframework/issues/detail?id=409) | Enhancement | High         | Possibility to implement BDD style keywords without `Given/When/Then/And` prefix |
| [Issue 416](https://code.google.com/p/robotframework/issues/detail?id=416) | Enhancement | High         | Enhance `libdoc.py` to enable uploading documentation to RFDoc  |
| [Issue 422](https://code.google.com/p/robotframework/issues/detail?id=422) | Enhancement | High         | Remove deprecation of using `BuiltIn.Set Variable` keyword with more/less than one value |
| [Issue 397](https://code.google.com/p/robotframework/issues/detail?id=397) | Defect   | Medium       | `Set Test/Suite/Global Variable` don't work anymore with names containing internal variables like `\${foo${bar}}` |
| [Issue 410](https://code.google.com/p/robotframework/issues/detail?id=410) | Defect   | Medium       | Command line arguments turned into lower case when using '--option=Value' format instead of '--option Value' |
| [Issue 411](https://code.google.com/p/robotframework/issues/detail?id=411) | Defect   | Medium       | Not possible to use variables inside a list variable |
| [Issue 407](https://code.google.com/p/robotframework/issues/detail?id=407) | Enhancement | Medium       | Don't show warning when importing libraries, resources or variables more than once |
| [Issue 412](https://code.google.com/p/robotframework/issues/detail?id=412) | Enhancement | Medium       | `Should Be Uppercase/Lowercase/Titlecase` keywords to String library |
| [Issue 414](https://code.google.com/p/robotframework/issues/detail?id=414) | Enhancement | Medium       | Keyword `Get selection from user` to Dialogs library  |
| [Issue 417](https://code.google.com/p/robotframework/issues/detail?id=417) | Enhancement | Medium       | Enable using old XML doc as input for `libdoc.py` |
| [Issue 418](https://code.google.com/p/robotframework/issues/detail?id=418) | Enhancement | Medium       | Convert tabs to spaces when parsing plain text format |
| [Issue 419](https://code.google.com/p/robotframework/issues/detail?id=419) | Enhancement | Medium       | Support for resource files in plain text and restructured text formats in `libdoc.py` tool |
| [Issue 394](https://code.google.com/p/robotframework/issues/detail?id=394) | Documentation | Medium       | Create example on how to call C code from test libraries |
| [Issue 387](https://code.google.com/p/robotframework/issues/detail?id=387) | Defect   | Low          | libdoc.py --name argument does not change the output file name with resource files |
| [Issue 420](https://code.google.com/p/robotframework/issues/detail?id=420) | Defect   | Low          | Not possible to escape first data cell with '\' and then continue line with '...' |
| [Issue 395](https://code.google.com/p/robotframework/issues/detail?id=395) | Enhancement | Low          | Plain text format support for robotidy.py |
| [Issue 396](https://code.google.com/p/robotframework/issues/detail?id=396) | Enhancement | Low          | Escape spaces in command line options given to unixy start-up scripts |

Altogether 18 issues.


# Robot Framework 2.1.3 #

Robot Framework 2.1.3 is (probably) the last release in the 2.1 series and
consequently it is the last version that supports Python 2.4 and Jython 2.2

2.1.3 contains mainly small bug fixes and enhancements, especially related to
unicode. Jython 2.5 support is also greatly improved. Additionally, a separate [tool](OutputFileFixingTool.md) for fixing broken output files was implemented.

In preparation for next major release, using parallel execution ([issue 491](https://code.google.com/p/robotframework/issues/detail?id=491)) or settings going to be removed from init files ([issue 478](https://code.google.com/p/robotframework/issues/detail?id=478)) now causes a deprecation warning.

Robot Framework 2.1.2 was released on Friday 2009-03-05.
[Installation](Installation.md) packages can be found from the
[download page](http://code.google.com/p/robotframework/downloads/list).

## Backwards incompatible changes in 2.1.3 ##

There should be no backwards incompatible changes in this release.

## Acknowledgements ##

Big thanks for everyone who have submitted bugs and enhancement requests to
the [issue tracker](http://code.google.com/p/robotframework/issues). Special thanks to Regis Desgroppes for providing a patch to fix [issue 434](https://code.google.com/p/robotframework/issues/detail?id=434)


## List of fixes and enhancements in 2.1.3 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 434](https://code.google.com/p/robotframework/issues/detail?id=434) | Defect   | High         | Incorrect paths in scripts when easy\_install'ing with Python 2.6 |
| [Issue 443](https://code.google.com/p/robotframework/issues/detail?id=443) | Defect   | High         | Test timeout occurring inside `Wait Until Keyword Succeeds` sometimes corrupts output file |
| [Issue 446](https://code.google.com/p/robotframework/issues/detail?id=446) | Defect   | High         | `Run` and `Start Process` keywords don't handle non-ASCII characters |
| [Issue 473](https://code.google.com/p/robotframework/issues/detail?id=473) | Defect   | High         | Logging Java objects whose toString() contains unicode fails with Jython 2.5. |
| [Issue 99](https://code.google.com/p/robotframework/issues/detail?id=99) | Enhancement | High         | Tool for fixing output XML |
| [Issue 478](https://code.google.com/p/robotframework/issues/detail?id=478) | Enhancement | High         | Deprecation warning for `Test Setup`, `Test Teardown`, `Default Tags` and `Test Timeout` in init files |
| [Issue 491](https://code.google.com/p/robotframework/issues/detail?id=491) | Enhancement | High         | Deprecate parallel execution of keywords (`:PARALLEL` ) because it doesn't work correctly and requires special syntax |
| [Issue 428](https://code.google.com/p/robotframework/issues/detail?id=428) | Defect   | Medium       | `Run Keyword` variants corrupt output file when given keyword name is not string |
| [Issue 454](https://code.google.com/p/robotframework/issues/detail?id=454) | Defect   | Medium       | It is not possible to use non-ascii character in test data path in Windows |
| [Issue 469](https://code.google.com/p/robotframework/issues/detail?id=469) | Defect   | Medium       | Java argument type coercion does not work with Jython 2.5 |
| [Issue 471](https://code.google.com/p/robotframework/issues/detail?id=471) | Defect   | Medium       | Replace all unsafe calls of `str()` with `unicode()` or `utils.unic()` |
| [Issue 438](https://code.google.com/p/robotframework/issues/detail?id=438) | Enhancement | Medium       | Use a relative reference to the original data source in the log file |
| [Issue 460](https://code.google.com/p/robotframework/issues/detail?id=460) | Enhancement | Medium       | `Wait Until Keyword Succeeds` should report the last error message when it fails |
| [Issue 465](https://code.google.com/p/robotframework/issues/detail?id=465) | Enhancement | Medium       | `Get Variables` keyword |
| [Issue 466](https://code.google.com/p/robotframework/issues/detail?id=466) | Enhancement | Medium       | Provide messages from libraries and RF to listener |
| [Issue 493](https://code.google.com/p/robotframework/issues/detail?id=493) | Enhancement | Medium       | No traceback available in syslog when reading data from XML fails |
| [Issue 494](https://code.google.com/p/robotframework/issues/detail?id=494) | Enhancement | Medium       | `Run` and `Read Process Output` should convert `\r\n` to `\n` on Jython 2.5 |

Altogether 17 issues.