

# Robot Framework 2.0 #

Version 2.0 is the first open source release of Robot Framework. Listing all the features here would not make much sense, especially when we have a comprehensive [user guide](UserGuide.md) available.

Old users of non-public Robot Framework should note that 2.0 version has exactly same functionality as 1.8.8 version.

Robot Framework 2.0 installers can be found from the [download page](http://code.google.com/p/robotframework/downloads/list) and
[installation instructions](http://robotframework.googlecode.com/svn/tags/robotframework-2.0/doc/userguide/RobotFrameworkUserGuide.html#installation-and-uninstallation) are in the user guide.


# Robot Framework 2.0.1 #

Robot Framework 2.0.1 contains mainly documentation and installation enhancements.
Biggest documentation improvement is the new [Quick Start Guide](QuickStartGuide.md),
which introduces the most important framework features and also acts as an
executable demo. Installation was enhanced by adding support for
[Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall), which basically
means that you can install or update Robot Framework by using command `easy_install robotframework`.

All implemented enhancements, fixes and tasks are listed in the table below,
with links to appropriate issues in the issue tracker. Installers can be found from the [download page](http://code.google.com/p/robotframework/downloads/list) and
[installation instructions](http://robotframework.googlecode.com/svn/tags/robotframework-2.0.1/doc/userguide/RobotFrameworkUserGuide.html#installation-and-uninstallation) are in the user guide.


|   **ID**   |     **Type**    |  **Priority**  |  **Summary**  |
|:-----------|:----------------|:---------------|:--------------|
| [Issue 32](https://code.google.com/p/robotframework/issues/detail?id=32) | Documentation   | Critical       | Getting started guide |
| [Issue 40](https://code.google.com/p/robotframework/issues/detail?id=40) | Enhancement     | Critical       | Better support for easy\_install |
| [Issue 41](https://code.google.com/p/robotframework/issues/detail?id=41) | Documentation   | Critical       | Possible to import libraries using physical path missing from user guide |
| [Issue 45](https://code.google.com/p/robotframework/issues/detail?id=45) | Defect          | Critical       | Several CollectionsLibrary keywords do not work with non-string items |
| [Issue 1](https://code.google.com/p/robotframework/issues/detail?id=1)  | Enhancement     | High           | Less noise to log for information about suites/tests/kws |
| [Issue 44](https://code.google.com/p/robotframework/issues/detail?id=44) | Documentation   | High           | User guide download package ought to be zip |
| [Issue 48](https://code.google.com/p/robotframework/issues/detail?id=48) | Documentation   | High           | TelnetLibrary documentation is unclear |
| [Issue 39](https://code.google.com/p/robotframework/issues/detail?id=39) | Enhancement     | Medium         | Packaging enhancements |
| [Issue 42](https://code.google.com/p/robotframework/issues/detail?id=42) | Task            | Medium         | User guide version ought to be got automatically |
| [Issue 43](https://code.google.com/p/robotframework/issues/detail?id=43) | Documentation   | Medium         | New appendix about templates to user guide |
| [Issue 53](https://code.google.com/p/robotframework/issues/detail?id=53) | Enhancement     | Medium         | Improve 'Sleep' of BuiltInLibrary |
| [Issue 54](https://code.google.com/p/robotframework/issues/detail?id=54) | Enhancement     | Medium         | Improve 'Login' in TelnetLibrary |
| [Issue 56](https://code.google.com/p/robotframework/issues/detail?id=56) | Task            | Medium         | Test Windows installers created on Linux |
| [Issue 57](https://code.google.com/p/robotframework/issues/detail?id=57) | Documentation   | Medium         | Change 'trunk' to something more easier to understand in wiki pages |
| [Issue 58](https://code.google.com/p/robotframework/issues/detail?id=58) | Enhancement     | Medium         | Disable creation of final Windows distribution in Linux |
| [Issue 61](https://code.google.com/p/robotframework/issues/detail?id=61) | Documentation   | Medium         | Improve global variable chapter in user guide |
| [Issue 38](https://code.google.com/p/robotframework/issues/detail?id=38) | Enhancement     | Low            | Telnet tests  |
| N/A        | Task            | Low            | Removed deprecated 'Get File With Encoding' from OperatingSystemLibrary |
| N/A        | Task            | Low            | Removed 'Create Dir' (old alias of 'Create Directory') from OperatingSystemLibrary |


# Robot Framework 2.0.2 #

Robot Framework 2.0.2 is a minor version containing miscellaneous fixes and improvements listed in the table below. Some of the fixed bugs are relatively severe, and there are also some pretty useful new features. A pretty significant change not explicitly listed is improving documentation of [standard libraries](TestLibraries.md). New functionality like internal links between keywords are due to enhancements to the [libdoc.py tool](LibraryDocumentationTool.md), but actual documentation texts have also been edited.

Robot Framework 2.0.2 was released on September 22nd 2008. Installers can be found from the [download page](http://code.google.com/p/robotframework/downloads/list) and
[installation instructions](http://robotframework.googlecode.com/svn/tags/robotframework-2.0.2/doc/userguide/RobotFrameworkUserGuide.html#installation-and-uninstallation) are in the user guide.

## Backwards incompatible changes ##

We try to avoid backwards incompatible changes in general and particularly between minor releases. This time there unfortunately was no fully safe way to fix problems listed below. Fortunately these changes affect only very few users.

  * To fix problems with 'Run' and 'Start Process' keywords on Jython ([issue 98](https://code.google.com/p/robotframework/issues/detail?id=98)), we needed to change arguments and return values of 'Read Process Output'. This might break test cases that try to return contents of the standard error with this keyword.

  * To defer processing arguments to built-in 'Run Keyword', 'Run Keyword If', and other similar keywords ([issue 67](https://code.google.com/p/robotframework/issues/detail?id=67)), we needed to special case how these keywords are handled internally. This change affects also external test libraries that use any of the run keyword variants internally. If you are responsible on such a library, see the documentation of `register_run_keyword` method in the BuiltIn test library module for more information.

  * Changed 'Split Extension' keyword from OperatingSystemLibrary so that leading and trailing dots in the file name are never considered to be extension separators ([issue 113](https://code.google.com/p/robotframework/issues/detail?id=113)). This was changed after the release candidate.

## List of fixes and enhancements ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 94](https://code.google.com/p/robotframework/issues/detail?id=94) | Defect   | Critical     | Libraries cannot be implemented as Python new style classes |
| [Issue 98](https://code.google.com/p/robotframework/issues/detail?id=98) | Defect   | Critical     | OperatingSystemLibrary keywords 'Run' and 'Read Process Output' hang on Jython if the executed command generates a lot of stderr |
| [Issue 69](https://code.google.com/p/robotframework/issues/detail?id=69) | Defect   | High         | Start Process keyword from OperatingSystemLibrary doesn't work on Jython 2.2 when stdout/stderr is redirected or command started on background |
| [Issue 106](https://code.google.com/p/robotframework/issues/detail?id=106) | Defect   | High         | Touch keyword from OperatingSystemLibrary deletes contents from existing files |
| [Issue 67](https://code.google.com/p/robotframework/issues/detail?id=67) | Enhancement | High         | Arguments to keywords executed with 'Run Keyword' variants should be resolved later |
| [Issue 73](https://code.google.com/p/robotframework/issues/detail?id=73) | Enhancement | High         | It should be possible to generate links to keywords inside keyword documentation using 'libdoc.py' |
| [Issue 75](https://code.google.com/p/robotframework/issues/detail?id=75) | Enhancement | High         | version information of test libraries into syslog |
| [Issue 113](https://code.google.com/p/robotframework/issues/detail?id=113) | Defect   | Medium       | Split Extension from OperatingSystemLibrary works differently on Python 2.6 than earlier versions |
| [Issue 50](https://code.google.com/p/robotframework/issues/detail?id=50) | Enhancement | Medium       | `Log List` and `Log Dictionary` keywords into CollectionsLibrary |
| [Issue 68](https://code.google.com/p/robotframework/issues/detail?id=68) | Enhancement | Medium       | Switch Connection in Telnet : return the old index or alias |
| [Issue 70](https://code.google.com/p/robotframework/issues/detail?id=70) | Enhancement | Medium       | New built-in variables ${SPACE} and ${EMPTY} |
| [Issue 76](https://code.google.com/p/robotframework/issues/detail?id=76) | Enhancement | Medium       | Information where a test library has been imported from should be written to syslog |
| [Issue 79](https://code.google.com/p/robotframework/issues/detail?id=79) | Enhancement | Medium       | Mechanism for getting warnings from deprecated keywords |
| [Issue 80](https://code.google.com/p/robotframework/issues/detail?id=80) | Enhancement | Medium       | Support for HTML log level for Log keyword from BuiltInLibrary |
| [Issue 87](https://code.google.com/p/robotframework/issues/detail?id=87) | Enhancement | Medium       | Better error messages when resolving extended variables fails |
| [Issue 90](https://code.google.com/p/robotframework/issues/detail?id=90) | Enhancement | Medium       | "Else If" support for "Set Variable If" keyword from BuiltInLibrary |
| [Issue 91](https://code.google.com/p/robotframework/issues/detail?id=91) | Enhancement | Medium       | Creating images from URLs ending with png, jpg, jpeg, gif, or bmp |
| [Issue 92](https://code.google.com/p/robotframework/issues/detail?id=92) | Enhancement | Medium       | Possibility to add new name for tags combined with option --tagstatcombine |
| [Issue 100](https://code.google.com/p/robotframework/issues/detail?id=100) | Enhancement | Medium       | Add methods start\_keyword and stop\_keyword to listener interface |
| [Issue 102](https://code.google.com/p/robotframework/issues/detail?id=102) | Enhancement | Medium       | It should be possible to implement Listeners as modules |
| [Issue 103](https://code.google.com/p/robotframework/issues/detail?id=103) | Enhancement | Medium       | Arguments to Listeners |
| [Issue 107](https://code.google.com/p/robotframework/issues/detail?id=107) | Enhancement | Medium       | Standard library keywords should accept / as a path separator regardless the operating system |
| [Issue 81](https://code.google.com/p/robotframework/issues/detail?id=81) | Documentation | Medium       | Need a keyword to check item counts of list/dictionary in CollectionsLibrary. |
| [Issue 104](https://code.google.com/p/robotframework/issues/detail?id=104) | Documentation | Medium       | Document and test that Listeners can be taken into use using a physical path |
| [Issue 72](https://code.google.com/p/robotframework/issues/detail?id=72) | Defect   | Low          | pythonpathsetter not working properly when Robot Framework is installed with easy\_install |
| [Issue 71](https://code.google.com/p/robotframework/issues/detail?id=71) | Enhancement | Low          | Add keyword Execute Command to Telnet Library |

# Robot Framework 2.0.3 #

Robot Framework 2.0.3 is another 2.0.x release with miscellaneous
fixes and improvements. The most visible change is changing the log
level of failure tracebacks to DEBUG ([issue 144](https://code.google.com/p/robotframework/issues/detail?id=144)), but the noticeable
performance improvement when processing larger output files ([issue 157](https://code.google.com/p/robotframework/issues/detail?id=157))
is probably the most important. We also have one new tool for
[generating test documentation](TestDataDocumentationTool.md) ([issue 147](https://code.google.com/p/robotframework/issues/detail?id=147)).

Robot Framework 2.0.3 was released on November 26th 2008. Installers
can be found from the
[download page](http://code.google.com/p/robotframework/downloads/list)
and [installation instructions](Installation.md) are same as for earlier
versions.

## Backwards incompatible changes ##

There should not be any backwards incompatible changes in the core
framework. Some of the [supporting tools](SupportingTools.md) work only
with this version, though, but their wiki pages have version specific
download links.

## List of fixes and enhancements ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 129](https://code.google.com/p/robotframework/issues/detail?id=129) | Defect   | High         | Test library scopes don't work correctly when libraries are imported "WITH NAME" |
| [Issue 156](https://code.google.com/p/robotframework/issues/detail?id=156) | Defect   | High         | PYTHONPATH not read when running tests on Jython |
| [Issue 117](https://code.google.com/p/robotframework/issues/detail?id=117) | Enhancement | High         | Using list variables as scalar variables |
| [Issue 147](https://code.google.com/p/robotframework/issues/detail?id=147) | Enhancement | High         | Tool for creating test plan |
| [Issue 157](https://code.google.com/p/robotframework/issues/detail?id=157) | Enhancement | High         | For performance reasons, use ElementTree for processing XML when it is available |
| [Issue 158](https://code.google.com/p/robotframework/issues/detail?id=158) | Enhancement | High         | Update OneClickInstaller to work with Python 2.6 |
| [Issue 115](https://code.google.com/p/robotframework/issues/detail?id=115) | Defect   | Medium       | Some file/dir related keywords from OperatingSystemLibrary don't work with non-absolute paths |
| [Issue 152](https://code.google.com/p/robotframework/issues/detail?id=152) | Defect   | Medium       | Default Tags, Test Setup, Test Teardown and Test Timeout do not work properly in init files |
| [Issue 159](https://code.google.com/p/robotframework/issues/detail?id=159) | Defect   | Medium       | --suite filter includes extra suites in case there are same named suites in multiple levels |
| [Issue 105](https://code.google.com/p/robotframework/issues/detail?id=105) | Enhancement | Medium       | Arguments to variable files taken use from command line |
| [Issue 116](https://code.google.com/p/robotframework/issues/detail?id=116) | Enhancement | Medium       | It should be possible to assign one None to multiple scalar variables and/or list variable |
| [Issue 119](https://code.google.com/p/robotframework/issues/detail?id=119) | Enhancement | Medium       | `Set Tags` and `Remove Tags` keywords |
| [Issue 144](https://code.google.com/p/robotframework/issues/detail?id=144) | Enhancement | Medium       | Change log level of traceback messages to DEBUG |
| [Issue 149](https://code.google.com/p/robotframework/issues/detail?id=149) | Enhancement | Medium       | Include constructor documentation in the library documentation generated by libdoc |
| [Issue 155](https://code.google.com/p/robotframework/issues/detail?id=155) | Enhancement | Medium       | Test libraries' argument counts should be checked before initialization |
| [Issue 143](https://code.google.com/p/robotframework/issues/detail?id=143) | Documentation | Medium       | Variable value assignment not clear in user guide |
| [Issue 125](https://code.google.com/p/robotframework/issues/detail?id=125) | Defect   | Low          | Variable names ${`*`} ${$} ${@} ${&} and ${%} don't work |
| [Issue 138](https://code.google.com/p/robotframework/issues/detail?id=138) | Defect   | Low          | Using $, @, %, & or `*` in variable name does not always work |


# Robot Framework 2.0.4 #

The most important fix in Robot Framework 2.0.4 is a workaround for installation problems with Python 2.6.1 on Windows ([issue 196](https://code.google.com/p/robotframework/issues/detail?id=196)),
but there are also some other important fixes and enhancements. Unless some critical bugs are found, this will be the final
2.0.x release.

Note that [issue 181](https://code.google.com/p/robotframework/issues/detail?id=181) and [issue 198](https://code.google.com/p/robotframework/issues/detail?id=198) are still left open at this point. This means that these issues were partly done in 2.0.4 and
they will be finalized in 2.1.

## Backwards incompatible changes ##

This release should not have any backwards incompatible changes. Users of TelnetLibrary should, however, note that the library nowadays
negotiates echo on, and this may affect some special cases. Please comment the [issue 183](https://code.google.com/p/robotframework/issues/detail?id=183) or send a note to [mailing lists](MailingLists.md)
if anything strange happens.

This release also deprecates the old special syntax for repeating a single keyword, but this only causes warnings until 2.2 release. See
[issue 193](https://code.google.com/p/robotframework/issues/detail?id=193) for more information why the syntax has been deprecated and how to easily replace it with new `Repeat Keyword` instead ([issue 192](https://code.google.com/p/robotframework/issues/detail?id=192)).
It is very unlikely that this syntax is in wide use, and [robotidy.py](TestDataTidyingTool.md) will be updated to fix it before
it is removed altogether ([issue 197](https://code.google.com/p/robotframework/issues/detail?id=197)).


## List of fixes and enhancements ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 196](https://code.google.com/p/robotframework/issues/detail?id=196) | Defect   | Critical     | Windows installer does not work with 2.6.1 Python |
| [Issue 168](https://code.google.com/p/robotframework/issues/detail?id=168) | Defect   | High         | Taking variable files and listeners into use with a path containing colons fails |
| [Issue 188](https://code.google.com/p/robotframework/issues/detail?id=188) | Defect   | High         | Methods in Java libraries starting with 'get' are executed at library load time |
| [Issue 185](https://code.google.com/p/robotframework/issues/detail?id=185) | Enhancement | High         | Arguments to libraries when their documentation is generated with libdoc.py |
| [Issue 192](https://code.google.com/p/robotframework/issues/detail?id=192) | Enhancement | High         | "Repeat Keyword" BuiltIn keyword |
| [Issue 193](https://code.google.com/p/robotframework/issues/detail?id=193) | Enhancement | High         | Deprecate the old syntax for repeating a single keyword multiple times |
| [Issue 198](https://code.google.com/p/robotframework/issues/detail?id=198) | Enhancement | High         | Jython 2.5 support |
| [Issue 171](https://code.google.com/p/robotframework/issues/detail?id=171) | Defect   | Medium       | It is not possible to build new packages using the source distribution |
| [Issue 172](https://code.google.com/p/robotframework/issues/detail?id=172) | Defect   | Medium       | OperatingSystem.Wait Until Removed doesn't work with patterns |
| [Issue 195](https://code.google.com/p/robotframework/issues/detail?id=195) | Defect   | Medium       | Confusing error when running out of memory while processing outputs |
| [Issue 175](https://code.google.com/p/robotframework/issues/detail?id=175) | Enhancement | Medium       | BuiltIn.Replace Variables should be allowed to return also non-string values |
| [Issue 181](https://code.google.com/p/robotframework/issues/detail?id=181) | Enhancement | Medium       | It should be possible to use OperatingSystem library standalone w/o Robot Framework |
| [Issue 183](https://code.google.com/p/robotframework/issues/detail?id=183) | Enhancement | Medium       | Telnet library should negotiate echo on |
| [Issue 184](https://code.google.com/p/robotframework/issues/detail?id=184) | Enhancement | Medium       | Support for --name and --title option to libdoc.py |
| [Issue 191](https://code.google.com/p/robotframework/issues/detail?id=191) | Documentation | Medium       | Add info how to increase JVM memory with Jython to RF User Guide |
| [Issue 189](https://code.google.com/p/robotframework/issues/detail?id=189) | Documentation | Low          | Need to document that Quick Start Guide demo cannot be executed with Jython |