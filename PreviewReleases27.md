

# Robot Framework 2.7 Preview Releases #

Robot Framework 2.7 is a new major release with loads of bigger
and smaller enhancements and bug fixes. Before the final release there
will be some alpha, beta, and release candidate releases in order

  * to make the already implemented features available to users,
  * to get feedback about the new features and enhancements, and
  * to allow users to test the new version on their environments.

Please submit possible bugs you encounter with the preview releases to
the [issue tracker](http://code.google.com/p/robotframework/issues/list)
and send general comments and questions to the [mailing lists](MailingLists.md).

## Downloads and installation ##

The latest pre-release is always available on the
[download page](http://code.google.com/p/robotframework/downloads/list).

You can follow the normal [installation instructions](Installation.md)
when installing RF 2.7 releases. If you have an earlier Robot version installed
it should be safe to install over it. Removing the old version first is always
safer, though, and should always be done if installation fails or running
tests always fails mysteriously.

## Compatibility with RIDE ##

Latest [RIDE](https://github.com/robotframework/RIDE) versions
are not anymore dependent on the installed Robot Framework version. It
is thus safe to install RF 2.7 releases alongside RIDE.

# Most important enhancements and new features #

## Faster and more memory efficient log and report generation ##

In [Robot Framework 2.6](ReleaseNotes26.md) logs and reports were heavily
enhanced, and nowadays they can contain huge amount of data and still
open to browsers fast and be responsive. The next bottleneck with huge
amounts of data was that generating logs and reports took a lot of time
and computer resources.

In Robot Framework 2.7 log/report generation performance with the
included `rebot` tool after test execution has been greatly
enhanced. Exact improvements depend on the actual data, but based on
several data points both `rebot` execution time and memory consumption
have dropped about 50% compared to RF 2.6.  Creating logs and reports
as part of the test execution is also about 10% faster.

With larger data sets these enhancements can mean that you get results
several minutes faster and generating them takes gigabytes less
memory.

## New installation and start-up system -- `pip` and IronPython are supported ##

Robot Framework installation and start-up have been changed heavily internally. The biggest enhancements and other changes compared to earlier version are listed below. For more information see [new installation instructions](NewInstallation.md) and [issue 480](https://code.google.com/p/robotframework/issues/detail?id=480).

  1. Installation using `pip` is finally supported ([issue 885](https://code.google.com/p/robotframework/issues/detail?id=885)).
  1. Installation using IronPython is officially supported. As a result you get new `ipybot` and `ipyrebot` start-up scripts.
  1. Installation using Jython creates new `jyrebot` start-up script in addition to `jybot`.
  1. Installing from source using Python **does not** create `jybot` script anymore. You need to install the framework using Jython to create it.
  1. All start-up scripts (`pybot`, `rebot`, `jybot`, ...) require the appropriate interpreter to be in `PATH`.
  1. Outside Windows, start-up scripts are implemented in Python to ease using them with virtualenv ([issue 1057](https://code.google.com/p/robotframework/issues/detail?id=1057)).
  1. Source distribution only contains actual source code and tools ([issue 1037](https://code.google.com/p/robotframework/issues/detail?id=1037)).

## Public APIs documented ##

There is quire often a need to use Robot Framework's modules by external tools. So far this has been problematic because the APIs have not been documented too much, public APIs have not been separated from internal APIs, and API documentation has not been available anywhere.

All this is changing. Nowadays the API documentation is available at http://robot-framework.readthedocs.org/ ([issue 482](https://code.google.com/p/robotframework/issues/detail?id=482)) and public entry points are listed separately and also documented ([issue 831](https://code.google.com/p/robotframework/issues/detail?id=831)). Comments and enhancement requests related to the API docs are highly appreciated on [mailing lists](MailingLists.md) and [issue tracker](http://code.google.com/p/robotframework/issues/list).

## Library documentation tool `libdoc` is bundled with core framework ##

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
also show library and resource documentation on the console. It has
special commands to list available keywords, show documentation of a
specific keyword or whole library/resource, and to display the library
version.

For more information and examples run `python -m robot.libdoc --help`
and see `libdoc` section in the [User Guide](UserGuide.md).

## Test data documentation tool `testdoc` fixed and bundled with core framework ##

`testdoc` generates a high level test documentation based on Robot
Framework test data. It has earlier been available as a
[separate tool](TestDataDocumentationTool.md) but it has not been
compatible with Robot Framework 2.6 ([issue 908](https://code.google.com/p/robotframework/issues/detail?id=908)). Now it is fixed and
also bundled with the core framework similarly as `libdoc`. It can be
executed after normal installation like `python -m robot.testdoc` and
it also has an entry point in the JAR distribution.

For more information and examples run `python -m robot.testdoc --help`
and see `testdoc` section in the [User Guide](UserGuide.md).

## New built-in tool `tidy` for cleaning up data and changing data format ##

`tidy` is a new tool for cleaning up test data and changing test data
format between plain text, HTML and TSV ([issue 801](https://code.google.com/p/robotframework/issues/detail?id=801)). Similarly as
`libdoc` and `testdoc` it is a built-in tool included in the normal
installation. It can be executed like `python -m robot.tidy` and it
also has an entry point in the JAR distribution.

For more information and examples run `python -m robot.tidy --help`
and see `tidy` section in the [User Guide](UserGuide.md).

## Enhancements for suite, test, and keyword documentation ##

  * Creating multi-line documentation in test data is easier (see [issue 1009](https://code.google.com/p/robotframework/issues/detail?id=1009) and [User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#representing-newlines))
  * Custom links and embedded images are supported (see [issue 1076](https://code.google.com/p/robotframework/issues/detail?id=1076) and [User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#custom-links-and-images))
  * Preformatted text is supported (see [issue 447](https://code.google.com/p/robotframework/issues/detail?id=447) and [User Guide](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#preformatted-text))
  * Suite and test documentation are available dynamically via `${SUITE DOCUMENTATION}` and `${TEST DOCUMENTATION}` variables and can be set with `Set Suite Documentation` and `Set Test Documentation` keywords (see [issue 1077](https://code.google.com/p/robotframework/issues/detail?id=1077) and [issue 1078](https://code.google.com/p/robotframework/issues/detail?id=1078))

## Several `--RemoveKeywords` enhancements ##

`--RemoveKeywords` command line option allows removing unnecessary
keywords from outputs to make their size smaller. It has been enhanced
multiple ways in RF 2.7 and nowadays it

  * works also when executing tests and not only with `rebot` ([issue 1027](https://code.google.com/p/robotframework/issues/detail?id=1027)),
  * can remove keywords inside for loops ([issue 990](https://code.google.com/p/robotframework/issues/detail?id=990)),
  * can remove keywords inside `Wait Until Keyword Succeeds` keyword ([issue 1007](https://code.google.com/p/robotframework/issues/detail?id=1007)), and
  * adds a message when it has removed keywords ([issue 1008](https://code.google.com/p/robotframework/issues/detail?id=1008)).

# Backwards incompatible changes and deprecated features #

There are several backwards incompatible changes in RF 2.7 but none of them should be too severe.

## Internal modules related to test result processing changed ##

Enhancing performance of `rebot` ([issue 865](https://code.google.com/p/robotframework/issues/detail?id=865)) required large changes to the modules used for processing test results. There are two main changes:

  1. `robot.output.TestSuite` entry point mentioned also in the User Guide has been removed. Instead there is new `robot.result.ExecutionResult`.
  1. The suite model itself has changed slightly. For example, TestCase.critical is nowadays Boolean True or False when it used to string 'yes' or 'no'.

## Handling suite, test, and keyword documentation changed ##

Nowadays suite, test, and keyword documentation split into multiple rows is automatically catenated with a newline instead of a space ([issue 1009](https://code.google.com/p/robotframework/issues/detail?id=1009)). This eases creating multiline documentation, but can also format existing documentation differently than earlier.

In practice this should not matter that much because documentation does not affect actual test execution. Also, no extra newline is added if the line already ends with a literal newline (`\n`). If the automatic newlines cause problems, it is possible to prevent them by ending a documentation row with a single backslash (`\`).

Documentation syntax also changed a little and it is now possible to create custom links or embed images using syntax `[link|content]`. This can only cause problems if someone has a pipe character between square brackets in documentation for some other reason.

## Source distribution does not contain documentation ##

Including documentation such as [User Guide](UserGuide.md) and [Quick Start Guide](QuickStartGuide.md) increased the size of the source distribution considerably. When installing the framework using a package manager such as pip or easy\_install, the source distribution was downloaded automatically and user never even saw the documentation.

To make the source distribution smaller, all extra content was removed. Nowadays it contains only the actual source code and [supporting tools](SupportingTools.md) ([issue 1037](https://code.google.com/p/robotframework/issues/detail?id=1037)) and the size dropped from 2.5MB to 0.5MB. All documentation is still available online and as separate downloads.

## Changes to programmatic execution APIs ##

  * `robot.run_rebot` method was renamed to `robot.rebot` ([issue 1044](https://code.google.com/p/robotframework/issues/detail?id=1044))
  * `robot.run` and `robot.rebot` return an error code if there are failures instead of raising exceptions ([issue 1045](https://code.google.com/p/robotframework/issues/detail?id=1045))
  * `robot.run_from_cli` and `robot.rebot_from_cli` method renamed to `robot.run_cli` and `robot.rebot_cli` and changed so that they don't need usage as an argument

## New built-in variables may class with existing variables with same name ##

New built-in variables `${KEYWORD STATUS}` and `${KEYWORD MESSAGE}` ([issue 1040](https://code.google.com/p/robotframework/issues/detail?id=1040)) and `${TEST DOCUMENTATION}` and `${SUITE DOCUMENTATION}` ([issue 1077](https://code.google.com/p/robotframework/issues/detail?id=1077)) may potentially clash with existing variables with same name. That should be pretty rare because the former two are available only in keyword teardowns and the latter two updated only when a test or a suite starts.

## Extended variable assign syntax may clash with existing variables ##

It is nowadays possible to set attributes of variables containing objects using a variation of the extended variable syntax like `${var.attr} =  My Keyword  arg` ([issue 1059](https://code.google.com/p/robotframework/issues/detail?id=1059)). This new syntax may cause problems if you have used dots in variable names. In practice problems should be rare, because most of the variables are strings and this syntax does not work with strings at all.

## Un-used `--SplitOutputs`, `--Summary`, and `--SummaryTitle` options removed ##

Functionality behind these options were removed already in RF 2.6 but the options were left for backwards compatibility reasons. Now they are removed and trying to use them causes an error.

## `robot/runner.py` deprecated in favor of `robot/run.py` ##

The `robot/runner.py` command line entry point has been renamed to `robot/run.py` ([issue 1044](https://code.google.com/p/robotframework/issues/detail?id=1044)). The old entry point works still in 2.7 but using it causes a deprecation warning.

# Acknowledgements #

Big thanks for everyone who has tested the preview releases. Several nasty regressions have been found and fixed thanks to your bug reports.

Thanks to Imran for suggesting and implementing [issue 1015](https://code.google.com/p/robotframework/issues/detail?id=1015): Attribute source to be passed on start/end suite listener methods	.

# Robot Framework 2.7 Alpha 1 #

The first RF 2.7 pre-release was releases on Thursday 2012-01-12. List
of all issues included into it can be found below. We are eagerly
waiting for feedback!

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 865](https://code.google.com/p/robotframework/issues/detail?id=865) | Enhancement | Critical     | Faster and more memory efficient log and report generation with rebot |
| [Issue 1003](https://code.google.com/p/robotframework/issues/detail?id=1003) | Defect   | High         | Log time differs from system time |
| [Issue 551](https://code.google.com/p/robotframework/issues/detail?id=551) | Defect   | Medium       | Recursive user keywords can break the whole test execution |
| [Issue 979](https://code.google.com/p/robotframework/issues/detail?id=979) | Defect   | Medium       | If a library implemented as a directory is in execution directory, importing it can result in corrupted library with Python 2.5 and 2.6 |
| [Issue 985](https://code.google.com/p/robotframework/issues/detail?id=985) | Defect   | Medium       | Logging with logging API when timeout is used does not work |
| [Issue 986](https://code.google.com/p/robotframework/issues/detail?id=986) | Defect   | Medium       | --tagdoc doesn't work if tag has underscore in name |
| [Issue 988](https://code.google.com/p/robotframework/issues/detail?id=988) | Defect   | Medium       | Variables used in embedded argument syntax leak to caller |
| [Issue 998](https://code.google.com/p/robotframework/issues/detail?id=998) | Defect   | Medium       | `logging` module is configured to emit messages with unnecessarily low level |
| [Issue 1022](https://code.google.com/p/robotframework/issues/detail?id=1022) | Defect   | Medium       | Setting non-string message to tests with `BuiltIn.Set Test Message` keyword crashes execution |
| [Issue 1029](https://code.google.com/p/robotframework/issues/detail?id=1029) | Defect   | Medium       | RunnerFactory returns instance with the same state on multiple invocations |
| [Issue 647](https://code.google.com/p/robotframework/issues/detail?id=647) | Enhancement | Medium       | Comments are not handled well in parsing model |
| [Issue 675](https://code.google.com/p/robotframework/issues/detail?id=675) | Enhancement | Medium       | DryRun should support `Import Library` keyword |
| [Issue 871](https://code.google.com/p/robotframework/issues/detail?id=871) | Enhancement | Medium       | Timeout speed optimization |
| [Issue 1011](https://code.google.com/p/robotframework/issues/detail?id=1011) | Enhancement | Medium       | Add keyword 'Split String To Characters' keyword |
| [Issue 1015](https://code.google.com/p/robotframework/issues/detail?id=1015) | Enhancement | Medium       | Attribute source to be passed on start/end suite listener methods |
| [Issue 1031](https://code.google.com/p/robotframework/issues/detail?id=1031) | Enhancement | Medium       | Log: Keep noncritically failed tests closed |
| [Issue 510](https://code.google.com/p/robotframework/issues/detail?id=510) | Defect   | Low          | Output files use Unix line endings on Windows |
| [Issue 920](https://code.google.com/p/robotframework/issues/detail?id=920) | Defect   | Low          | Statistics graph sometimes has a small gray area at the end |
| [Issue 982](https://code.google.com/p/robotframework/issues/detail?id=982) | Defect   | Low          | Hexadecimal HTML entiry references (e.g. &#x2603;) are not parsed correctly |
| [Issue 1019](https://code.google.com/p/robotframework/issues/detail?id=1019) | Enhancement | Low          | Cleaner error message when importing test libraries or variable files fails |

Altogether 20 issues.

# Robot Framework 2.7 Alpha 2 #

The second RF 2.7 pre-release was released on Friday 2012-02-03. The most
important changes from first alpha is full support for IronPython via the new
installation and start-up system. The new system also fixes the previous
incompatibility with pip.  In addition, `tidy`, a tool for cleaning up and
changing format of test data files is included. List of all issues included
into alpha2 release can be found below.

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 885](https://code.google.com/p/robotframework/issues/detail?id=885) | Defect   | High         | Installation using pip does not work |
| [Issue 480](https://code.google.com/p/robotframework/issues/detail?id=480) | Enhancement | High         | New installation and start-up system |
| [Issue 801](https://code.google.com/p/robotframework/issues/detail?id=801) | Enhancement | High         | Built-in `robot.tidy` tool for changing format and cleaning-up test data |
| [Issue 59](https://code.google.com/p/robotframework/issues/detail?id=59) | Enhancement | Medium       | Support capturing stdout and stderr when running Robot and Rebot programmatically |
| [Issue 759](https://code.google.com/p/robotframework/issues/detail?id=759) | Enhancement | Medium       | It should be possible to save parsed data to disk and memory |
| [Issue 775](https://code.google.com/p/robotframework/issues/detail?id=775) | Enhancement | Medium       | Allow specifying `Test Timeout` in suite init files |
| [Issue 1044](https://code.google.com/p/robotframework/issues/detail?id=1044) | Enhancement | Medium       | Rename `robot/runner.py` script to `robot/run.py` and `robot.run_rebot` method to `robot.rebot` |
| [Issue 1046](https://code.google.com/p/robotframework/issues/detail?id=1046) | Enhancement | Medium       | Log: Allow opening suites, tests and keywords by clicking anywhere in the header |
| [Issue 1047](https://code.google.com/p/robotframework/issues/detail?id=1047) | Enhancement | Medium       | Command line help for robotframework.jar |
| [Issue 1045](https://code.google.com/p/robotframework/issues/detail?id=1045) | Defect   | Low          | `robot.run` and `robot.run_rebot` methods leave framework to inconsistent state if they fail |
| [Issue 1036](https://code.google.com/p/robotframework/issues/detail?id=1036) | Enhancement | Low          | expose `TxtReader._split_row` as a public function |
| [Issue 1048](https://code.google.com/p/robotframework/issues/detail?id=1048) | Enhancement | Low          | Remove un-used --SplitOutputs, --Summary, and --SummaryTitle options |
| [Issue 1043](https://code.google.com/p/robotframework/issues/detail?id=1043) | Documentation | Low          | Document that Dialogs library doesn't work with Timeouts in Python |

Altogether 13 issues.

# Robot Framework 2.7 Beta 1 #

The first and hopefully last RF 2.7 beta release adds several
enhancements and few bug fixes. The most important new features are
bundling `libdoc` with the core framework ([issue 1028](https://code.google.com/p/robotframework/issues/detail?id=1028)) and several
enhancements to `--RemoveKeywords` option ([issue 990](https://code.google.com/p/robotframework/issues/detail?id=990), [issue 1007](https://code.google.com/p/robotframework/issues/detail?id=1007),
[issue 1008](https://code.google.com/p/robotframework/issues/detail?id=1008), [issue 1027](https://code.google.com/p/robotframework/issues/detail?id=1027)). RF 2.7 beta 1 was released on Friday
2012-02-17.

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1028](https://code.google.com/p/robotframework/issues/detail?id=1028) | Enhancement | High         | `libdoc` should be bundled with Robot Framework core |
| [Issue 1049](https://code.google.com/p/robotframework/issues/detail?id=1049) | Defect   | Medium       | Environment variable related keywords and %{NAME} variable do not encode non-ASCII strings correctly |
| [Issue 1051](https://code.google.com/p/robotframework/issues/detail?id=1051) | Defect   | Medium       | `Should Be Equal` and other similar keywords fail to compare non-ASCII byte values |
| [Issue 800](https://code.google.com/p/robotframework/issues/detail?id=800) | Enhancement | Medium       | Robot Framework jar should have entry point for libdoc |
| [Issue 990](https://code.google.com/p/robotframework/issues/detail?id=990) | Enhancement | Medium       | Improve `--RemoveKeywords` so that it can remove keywords from for loops |
| [Issue 1007](https://code.google.com/p/robotframework/issues/detail?id=1007) | Enhancement | Medium       | Enhance `--RemoveKeywords` so that it can remove unnecessary keywords inside `Wait Until Keyword Succeeds` |
| [Issue 1008](https://code.google.com/p/robotframework/issues/detail?id=1008) | Enhancement | Medium       | `--RemoveKeywords` should log message when it removes keywords |
| [Issue 1027](https://code.google.com/p/robotframework/issues/detail?id=1027) | Enhancement | Medium       | `--RemoveKeywords` option should also work when running tests |
| [Issue 1053](https://code.google.com/p/robotframework/issues/detail?id=1053) | Enhancement | Medium       | Log: `Expand All` functionality for individual keywords |
| [Issue 447](https://code.google.com/p/robotframework/issues/detail?id=447) | Enhancement | Low          | `libdoc` should support preformatted text  |
| [Issue 1052](https://code.google.com/p/robotframework/issues/detail?id=1052) | Enhancement | Low          | Internal id of tests and suites should be added to XML output |
| [Issue 1056](https://code.google.com/p/robotframework/issues/detail?id=1056) | Enhancement | Low          | New keywords `Get Environment Variables` and `Log Environment Variables` to `OperatingSystem` library. |
| [Issue 1057](https://code.google.com/p/robotframework/issues/detail?id=1057) | Enhancement | Low          | Show red failure texts using bold to make them easier to notice for color blind |
| [Issue 1058](https://code.google.com/p/robotframework/issues/detail?id=1058) | Enhancement | Low          | `OperatingSystem.Remove Environment Variable` should allow removing multiple variables |

Altogether 14 issues.

# Robot Framework 2.7 Beta 2 #

Another RF 2.7 beta release was needed but now all the features and fixes
to be included into the final release ought to be done. This is not yet
a release candidate as we are going to do some internal clean-up
and also some documentation related issues are still open.

The most important new enhancements in beta 2 are fixing `testdoc`
([issue 908](https://code.google.com/p/robotframework/issues/detail?id=908)) and bundling it with the core framework ([issue 1064](https://code.google.com/p/robotframework/issues/detail?id=1064)). RF
2.7 beta 2 was released on Wednesday 2012-02-29.

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 908](https://code.google.com/p/robotframework/issues/detail?id=908) | Defect   | High         | `testdoc` tool is broken in RF 2.6 |
| [Issue 1064](https://code.google.com/p/robotframework/issues/detail?id=1064) | Enhancement | High         | `testdoc` should be bundled with core framework |
| [Issue 1054](https://code.google.com/p/robotframework/issues/detail?id=1054) | Enhancement | Medium       | Convert start-up script to Python outside Windows to ease using them on virtualenv |
| [Issue 1009](https://code.google.com/p/robotframework/issues/detail?id=1009) | Enhancement | Medium       | Ease creating multiline documentation or metadata values. |
| [Issue 1021](https://code.google.com/p/robotframework/issues/detail?id=1021) | Enhancement | Medium       | Support variable files based on Python and Java classes |
| [Issue 1040](https://code.google.com/p/robotframework/issues/detail?id=1040) | Enhancement | Medium       | New automatic variables `${KEYWORD STATUS}` and `${KEYWORD MESSAGE}` to know keyword status in keyword teardown |
| [Issue 1061](https://code.google.com/p/robotframework/issues/detail?id=1061) | Enhancement | Medium       | Support for `libdoc` to show library/resource information on console |
| [Issue 1066](https://code.google.com/p/robotframework/issues/detail?id=1066) | Enhancement | Medium       | Show notification on console when a top-level keyword ends |

Altogether 8 issues.

# Robot Framework 2.7 Release Candidate 1 #

RF 2.7 rc 1 contains some last minute enhancements and fixes as well
as all the internal clean-ups and refactorings planned for the final
release. Most important new features are adding support for custom
links and embedded images in documentation ([issue 1076](https://code.google.com/p/robotframework/issues/detail?id=1076)) and
dynamically retrieving and setting test and suite documentation ([issue 1077](https://code.google.com/p/robotframework/issues/detail?id=1077)
and [issue 1078](https://code.google.com/p/robotframework/issues/detail?id=1078)). All the [supporting tools](SupportingTools.md)
distributed with the framework are also fixed ([issue 1074](https://code.google.com/p/robotframework/issues/detail?id=1074)).

RF 2.7 rc 1 was released on Thursday 2012-03-08.

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 1076](https://code.google.com/p/robotframework/issues/detail?id=1076) | Enhancement | High         | Support for custom links and images in suite/test/keyword documentation and suite metadata |
| [Issue 1030](https://code.google.com/p/robotframework/issues/detail?id=1030) | Defect   | Medium       | Resources file changes are not picked up during multiple executions with jython |
| [Issue 1072](https://code.google.com/p/robotframework/issues/detail?id=1072) | Defect   | Medium       | `--TagStatInclude` and `--TagStatExclude` do not ignore underscores |
| [Issue 1079](https://code.google.com/p/robotframework/issues/detail?id=1079) | Defect   | Medium       | Exception shown on console if libraries register `logging.StreamHandler` using `sys.stderr` |
| [Issue 1059](https://code.google.com/p/robotframework/issues/detail?id=1059) | Enhancement | Medium       | Support for "extended assign" like `${var.attr} =    Some Keyword` |
| [Issue 1077](https://code.google.com/p/robotframework/issues/detail?id=1077) | Enhancement | Medium       | New built in variables ${TEST DOCUMENTATION} and ${SUITE DOCUMENTATION} |
| [Issue 1078](https://code.google.com/p/robotframework/issues/detail?id=1078) | Enhancement | Medium       | New keywords to Builtin-library: "Set test documentation" and "Set suite documentation"  |
| [Issue 1080](https://code.google.com/p/robotframework/issues/detail?id=1080) | Defect   | Low          | Execution fails on Python 2.5.0 |

Altogether 8 issues.