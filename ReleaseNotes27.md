

# Robot Framework 2.7 #

Robot Framework 2.7 is a new major release with loads of bigger
and smaller enhancements and bug fixes. It was released after several
[preview releases](PreviewReleases27.md) on Wednesday 14th March 2012.

Questions and comments related to the
release can be sent to the [mailing lists](MailingLists.md) and possible
bugs submitted to
the [issue tracker](http://code.google.com/p/robotframework/issues).

## Downloads and installation ##

Installers and other packages are available on the
[download page](http://code.google.com/p/robotframework/downloads/list).

As [discussed below](#New_installation_and_start-up_system_--_pip_and_IronPython_are_s.md), installation has undergone some changes in 2.7 version. [Installation instructions](Installation.md) have been updated.

## Compatibility with RIDE ##

Latest [RIDE](https://github.com/robotframework/RIDE) versions
are not dependent on the installed Robot Framework version. It
is thus safe to install any Robot Framework release alongside RIDE.

## Most important enhancements and new features ##

### Faster and more memory efficient log and report generation ###

In [Robot Framework 2.6](ReleaseNotes26.md) logs and reports were heavily
enhanced, and nowadays they can contain huge amount of data and still
open to browsers fast and be responsive. The next bottleneck with huge
amounts of data was that generating logs and reports took a lot of time
and computer resources.

In Robot Framework 2.7 log/report generation performance with the
included `rebot` tool after test execution has been greatly
enhanced. Exact improvements depend on the executed tests, but based on
several data points both `rebot` execution time and memory consumption
have dropped about 50% compared to RF 2.6.  Creating logs and reports
as part of the test execution is also about 10% faster.

With larger data sets these enhancements can mean that you get reports
and logs several minutes faster than earlier and generating them takes
gigabytes less memory.

### New installation and start-up system -- `pip` and IronPython are supported ###

Robot Framework installation and start-up have been changed heavily internally. The biggest enhancements and other changes compared to earlier version are listed below. For more information see [updated installation instructions in wiki](Installation.md) and installation section in [Robot Framework 2.7 User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.2#installation-and-uninstallation).

  1. Installation using `pip` is finally supported ([issue 885](https://code.google.com/p/robotframework/issues/detail?id=885)).
  1. Installation using IronPython is officially supported. As a result you get new `ipybot` and `ipyrebot` start-up scripts.
  1. Installation using Jython creates new `jyrebot` start-up script in addition to `jybot`.
  1. Installing from source using Python **does not** create `jybot` script anymore. You need to install the framework using Jython to create it.
  1. All start-up scripts (`pybot`, `rebot`, `jybot`, ...) require the appropriate interpreter to be in `PATH`.
  1. Outside Windows, start-up scripts are implemented in Python to ease using them with virtualenv ([issue 1057](https://code.google.com/p/robotframework/issues/detail?id=1057)).
  1. `robot/runner.py` entry point has been deprecated in favor of `robot/run.py` and also programmatic execution API has changed ([issue 1044](https://code.google.com/p/robotframework/issues/detail?id=1044)).
  1. Source distribution only contains actual source code and tools ([issue 1037](https://code.google.com/p/robotframework/issues/detail?id=1037)).

### Log file enhancements ###

  * Possibility to open suites, tests, and keywords by clicking anywhere in the header ([issue 1046](https://code.google.com/p/robotframework/issues/detail?id=1046)).
  * `Expand All` functionality for individual keywords ([issue 1053](https://code.google.com/p/robotframework/issues/detail?id=1053)).
  * Possibility to select visible log level when there are DEBUG or TRACE level messages (new in RF 2.7.2, [issue 1108](https://code.google.com/p/robotframework/issues/detail?id=1108)).

### Public APIs documented ###

There is quite often a need to use Robot Framework's modules by external tools. So far this has been problematic because the APIs have not been documented too much, public APIs have not been separated from internal APIs, and API documentation has not been available anywhere.

All this is changing. Nowadays the API documentation is available at http://robot-framework.readthedocs.org/ ([issue 482](https://code.google.com/p/robotframework/issues/detail?id=482)) and public entry points are listed separately and also documented ([issue 831](https://code.google.com/p/robotframework/issues/detail?id=831)). Comments and enhancement requests related to the API docs are highly appreciated on [mailing lists](MailingLists.md) and [issue tracker](http://code.google.com/p/robotframework/issues/list).

### Library documentation tool `libdoc` is bundled with core framework ###

`libdoc` is a tool for creating documentation for Robot Framework test
libraries and resource files. Previously it has been available as a
[separate script](LibraryDocumentationTool.md), but nowadays it is a
build-in tool. It is included in the normal installation and can be
executed like `python -m robot.libdoc` ([issue 1028](https://code.google.com/p/robotframework/issues/detail?id=1028)). It also has its
own entry point in the stand-alone JAR distribution and that allows
executing `java -jar robotframework.jar libdoc` ([issue 800](https://code.google.com/p/robotframework/issues/detail?id=800)).

The command line usage of the tool has changed a little, but updating
existing scripts that use the tool ought to be easy. Most importantly
the documentation syntax itself has not been changed, except that it
now supports also pre-formatted text ([issue 447](https://code.google.com/p/robotframework/issues/detail?id=447)) and custom links and
images ([issue 1076](https://code.google.com/p/robotframework/issues/detail?id=1076)).

`libdoc` has also got totally new functionality and it can nowadays
also show library and resource documentation on the console ([issue 1061](https://code.google.com/p/robotframework/issues/detail?id=1061)). It has
special commands to list all available keywords, show documentation of a
specific keyword or whole library/resource, and to display the library
version.

For more information and examples run `python -m robot.libdoc --help`
and see [libdoc section in User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.2#libdoc).

### Test data documentation tool `testdoc` fixed and bundled with core framework ###

`testdoc` generates a high level test documentation based on Robot
Framework test data. It has earlier been available as a
[separate tool](TestDataDocumentationTool.md) but it has not been
compatible with Robot Framework 2.6 ([issue 908](https://code.google.com/p/robotframework/issues/detail?id=908)). Now it is fixed and
also bundled with the core framework similarly as `libdoc`. It can be
executed after normal installation like `python -m robot.testdoc` and
it also has an entry point in the JAR distribution.

For more information and examples run `python -m robot.testdoc --help`
and see [testdoc section in User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.2#testdoc).

### New built-in tool `tidy` for cleaning up data and changing data format ###

`tidy` is a new tool for cleaning up test data and changing test data
format between plain text, HTML and TSV ([issue 801](https://code.google.com/p/robotframework/issues/detail?id=801)). Similarly as
`libdoc` and `testdoc` it is a built-in tool included in the normal
installation. It can be executed like `python -m robot.tidy` and it
also has an entry point in the JAR distribution.

For more information and examples run `python -m robot.tidy --help`
and see [tidy section in User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.2#tidy).

### Enhancements for suite, test, and keyword documentation ###

  * Creating multi-line documentation in test data is easier (see [issue 1009](https://code.google.com/p/robotframework/issues/detail?id=1009) and [User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.2#representing-newlines))
  * Custom links and embedded images are supported (see [issue 1076](https://code.google.com/p/robotframework/issues/detail?id=1076) and [User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.2#custom-links-and-images))
  * Pre-formatted text (see [issue 447](https://code.google.com/p/robotframework/issues/detail?id=447) and [User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.2#preformatted-text)) and starting from RF 2.7.2 lists ([issue 1136](https://code.google.com/p/robotframework/issues/detail?id=1136) and [User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.2#lists)) are supported.
  * Suite and test documentation are available dynamically via `${SUITE DOCUMENTATION}` and `${TEST DOCUMENTATION}` variables ([issue 1077](https://code.google.com/p/robotframework/issues/detail?id=1077)) and can be set with `Set Suite Documentation` and `Set Test Documentation` keywords ([issue 1078](https://code.google.com/p/robotframework/issues/detail?id=1078))

### Several `--RemoveKeywords` enhancements ###

`--RemoveKeywords` command line option allows removing unnecessary
keywords from outputs to make their size smaller. It has been enhanced
multiple ways in RF 2.7 and nowadays it

  * works also when executing tests and not only with `rebot` ([issue 1027](https://code.google.com/p/robotframework/issues/detail?id=1027)),
  * can remove keywords inside for loops ([issue 990](https://code.google.com/p/robotframework/issues/detail?id=990)),
  * can remove keywords inside `Wait Until Keyword Succeeds` keyword ([issue 1007](https://code.google.com/p/robotframework/issues/detail?id=1007)), and
  * adds a message when it has removed keywords ([issue 1008](https://code.google.com/p/robotframework/issues/detail?id=1008)).

## Backwards incompatible changes and deprecated features ##

There are several backwards incompatible changes in RF 2.7 but none of them should be too severe.

### Internal modules related to test result processing changed ###

Enhancing performance of `rebot` ([issue 865](https://code.google.com/p/robotframework/issues/detail?id=865)) required large changes to the modules used for processing test results. There are two main changes:

  1. `robot.output.TestSuite` entry point mentioned also in the User Guide has been removed. Instead there is new `robot.result.ExecutionResult`.
  1. The suite model itself has changed slightly. For example, `TestCase.critical` is nowadays Boolean True or False when it used to string 'yes' or 'no'.

For more information about the current APIs see
http://robot-framework.readthedocs.org/.

### Handling suite, test, and keyword documentation changed ###

Nowadays suite, test, and keyword documentation split into multiple rows is automatically catenated with a newline instead of a space ([issue 1009](https://code.google.com/p/robotframework/issues/detail?id=1009)). This eases creating multiline documentation, but can also format existing documentation differently than earlier.

In practice this should not matter that much because documentation does not affect actual test execution. Also, no extra newline is added if the line already ends with a literal newline (`\n`). If the automatic newlines cause problems, it is possible to prevent them by ending a documentation row with a single backslash (`\`).

Documentation syntax also changed a little and it is now possible to create custom links or embed images using syntax `[link|content]`. This causes problems if you have used same syntax in documentation for other purposes.

### Source distribution does not contain documentation ###

Including documentation such as [User Guide](UserGuide.md) and [Quick Start Guide](QuickStartGuide.md) increased the size of the source distribution considerably. When installing the framework using a package manager such as pip or easy\_install, the source distribution was downloaded automatically and user never even saw the documentation.

To make the source distribution smaller, all extra content was removed. Nowadays it contains only the actual source code and [supporting tools](SupportingTools.md) ([issue 1037](https://code.google.com/p/robotframework/issues/detail?id=1037)) and the size dropped from 2.5MB to 0.5MB. All documentation is still available online and as separate downloads.

### Changes to programmatic execution APIs ###

  * `robot.run_rebot` method was renamed to `robot.rebot` ([issue 1044](https://code.google.com/p/robotframework/issues/detail?id=1044))
  * `robot.run` and `robot.rebot` return an error code if there are failures instead of raising exceptions ([issue 1045](https://code.google.com/p/robotframework/issues/detail?id=1045))
  * `robot.run_from_cli` and `robot.rebot_from_cli` method renamed to `robot.run_cli` and `robot.rebot_cli` and changed so that they don't need usage as an argument

### New built-in variables may class with existing variables with same name ###

New built-in variables `${KEYWORD STATUS}` and `${KEYWORD MESSAGE}` ([issue 1040](https://code.google.com/p/robotframework/issues/detail?id=1040)) and `${TEST DOCUMENTATION}` and `${SUITE DOCUMENTATION}` ([issue 1077](https://code.google.com/p/robotframework/issues/detail?id=1077)) may potentially clash with existing variables with same name. That should be pretty rare because the former two are available only in keyword teardowns and the latter two updated only when a test or a suite starts.

### Extended variable assign syntax may clash with existing variables ###

It is nowadays possible to set attributes of variables containing objects using a variation of the extended variable syntax like `${var.attr} =  My Keyword  arg` ([issue 1059](https://code.google.com/p/robotframework/issues/detail?id=1059)). This new syntax may cause problems if you have used dots in variable names. In practice problems should be rare, because most of the variables are strings and this syntax does not work with strings at all.

### Un-used `--SplitOutputs`, `--Summary`, and `--SummaryTitle` options removed ###

Functionality behind these options were removed already in RF 2.6 but the options were left for backwards compatibility reasons. Now they are removed and trying to use them causes an error.

### `robot/runner.py` deprecated in favor of `robot/run.py` ###

The `robot/runner.py` command line entry point has been renamed to `robot/run.py` ([issue 1044](https://code.google.com/p/robotframework/issues/detail?id=1044)). The old entry point works still in 2.7 but using it causes a deprecation warning.

## Acknowledgements ##

Big thanks for everyone who has tested the preview releases. Several nasty regressions have been found and fixed thanks to your bug reports.

Thanks to Imran for suggesting and implementing [issue 1015](https://code.google.com/p/robotframework/issues/detail?id=1015): Attribute source to be passed on start/end suite listener methods.

## Full list of fixes and enhancements in 2.7 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 865](https://code.google.com/p/robotframework/issues/detail?id=865) | Enhancement | Critical     | Faster and more memory efficient log and report generation with rebot |
| [Issue 885](https://code.google.com/p/robotframework/issues/detail?id=885) | Defect   | High         | Installation using pip does not work |
| [Issue 908](https://code.google.com/p/robotframework/issues/detail?id=908) | Defect   | High         | `testdoc` tool is broken in RF 2.6 |
| [Issue 1003](https://code.google.com/p/robotframework/issues/detail?id=1003) | Defect   | High         | Log time differs from system time |
| [Issue 480](https://code.google.com/p/robotframework/issues/detail?id=480) | Enhancement | High         | New installation and start-up system |
| [Issue 801](https://code.google.com/p/robotframework/issues/detail?id=801) | Enhancement | High         | Built-in `robot.tidy` tool for changing format and cleaning-up test data |
| [Issue 990](https://code.google.com/p/robotframework/issues/detail?id=990) | Enhancement | High         | Improve `--RemoveKeywords` so that it can remove keywords from for loops |
| [Issue 1007](https://code.google.com/p/robotframework/issues/detail?id=1007) | Enhancement | High         | Enhance `--RemoveKeywords` so that it can remove unnecessary keywords inside `Wait Until Keyword Succeeds` |
| [Issue 1027](https://code.google.com/p/robotframework/issues/detail?id=1027) | Enhancement | High         | `--RemoveKeywords` option should also work when running tests |
| [Issue 1028](https://code.google.com/p/robotframework/issues/detail?id=1028) | Enhancement | High         | `libdoc` should be bundled with Robot Framework core |
| [Issue 1046](https://code.google.com/p/robotframework/issues/detail?id=1046) | Enhancement | High         | Log: Allow opening suites, tests and keywords by clicking anywhere in the header |
| [Issue 1053](https://code.google.com/p/robotframework/issues/detail?id=1053) | Enhancement | High         | Log: `Expand All` functionality for individual keywords |
| [Issue 1061](https://code.google.com/p/robotframework/issues/detail?id=1061) | Enhancement | High         | Support for `libdoc` to show library/resource information on console |
| [Issue 1064](https://code.google.com/p/robotframework/issues/detail?id=1064) | Enhancement | High         | `testdoc` should be bundled with core framework |
| [Issue 1076](https://code.google.com/p/robotframework/issues/detail?id=1076) | Enhancement | High         | Support for custom links and images in suite/test/keyword documentation and suite metadata |
| [Issue 482](https://code.google.com/p/robotframework/issues/detail?id=482) | Documentation | High         | Generate API documentation |
| [Issue 831](https://code.google.com/p/robotframework/issues/detail?id=831) | Documentation | High         | Write documentation for most important APIs |
| [Issue 551](https://code.google.com/p/robotframework/issues/detail?id=551) | Defect   | Medium       | Recursive user keywords can break the whole test execution |
| [Issue 979](https://code.google.com/p/robotframework/issues/detail?id=979) | Defect   | Medium       | If a library implemented as a directory is in execution directory, importing it can result in corrupted library with Python 2.5 and 2.6 |
| [Issue 985](https://code.google.com/p/robotframework/issues/detail?id=985) | Defect   | Medium       | Logging with logging API when timeout is used does not work |
| [Issue 986](https://code.google.com/p/robotframework/issues/detail?id=986) | Defect   | Medium       | --tagdoc doesn't work if tag has underscore in name |
| [Issue 988](https://code.google.com/p/robotframework/issues/detail?id=988) | Defect   | Medium       | Variables used in embedded argument syntax leak to caller |
| [Issue 998](https://code.google.com/p/robotframework/issues/detail?id=998) | Defect   | Medium       | `logging` module is configured to emit messages with unnecessarily low level |
| [Issue 1022](https://code.google.com/p/robotframework/issues/detail?id=1022) | Defect   | Medium       | Setting non-string message to tests with `BuiltIn.Set Test Message` keyword crashes execution |
| [Issue 1029](https://code.google.com/p/robotframework/issues/detail?id=1029) | Defect   | Medium       | RunnerFactory returns instance with the same state on multiple invocations |
| [Issue 1049](https://code.google.com/p/robotframework/issues/detail?id=1049) | Defect   | Medium       | Environment variable related keywords and %{NAME} variable do not encode non-ASCII strings correctly |
| [Issue 1051](https://code.google.com/p/robotframework/issues/detail?id=1051) | Defect   | Medium       | `Should Be Equal` and other similar keywords fail to compare non-ASCII byte values |
| [Issue 1072](https://code.google.com/p/robotframework/issues/detail?id=1072) | Defect   | Medium       | `--TagStatInclude` and `--TagStatExclude` do not ignore underscores |
| [Issue 1079](https://code.google.com/p/robotframework/issues/detail?id=1079) | Defect   | Medium       | Exception shown on console if libraries register `logging.StreamHandler` using `sys.stderr` |
| [Issue 1081](https://code.google.com/p/robotframework/issues/detail?id=1081) | Defect   | Medium       | Using --test option multiple times is extremely slow when there are lot of tests |
| [Issue 59](https://code.google.com/p/robotframework/issues/detail?id=59) | Enhancement | Medium       | Support capturing stdout and stderr when running Robot and Rebot programmatically |
| [Issue 447](https://code.google.com/p/robotframework/issues/detail?id=447) | Enhancement | Medium       | Support for preformatted text in documentation |
| [Issue 647](https://code.google.com/p/robotframework/issues/detail?id=647) | Enhancement | Medium       | Comments are not handled well in parsing model |
| [Issue 675](https://code.google.com/p/robotframework/issues/detail?id=675) | Enhancement | Medium       | Dry-run should support `Import Library` keyword |
| [Issue 759](https://code.google.com/p/robotframework/issues/detail?id=759) | Enhancement | Medium       | It should be possible to save parsed data to disk and memory |
| [Issue 775](https://code.google.com/p/robotframework/issues/detail?id=775) | Enhancement | Medium       | Allow specifying `Test Timeout` in suite init files |
| [Issue 800](https://code.google.com/p/robotframework/issues/detail?id=800) | Enhancement | Medium       | Robot Framework jar should have entry point for libdoc |
| [Issue 871](https://code.google.com/p/robotframework/issues/detail?id=871) | Enhancement | Medium       | Timeout speed optimization |
| [Issue 1008](https://code.google.com/p/robotframework/issues/detail?id=1008) | Enhancement | Medium       | `--RemoveKeywords` should log message when it removes keywords |
| [Issue 1009](https://code.google.com/p/robotframework/issues/detail?id=1009) | Enhancement | Medium       | Ease creating multiline documentation or metadata values. |
| [Issue 1011](https://code.google.com/p/robotframework/issues/detail?id=1011) | Enhancement | Medium       | Add keyword 'Split String To Characters' keyword |
| [Issue 1015](https://code.google.com/p/robotframework/issues/detail?id=1015) | Enhancement | Medium       | Attribute source to be passed on start/end suite listener methods |
| [Issue 1021](https://code.google.com/p/robotframework/issues/detail?id=1021) | Enhancement | Medium       | Support variable files based on Python and Java classes |
| [Issue 1031](https://code.google.com/p/robotframework/issues/detail?id=1031) | Enhancement | Medium       | Log: Keep non-critical failed tests closed by default and differentiate them from critical failed tests |
| [Issue 1037](https://code.google.com/p/robotframework/issues/detail?id=1037) | Enhancement | Medium       | Only include source code and tools in the source distribution to make it smaller |
| [Issue 1040](https://code.google.com/p/robotframework/issues/detail?id=1040) | Enhancement | Medium       | New automatic variables `${KEYWORD STATUS}` and `${KEYWORD MESSAGE}` to know keyword status in keyword teardown |
| [Issue 1054](https://code.google.com/p/robotframework/issues/detail?id=1054) | Enhancement | Medium       | Convert start-up script to Python outside Windows to ease using them on virtualenv |
| [Issue 1059](https://code.google.com/p/robotframework/issues/detail?id=1059) | Enhancement | Medium       | Support for "extended assign" like `${var.attr} =    Some Keyword` |
| [Issue 1066](https://code.google.com/p/robotframework/issues/detail?id=1066) | Enhancement | Medium       | Show notification on console when a top-level keyword ends |
| [Issue 1077](https://code.google.com/p/robotframework/issues/detail?id=1077) | Enhancement | Medium       | New built-in variables `${TEST DOCUMENTATION}` and `${SUITE DOCUMENTATION}` |
| [Issue 1078](https://code.google.com/p/robotframework/issues/detail?id=1078) | Enhancement | Medium       | New keywords to Builtin-library: "Set test documentation" and "Set suite documentation"  |
| [Issue 510](https://code.google.com/p/robotframework/issues/detail?id=510) | Defect   | Low          | Output files use Unix line endings on Windows |
| [Issue 920](https://code.google.com/p/robotframework/issues/detail?id=920) | Defect   | Low          | Statistics graph sometimes has a small gray area at the end |
| [Issue 982](https://code.google.com/p/robotframework/issues/detail?id=982) | Defect   | Low          | Hexadecimal HTML entiry references (e.g. &#x2603;) are not parsed correctly |
| [Issue 1030](https://code.google.com/p/robotframework/issues/detail?id=1030) | Defect   | Low          | Resources and libraries from previous runs should not be re-used when executing tests programmatically multiple times |
| [Issue 1045](https://code.google.com/p/robotframework/issues/detail?id=1045) | Defect   | Low          | `robot.run` and `robot.run_rebot` methods leave framework to inconsistent state if they fail |
| [Issue 1080](https://code.google.com/p/robotframework/issues/detail?id=1080) | Defect   | Low          | Execution fails on Python 2.5.0 |
| [Issue 1082](https://code.google.com/p/robotframework/issues/detail?id=1082) | Defect   | Low          | Critical and non-critical tags are not underscore insensitive |
| [Issue 1019](https://code.google.com/p/robotframework/issues/detail?id=1019) | Enhancement | Low          | Cleaner error message when importing test libraries or variable files fails |
| [Issue 1036](https://code.google.com/p/robotframework/issues/detail?id=1036) | Enhancement | Low          | Expose `TxtReader._split_row` as a public function |
| [Issue 1044](https://code.google.com/p/robotframework/issues/detail?id=1044) | Enhancement | Low          | Rename `robot/runner.py` script to `robot/run.py` and `robot.run_rebot` method to `robot.rebot` |
| [Issue 1047](https://code.google.com/p/robotframework/issues/detail?id=1047) | Enhancement | Low          | Command line help for robotframework.jar |
| [Issue 1048](https://code.google.com/p/robotframework/issues/detail?id=1048) | Enhancement | Low          | Remove un-used `--SplitOutputs`, `--Summary`, and `--SummaryTitle` options |
| [Issue 1052](https://code.google.com/p/robotframework/issues/detail?id=1052) | Enhancement | Low          | Internal id of tests and suites should be added to XML output |
| [Issue 1056](https://code.google.com/p/robotframework/issues/detail?id=1056) | Enhancement | Low          | New keywords `Get Environment Variables` and `Log Environment Variables` to `OperatingSystem` library. |
| [Issue 1057](https://code.google.com/p/robotframework/issues/detail?id=1057) | Enhancement | Low          | Show red failure texts using bold to make them easier to notice for color blind |
| [Issue 1058](https://code.google.com/p/robotframework/issues/detail?id=1058) | Enhancement | Low          | `OperatingSystem.Remove Environment Variable` should allow removing multiple variables |
| [Issue 1043](https://code.google.com/p/robotframework/issues/detail?id=1043) | Documentation | Low          | Document that Dialogs library doesn't work with Timeouts in Python |

Altogether 68 issues.

# Robot Framework 2.7.1 #

Robot Framework 2.7.1 is a minor release which fixes a couple of high impact bugs. It was released on Monday 26th March 2012.

This release fixes several issues related to character encodings ([issue 1086](https://code.google.com/p/robotframework/issues/detail?id=1086), [issue 1092](https://code.google.com/p/robotframework/issues/detail?id=1092), [issue 1091](https://code.google.com/p/robotframework/issues/detail?id=1091), and [issue 1095](https://code.google.com/p/robotframework/issues/detail?id=1095)). There also was a problem with the dynamic library API that prevented SwingLibrary from working ([issue 1090](https://code.google.com/p/robotframework/issues/detail?id=1090)).

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1090](https://code.google.com/p/robotframework/issues/detail?id=1090) | Defect   | Critical     | Adding keyword to a dynamic library fails if `get_keyword_arguments()` returns `None` (affects at least `SwingLibrary`) |
| [Issue 1091](https://code.google.com/p/robotframework/issues/detail?id=1091) | Defect   | Critical     | Crash with Jython on Windows with Chinese locale |
| [Issue 1095](https://code.google.com/p/robotframework/issues/detail?id=1095) | Defect   | Critical     | Crash when resource or variable file is not found directly and PYTHONPATH contains non-ASCII paths |
| [Issue 1086](https://code.google.com/p/robotframework/issues/detail?id=1086) | Defect   | High         | `Get Environment Variable` keyword fails on Jython on non-Western Windows |
| [Issue 1092](https://code.google.com/p/robotframework/issues/detail?id=1092) | Defect   | High         | Reporting library import error fails with UnicodeDecodeError if PYTHONPATH contains non-ASCII paths |
| [Issue 1087](https://code.google.com/p/robotframework/issues/detail?id=1087) | Defect   | Medium       | No warning when multiple data sources is given and parsing some of them fails |
| [Issue 1097](https://code.google.com/p/robotframework/issues/detail?id=1097) | Defect   | Medium       | Rowsplitter infinent loop when enough empty cells |
| [Issue 1088](https://code.google.com/p/robotframework/issues/detail?id=1088) | API      | Medium       | Number of spaces should be configurable when writing space separated text files. |
| [Issue 1096](https://code.google.com/p/robotframework/issues/detail?id=1096) | Defect   | Low          | All East Asian characters are not aligned correctly on console |

Altogether 9 issues.


# Robot Framework 2.7.2 #

Robot Framework 2.7.2 includes a couple of really nice enhancements. The first
is the ability to select which log messages are shown, according to their
levels ([issue 1108](https://code.google.com/p/robotframework/issues/detail?id=1108)). The second enhancement is related to execution speed ([issue 1145](https://code.google.com/p/robotframework/issues/detail?id=1145)),
where we were able to reduce the framework overhead quite significantly in some cases.

In addition, this release contains quite a few bug fixes and minor enhancements, all of which are listed in the table below.

Robot Framework 2.7.2 was released on Friday 8th of June, 2012.

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1108](https://code.google.com/p/robotframework/issues/detail?id=1108) | Enhancement | High         | Possibility to select visible log level when there are `DEBUG` or `TRACE` level messages |
| [Issue 1145](https://code.google.com/p/robotframework/issues/detail?id=1145) | Enhancement | High         | Reduce test execution overhead |
| [Issue 1106](https://code.google.com/p/robotframework/issues/detail?id=1106) | Defect   | Medium       | Global variables are not cleared when executing tests several times using the programmatic API |
| [Issue 1110](https://code.google.com/p/robotframework/issues/detail?id=1110) | Defect   | Medium       | `Import Library` keyword fails with `AttributeError` if second last argument to imported library is not string |
| [Issue 1113](https://code.google.com/p/robotframework/issues/detail?id=1113) | Defect   | Medium       | Library documentation created with libdoc does not support #anchors in incoming links anymore |
| [Issue 1114](https://code.google.com/p/robotframework/issues/detail?id=1114) | Defect   | Medium       | Remote library does not work with IronPython |
| [Issue 1130](https://code.google.com/p/robotframework/issues/detail?id=1130) | Defect   | Medium       | Cannot run tests if Saxon XML library is found in the `CLASSPATH` |
| [Issue 1135](https://code.google.com/p/robotframework/issues/detail?id=1135) | Defect   | Medium       | Inconsistent handling of documentation paragraphs in log/report vs. libdoc |
| [Issue 1139](https://code.google.com/p/robotframework/issues/detail?id=1139) | Defect   | Medium       | Relative imports found from the `PYTHONPATH` do not work |
| [Issue 1144](https://code.google.com/p/robotframework/issues/detail?id=1144) | Defect   | Medium       | Generating log and report fails if executed suite is empty even with `--RunEmptySuite` option |
| [Issue 1146](https://code.google.com/p/robotframework/issues/detail?id=1146) | Defect   | Medium       | Using multiple NOT operators in commandline tag options is broken |
| [Issue 1136](https://code.google.com/p/robotframework/issues/detail?id=1136) | Enhancement | Medium       | Real support for lists in documentation |
| [Issue 1147](https://code.google.com/p/robotframework/issues/detail?id=1147) | Enhancement | Medium       | New `--ProcessEmptySuite` option for rebot to allow processing empty suites |
| [Issue 1117](https://code.google.com/p/robotframework/issues/detail?id=1117) | Documentation | Medium       | Enhance documentation of `Stop Process` and `Stop All Processes` keywords |
| [Issue 1126](https://code.google.com/p/robotframework/issues/detail?id=1126) | Documentation | Medium       | Include Javadocs in the API documentation |
| [Issue 1137](https://code.google.com/p/robotframework/issues/detail?id=1137) | Defect   | Low          | Using Python's `multiprocessing` module in test libraries does not work on Windows |
| [Issue 1140](https://code.google.com/p/robotframework/issues/detail?id=1140) | Defect   | Low          | Showing combined tags in report can fail with patterns containing NOTs |
| [Issue 1103](https://code.google.com/p/robotframework/issues/detail?id=1103) | Enhancement | Low          | Public APIs expecting lists as arguments should also accept single items when possible |
| [Issue 1119](https://code.google.com/p/robotframework/issues/detail?id=1119) | Enhancement | Low          | statuschecker.py tool should support testing only the beginning of the expected error |
| [Issue 1132](https://code.google.com/p/robotframework/issues/detail?id=1132) | Enhancement | Low          | Dialogs created by `Dialogs` library using Jython should appear always on top |

Altogether 20 issues.

# Robot Framework 2.7.3 #

Robot Framework 2.7.2 release had some nice performance enhancements ([issue 1145](https://code.google.com/p/robotframework/issues/detail?id=1145)) that unfortunately caused few nasty regressions ([issue 1154](https://code.google.com/p/robotframework/issues/detail?id=1154), [issue 1162](https://code.google.com/p/robotframework/issues/detail?id=1162), [issue 1153](https://code.google.com/p/robotframework/issues/detail?id=1153)). These bugs occurred only in somewhat special circumstances, but they all resulted with corrupted outputs so their impact was pretty severe.

In addition to fixes to these problems, RF 2.7.3 contains some lower priority fixes/features mainly related to `robot.tidy` tool. All the issues resolved in this release are listed in the table below.

Robot Framework 2.7.3 was released on Monday 18th of June, 2012.

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1154](https://code.google.com/p/robotframework/issues/detail?id=1154) | Defect   | Critical     | Binary characters in FOR loop values (and possibly elsewhere) can break XML output |
| [Issue 1162](https://code.google.com/p/robotframework/issues/detail?id=1162) | Defect   | Critical     | Creating xUnit combatible output with non-ASCII data fails |
| [Issue 1153](https://code.google.com/p/robotframework/issues/detail?id=1153) | Defect   | High         | Using `BuiltIn.run_keyword` with non-string arguments in test libraries fails and results with broken output XML |
| [Issue 1149](https://code.google.com/p/robotframework/issues/detail?id=1149) | Defect   | Medium       | Tidy should preserve existing tables even if they are empty |
| [Issue 1158](https://code.google.com/p/robotframework/issues/detail?id=1158) | Defect   | Medium       | Using `OperatingSystem.Start Process` causes deprecation warning with Python 2.6 and 2.7 |
| [Issue 1155](https://code.google.com/p/robotframework/issues/detail?id=1155) | Enhancement | Medium       | Command line option to set number of spaces used by `tidy` |
| [Issue 1156](https://code.google.com/p/robotframework/issues/detail?id=1156) | Defect   | Low          | Tidy does not align data correctly in all cases |
| [Issue 1157](https://code.google.com/p/robotframework/issues/detail?id=1157) | Defect   | Low          | Tidy writes unnecessary empty row at the end of file |

Altogether 8 issues.

# Robot Framework 2.7.4 #

Robot Framework 2.7.4 is a bigger-than-normal minor release that brings
some really nice new enhancements and some bug fixes. It was released on Thursday 6th of September, 2012.

## Most important enhancements ##

### New library for verifying XML contents ###

New standard library [XML](XMLLibrary.md) makes verifying XML contents
with Robot Framework easy ([issue 1196](https://code.google.com/p/robotframework/issues/detail?id=1196)). This library works also with
earlier 2.7 versions, but needs to be downloaded separately.

### Enhanced statistics ###

Statistics nowadays contain elapsed times per suite and per tag ([issue 1194](https://code.google.com/p/robotframework/issues/detail?id=1194)) to make it easier to monitor which tests take most time. Elapsed times also have their own column in test details ([issue 1206](https://code.google.com/p/robotframework/issues/detail?id=1206)) to ease further investigation.

Statistics are also sortable, for example, by elapsed times ([issue 1199](https://code.google.com/p/robotframework/issues/detail?id=1199)). A small but convenient new feature is that clicking anywhere in the statistics row, as well as in test detail row, navigates to more details ([issue 1200](https://code.google.com/p/robotframework/issues/detail?id=1200)). No need to move mouse over the tag, suite, or test name before clicking.

### `ELSE` and `ELSE IF` support for `Run Keyword If` keyword ###

It is easier to create if/else constructs now that `Run Keyword If` has built-in support for them ([issue 1219](https://code.google.com/p/robotframework/issues/detail?id=1219)). This is especially handy when you want to get the return value of the actually executed keyword:

| ${ret} = | Run Keyword If | ${rc} == 0 |Handle Zero Return Value |  |
|:---------|:---------------|:-----------|:------------------------|:-|
| ...      | ELSE IF        | ${rc} < 0  | Handle Negative Return Value | ${rc} |
| ...      | ELSE           | Handle Positive Return Value | ${rc}                   | second arg |

## Potentially backwards-incompatible changes ##

It is possible, but very unlikely, that the changes listed below could cause backwards-compatibility problems.

  * Modifying tags test have is not anymore possible by altering `${TEST TAGS}` variable ([issue 1215](https://code.google.com/p/robotframework/issues/detail?id=1215)).
  * Return value of `Get Variables` is a normal dictionary and not a custom object with access to internals of the framework ([issue 1180](https://code.google.com/p/robotframework/issues/detail?id=1180)).
  * Because `ELSE` and `ELSE IF` have special meaning `Run Keyword If` ([issue 1219](https://code.google.com/p/robotframework/issues/detail?id=1219)), using them as literal strings requires escaping like `\ELSE`.
  * New automatic variables `${SUITE METADATA}` ([issue 1134](https://code.google.com/p/robotframework/issues/detail?id=1134)) may overwrite variable with same name used otherwise in test data.

## Full list of enhancements and fixes ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1196](https://code.google.com/p/robotframework/issues/detail?id=1196) | Enhancement | Critical     | New library for verifying XML contents |
| [Issue 1164](https://code.google.com/p/robotframework/issues/detail?id=1164) | Defect   | High         | Log and report can break if test data contains text `</script>`  |
| [Issue 1194](https://code.google.com/p/robotframework/issues/detail?id=1194) | Enhancement | High         | Run times per suite and per tag should be shown in statistics |
| [Issue 1199](https://code.google.com/p/robotframework/issues/detail?id=1199) | Enhancement | High         | Sortable statistics |
| [Issue 1206](https://code.google.com/p/robotframework/issues/detail?id=1206) | Enhancement | High         | Separate column for elapsed time in report's test details table to allow sorting by it |
| [Issue 1219](https://code.google.com/p/robotframework/issues/detail?id=1219) | Enhancement | High         | `ELSE` and `ELSE IF` support for `Run Keyword If` |
| [Issue 1165](https://code.google.com/p/robotframework/issues/detail?id=1165) | Defect   | Medium       | Error message when creating log or report fails doesn't have enough information |
| [Issue 1176](https://code.google.com/p/robotframework/issues/detail?id=1176) | Defect   | Medium       | Stop Process cannot be used to "stop" a process anymore |
| [Issue 1180](https://code.google.com/p/robotframework/issues/detail?id=1180) | Defect   | Medium       | The return value of the BuiltIn library's Get Variables keyword cannot be used like normal dictionary |
| [Issue 1190](https://code.google.com/p/robotframework/issues/detail?id=1190) | Defect   | Medium       | `times2csv.py` does not handle non-ASCII characters |
| [Issue 1191](https://code.google.com/p/robotframework/issues/detail?id=1191) | Defect   | Medium       | Trying to use Java class without public constructor as test library crashes execution |
| [Issue 1192](https://code.google.com/p/robotframework/issues/detail?id=1192) | Defect   | Medium       | Linking to warnings in log files does not work when using `--SplitLog` option |
| [Issue 1212](https://code.google.com/p/robotframework/issues/detail?id=1212) | Defect   | Medium       | Errors happening in Python's `logging` module should not fail a test case |
| [Issue 1134](https://code.google.com/p/robotframework/issues/detail?id=1134) | Enhancement | Medium       | Add `Set Suite Metadata` keyword and `${SUITE METADATA}` variable |
| [Issue 1184](https://code.google.com/p/robotframework/issues/detail?id=1184) | Enhancement | Medium       | Better reporting when using invalid command line options |
| [Issue 1200](https://code.google.com/p/robotframework/issues/detail?id=1200) | Enhancement | Medium       | Navigate to destination by clicking anywhere in statistics and test detail rows in log/report |
| [Issue 1210](https://code.google.com/p/robotframework/issues/detail?id=1210) | Enhancement | Medium       | Tidy tool (and parsing modules) should preserve standalone comments in variable table |
| [Issue 1220](https://code.google.com/p/robotframework/issues/detail?id=1220) | Enhancement | Medium       | `--MonitorMarkers` option to control are `.` and `F` used on console when top-level keywords end |
| [Issue 1163](https://code.google.com/p/robotframework/issues/detail?id=1163) | Defect   | Low          | HTML formatted tables do not anymore have `border="1"` attribute |
| [Issue 1211](https://code.google.com/p/robotframework/issues/detail?id=1211) | Defect   | Low          | Small problems showing total, tag, or suite name when printing tests in report |
| [Issue 1213](https://code.google.com/p/robotframework/issues/detail?id=1213) | Defect   | Low          | Libdoc does not differentiate varargs from normal arguments with Java libraries |
| [Issue 1215](https://code.google.com/p/robotframework/issues/detail?id=1215) | Defect   | Low          | Modifying `${TEST TAGS}` should not affect actual tags tests have |
| [Issue 1166](https://code.google.com/p/robotframework/issues/detail?id=1166) | Enhancement | Low          | New `@{EMPTY}` variable |
| [Issue 1174](https://code.google.com/p/robotframework/issues/detail?id=1174) | Enhancement | Low          | Documentation formatting: Allow splitting list items into multiple lines by indenting continuing lines |
| [Issue 1177](https://code.google.com/p/robotframework/issues/detail?id=1177) | Enhancement | Low          | Keywords in `Collections` for comparing lists and dictionaries should report errors better when items look same but have different type |
| [Issue 1218](https://code.google.com/p/robotframework/issues/detail?id=1218) | Enhancement | Low          | Allow modifying test tags with `Fail` keyword |

Altogether 26 issues.

# Robot Framework 2.7.5 #

Robot Framework 2.7.5 is another bigger-than-normal minor release. It
was released on Wednesday 24th of October, 2012.

## Most important enhancements ##

### Enhancements to XML library ###

[XML library](XMLLibrary.md) added in RF 2.7.4 has been greatly enhanced in RF 2.7.5. It
can now be used for modifying XML and saving it back to disk ([issue 1234](https://code.google.com/p/robotframework/issues/detail?id=1234)),
it has better support for XML namepaces ([issue 1241](https://code.google.com/p/robotframework/issues/detail?id=1241)), and some new
keywords were added for verifying contents ([issue 1236](https://code.google.com/p/robotframework/issues/detail?id=1236), [issue 1260](https://code.google.com/p/robotframework/issues/detail?id=1260)).

### New features to `libdoc` ###

`libdoc` tool used for documenting test libraries and resource files
got some nice enhancements. Most importantly, it is now possible to
use HTML, plain text, and reStructuredText in documentation and not
only Robot Framework's own documentation format ([issue 489](https://code.google.com/p/robotframework/issues/detail?id=489)). To make
longer documentations easier to navigate around, headers used in
introduction ([issue 1247](https://code.google.com/p/robotframework/issues/detail?id=1247)) as well as Shortcuts and Keywords sections
([issue 1250](https://code.google.com/p/robotframework/issues/detail?id=1250)) can be used as link targets. How the results of the
latter enhancements look in practice can be seen in the documentation
of [XML library](XMLLibrary.md).

### Enhanced IronPython support ###

Nowadays ScreenshotLibrary works with IronPython ([issue 1225](https://code.google.com/p/robotframework/issues/detail?id=1225)) and
[XML library](XMLLibrary.md) can be used with non-ASCII characters ([issue 1228](https://code.google.com/p/robotframework/issues/detail?id=1228)). Several
smaller issues were also fixed in the code and in acceptance tests. As
a result all Robot Framework's acceptance tests now
[pass also with IronPython](http://robot.radiaatto.ri.fi/job/RobotFramework-Windows-IronPython/).

DialogsLibrary is now the only standard library that does not work with
IronPython ([issue 1235](https://code.google.com/p/robotframework/issues/detail?id=1235)). A bigger limitation is that using C# for
creating test libraries is not possible ([issue 721](https://code.google.com/p/robotframework/issues/detail?id=721)). Let us know by
commenting these issue or on [mailing lists](MailingLists.md) if you are interested to help getting these issues done.

## Potentially backwards-incompatible changes ##

It is possible, but very unlikely, that these changes could cause
backwards-compatibility problems:

  * Non-breaking spaces in test data are considered normal spaces ([issue 1264](https://code.google.com/p/robotframework/issues/detail?id=1264)).
  * `&tilde;` in HTML test data is nowadays correctly parsed to `˜` and not to `~` ([issue 1265](https://code.google.com/p/robotframework/issues/detail?id=1265)).

## Acknowledgements ##

Tatu Aalto provided a patch for `Get Time` keyword enhancement ([issue 1233](https://code.google.com/p/robotframework/issues/detail?id=1233)) he had proposed. Eemeli Kantola reported and helped fixing an
issue with non-breaking spaces ([issue 1264](https://code.google.com/p/robotframework/issues/detail?id=1264)). Thanks also for everyone reporting issues and otherwise making RF 2.7.5 a great release!

## Full list of enhancements and fixes ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1249](https://code.google.com/p/robotframework/issues/detail?id=1249) | Defect   | High         | Chrome can fail to open log file when running tests with debug or trace levels |
| [Issue 1261](https://code.google.com/p/robotframework/issues/detail?id=1261) | Defect   | High         | Performance: Keywords are unnecessarily parsed from output when creating only report |
| [Issue 1225](https://code.google.com/p/robotframework/issues/detail?id=1225) | Enhancement | High         | Support `Screenshot` library with IronPython |
| [Issue 1234](https://code.google.com/p/robotframework/issues/detail?id=1234) | Enhancement | High         | `XML` library: Keywords for modifying and saving XML |
| [Issue 1241](https://code.google.com/p/robotframework/issues/detail?id=1241) | Enhancement | High         | `XML` lib: Enhanced support for namespaces |
| [Issue 1231](https://code.google.com/p/robotframework/issues/detail?id=1231) | Defect   | Medium       | Using variables containing non-ASCII byte strings with other text is not possible |
| [Issue 1240](https://code.google.com/p/robotframework/issues/detail?id=1240) | Defect   | Medium       | Dry-run mode does not handle `ELSE IF/ELSE` functionality provided by `Run Keyword If` |
| [Issue 1253](https://code.google.com/p/robotframework/issues/detail?id=1253) | Defect   | Medium       | `tidy` should not resolve `${CURDIR}` |
| [Issue 1264](https://code.google.com/p/robotframework/issues/detail?id=1264) | Defect   | Medium       | Non-breaking spaces interpreted as not whitespace in test data |
| [Issue 489](https://code.google.com/p/robotframework/issues/detail?id=489) | Enhancement | Medium       | `libdoc`: Support for documentation in HTML, plain text, and reStructuredText formats |
| [Issue 1227](https://code.google.com/p/robotframework/issues/detail?id=1227) | Enhancement | Medium       | `--RemoveKeywords FOR` should not remove last keyword |
| [Issue 1236](https://code.google.com/p/robotframework/issues/detail?id=1236) | Enhancement | Medium       | `XML` library: `Element Should (Not) Exist` and `Get Element Count` keywords |
| [Issue 1247](https://code.google.com/p/robotframework/issues/detail?id=1247) | Enhancement | Medium       | Libdoc: Linking to headers in introduction |
| [Issue 1251](https://code.google.com/p/robotframework/issues/detail?id=1251) | Enhancement | Medium       | `Remove Duplicates` keyword to `Collections` |
| [Issue 1254](https://code.google.com/p/robotframework/issues/detail?id=1254) | Enhancement | Medium       | Add built-in variable `${\n}` that contains OS specific line separator (`\r\n` on Windows and `\n` elsewhere) |
| [Issue 1224](https://code.google.com/p/robotframework/issues/detail?id=1224) | Defect   | Low          | Extended variable syntax does not work if variable name contains non-ASCII characters |
| [Issue 1228](https://code.google.com/p/robotframework/issues/detail?id=1228) | Defect   | Low          | Creating XML containing non-ASCII characters in test data using `XML` library fails on IronPython |
| [Issue 1237](https://code.google.com/p/robotframework/issues/detail?id=1237) | Defect   | Low          | Using keywords with non-ASCII characters in name case-insensitively does not work with IronPython |
| [Issue 1244](https://code.google.com/p/robotframework/issues/detail?id=1244) | Defect   | Low          | `Run Keyword If` does not escape `ELSE IF` and `ELSE` from list variables |
| [Issue 1262](https://code.google.com/p/robotframework/issues/detail?id=1262) | Defect   | Low          | Long title can mess up the beginning of log and report |
| [Issue 1265](https://code.google.com/p/robotframework/issues/detail?id=1265) | Defect   | Low          | `&tilde;` in HTML test data parsed incorrectly |
| [Issue 1233](https://code.google.com/p/robotframework/issues/detail?id=1233) | Enhancement | Low          | Support for returning time in UTC for `Get Time` and `Set Modified Time` keywords |
| [Issue 1239](https://code.google.com/p/robotframework/issues/detail?id=1239) | Enhancement | Low          | `Tidy`: Possibility to give output file |
| [Issue 1246](https://code.google.com/p/robotframework/issues/detail?id=1246) | Enhancement | Low          | Support for sections titles (a.k.a. headings) in documentation suite/test/keyword documentation |
| [Issue 1250](https://code.google.com/p/robotframework/issues/detail?id=1250) | Enhancement | Low          | Libdoc: Make `Shortcuts` and `Keywords` sections linkable targets |
| [Issue 1260](https://code.google.com/p/robotframework/issues/detail?id=1260) | Enhancement | Low          | `Element Should Not Have Attribute` keyword to `XML` library |
| [Issue 1229](https://code.google.com/p/robotframework/issues/detail?id=1229) | Documentation | Low          | Support ANSI colors on console output also on Windows |

Altogether 27 issues.

# Robot Framework 2.7.6 #

Robot Framework 2.7.6 fixes a big memory leak ([issue 1202](https://code.google.com/p/robotframework/issues/detail?id=1202)), adds new
`*.robot` extension for plain text data files ([issue 1018](https://code.google.com/p/robotframework/issues/detail?id=1018)), and
contains several other higher and lower priority enhancements and
fixes. It was released on Monday 7th of January, 2013.

## Most important fixes and enhancements ##

### Big memory leak fixed ###

Running tests leaked memory ([issue 1202](https://code.google.com/p/robotframework/issues/detail?id=1202)) resulting to excess memory
usage with larger test data sets. In one case memory usage dropped
whopping 95% from 10GB to 0.5GB, and about 20% enhancements were
noticed with other cases.

### New `*.robot` extension for plain text test data ###

It is nowadays possible to use special `.robot` extension with Robot
Framework test data ([issue 1018](https://code.google.com/p/robotframework/issues/detail?id=1018)). This can be handy in order to separate these
files from other files used for testing. Other than the extension
these files do not differ from `.txt` files at all.

The built-in Tidy tool has been enhanced to support `*.robot` files but
[RIDE does not yet support them](http://code.google.com/p/robotframework-ride/issues/detail?id=1182).

### Enhancements to running keywords dynamically ###

  * New `Run Keyword And Return Status` keyword was added to return true/false depending on the keyword status ([issue 1302](https://code.google.com/p/robotframework/issues/detail?id=1302)). It is easier to use than old `Run Keyword And Ignore Error` in many cases, especially with `Run Keyword If`.
  * `Run Keywords` keyword allows running several keywords with arguments by separating keyword calls with `AND` ([issue 1303](https://code.google.com/p/robotframework/issues/detail?id=1303)).

### Several enhancements to `Telnet` library ###

[Telnet library](TelnetLibrary.md) received plenty of enhancements:

  * Messages are logged so that they get accurate timestamps ([issue 1301](https://code.google.com/p/robotframework/issues/detail?id=1301)).
  * Other encodings than ASCII are supported ([issue 1312](https://code.google.com/p/robotframework/issues/detail?id=1312) and [issue 1310](https://code.google.com/p/robotframework/issues/detail?id=1310)).
  * `Login` keyword was enhanced and its logging fixed ([issue 1314](https://code.google.com/p/robotframework/issues/detail?id=1314)).
  * It is possible to set default log level globally ([issue 1318](https://code.google.com/p/robotframework/issues/detail?id=1318)).
  * Library documentation has been heavily enhanced ([issue 1315](https://code.google.com/p/robotframework/issues/detail?id=1315)).

Some of these enhancements caused potentially backwards-incompatible
changes discussed below.

## Backwards-incompatible changes ##

It is possible that the following changes can cause
backwards-compatibility problems. Most of these changes affect only [Telnet library](TelnetLibrary.md) that was heavily enhanced in this release.

  * All standard libraries use logging API instead of `print` for logging ([issue 1301](https://code.google.com/p/robotframework/issues/detail?id=1301)). This may cause messages to appear in wrong order in log files if you extend these libraries and use `print` for logging. In practice this is likely to cause problems only with `Telnet`. The fix is to start using the logging API with custom libraries extending it.
  * Previously `Telnet` library used ASCII encoding when writing or reading and ignored possible encoding errors. In RF 2.7.6 encoding is configurable ([issue 1312](https://code.google.com/p/robotframework/issues/detail?id=1312)), UTF-8 is used by default, and possible encoding errors are not ignored. As a result there are problems with connections using other than UTF-8 or ASCII encoding (latter is a subset of the former and thus works by default), unless the correct encoding is explicitly specified. This will be fixed in RF 2.7.7 by ignoring encoding errors by default and making the error handler configurable ([issue 1328](https://code.google.com/p/robotframework/issues/detail?id=1328)).
  * `Telnet.Read Until Regexp` keyword fails if a compiled regular expression is used as the last argument. This bug ([issue 1327](https://code.google.com/p/robotframework/issues/detail?id=1327)) will be fixed in RF 2.7.7.
  * `Telnet` library got two new configuration parameters encoding ([issue 1312](https://code.google.com/p/robotframework/issues/detail?id=1312)) and default log level ([issue 1318](https://code.google.com/p/robotframework/issues/detail?id=1318)). As discussed in those issues, custom libraries extending `Telnet` may be affected.
  * `Run Keywords` keyword separates keyword calls with `AND` ([issue 1303](https://code.google.com/p/robotframework/issues/detail?id=1303)). This causes problems in the _very_ unlikely case that you use a keyword with exact this name, including case. Using the keyword e.g. like `And` or escaping it like `\AND` fix the problem.

## Acknowledgements ##

Chris Prinos provided documentation how to debug test execution with
`pdb` ([issue 1282](https://code.google.com/p/robotframework/issues/detail?id=1282)). Thanks also for everyone else who has reported issues,
helped debugging problems, or otherwise made RF 2.7.6 a great release!

## Full list of enhancements and fixes ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1202](https://code.google.com/p/robotframework/issues/detail?id=1202) | Defect   | Critical     | Test execution leaks memory |
| [Issue 1266](https://code.google.com/p/robotframework/issues/detail?id=1266) | Defect   | High         | User keywords return no value if they contain continuable failures |
| [Issue 1277](https://code.google.com/p/robotframework/issues/detail?id=1277) | Defect   | High         | Teardown for user keyword not executed if keyword uses embedded arguments |
| [Issue 1278](https://code.google.com/p/robotframework/issues/detail?id=1278) | Defect   | High         | `Exit For Loop` does not work inside teardowns |
| [Issue 1286](https://code.google.com/p/robotframework/issues/detail?id=1286) | Defect   | High         | Testdoc is broken in RF 2.7.5 |
| [Issue 1018](https://code.google.com/p/robotframework/issues/detail?id=1018) | Enhancement | High         | Alternative `*.robot` extension for test data in plain text files |
| [Issue 1289](https://code.google.com/p/robotframework/issues/detail?id=1289) | Enhancement | High         | Tidy: Split multiline documentation into multiple lines |
| [Issue 1307](https://code.google.com/p/robotframework/issues/detail?id=1307) | Enhancement | High         | Include original error message in suite setup/teardown failed messages |
| [Issue 1271](https://code.google.com/p/robotframework/issues/detail?id=1271) | Defect   | Medium       | `tidy` should not resolve `${CURDIR}` with --recursive |
| [Issue 1280](https://code.google.com/p/robotframework/issues/detail?id=1280) | Defect   | Medium       | Output and xunit files have invalid line endings (\r\r\n) on Windows |
| [Issue 1284](https://code.google.com/p/robotframework/issues/detail?id=1284) | Defect   | Medium       | libdoc: Creating documentation for resource file fails if it has multiple keywords with same name |
| [Issue 1288](https://code.google.com/p/robotframework/issues/detail?id=1288) | Defect   | Medium       | Tags in statistics are not sorted case-insensitively |
| [Issue 1300](https://code.google.com/p/robotframework/issues/detail?id=1300) | Defect   | Medium       | UNC paths are not handled correctly when tests are executed in directory root |
| [Issue 1310](https://code.google.com/p/robotframework/issues/detail?id=1310) | Defect   | Medium       | Telnet library: `Read Until` keywords fail if output contains non-ASCII characters |
| [Issue 1311](https://code.google.com/p/robotframework/issues/detail?id=1311) | Defect   | Medium       | Tests execution freezes with standalone jar at least when using SSHLibrary |
| [Issue 1321](https://code.google.com/p/robotframework/issues/detail?id=1321) | Defect   | Medium       | Recursive for loops can cause corrupted outputs |
| [Issue 1301](https://code.google.com/p/robotframework/issues/detail?id=1301) | Enhancement | Medium       | All standard libraries should use logging API and not print for logging |
| [Issue 1302](https://code.google.com/p/robotframework/issues/detail?id=1302) | Enhancement | Medium       | New `Run Keyword And Return Status` keyword to return true/false depending on keyword status |
| [Issue 1303](https://code.google.com/p/robotframework/issues/detail?id=1303) | Enhancement | Medium       | `Run Keywords` should support running keywords with arguments |
| [Issue 1309](https://code.google.com/p/robotframework/issues/detail?id=1309) | Enhancement | Medium       | Tidy: Option to specify line separator (and fix default line separators on Windows) |
| [Issue 1312](https://code.google.com/p/robotframework/issues/detail?id=1312) | Enhancement | Medium       | Telnet library: Possibility to specify encoding |
| [Issue 1282](https://code.google.com/p/robotframework/issues/detail?id=1282) | Documentation | Medium       | Document how to debug execution with `pdb` in User Guide |
| [Issue 1315](https://code.google.com/p/robotframework/issues/detail?id=1315) | Documentation | Medium       | Telnet library: Better library documentation |
| [Issue 1304](https://code.google.com/p/robotframework/issues/detail?id=1304) | Defect   | Low          | `Screenshot` library should not create wx app references in module level |
| [Issue 1306](https://code.google.com/p/robotframework/issues/detail?id=1306) | Defect   | Low          | Parsing modules should preserve all comment characters |
| [Issue 1308](https://code.google.com/p/robotframework/issues/detail?id=1308) | Defect   | Low          | Parsing modules do not preserve comments after FOR loop declaration |
| [Issue 1314](https://code.google.com/p/robotframework/issues/detail?id=1314) | Defect   | Low          | Telnet library: Fixes and enhancements to `Login` keyword |
| [Issue 1317](https://code.google.com/p/robotframework/issues/detail?id=1317) | Defect   | Low          | `ELSE IF`, `ELSE` and `AND` are not always escaped properly |
| [Issue 1320](https://code.google.com/p/robotframework/issues/detail?id=1320) | Defect   | Low          | Dry-run mode fails if `Set Global/Suite/Test Variable`, `Variable Should (Not) Exist`, or `Get Variable Value` is used with escaped variable |
| [Issue 1281](https://code.google.com/p/robotframework/issues/detail?id=1281) | Enhancement | Low          | Argument files should support '=' and any number of spaces as separator between options and values |
| [Issue 1293](https://code.google.com/p/robotframework/issues/detail?id=1293) | Enhancement | Low          | Warn when using invalid run-mode |
| [Issue 1318](https://code.google.com/p/robotframework/issues/detail?id=1318) | Enhancement | Low          | Telnet library: Possibility to set default log level globally |

Altogether 32 issues.

# Robot Framework 2.7.7 #

Robot Framework 2.7.7 contains enhanced reports and logs as well as enhancements and fixes to Telnet library and elsewhere. It was released
on Tuesday 26th of February, 2013.

## Most important fixes and enhancements ##

### Hiding columns in test details table ###

It is nowadays possible to hide columns in test details table of a report
by clicking a small `x` on column headers ([issue 1362](https://code.google.com/p/robotframework/issues/detail?id=1362)). Columns are
hidden persistently, based on a domain, and it is always easy to show
them again by clicking "..." on the closed header. Persistently hiding columns works also with local files except with Internet Explorer.

### General performance and style enhancements to report and log ###

There were several performance and style enhancements to reports and logs ([issue 1368](https://code.google.com/p/robotframework/issues/detail?id=1368)):

  * Test details table of a report is rendered at least three times faster than earlier. The difference is noticeable especially when there are a lot of test cases.
  * Rows in test details table have a maximum height. Scrollbars are added if content does not fit otherwise.
  * Long words are split into multiple rows both in report and log even if they do not contain spaces. This prevents text from overflowing horizontally.
  * When opening a suite, a test or a keyword in a log file via a link, the opened item is highlighted briefly.
  * `Expand All` button in log files got better styles.
  * Expanding large test suites in log files is faster.

### Enhancements and fixes to `Telnet` library ###

[Telnet library](TelnetLibrary.md) was [heavily enhanced in version 2.7.6](#Several_enhancements_to_Telnet_library.md). Unfortunately some of these changes caused regressions ([issue 1327](https://code.google.com/p/robotframework/issues/detail?id=1327) and [issue 1371](https://code.google.com/p/robotframework/issues/detail?id=1371)) as well as backwards-incompatibility problems related to encoding ([issue 1328](https://code.google.com/p/robotframework/issues/detail?id=1328)). In addition to fixes to these problems, Telnet library in RF 2.7.7 also contains few new enhancements:

  * Possibility to select error handler when encoding sent/received data fails (part of [issue 1328](https://code.google.com/p/robotframework/issues/detail?id=1328)).
  * Possibility to disable encoding altogether ([issue 1351](https://code.google.com/p/robotframework/issues/detail?id=1351)).
  * Writing low level network traffic into the log file using TRACE level ([issue 1358](https://code.google.com/p/robotframework/issues/detail?id=1358)).

## Backwards-incompatible changes ##

[Telnet library](TelnetLibrary.md) got new `encoding_errors` argument ([issue 1328](https://code.google.com/p/robotframework/issues/detail?id=1328)) before the recently added `default_log_level` argument. This is a backwards-incompatible change, but it is very unlikely that anyone uses `default_log_level` in a way that it would actually cause problems.

## Acknowledgements ##

Guy Kisel documented how to use decorators when creating custom test
libraries ([issue 1343](https://code.google.com/p/robotframework/issues/detail?id=1343)) and Mike provided a patch for Remote library to
report connection errors better ([issue 1334](https://code.google.com/p/robotframework/issues/detail?id=1334)). Thanks also for everyone
else who has reported issues, helped debugging problems, or otherwise
made 2.7.7 the best Robot Framework release so far!

## Full list of enhancements and fixes ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1327](https://code.google.com/p/robotframework/issues/detail?id=1327) | Defect   | High         | Telnet: Compiled regular expression argument fails `Read Until Regexp` keyword (regression) |
| [Issue 1328](https://code.google.com/p/robotframework/issues/detail?id=1328) | Enhancement | High         | Telnet library: Encoding errors should be ignored by default and error handler should be configurable |
| [Issue 1362](https://code.google.com/p/robotframework/issues/detail?id=1362) | Enhancement | High         | Report: Possibility to hide columns in test details table |
| [Issue 1368](https://code.google.com/p/robotframework/issues/detail?id=1368) | Enhancement | High         | Performance and style enhancements to report and log |
| [Issue 1269](https://code.google.com/p/robotframework/issues/detail?id=1269) | Defect   | Medium       | `Get Time` with `UTC` option does not work correctly when daylight saving time is not used |
| [Issue 1331](https://code.google.com/p/robotframework/issues/detail?id=1331) | Defect   | Medium       | Windows installer: Avoid "close failed in file object destructor" error when UAC disabled |
| [Issue 1335](https://code.google.com/p/robotframework/issues/detail?id=1335) | Defect   | Medium       | robot.api.logging.console should flush standard output after writing |
| [Issue 1354](https://code.google.com/p/robotframework/issues/detail?id=1354) | Defect   | Medium       | Dry-run: Library keywords as suite teardowns are always considered failed |
| [Issue 1360](https://code.google.com/p/robotframework/issues/detail?id=1360) | Defect   | Medium       | Testdoc prints errors from ${CURDIR} and non-existing variables |
| [Issue 1371](https://code.google.com/p/robotframework/issues/detail?id=1371) | Defect   | Medium       | Telnet: `Login` keyword does not work when using Microsoft Telnet Service (regression) |
| [Issue 1339](https://code.google.com/p/robotframework/issues/detail?id=1339) | Enhancement | Medium       | `Set Suite Metadata` and `Set Suite Documentation` keywords should allow setting metadata/doc of the top level suite |
| [Issue 1348](https://code.google.com/p/robotframework/issues/detail?id=1348) | Enhancement | Medium       | `Set Test Message`, `Set Test Documentation`, `Set Suite Documentation`, and `Set Suite Metadata` should allow appending to the existing value |
| [Issue 1353](https://code.google.com/p/robotframework/issues/detail?id=1353) | Enhancement | Medium       | String library: New keywords for converting between Unicode and byte strings and for verifying string types |
| [Issue 1358](https://code.google.com/p/robotframework/issues/detail?id=1358) | Enhancement | Medium       | Telnet: Write telnetlib's debug messages into log file using TRACE level |
| [Issue 1357](https://code.google.com/p/robotframework/issues/detail?id=1357) | Documentation | Medium       | OperatingSystem library: Document that `Stop Process` and `Stop All Process` don't wait for processes to complete |
| [Issue 1323](https://code.google.com/p/robotframework/issues/detail?id=1323) | Defect   | Low          | Libdoc creates broken output if generating fails for some reason |
| [Issue 1326](https://code.google.com/p/robotframework/issues/detail?id=1326) | Defect   | Low          | Error contains empty suite name when executing/processing multiple suites and no matching tests found |
| [Issue 1332](https://code.google.com/p/robotframework/issues/detail?id=1332) | Defect   | Low          | Minor glitch in log/report if URLs or quotes are used test and keyword names |
| [Issue 1333](https://code.google.com/p/robotframework/issues/detail?id=1333) | Defect   | Low          | Using Tidy with directory fails with an exception (unless using --recursive) |
| [Issue 1350](https://code.google.com/p/robotframework/issues/detail?id=1350) | Defect   | Low          | Not possible to specify argument file together with option like `--argumentfile=args.txt` or `-Aargs.txt` |
| [Issue 1355](https://code.google.com/p/robotframework/issues/detail?id=1355) | Defect   | Low          | Testdoc output is broken if `</script>` is used in test data |
| [Issue 1361](https://code.google.com/p/robotframework/issues/detail?id=1361) | Defect   | Low          | Report: Inconvenient to open links in test details and statistics table on background tab |
| [Issue 1334](https://code.google.com/p/robotframework/issues/detail?id=1334) | Enhancement | Low          | `Remote` library should report the address of the server if connecting fails |
| [Issue 1351](https://code.google.com/p/robotframework/issues/detail?id=1351) | Enhancement | Low          | Telnet: Possibility to disable encoding/decoding written/read text |
| [Issue 1343](https://code.google.com/p/robotframework/issues/detail?id=1343) | Documentation | Low          | Explain how to use Python decorators in User Guide |
| [Issue 1345](https://code.google.com/p/robotframework/issues/detail?id=1345) | Documentation | Low          | Installation: Document that directories in `PATH` should not be quoted |

Altogether 26 issues.