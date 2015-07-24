

There are several tools that can be used with Robot Framework including tools for
editing test data and processing outputs. Some tools are distributed with Robot
Framework itself, but some others are available as separate projects.

The tools that are distributed with Robot Framework are included in the source
distribution under `tools` directory. Additionally they can be downloaded separately,
and the download locations are listed under the respective tool pages.


# Tools distributed with Robot Framework #

**NOTE** Following tools have been moved to separate projects at https://bitbucket.org/robotframework/,
and will be removed from standard source distribution starting from version 2.9:
- Historical Reporter (risto.py)
- Output File Fixer (fixml.py)
- Test Result Diff (robotdiff.py)
- File Viewer (fileviewer.py)
- One Click Installer
- Test Status Checker (statuschecker.py)
- Execution Time Reporter (times2csv.py)

Following tools are now included in Robot Framework installation:
- Library Documentation Generator (libdoc.py)
- Test Documentation Generator (testdoc.py)
- Test Data Tidyer (robotidy.py)

See tool pages for more detailed information on where the tools have been moved.

## Library Documentation Generator (libdoc.py) ##

[libdoc.py](LibraryDocumentationTool.md) is tool for generating HTML or XML documentation from keywords of a test library or a resource file.

## Test Documentation Generator (testdoc.py) ##

[testdoc.py](TestDataDocumentationTool.md) is tool for generating high level test documentation from given test data. The generated documentation includes names, documentations and other metadata of test suites and test cases, as well as names and arguments of top-level keywords. Requires Robot Framework 2.0.3 or newer.

## Historical Reporter (risto.py) ##

[risto.py](HistoricalReportingTool.md) is a tool for generating graphs about historical statistics of test executions.

## Output File Fixer (fixml.py) ##

[fixml.py](OutputFileFixingTool.md) is a tool for fixing broken Robot Framework output files.

## Test Data Tidyer (robotidy.py) ##

[robotidy.py](TestDataTidyingTool.md) is a tool for cleaning Robot Framework test data, changing test data format between HTML and TSV and fixing inline comments to format supported by Robot IDE.

## Test Result Diff (robotdiff.py) ##

[robotdiff.py](TestResultDiffingTool.md) is a tool for generating diff reports from Robot Framework output files.

## Execution Time Reporter (times2csv.py) ##

[times2csv.py](ExecutionTimeReportingTool.md) is a tool for generating start, end and elapsed time information about suites, tests and keywords in CSV format.

## File Viewer (fileviewer.py) ##

[fileviewer.py](FileViewingTool.md) is a graphical tool implementing UNIX tail-like functionality. It is especially designed to view debug files

## One Click Installer ##

OneClickInstaller is an [AutoIT](http://www.autoitscript.com/autoit3/) script that installs Robot Framework and its dependencies.

## Test Status Checker (statuschecker.py) ##

[statuschecker.py](TestStatusCheckerTool.md) is a tool for verifying that test case statuses and messages and also keyword log messages are as expected.


# External tools #

## Robot IDE (RIDE) ##

[RobotIDE](http://code.google.com/p/robotframework-ride) is a tool for editing test data.

## Manual Test Reporter (Mabot) ##

[Mabot](http://code.google.com/p/robotframework-mabot/) is a tool for manual test result reporting.

## Java Tools ##

[Java Tools](http://code.google.com/p/robotframework-javatools/) is a collection of utilities which help creating test libraries using Java.