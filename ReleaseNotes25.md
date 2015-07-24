

# Robot Framework 2.5 #

Robot Framework (RF) 2.5 is a new major release with loads of bigger
and smaller enhancements and bug fixes. It was released after few
[preview releases](PreviewReleases25.md) on Thursday 2010-06-10.

Questions and comments related to the
release can be sent to the [mailing lists](MailingLists.md) and possible
bugs submitted to
the [issue tracker](http://code.google.com/p/robotframework/issues).

## Downloads ##

Installers and other packages can be downloaded from the
[download page](http://code.google.com/p/robotframework/downloads/list).
See [installation instructions](Installation.md) for installation
and upgrading information.

## Most important new features ##

### Continuing test execution on failure ###

Being able to continue the test execution after failures was the most
requested feature in RF 2.5. There are now several ways to accomplish it:

  * Raising a _continuable_ exception from a test library ([issue 137](https://code.google.com/p/robotframework/issues/detail?id=137)).
  * Using `Run Keyword And Continue On Failure` keyword ([issue 545](https://code.google.com/p/robotframework/issues/detail?id=545)).
  * In teardowns all keywords are automatically executed even if there are failures ([issue 544](https://code.google.com/p/robotframework/issues/detail?id=544)).

For more information about this new feature, see the [Continue on failure](http://robotframework.googlecode.com/svn/tags/robotframework-2.5/doc/userguide/RobotFrameworkUserGuide.html#continue-on-failure) section in the [User Guide](UserGuide.md).

### Stopping test execution gracefully ###

Another important test execution related feature is the ability to
stop the test execution fully so that reports and logs are
generated. Nowadays there are several ways to do it:

  * Pressing `Ctrl-C` ([issue 108](https://code.google.com/p/robotframework/issues/detail?id=108)).
  * Using signals `SIGINT` and `SIGTERM` ([issue 349](https://code.google.com/p/robotframework/issues/detail?id=349)).
  * Raising a _fatal_ exception from a test library ([issue 366](https://code.google.com/p/robotframework/issues/detail?id=366)).
  * Using `Fatal Error` keyword ([issue 546](https://code.google.com/p/robotframework/issues/detail?id=546)).

This feature is explained more thoroughly in the [Stopping test execution gracefully](http://robotframework.googlecode.com/svn/tags/robotframework-2.5/doc/userguide/RobotFrameworkUserGuide.html#stopping-test-execution-gracefully) section in the [User Guide](UserGuide.md).

### Support for named arguments ###

The named arguments syntax ([issue 215](https://code.google.com/p/robotframework/issues/detail?id=215)) makes it possible to use
keywords that have several arguments with default values so that only
certain arguments are overridden.  For example, the keyword below
could be used like `| Named Arg Example | zap=42 |` and first two
arguments would get their default values.

```
  def named_arg_example(foo=1, bar=2, zap=3):
      print foo, bar, zap
```

See also the [Named arguments](http://robotframework.googlecode.com/svn/tags/robotframework-2.5/doc/userguide/RobotFrameworkUserGuide.html#named-arguments) section in the [User Guide](UserGuide.md).

### Possibility to specify test template to ease data-driven testing ###

Test templates ([issue 500](https://code.google.com/p/robotframework/issues/detail?id=500)) allow specifying the keyword to use in test
cases only once. This makes data-driven testing, where the same
keyword is executed with different input and/or output values, easier
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

See also the [Test templates](http://robotframework.googlecode.com/svn/tags/robotframework-2.5/doc/userguide/RobotFrameworkUserGuide.html#test-templates) and [Data-driven style](http://robotframework.googlecode.com/svn/tags/robotframework-2.5/doc/userguide/RobotFrameworkUserGuide.html#data-driven-style) sections in the [User Guide](UserGuide.md).

### Possibility to validate test data using dry-run ###

A new command line option `--runmode dryrun` was added to support
validation of test data without actually executing the lowest level
keywords ([issue 452](https://code.google.com/p/robotframework/issues/detail?id=452)).

### Full Jython 2.5 support ###

Robot Framework 2.1.3 already works with Jython 2.5 but there were
some rough edges . Nowadays Jython 2.5 is fully and officially
supported ([issue 198](https://code.google.com/p/robotframework/issues/detail?id=198)), and even installation using it works
([issue 547](https://code.google.com/p/robotframework/issues/detail?id=547)).

## Backwards incompatible changes ##

### Minimum Python/Jython version is 2.5 ###

Robot Framework 2.5 only runs on Python and Jython 2.5 or newer (but
not on 3.x yet). If you cannot upgrade your Python/Jython installation,
you can use older Robot Framework releases that support Jython 2.2 and
Python 2.3 and newer.

### Not compatible with previous RIDE and Mabot releases ###

The internal changes in the framework have made it incompatible with
the previous [RIDE](http://code.google.com/p/robotframework-ride) and
[Mabot](http://code.google.com/p/robotframework-mabot)
releases. RF 2.5 compatible RIDE release is under development.

### Parsing modules have been rewritten ###

In order to support RIDE better in the future, Robot Framework's
internal parsing modules were rewritten ([issue 486](https://code.google.com/p/robotframework/issues/detail?id=486)). These changes do
not affect test execution but custom tools using the parsing modules
need to be updated. The good news is that the new parsing modules are
much easier to use externally than the old ones.

### Parallel execution of keywords was removed ###

The special `:PARALLEL` syntax was removed because it was buggy,
fixing it fully would have been too big task, and supporting the
special syntax in the core framework, in RIDE, and elsewhere is extra
work. For more information see [issue 490](https://code.google.com/p/robotframework/issues/detail?id=490).

### Default Tags and Test Timeout removed from initialization files ###

It is not possible to use `Default Tags` or `Test Timeout` settings
in test suite initialization files anymore. See [issue 398](https://code.google.com/p/robotframework/issues/detail?id=398) for details.

#### List variables are not supported with certain settings ####

It is not possible to use `@{LIST}` variables anymore with settings
that require a scalar value. [Issue 564](https://code.google.com/p/robotframework/issues/detail?id=564) explains this limitation more
throughly.

### Other backwards incompatible changes ###

  * Old syntax for repeating single keyword multiple times was removed ([issue 194](https://code.google.com/p/robotframework/issues/detail?id=194)).
  * Several helper methods were removed from the `robot.utils` module ([issue 481](https://code.google.com/p/robotframework/issues/detail?id=481)).
  * Built-in keywords executing other keywords (`Run Keyword And Ignore/Expect Error`, `Wait Until Keyword Succeeds`) do not hide syntax errors or timeouts ([issue 521](https://code.google.com/p/robotframework/issues/detail?id=521)).
  * Running all the keywords in teardowns even if there are failures ([issue 544](https://code.google.com/p/robotframework/issues/detail?id=544)) may cause problems. Keywords that were previously skipped after failures are now run.
  * `robotidy.py` tool was removed ([issue 553](https://code.google.com/p/robotframework/issues/detail?id=553)).
  * `:FOR` loops without body or without values to loop over fail ([issue 560](https://code.google.com/p/robotframework/issues/detail?id=560)).
  * New automatic variable `${SUITE SOURCE}` may overwrite existing variables with the same name ([issue 346](https://code.google.com/p/robotframework/issues/detail?id=346)).
  * The way how test suite, test case, user keyword, and metadata names are created was changed ([issue 377](https://code.google.com/p/robotframework/issues/detail?id=377) and [issue 562](https://code.google.com/p/robotframework/issues/detail?id=562)).
  * Deprecated `mode` argument of `Create File` keyword was changed to `encoding` ([issue 256](https://code.google.com/p/robotframework/issues/detail?id=256)).
  * Deprecated `pattern_type` argument was removed from `Grep File` and `List Directory` keywords ([issue 258](https://code.google.com/p/robotframework/issues/detail?id=258) and [issue 260](https://code.google.com/p/robotframework/issues/detail?id=260)).
  * Deprecated `return_mode` argument was removed from `Run` keyword ([issue 358](https://code.google.com/p/robotframework/issues/detail?id=358)).
  * Deprecated `mode` argument of `Read Process Output` was removed.
  * Deprecated keywords `Syslog` and `Grep` were removed ([issue 271](https://code.google.com/p/robotframework/issues/detail?id=271) and [issue 287](https://code.google.com/p/robotframework/issues/detail?id=287)).
  * Deprecated `--transform` and `--colormonitor` options were removed ([issue 526](https://code.google.com/p/robotframework/issues/detail?id=526) and [issue 527](https://code.google.com/p/robotframework/issues/detail?id=527)).

## Deprecated features ##

These features have been deprecated and will be removed in RF 2.6:

  * The possibility to create scalar variables with a list value in the Variable table ([issue 401](https://code.google.com/p/robotframework/issues/detail?id=401)).
  * The possibility to have scalar and list variables with the same base name (e.g. `${VAR}` and `@{VAR}`) ([issue 484](https://code.google.com/p/robotframework/issues/detail?id=484)).
  * `Create File With Encoding` keyword ([issue 256](https://code.google.com/p/robotframework/issues/detail?id=256)).

## All fixes and enhancements in 2.5 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 198](https://code.google.com/p/robotframework/issues/detail?id=198) | Enhancement | Critical     | Jython 2.5 support |
| [Issue 529](https://code.google.com/p/robotframework/issues/detail?id=529) | Defect   | High         | UTF-8 BOM is not ignored in plain text or TSV test data files |
| [Issue 108](https://code.google.com/p/robotframework/issues/detail?id=108) | Enhancement | High         | Ctrl-c should stop test execution gracefully |
| [Issue 137](https://code.google.com/p/robotframework/issues/detail?id=137) | Enhancement | High         | Support continuing test execution regardless of failures |
| [Issue 215](https://code.google.com/p/robotframework/issues/detail?id=215) | Enhancement | High         | Support for named arguments to ease overriding only certain default values |
| [Issue 349](https://code.google.com/p/robotframework/issues/detail?id=349) | Enhancement | High         | It should be possible to stop test execution gracefully with signal |
| [Issue 366](https://code.google.com/p/robotframework/issues/detail?id=366) | Enhancement | High         | Stop execution if special "fatal" exception raised |
| [Issue 377](https://code.google.com/p/robotframework/issues/detail?id=377) | Enhancement | High         | Don't convert test suite, test case and keyword names unnecessarily |
| [Issue 452](https://code.google.com/p/robotframework/issues/detail?id=452) | Enhancement | High         | Possibility to verify test data without actually executing tests (dry-run) |
| [Issue 486](https://code.google.com/p/robotframework/issues/detail?id=486) | Enhancement | High         | Parsing modules should preserve comments to keep them available for RIDE and other tools |
| [Issue 487](https://code.google.com/p/robotframework/issues/detail?id=487) | Enhancement | High         | Make the parsed test data model easier to use externally by RIDE and other tools |
| [Issue 490](https://code.google.com/p/robotframework/issues/detail?id=490) | Enhancement | High         | Remove parallel execution of keywords (`:PARALLEL` ) because it doesn't work correctly and requires special syntax |
| [Issue 500](https://code.google.com/p/robotframework/issues/detail?id=500) | Enhancement | High         | Possibility to specify 'Test Template'  for all tests to ease data-driven testing |
| [Issue 544](https://code.google.com/p/robotframework/issues/detail?id=544) | Enhancement | High         | Run all keywords in teardown even if there are failures |
| [Issue 564](https://code.google.com/p/robotframework/issues/detail?id=564) | Enhancement | High         | Disallow using `@{list}` variables with settings that require scalar values to ease parsing |
| [Issue 518](https://code.google.com/p/robotframework/issues/detail?id=518) | Documentation | High         | Document that Python/Jython version must be >= 2.5 (and < 3.0) |
| [Issue 541](https://code.google.com/p/robotframework/issues/detail?id=541) | Documentation | High         | Document test execution flow (incl. continue on failure and stopping gracefully) |
| [Issue 288](https://code.google.com/p/robotframework/issues/detail?id=288) | Defect   | Medium       | It is not possible to assign all Python and Java iterables to list variables |
| [Issue 444](https://code.google.com/p/robotframework/issues/detail?id=444) | Defect   | Medium       | Quickstart demo fails when executed in a directory containing space in its name |
| [Issue 474](https://code.google.com/p/robotframework/issues/detail?id=474) | Defect   | Medium       | Byte strings containing non-ASCII characters not escaped on Jython |
| [Issue 499](https://code.google.com/p/robotframework/issues/detail?id=499) | Defect   | Medium       | HTML entity references having values outside ISO-8859-1 are not resolved correctly. |
| [Issue 509](https://code.google.com/p/robotframework/issues/detail?id=509) | Defect   | Medium       | Non-ASCII output returned by `Run` and `Start Process` keywords is decoded incorrectly when stdout is redirected (e.g. in CI environment) |
| [Issue 516](https://code.google.com/p/robotframework/issues/detail?id=516) | Defect   | Medium       | Non-ASCII characters not shown correctly on the console output  |
| [Issue 520](https://code.google.com/p/robotframework/issues/detail?id=520) | Defect   | Medium       | Using a timeouted keyword with wrong number of arguments causes `FrameworkError` |
| [Issue 521](https://code.google.com/p/robotframework/issues/detail?id=521) | Defect   | Medium       | Keywords executing other keywords (`Run Kw and Ignore/Expect Error`, `Wait Until Kw Succeeds`) hide syntax errors and timeouts |
| [Issue 523](https://code.google.com/p/robotframework/issues/detail?id=523) | Defect   | Medium       | Quote character `"` at the end of test suite documentation breaks report (and log) generation |
| [Issue 530](https://code.google.com/p/robotframework/issues/detail?id=530) | Defect   | Medium       | Creating logs and reports fails on Jython when suite name and test name contain non-ASCII characters |
| [Issue 534](https://code.google.com/p/robotframework/issues/detail?id=534) | Defect   | Medium       | Showing non-ASCII characters printed from Java libraries in logs depends on system encoding |
| [Issue 550](https://code.google.com/p/robotframework/issues/detail?id=550) | Defect   | Medium       | Non-integer value with `FOR IN RANGE` can break the whole test execution |
| [Issue 573](https://code.google.com/p/robotframework/issues/detail?id=573) | Defect   | Medium       | Runner scripts (`pybot`, `jybot`, `rebot`) require bash on unixy machines |
| [Issue 194](https://code.google.com/p/robotframework/issues/detail?id=194) | Enhancement | Medium       | Remove the old syntax for repeating a single keyword multiple times |
| [Issue 232](https://code.google.com/p/robotframework/issues/detail?id=232) | Enhancement | Medium       | Possibility to configure parsing so that files having test case table are not ignored even if they don't have tests |
| [Issue 321](https://code.google.com/p/robotframework/issues/detail?id=321) | Enhancement | Medium       | Enhance listener `start_suite` method to provide test/suite names and and total test count |
| [Issue 341](https://code.google.com/p/robotframework/issues/detail?id=341) | Enhancement | Medium       | New `Set Test Message` keyword to set or override test message |
| [Issue 342](https://code.google.com/p/robotframework/issues/detail?id=342) | Enhancement | Medium       | New `BuiltIn` keyword `Run Keyword If Timeout Occurred` |
| [Issue 343](https://code.google.com/p/robotframework/issues/detail?id=343) | Enhancement | Medium       | Add free metadata to attributes passed to `start_suite` and `end_suite` listener methods |
| [Issue 346](https://code.google.com/p/robotframework/issues/detail?id=346) | Enhancement | Medium       | New variable `${SUITE SOURCE}` containing an absolute path to suite file or directory |
| [Issue 398](https://code.google.com/p/robotframework/issues/detail?id=398) | Enhancement | Medium       | Remove `Default Tags` and `Test Timeout` from test suite initialization files |
| [Issue 401](https://code.google.com/p/robotframework/issues/detail?id=401) | Enhancement | Medium       | Deprecate possibility to create scalar variables containing list in variable table |
| [Issue 404](https://code.google.com/p/robotframework/issues/detail?id=404) | Enhancement | Medium       | Better styles for `libdoc.py` |
| [Issue 427](https://code.google.com/p/robotframework/issues/detail?id=427) | Enhancement | Medium       | Allow variable files' `get_variables` to return any mapping |
| [Issue 484](https://code.google.com/p/robotframework/issues/detail?id=484) | Enhancement | Medium       | Deprecate the possibility to have scalar and list variables with same base name (e.g. `${FOO}` and `@{FOO}`) |
| [Issue 515](https://code.google.com/p/robotframework/issues/detail?id=515) | Enhancement | Medium       | Importing Java libraries does not work on standalone Jython |
| [Issue 524](https://code.google.com/p/robotframework/issues/detail?id=524) | Enhancement | Medium       | Parsing modules should preserve table headers to make them available for RIDE and other tools |
| [Issue 528](https://code.google.com/p/robotframework/issues/detail?id=528) | Enhancement | Medium       | Argument files cannot have non-ASCII content |
| [Issue 531](https://code.google.com/p/robotframework/issues/detail?id=531) | Enhancement | Medium       | Show repr instead string value of the arguments and return value in the log file |
| [Issue 533](https://code.google.com/p/robotframework/issues/detail?id=533) | Enhancement | Medium       | Documentation generated by `libdoc.py` should show the test library scope |
| [Issue 535](https://code.google.com/p/robotframework/issues/detail?id=535) | Enhancement | Medium       | Possibility to give custom styles for `libdoc.py` |
| [Issue 545](https://code.google.com/p/robotframework/issues/detail?id=545) | Enhancement | Medium       | New `BuiltIn` keyword `Run Keyword And Continue On Failure` |
| [Issue 546](https://code.google.com/p/robotframework/issues/detail?id=546) | Enhancement | Medium       | New `BuiltIn` keyword `Fatal Error` to stop the whole test execution |
| [Issue 547](https://code.google.com/p/robotframework/issues/detail?id=547) | Enhancement | Medium       | Support for installation using Jython |
| [Issue 553](https://code.google.com/p/robotframework/issues/detail?id=553) | Enhancement | Medium       | Remove `robotidy.py` tool |
| [Issue 554](https://code.google.com/p/robotframework/issues/detail?id=554) | Enhancement | Medium       | Add an option to define report background colors |
| [Issue 563](https://code.google.com/p/robotframework/issues/detail?id=563) | Enhancement | Medium       | Support for setting suite metadata using syntax  `| Metadata | Name | Value |` |
| [Issue 572](https://code.google.com/p/robotframework/issues/detail?id=572) | Enhancement | Medium       | `Run Keywords` keyword to allow running multiple keywords in setup/teardown easily |
| [Issue 497](https://code.google.com/p/robotframework/issues/detail?id=497) | Documentation | Medium       | Document that timeouts might cause performance problems if tests are executed with Python |
| [Issue 513](https://code.google.com/p/robotframework/issues/detail?id=513) | Documentation | Medium       | Add "how to debug problems" section to the User Guide |
| [Issue 403](https://code.google.com/p/robotframework/issues/detail?id=403) | Refactoring | Medium       | Parsed user keyword objects should have all data even if part of the data is invalid |
| [Issue 511](https://code.google.com/p/robotframework/issues/detail?id=511) | Defect   | Low          | Easter is coming but the egg is missing |
| [Issue 522](https://code.google.com/p/robotframework/issues/detail?id=522) | Defect   | Low          | Errors are corrupted when test data paths contain non-ASCII characters |
| [Issue 569](https://code.google.com/p/robotframework/issues/detail?id=569) | Defect   | Low          | Non-existing variable in user keyword return value very hard to debug |
| [Issue 256](https://code.google.com/p/robotframework/issues/detail?id=256) | Enhancement | Low          | Change deprecated `mode` argument of `Create File` keyword to `encoding` and deprecate `Create File With Encoding` |
| [Issue 258](https://code.google.com/p/robotframework/issues/detail?id=258) | Enhancement | Low          | Remove deprecated `pattern_type` argument of `Grep File` keyword |
| [Issue 260](https://code.google.com/p/robotframework/issues/detail?id=260) | Enhancement | Low          | Remove deprecated `pattern_type` argument from `List Directory` keywords |
| [Issue 271](https://code.google.com/p/robotframework/issues/detail?id=271) | Enhancement | Low          | Remove deprecated `Syslog` keyword |
| [Issue 287](https://code.google.com/p/robotframework/issues/detail?id=287) | Enhancement | Low          | Remove deprecated `Grep` keyword |
| [Issue 340](https://code.google.com/p/robotframework/issues/detail?id=340) | Enhancement | Low          | Increased the maximum size of the error message to 40 lines |
| [Issue 358](https://code.google.com/p/robotframework/issues/detail?id=358) | Enhancement | Low          | Remove deprecated `return_mode` argument of `Run` keyword |
| [Issue 514](https://code.google.com/p/robotframework/issues/detail?id=514) | Enhancement | Low          | Remove deprecated `mode` argument from `Read Process Output` keyword |
| [Issue 526](https://code.google.com/p/robotframework/issues/detail?id=526) | Enhancement | Low          | Remove already deprecated and ignored `--transform` option |
| [Issue 527](https://code.google.com/p/robotframework/issues/detail?id=527) | Enhancement | Low          | Remove deprecated `--colormonitor` option |
| [Issue 560](https://code.google.com/p/robotframework/issues/detail?id=560) | Enhancement | Low          | `:FOR` loops without body or without values to loop through should fail |
| [Issue 562](https://code.google.com/p/robotframework/issues/detail?id=562) | Enhancement | Low          | Suite metadata names should not be converted unnecessarily |
| [Issue 481](https://code.google.com/p/robotframework/issues/detail?id=481) | Refactoring | Low          | Cleanup `robot.utils` module |

Altogether 74 issues.

# Robot Framework 2.5.1 #

Robot Framework 2.5.1 fixes two high priority bugs: files without extension no longer cause a crash ([issue 580](https://code.google.com/p/robotframework/issues/detail?id=580)) and variables are now resolved correctly from arguments to Java libraries ([issue 584](https://code.google.com/p/robotframework/issues/detail?id=584)). Other changes are minor bug fixes and enhancements.

Robot Framework 2.5.1 was released on Thursday 2010-07-22.
[Installation](Installation.md) packages can be found from the
[download page](http://code.google.com/p/robotframework/downloads/list).

## All fixes and enhancements in 2.5.1 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 580](https://code.google.com/p/robotframework/issues/detail?id=580) | Defect   | High         | Files without extension inside test data directories crash execution |
| [Issue 584](https://code.google.com/p/robotframework/issues/detail?id=584) | Defect   | High         | Variables are not resolved from arguments to Java libraries |
| [Issue 577](https://code.google.com/p/robotframework/issues/detail?id=577) | Defect   | Medium       | Splitting outputs - log, report, summary headings say "None Test Report" |
| [Issue 585](https://code.google.com/p/robotframework/issues/detail?id=585) | Defect   | Medium       | Timeouts, fatal errors, and syntax errors should stop execution of templated tests immediately |
| [Issue 589](https://code.google.com/p/robotframework/issues/detail?id=589) | Defect   | Medium       | Already imported libraries are instantiated again |
| [Issue 600](https://code.google.com/p/robotframework/issues/detail?id=600) | Defect   | Medium       | All keywords are not executed in dry-run mode if there are failures |
| [Issue 599](https://code.google.com/p/robotframework/issues/detail?id=599) | Enhancement | Medium       | Comment values should be stripped and should not have pipes between cells |
| [Issue 586](https://code.google.com/p/robotframework/issues/detail?id=586) | Defect   | Low          | `Run Keywords` keyword reports continuable failures incorrectly |

Altogether 8 issues.

# Robot Framework 2.5.2 #

Robot Framework 2.5.2 fixes two encoding related bugs that could crash execution in certain environments ([issue 614](https://code.google.com/p/robotframework/issues/detail?id=614) and [issue 616](https://code.google.com/p/robotframework/issues/detail?id=616)) and slightly enhances compatibility with RF 2.1.x versions ([issue 607](https://code.google.com/p/robotframework/issues/detail?id=607) and [issue 611](https://code.google.com/p/robotframework/issues/detail?id=611)). The biggest new features are the possibility to get the active test library instance ([issue 622](https://code.google.com/p/robotframework/issues/detail?id=622)) and running all keywords in teardowns even if there are syntax errors ([issue 615](https://code.google.com/p/robotframework/issues/detail?id=615)).

Starting from this release Robot Framework is available as single JAR package that contains both Jython and the framework ([issue 36](https://code.google.com/p/robotframework/issues/detail?id=36)). The JAR file allows executing tests as simply as `java -jar robotframework-2.5.2.jar my_tests.txt` and also contains a Java API for running tests. For more information see the  [Java Integration](JavaIntegration.md) wiki page and the [User Guide](UserGuide.md).

Robot Framework 2.5.2 was released on Friday 2010-08-27.
[Installation](Installation.md) packages can be found from the
[download page](http://code.google.com/p/robotframework/downloads/list).

## List of fixes and enhancements in 2.5.2 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 614](https://code.google.com/p/robotframework/issues/detail?id=614) | Defect   | High         | Redirected output crashes when encoding not found from environment |
| [Issue 616](https://code.google.com/p/robotframework/issues/detail?id=616) | Defect   | High         | Encoding got from environment may be invalid and crash execution on Unixes |
| [Issue 36](https://code.google.com/p/robotframework/issues/detail?id=36) | Enhancement | High         | JAR distribution package |
| [Issue 615](https://code.google.com/p/robotframework/issues/detail?id=615) | Enhancement | High         | All keywords in teardowns should be executed even if there are syntax errors |
| [Issue 622](https://code.google.com/p/robotframework/issues/detail?id=622) | Enhancement | High         | Possibility to interact with other active libraries via `Get Library Instance` keyword |
| [Issue 625](https://code.google.com/p/robotframework/issues/detail?id=625) | Defect   | Medium       | Rename function `rebot` to `run_rebot` in `robot/__init__.py` to avoid collision with `robot.rebot` module |
| [Issue 502](https://code.google.com/p/robotframework/issues/detail?id=502) | Enhancement | Medium       | Possibility to exit for loops with  `BuiltIn.Exit For Loop` keyword and with custom exceptions |
| [Issue 593](https://code.google.com/p/robotframework/issues/detail?id=593) | Enhancement | Medium       | Command line option to skip teardowns when execution is stopped gracefully (e.g. with `Ctrl-C`) |
| [Issue 608](https://code.google.com/p/robotframework/issues/detail?id=608) | Enhancement | Medium       | Add --loglevel option to rebot |
| [Issue 609](https://code.google.com/p/robotframework/issues/detail?id=609) | Enhancement | Medium       | Row continuation with `...` should ignore leading empty cells |
| [Issue 610](https://code.google.com/p/robotframework/issues/detail?id=610) | Enhancement | Medium       | `Run Keyword` variants should be executed in dry-run mode when feasible |
| [Issue 623](https://code.google.com/p/robotframework/issues/detail?id=623) | Enhancement | Medium       | Warning caused by creating scalar with multiple values does not contain enough details  |
| [Issue 624](https://code.google.com/p/robotframework/issues/detail?id=624) | Enhancement | Medium       | Warning caused by creating scalar and list variable with same basename does not contain enough details |
| [Issue 627](https://code.google.com/p/robotframework/issues/detail?id=627) | Enhancement | Medium       | Create link from Test Execution Errors to exact place in Test Execution Log |
| [Issue 626](https://code.google.com/p/robotframework/issues/detail?id=626) | Documentation | Medium       | Document different ways to extend existing test libraries |
| [Issue 607](https://code.google.com/p/robotframework/issues/detail?id=607) | Defect   | Low          | Continuing for loop row works differently in RF 2.5 than in earlier versions |
| [Issue 611](https://code.google.com/p/robotframework/issues/detail?id=611) | Defect   | Low          | For loops are not space insensitive as in RF 2.1.3 and earlier |

Altogether 17 issues.


# Robot Framework 2.5.3 #

Robot Framework 2.5.3 was mainly created to fix a critical bug in the
new JAR distribution on Windows ([issue 629](https://code.google.com/p/robotframework/issues/detail?id=629)). It also contains fully RF
2.5.x compatible User Guide ([issue 632](https://code.google.com/p/robotframework/issues/detail?id=632)), fixes to console output alignment
with East Asian characters based on a clever patch by xieyanbo ([issue 604](https://code.google.com/p/robotframework/issues/detail?id=604)), and some less
critical fixes and enhancements that were originally descoped from the
2.5.2 release.

Robot Framework 2.5.3 was released on Tuesday 2010-08-31.
[Installation](Installation.md) packages can be found from the
[download page](http://code.google.com/p/robotframework/downloads/list).

**Update:** Thanks to Robert Spielmann we now have a separate installer
for 64 bit Windows ([issue 613](https://code.google.com/p/robotframework/issues/detail?id=613)) available on the download page.

## List of fixes and enhancements in 2.5.3 ##

| [Issue 629](https://code.google.com/p/robotframework/issues/detail?id=629) | Defect | Critical | New JAR distribution does not work on Windows |
|:---------------------------------------------------------------------------|:-------|:---------|:----------------------------------------------|
| [Issue 613](https://code.google.com/p/robotframework/issues/detail?id=613) | Defect | High     | Using binary installer fails on 64 bit Windows |
| [Issue 632](https://code.google.com/p/robotframework/issues/detail?id=632) | Documentation | High     | User Guide is not fully 2.5.x compatible      |
| [Issue 628](https://code.google.com/p/robotframework/issues/detail?id=628) | Enhancement | Medium   | Create link from Test Execution Errors to Test Execution Log only if message exists in there |
| [Issue 604](https://code.google.com/p/robotframework/issues/detail?id=604) | Defect | Low      | East asian characters are not aligned correctly in console output |
| [Issue 635](https://code.google.com/p/robotframework/issues/detail?id=635) | Defect | Low      | Warnings from keywords are logged twice       |
| [Issue 634](https://code.google.com/p/robotframework/issues/detail?id=634) | Enhancement | Low      | Use `html` attribute with log messages in XML outputs only when necessary |
| [Issue 636](https://code.google.com/p/robotframework/issues/detail?id=636) | Enhancement | Low      | Warning caused by creating scalar and list variable with same base name is logged multiple times |

Altogether 7 issues.


# Robot Framework 2.5.4 #

Robot Framework 2.5.4 is mainly a bug fix release. Biggest new feature is 'import resource' keyword, thanks to user Grompy.

Robot Framework 2.5.4 was released on Tuesday 2010-09-28.
[Installation](Installation.md) packages can be found from the
[download page](http://code.google.com/p/robotframework/downloads/list).

## List of fixes and enhancements in 2.5.4 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 643](https://code.google.com/p/robotframework/issues/detail?id=643) | Defect   | High         | Several `OperatingSystem` keywords (`List Directory`, `Remove Directory`, ...) fail to handle non-ASCII file names on Jython |
| [Issue 651](https://code.google.com/p/robotframework/issues/detail?id=651) | Defect   | High         | Failure messages in log are cut |
| [Issue 654](https://code.google.com/p/robotframework/issues/detail?id=654) | Defect   | High         | Some `BuiltIn` keywords (e.g. `Run Keyword`) can fail if `BuiltIn` module is imported before execution starts |
| [Issue 656](https://code.google.com/p/robotframework/issues/detail?id=656) | Defect   | High         | Execution crashes if setup or teardown fails with error message containing non-ASCII characters |
| [Issue 638](https://code.google.com/p/robotframework/issues/detail?id=638) | Enhancement | High         | Python 2.7 compatibility |
| [Issue 657](https://code.google.com/p/robotframework/issues/detail?id=657) | Enhancement | High         | Ctrl-C and signals should stop execution gracefully even if keyword swallows exceptions |
| [Issue 659](https://code.google.com/p/robotframework/issues/detail?id=659) | Enhancement | High         | Jython 2.5.2 (beta 2) compatibility |
| [Issue 637](https://code.google.com/p/robotframework/issues/detail?id=637) | Defect   | Medium       | `--help` and `--version` can fail with "unknown encoding" error |
| [Issue 641](https://code.google.com/p/robotframework/issues/detail?id=641) | Defect   | Medium       | Dialog library keyword hangs when timeouts are used on Windows with Python |
| [Issue 650](https://code.google.com/p/robotframework/issues/detail?id=650) | Defect   | Medium       | Robot Framework 2.5.3 cannot be extended using `jar` command |
| [Issue 655](https://code.google.com/p/robotframework/issues/detail?id=655) | Defect   | Medium       | `\n` and `\t` are not processed correctly by `testdoc.py` |
| [Issue 663](https://code.google.com/p/robotframework/issues/detail?id=663) | Defect   | Medium       | Metadata given from command line is not escaped |
| [Issue 578](https://code.google.com/p/robotframework/issues/detail?id=578) | Enhancement | Medium       | New BuiltIn keyword `Import Resource` |
| [Issue 671](https://code.google.com/p/robotframework/issues/detail?id=671) | Enhancement | Medium       | XmlLogger's start/end methods should be called before/after listeners |
| [Issue 670](https://code.google.com/p/robotframework/issues/detail?id=670) | Documentation | Medium       | Document that named argument syntax is case and space sensitive and user keyword default value syntax is space sensitive |
| [Issue 666](https://code.google.com/p/robotframework/issues/detail?id=666) | Defect   | Low          | Starting execution from Python fails if stdout/stderr is replaced with StringIO (or any object not having encoding) |
| [Issue 672](https://code.google.com/p/robotframework/issues/detail?id=672) | Enhancement | Low          | `OperatingSystem.Get File Size` should not work with directories |
| [Issue 660](https://code.google.com/p/robotframework/issues/detail?id=660) | Documentation | Low          | Typo in listener docs - 'elapsetime' should be 'elapsedtime' |
| [Issue 665](https://code.google.com/p/robotframework/issues/detail?id=665) | Documentation | Low          | Dry-run documentation should mention that variables are not validated |
| [Issue 667](https://code.google.com/p/robotframework/issues/detail?id=667) | Documentation | Low          | Document that whitespace characters are ignored after `\n` except inside extended variable syntax |

Altogether 20 issues.


# Robot Framework 2.5.4.1 #

Robot Framework 2.5.4.1 is a micro release of only the jar package. This new package includes compiled class files for Jython's standard libraries. This improves the speed of the standalone jar package while increasing the size of the distribution a few megabytes.

Robot Framework 2.5.4.1 was released on Tuesday 2010-09-30.

[Installation](Installation.md) packages can be found from the
[download page](http://code.google.com/p/robotframework/downloads/list).

## List of fixes and enhancements in 2.5.4.1 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 674](https://code.google.com/p/robotframework/issues/detail?id=674) | Enhancement | Medium       | Speed up JAR distribution by precompiling jython standard library |

Altogether 1 issue.


# Robot Framework 2.5.5 #

Robot Framework 2.5.5 is a bigger-than-normal minor release. New features and fixes
are listed below, and installers and other packages are available on the
[download page](http://code.google.com/p/robotframework/downloads/list). Robot Framework
2.5.5 was released on Friday 2010-12-10.

Questions and comments related to the release can be sent to the
[mailing lists](MailingLists.md), and possible bugs submitted to
the [issue tracker](http://code.google.com/p/robotframework/issues).

## Installation ##

See [installation instructions](Installation.md) for detailed installation and
upgrading instructions. If you have an earlier 2.5.x release installed,
it should be safe to install this version over it without uninstallation.

## Mosts important features and fixes ##

The most interesting new features are initial [support for .NET](DotNetSupport.md)
via IronPython ([issue 154](https://code.google.com/p/robotframework/issues/detail?id=154)), built-in support for producing xUnit compatible
outputs ([issue 442](https://code.google.com/p/robotframework/issues/detail?id=442)), and Python support and general cleanup for
[Screenshot library](ScreenshotLibrary.md) ([issue 692](https://code.google.com/p/robotframework/issues/detail?id=692) and [issue 732](https://code.google.com/p/robotframework/issues/detail?id=732)). The biggest fixes
are Java 1.5 support for the JAR distribution ([issue 690](https://code.google.com/p/robotframework/issues/detail?id=690))
and support for Jython 2.5.2 RC 2 ([issue 707](https://code.google.com/p/robotframework/issues/detail?id=707)).

## Backwards incompatible changes and deprecations ##

All known backwards incompatible changes are related to cleaning up
[Screenshot library](ScreenshotLibrary.md) ([issue 732](https://code.google.com/p/robotframework/issues/detail?id=732)). The default saving location
of screenshots was changed from the system temporary directory to the directory
where the execution log file is written. This should not matter in tests, but
possible external scripts handling the screenshots may be affected. At the same time
configuration argument `log_file_directory` was deprecated (that information is
nowadays got automatically) and old screenshot taking keywords were marked obsolete.

## Acknowledgements ##

Big thanks to everyone who has submitted reports, suggested fixes, or otherwise helped
to make 2.5.5 a great release. Special thanks to Régis Desgroppes for an excellent patch
to add support for xUnit compatible outputs.

## List of fixes and enhancements in 2.5.5 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 690](https://code.google.com/p/robotframework/issues/detail?id=690) | Defect   | High         | RF JAR 2.5.4.1 connot be read with java 1.5 |
| [Issue 154](https://code.google.com/p/robotframework/issues/detail?id=154) | Enhancement | High         | Initial IronPython compatibility |
| [Issue 442](https://code.google.com/p/robotframework/issues/detail?id=442) | Enhancement | High         | xUnit-compatible results |
| [Issue 678](https://code.google.com/p/robotframework/issues/detail?id=678) | Enhancement | High         | Enable exposing only some of the functions in a module as keywords with Python's `__all__` attribute |
| [Issue 683](https://code.google.com/p/robotframework/issues/detail?id=683) | Enhancement | High         | Remove deprecation warning when using scalar and list variables with same base name (e.g. `${FOO}` and `@{FOO}`) |
| [Issue 691](https://code.google.com/p/robotframework/issues/detail?id=691) | Enhancement | High         | Command line option to report skipped test data files as warnings |
| [Issue 692](https://code.google.com/p/robotframework/issues/detail?id=692) | Enhancement | High         | Screenshot library should be supported also on Python |
| [Issue 677](https://code.google.com/p/robotframework/issues/detail?id=677) | Defect   | Medium       | Helper methods accidentally exposed as keywords in Dialogs library |
| [Issue 707](https://code.google.com/p/robotframework/issues/detail?id=707) | Defect   | Medium       | Jython 2.5.2(rc2) compatibility |
| [Issue 723](https://code.google.com/p/robotframework/issues/detail?id=723) | Defect   | Medium       | Libraries/resources/variables are imported when execution has been stopped gracefully |
| [Issue 679](https://code.google.com/p/robotframework/issues/detail?id=679) | Enhancement | Medium       | Allow colon after setting names (e.g. `Documentation:`) |
| [Issue 686](https://code.google.com/p/robotframework/issues/detail?id=686) | Enhancement | Medium       | Better error message when using extended variable syntax and variable not found |
| [Issue 698](https://code.google.com/p/robotframework/issues/detail?id=698) | Enhancement | Medium       | Keyword `Get Binary File` to `OperatingSystem` library |
| [Issue 701](https://code.google.com/p/robotframework/issues/detail?id=701) | Enhancement | Medium       | "In Range" for loop should support arithmetics |
| [Issue 703](https://code.google.com/p/robotframework/issues/detail?id=703) | Enhancement | Medium       | Speedup test data file parsing |
| [Issue 714](https://code.google.com/p/robotframework/issues/detail?id=714) | Enhancement | Medium       | Line breaks are not preserved when viewing report with Excel |
| [Issue 730](https://code.google.com/p/robotframework/issues/detail?id=730) | Enhancement | Medium       | Add `Grep` that was removed from `BuiltIn` into `DeprecatedBuiltIn` |
| [Issue 731](https://code.google.com/p/robotframework/issues/detail?id=731) | Enhancement | Medium       | Add removed `X times` syntax (but keep it deprecated) |
| [Issue 732](https://code.google.com/p/robotframework/issues/detail?id=732) | Enhancement | Medium       | Make `Screenshot` library easier to use (incl. new keywords `Take Screenshot` and `Take Screenshot Without Embedding`) |
| [Issue 728](https://code.google.com/p/robotframework/issues/detail?id=728) | Defect   | Low          | Errors with positional arguments and arguments with default values |
| [Issue 682](https://code.google.com/p/robotframework/issues/detail?id=682) | Enhancement | Low          | Make internal `LOGGER` iterable |
| [Issue 687](https://code.google.com/p/robotframework/issues/detail?id=687) | Enhancement | Low          | The string presentation of `RobotError` base exception should handle situation when it has no message |

Altogether 22 issues.

# Robot Framework 2.5.6 #

Robot Framework 2.5.6 is a bug fix release with some nice enhancements. New features and fixes
are listed below, and installers and other packages are available on the
[download page](http://code.google.com/p/robotframework/downloads/list). Robot Framework
2.5.6 was released on Friday 2011-02-07.

Questions and comments related to the release can be sent to the
[mailing lists](MailingLists.md), and possible bugs submitted to
the [issue tracker](http://code.google.com/p/robotframework/issues).

## Installation ##

See [installation instructions](Installation.md) for detailed installation and
upgrading instructions. If you have an earlier 2.5.x release installed,
it should be safe to install this version over it without uninstallation.

## Mosts important features and fixes ##

### Faster log/report generation ###

Processing XML output files has been enhanced. This can reduce memory usage and fasten log/report generation considerably (20%-50%) depending on the environment. For more information see [issue 501](https://code.google.com/p/robotframework/issues/detail?id=501) and related [mailing list discussion](http://groups.google.com/group/robotframework-users/browse_frm/thread/22d984dc374f9498?tvc=1).

### Enhanced color support on console ###

Colors are now supported also on Windows ([issue 753](https://code.google.com/p/robotframework/issues/detail?id=753)) except when using Jython. Colors are also automatically turned off when the console output is redirected into a file ([issue 777](https://code.google.com/p/robotframework/issues/detail?id=777)). This makes using option `--monitorcolors off` unnecessary, for example, when tests are started by a continuous integration system.

### Easier disabling of setup, teardown, template, timeout and tags ###

Disabling setup, teardown, template, timeout or tags set in higher level used work only using the setting so that it gets no value. Nowadays all these settings can be overridden with a special value `NONE` which is more clear and allows using variables. For more information and examples see [issue 776](https://code.google.com/p/robotframework/issues/detail?id=776).

## Backwards incompatible changes ##

Special `NONE` value to override settings (see above) can potentially cause backwards incompatibility problems. This happens if there is a keyword or tag with name `NONE` (case insensitively) which we expect not to be common.

Automatic disabling of console colors when output is redirect (also discussed above) affected values accepted by `--monitorcolors` option. As explained in [issue 777](https://code.google.com/p/robotframework/issues/detail?id=777), this should not cause problems in practice.

## List of fixes and enhancements in 2.5.6 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 749](https://code.google.com/p/robotframework/issues/detail?id=749) | Defect   | High         | When a keyword within a timeout fails in python library, traceback does not contain original cause. |
| [Issue 756](https://code.google.com/p/robotframework/issues/detail?id=756) | Defect   | High         | Using `--xunitfile` and `--listener` together throws non-fatal exception |
| [Issue 763](https://code.google.com/p/robotframework/issues/detail?id=763) | Defect   | High         | Fatal Exception in suite setup does not stop test execution |
| [Issue 501](https://code.google.com/p/robotframework/issues/detail?id=501) | Enhancement | High         | Refactor XML processing to enhance memory usage |
| [Issue 753](https://code.google.com/p/robotframework/issues/detail?id=753) | Enhancement | High         | Support colors on Windows console |
| [Issue 757](https://code.google.com/p/robotframework/issues/detail?id=757) | Enhancement | High         | `--test` option does not work with long names (e.g. `--test mysuite.mytest`) |
| [Issue 776](https://code.google.com/p/robotframework/issues/detail?id=776) | Enhancement | High         | Allow using special `NONE` value to indicate there is no setup, teardown, tags, template or timeout |
| [Issue 750](https://code.google.com/p/robotframework/issues/detail?id=750) | Defect   | Medium       | Rebot ignores `--loglevel` option inside user keywords |
| [Issue 751](https://code.google.com/p/robotframework/issues/detail?id=751) | Defect   | Medium       | `Set Log Level` keyword does not work with levels below INFO on test case level (since RF 2.5.2) |
| [Issue 755](https://code.google.com/p/robotframework/issues/detail?id=755) | Defect   | Medium       | Critical/Noncritical in split logs don't work correctly |
| [Issue 768](https://code.google.com/p/robotframework/issues/detail?id=768) | Defect   | Medium       | Get Length doesn't work on result of Get Variables |
| [Issue 770](https://code.google.com/p/robotframework/issues/detail?id=770) | Defect   | Medium       | Using Robot in non-mainthread causes unhandled exception |
| [Issue 681](https://code.google.com/p/robotframework/issues/detail?id=681) | Enhancement | Medium       | Rebot should always support `--starttime` and `--endtime` options |
| [Issue 773](https://code.google.com/p/robotframework/issues/detail?id=773) | Enhancement | Medium       | Pass argument files via stdin like `--argumentfile stdin` |
| [Issue 777](https://code.google.com/p/robotframework/issues/detail?id=777) | Enhancement | Medium       | Disable colors in console output automatically when output redirected to file |
| [Issue 771](https://code.google.com/p/robotframework/issues/detail?id=771) | Defect   | Low          | Non-existing argument file causes traceback |
| [Issue 590](https://code.google.com/p/robotframework/issues/detail?id=590) | Documentation | Low          | Document that `PYTHONCASEOK` environment variable should not be set |

Altogether 17 issues.


# Robot Framework 2.5.7 #

Robot Framework 2.5.7 is a minor release with fixes and enhancements listed below, and installers and other packages are
available on the [download page](http://code.google.com/p/robotframework/downloads/list). Robot Framework 2.5.7 was released on Friday 2011-04-21.

## List of fixes and enhancements in 2.5.7 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 804](https://code.google.com/p/robotframework/issues/detail?id=804) | Defect   | High         | Cannot run tests if execution directory has non-ascii characters |
| [Issue 815](https://code.google.com/p/robotframework/issues/detail?id=815) | Defect   | High         | Execution crashes if registering signal handler fails on Jython |
| [Issue 791](https://code.google.com/p/robotframework/issues/detail?id=791) | Enhancement | High         | `--removekeywords passed` should not remove warnings |
| [Issue 789](https://code.google.com/p/robotframework/issues/detail?id=789) | Defect   | Medium       | Unsufficient error message if resource or init files contain test cases |
| [Issue 820](https://code.google.com/p/robotframework/issues/detail?id=820) | Defect   | Medium       | Test criticality written to output XML before it is finally determined |
| [Issue 803](https://code.google.com/p/robotframework/issues/detail?id=803) | Enhancement | Medium       | A command line option for disabling status return code |
| [Issue 816](https://code.google.com/p/robotframework/issues/detail?id=816) | Enhancement | Medium       | Issue warning when signal handlers cannot be registered |
| [Issue 817](https://code.google.com/p/robotframework/issues/detail?id=817) | Enhancement | Medium       | Bad error message when `Should Be Equal` compares items that have same string representation but different type |
| [Issue 781](https://code.google.com/p/robotframework/issues/detail?id=781) | Defect   | Low          | Console colors on Windows always have black background |
| [Issue 818](https://code.google.com/p/robotframework/issues/detail?id=818) | Defect   | Low          | Syslog is written using unix line separators on Windows |

Altogether 10 issues.