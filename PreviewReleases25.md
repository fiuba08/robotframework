

# Robot Framework 2.5 Preview Releases #

Robot Framework (RF) 2.5 is a new major release with loads of bigger and smaller enhancements and bug fixes. Before the final release there will be some alpha, beta, and release candidate releases in order to:

  * make the already implemented features available to users,
  * get feedback from the new features, and
  * allow users to test the new version on their environments.

[RF 2.5 apha 1](#Robot_Framework_2.5_Alpha_1.md) was released on 2010-05-06, and
[RF 2.5 release candidate 1](#Robot_Framework_2.5_Release_Candidate_1.md) on 2010-05-31.
The final [Robot Framework 2.5](ReleaseNotes25.md) version was released on 2010-06-10.

Please submit possible bugs you encounter with the preview releases to the
[issue tracker](http://code.google.com/p/robotframework/issues/list), and send general
comments and questions to the [mailing lists](MailingLists.md).

# Downloads #

The latest pre-release is always available on the
[download page](http://code.google.com/p/robotframework/downloads/list).

# Most important new features #

## Continuing test execution on failure ##

Being able to continue the test execution after failures was the most requested feature in RF 2.5. There are several ways to accomplish it:

  * Raising a _continuable_ exception from a test library ([issue 137](https://code.google.com/p/robotframework/issues/detail?id=137))
  * Using `Run Keyword And Continue On Failure` keyword ([issue 545](https://code.google.com/p/robotframework/issues/detail?id=545))
  * In teardowns all keywords are executed automatically ([issue 544](https://code.google.com/p/robotframework/issues/detail?id=544))

In all these cases the test will be marked failed at the end. Its final error message is created by combining the messages from the occurred failures together.

## Stopping test execution gracefully ##

Another important test execution related feature is the ability to stop the test execution fully so that reports and logs are generated. Nowadays there are several ways to do it:

  * Pressing `Ctrl-C` ([issue 108](https://code.google.com/p/robotframework/issues/detail?id=108))
  * Using signals `SIGINT` and `SIGTERM` ([issue 349](https://code.google.com/p/robotframework/issues/detail?id=349))
  * Raising a _fatal_ exception from a test library ([issue 366](https://code.google.com/p/robotframework/issues/detail?id=366))
  * Using `Fatal Error` keyword ([issue 546](https://code.google.com/p/robotframework/issues/detail?id=546))

## Support for named arguments ##

The named arguments syntax ([issue 215](https://code.google.com/p/robotframework/issues/detail?id=215)) makes it possible to use keywords that have several arguments with default values so that only certain arguments are overridden.
For example, the keyword below could be used like `| Named Arg Example | zap=42 |` and first two arguments would get their default values.

```
  def named_arg_example(foo=1, bar=2, zap=3):
      print foo, bar, zap
```

## Possibility to specify test template to ease data-driven testing ##

**NOTE:** This is a new feature in RF 2.5 release candidate 1.

Test templates ([issue 500](https://code.google.com/p/robotframework/issues/detail?id=500)) allow specifying the keyword to use in test
cases only once. This makes data-driven testing, where the same
keyword is executed with the same input and/or output values, easier
and reduces duplication. An added benefit is that when a test has
multiple steps, all of them will be executed even if one of the steps
fails.

This functionality can be enabled for all tests in a file with in the
setting table with the setting `Test Template` or for individual tests
with the setting `[Template]`. The example below illustrates the
latter usage.

```
***Test Case***
Invalid login
    [Template]  Login with invalid user name and password should fail
    ${VALID USER}  invalid password
    invalid user   ${VALID PASSWORD}
    invalid user   xxx
    ${VALID USER}  ${EMPTY}
    ${EMPTY}       ${VALID PASSWORD}
    ${EMPTY}       ${EMPTY}
```

## Possibility to validate test data using dry-run ##

A new command line option `--runmode dryrun` was added to support validation of test data without actually executing the lowest level keywords ([issue 452](https://code.google.com/p/robotframework/issues/detail?id=452)).

## Full Jython 2.5 support ##

Robot Framework 2.1.3 already works with Jython 2.5 but there were some rough edges . Nowadays Jython 2.5 is fully and officially supported ([issue 198](https://code.google.com/p/robotframework/issues/detail?id=198)), and even installation using it works ([issue 547](https://code.google.com/p/robotframework/issues/detail?id=547)).


# Backwards incompatible changes #

## Minimum Python/Jython version is 2.5 ##

Robot Framework 2.5 only runs on Python and Jython 2.5 or newer (but on 3.x yet).
If you cannot upgrade your Python/Jython installation, you can use older Robot Framework releases that support Jython 2.2 and Python 2.3 and newer.

## Not compatible with previous RIDE and Mabot releases ##

The internal changes in the framework have made it incompatible with
the previous [RIDE](http://code.google.com/p/robotframework-ride) and
[Mabot](http://code.google.com/p/robotframework-mabot)
releases.

  * RF 2.5 alpha 1 is compatible with [RIDE 0.23](http://code.google.com/p/robotframework-ride/wiki/ReleaseNotes#RIDE_0.23), which is also compatible with [RF 2.1.3](http://code.google.com/p/robotframework/wiki/ReleaseNotes21#Robot_Framework_2.1.3).
  * RF 2.5 rc 1 is currently not compatible with any RIDE release.
  * No RF 2.5 preview release is compatible with Mabot.

## Other backwards incompatible changes ##

Potentially backwards incompatible issues are
[labeled with bwic label in the issue tracker](http://code.google.com/p/robotframework/issues/list?can=1&q=target%3D2.5+label%3Dbwic). Why these changes may cause problems will be explained thoroughly later when these release notes are improved.

# Deprecated features #

Will be listed later.

# Robot Framework 2.5 Release Candidate 1 #

Robot Framework Release Candidate 1 was released 2010-05-31. This release contains all
functionality intended to be included in RF 2.5 and the main issues holding back the final
release are related to documentation. Additionally, we'll continue implementing compatible
RIDE release straight after the RC.

Full list of issues that were closed after alpha1 is listed below.


| [Issue 377](https://code.google.com/p/robotframework/issues/detail?id=377) | Enhancement | High | Don't convert test suite, test case and keyword names unnecessarily |
|:---------------------------------------------------------------------------|:------------|:-----|:--------------------------------------------------------------------|
| [Issue 452](https://code.google.com/p/robotframework/issues/detail?id=452) | Enhancement | High | Possibility to verify test data without actually executing tests (dry-run) |
| [Issue 486](https://code.google.com/p/robotframework/issues/detail?id=486) | Enhancement | High | Parsing modules should preserve comments to keep them available for RIDE and other tools |
| [Issue 500](https://code.google.com/p/robotframework/issues/detail?id=500) | Enhancement | High | Possibility to specify 'Test Template'  for all tests to ease data-driven testing |
| [Issue 564](https://code.google.com/p/robotframework/issues/detail?id=564) | Enhancement | High | Disallow using `@{list}` variables with settings that require scalar values to ease parsing |
| [Issue 518](https://code.google.com/p/robotframework/issues/detail?id=518) | Documentation | High | Document that Python/Jython version must be >= 2.5 (and < 3.0)      |
| [Issue 444](https://code.google.com/p/robotframework/issues/detail?id=444) | Defect      | Medium | Quickstart Demo fails in windows if sut directory has whitespace    |
| [Issue 550](https://code.google.com/p/robotframework/issues/detail?id=550) | Defect      | Medium | Non-integer value with `FOR IN RANGE` can break the whole test execution |
| [Issue 232](https://code.google.com/p/robotframework/issues/detail?id=232) | Enhancement | Medium | Possibility to configure parsing so that files having test case table are not ignored even if they don't have tests |
| [Issue 515](https://code.google.com/p/robotframework/issues/detail?id=515) | Enhancement | Medium | Importing Java libraries does not work on standalone Jython         |
| [Issue 524](https://code.google.com/p/robotframework/issues/detail?id=524) | Enhancement | Medium | Parsing modules should preserve table headers to make them available for RIDE and other tools |
| [Issue 553](https://code.google.com/p/robotframework/issues/detail?id=553) | Enhancement | Medium | Remove `robotidy.py` tool                                           |
| [Issue 563](https://code.google.com/p/robotframework/issues/detail?id=563) | Enhancement | Medium | Support for setting suite metadata using syntax  `| Metadata | Name | Value |` |
| [Issue 403](https://code.google.com/p/robotframework/issues/detail?id=403) | Refactoring | Medium | Parsed user keyword objects should have all data even if part of the data is invalid |
| [Issue 560](https://code.google.com/p/robotframework/issues/detail?id=560) | Enhancement | Low  | For loop without body or without values should fail                 |
| [Issue 562](https://code.google.com/p/robotframework/issues/detail?id=562) | Enhancement | Low  | Suite metadata names should not be converted unnecessarily          |
| [Issue 481](https://code.google.com/p/robotframework/issues/detail?id=481) | Refactoring | Low  | Cleanup `robot.utils` module                                        |

Altogether 17 issues.


# Robot Framework 2.5 Alpha 1 #

The first RF 2.5 pre-release was releases on 2010-05-06. Full list of issues is below.

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 198](https://code.google.com/p/robotframework/issues/detail?id=198) | Enhancement | Critical     | Jython 2.5 support |
| [Issue 288](https://code.google.com/p/robotframework/issues/detail?id=288) | Defect   | High         | It is not possible to assign all Python and Java iterables to list variables |
| [Issue 529](https://code.google.com/p/robotframework/issues/detail?id=529) | Defect   | High         | UTF-8 BOM is not ignored in plain text or TSV test data files |
| [Issue 108](https://code.google.com/p/robotframework/issues/detail?id=108) | Enhancement | High         | Ctrl-c should stop test execution gracefully |
| [Issue 137](https://code.google.com/p/robotframework/issues/detail?id=137) | Enhancement | High         | Support for continuing test execution regardless of failures (ContinueOnFailure) |
| [Issue 215](https://code.google.com/p/robotframework/issues/detail?id=215) | Enhancement | High         | Support for named arguments to ease overriding only certain default values |
| [Issue 349](https://code.google.com/p/robotframework/issues/detail?id=349) | Enhancement | High         | It should be possible to stop test execution gracefully with signal |
| [Issue 366](https://code.google.com/p/robotframework/issues/detail?id=366) | Enhancement | High         | Stop execution if special "fatal" exception raised |
| [Issue 398](https://code.google.com/p/robotframework/issues/detail?id=398) | Enhancement | High         | Remove `Default Tags` and `Test Timeout` from test suite initialization files |
| [Issue 544](https://code.google.com/p/robotframework/issues/detail?id=544) | Enhancement | High         | Run all keywords in teardown even if there are failures |
| [Issue 474](https://code.google.com/p/robotframework/issues/detail?id=474) | Defect   | Medium       | Byte strings containing non-ASCII characters not escaped on Jython |
| [Issue 499](https://code.google.com/p/robotframework/issues/detail?id=499) | Defect   | Medium       | HTML entity references having values outside ISO-8859-1 are not resolved correctly. |
| [Issue 509](https://code.google.com/p/robotframework/issues/detail?id=509) | Defect   | Medium       | Non-ASCII output returned by `Run` and `Start Process` keywords is decoded incorrectly when stdout is redirected (e.g. in CI environment) |
| [Issue 516](https://code.google.com/p/robotframework/issues/detail?id=516) | Defect   | Medium       | Non-ASCII characters not shown correctly on the console output  |
| [Issue 520](https://code.google.com/p/robotframework/issues/detail?id=520) | Defect   | Medium       | Using a timeouted keyword with wrong number of arguments causes FrameworkError |
| [Issue 521](https://code.google.com/p/robotframework/issues/detail?id=521) | Defect   | Medium       | Keywords executing other keywords (`Run Kw and Ignore/Expect Error`, `Wait Until Kw Succeeds`) hide syntax errors and timeouts |
| [Issue 523](https://code.google.com/p/robotframework/issues/detail?id=523) | Defect   | Medium       | " character at the end of test suite documentation breaks report (and log) generation |
| [Issue 530](https://code.google.com/p/robotframework/issues/detail?id=530) | Defect   | Medium       | Creating logs and reports fails on Jython when suite name and test name contain non-ASCII characters |
| [Issue 534](https://code.google.com/p/robotframework/issues/detail?id=534) | Defect   | Medium       | Showing non-ASCII characters printed from Java libraries in logs depends on system encoding |
| [Issue 194](https://code.google.com/p/robotframework/issues/detail?id=194) | Enhancement | Medium       | Remove the old syntax for repeating a single keyword multiple times |
| [Issue 321](https://code.google.com/p/robotframework/issues/detail?id=321) | Enhancement | Medium       | Enhance listener `start_suite` method to provide test/suite names and and total test count |
| [Issue 341](https://code.google.com/p/robotframework/issues/detail?id=341) | Enhancement | Medium       | New `Set Test Message` keyword to set or override test message |
| [Issue 342](https://code.google.com/p/robotframework/issues/detail?id=342) | Enhancement | Medium       | New keyword `Run Keyword If Timeout Occurred` to BuiltIn |
| [Issue 343](https://code.google.com/p/robotframework/issues/detail?id=343) | Enhancement | Medium       | Add free metadata to attributes passed to start\_suite and end\_suite listener methods |
| [Issue 346](https://code.google.com/p/robotframework/issues/detail?id=346) | Enhancement | Medium       | New variable ${SUITE SOURCE} containing an absolute path to suite file or directory |
| [Issue 401](https://code.google.com/p/robotframework/issues/detail?id=401) | Enhancement | Medium       | Deprecate possibility to create scalar variables containing list in variable table |
| [Issue 404](https://code.google.com/p/robotframework/issues/detail?id=404) | Enhancement | Medium       | Better styles for `libdoc.py` |
| [Issue 427](https://code.google.com/p/robotframework/issues/detail?id=427) | Enhancement | Medium       | Allow variable files' `get_variables` to return any mapping |
| [Issue 484](https://code.google.com/p/robotframework/issues/detail?id=484) | Enhancement | Medium       | Deprecate the possibility to have scalar and list variables with same base name (e.g. `${FOO}` and `@{FOO}`) |
| [Issue 490](https://code.google.com/p/robotframework/issues/detail?id=490) | Enhancement | Medium       | Remove parallel execution of keywords (`:PARALLEL` ) because it doesn't work correctly and requires special syntax |
| [Issue 528](https://code.google.com/p/robotframework/issues/detail?id=528) | Enhancement | Medium       | Argument files cannot have non-ASCII content |
| [Issue 531](https://code.google.com/p/robotframework/issues/detail?id=531) | Enhancement | Medium       | Show repr instead string value of the arguments and return value in the log file |
| [Issue 533](https://code.google.com/p/robotframework/issues/detail?id=533) | Enhancement | Medium       | Documentation should include the scope |
| [Issue 535](https://code.google.com/p/robotframework/issues/detail?id=535) | Enhancement | Medium       | Possibility to give custom styles for `libdoc.py` |
| [Issue 545](https://code.google.com/p/robotframework/issues/detail?id=545) | Enhancement | Medium       | New keyword 'Run Keyword And Continue On Failure' |
| [Issue 546](https://code.google.com/p/robotframework/issues/detail?id=546) | Enhancement | Medium       | New BuiltIn keyword `Fatal Error` to stop the whole test execution |
| [Issue 547](https://code.google.com/p/robotframework/issues/detail?id=547) | Enhancement | Medium       | Enhance install.py script so that pybot-script is not created when run with Jython |
| [Issue 497](https://code.google.com/p/robotframework/issues/detail?id=497) | Documentation | Medium       | Document that timeouts might cause performance problems if tests are executed with Python |
| [Issue 511](https://code.google.com/p/robotframework/issues/detail?id=511) | Defect   | Low          | Easter is coming but the egg is missing |
| [Issue 522](https://code.google.com/p/robotframework/issues/detail?id=522) | Defect   | Low          | Errors are corrupted when test data paths contain non-ASCII characters |
| [Issue 256](https://code.google.com/p/robotframework/issues/detail?id=256) | Enhancement | Low          | Change 'mode' argument 'Create File' to 'encoding' and deprecate 'Create File With Encoding' |
| [Issue 258](https://code.google.com/p/robotframework/issues/detail?id=258) | Enhancement | Low          | Remove deprecated `pattern_type` argument of `Grep File` keyword |
| [Issue 260](https://code.google.com/p/robotframework/issues/detail?id=260) | Enhancement | Low          | Remove deprecated `pattern_type` argument from `List Directory` keywords |
| [Issue 271](https://code.google.com/p/robotframework/issues/detail?id=271) | Enhancement | Low          | Remove deprecated `Syslog` keyword |
| [Issue 287](https://code.google.com/p/robotframework/issues/detail?id=287) | Enhancement | Low          | Remove deprecated `BuiltIn.Grep` keyword |
| [Issue 340](https://code.google.com/p/robotframework/issues/detail?id=340) | Enhancement | Low          | Increased the maximum size of the error message to 40 lines |
| [Issue 358](https://code.google.com/p/robotframework/issues/detail?id=358) | Enhancement | Low          | Remove deprecated `return_mode` argument of `Run` keyword |
| [Issue 514](https://code.google.com/p/robotframework/issues/detail?id=514) | Enhancement | Low          | Remove deprecated `mode` argument from `Read Process Output` keyword |
| [Issue 526](https://code.google.com/p/robotframework/issues/detail?id=526) | Enhancement | Low          | Remove already deprecated and ignored `--transform` option |
| [Issue 527](https://code.google.com/p/robotframework/issues/detail?id=527) | Enhancement | Low          | Remove deprecated `--colormonitor` option |

Altogether 50 issues.