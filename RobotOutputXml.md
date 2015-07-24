

# Introduction #

While Robot Framework is running tests, it generates an XML output file containing all information about the execution. After execution is over it creates, by default, log and report files using [rebot tool](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html#rebot) internally. The same `rebot` functionality can also be used externally afterwards both as a standalone tool and [programmatically](http://robot-framework.readthedocs.org/en/latest/autodoc/robot.html#robot.rebot.rebot).

This document describes the format of the output file in high level and contains detailed [XML schema files](#XML_Schema.md) that can be used for validating that an XML file is Robot Framework compatible. The output file format can be useful both for people interested in parsing the output and for people interested to create Robot Framework compatible outputs.

# General structure #

These are the main elements of the XML output with descriptions of their sub-elements. Unless stated otherwise, all attributes are optional. Additionally `rebot` does not care of the order of the XML elements, except for the order of suite, test, and kw elements.

robot - root element
  * suite - root element always has one suite which contains the subsuites and tests
  * statistics - statistics contains statistics of the test run
  * errors - if there were any errors, they are listed in this element

suite - suite element, name is a required attribute
  * kw - suite can have two kw elements: setup and teardown, both are optional
  * suite - any number of sub suites in execution order
  * test - any number of tests in execution order
  * doc - optional documentation element
  * metadata - optional suite metadata
  * status - suite has to have a status element

test - test element, name is a required attribute
  * kw - keywords of the test in execution order
  * msg - optional test message
  * doc - optional test documentation
  * tags - optional test tags
  * status - test has to have a status

kw - keyword element, name is a required attribute
  * doc - optional keyword documentation
  * arguments - optional keyword arguments
  * kw - possible sub-keywords in execution order
  * msg - any number of optional keyword messages
  * status - keyword has to have a status

For more details and full list of elements and attributes, please see the XML schema files below.

# XML Schema #

Available schema files:

  * [robot-xsd10.xsd](http://robotframework.googlecode.com/hg/doc/schema/robot-xsd10.xsd) - XML schema 1.0 compatible version
  * [robot-xsd11.xsd](http://robotframework.googlecode.com/hg/doc/schema/robot-xsd11.xsd) - XML schema 1.1 compatible version

The latter schema file is more complete, but XML schema 1.1 is not as widely supported as 1.0 version.