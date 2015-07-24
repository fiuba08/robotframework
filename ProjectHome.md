# Robot Framework #


---


> _Robot Framework project has been moved to **[GitHub](https://github.com/robotframework/robotframework)** and generic information about the ecosystem to **[http://robotframework.org](http://robotframework.org)**._


---


Robot Framework is a generic test automation framework
for acceptance testing and acceptance test-driven development (ATDD).
It has easy-to-use tabular test data syntax and utilizes the
keyword-driven testing approach. Its testing capabilities can be
extended by test libraries implemented either with Python or Java, and
users can create new keywords from existing ones using the same syntax
that is used for creating test cases.

These project pages are only for Robot Framework core framework.
See **[http://robotframework.org](http://robotframework.org)** for more
information about the whole Robot Framework ecosystem.

Robot Framework is open source software released under [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0.html). Its copyrights are owned and development supported by [NSN](http://www.nsn.com). Most tools and libraries in the ecosystem are also open source, but they have various different licenses and copyright owners.

## Features ##

  * Enables easy-to-use tabular syntax for [creating test cases](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#creating-test-cases) in a uniform way.
  * Allows using [keyword-driven, data-driven and behavior-driven (BDD)](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#different-test-case-styles) approaches.
  * Provides ability to create reusable [higher-level keywords](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#creating-user-keywords) from the existing keywords.
  * Provides easy-to-read [reports and logs](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#created-outputs) in HTML format.
  * Is platform and application independent.
  * The [modular architecture](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#high-level-architecture) supports creating tests even for applications with several diverse interfaces.
  * Provides a simple [library API](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#creating-test-libraries) for creating customized test libraries.
  * Provides a [command line interface and XML based outputs](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#executing-test-cases) for integration into existing build infrastructure (continuous integration systems).
  * Provides support for [Selenium](http://code.google.com/p/robotframework-seleniumlibrary/) for web testing, [Java GUI testing](http://code.google.com/p/robotframework-swinglibrary/), [running processes](OperatingSystemLibrary.md), [Telnet](TelnetLibrary.md), [SSH](http://code.google.com/p/robotframework-sshlibrary/), and so on.
  * [Remote library interface](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#remote-library-interface) enables distributed testing and implementing test libraries in any programming language.
  * Provides [tagging](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#tagging-test-cases) to categorize and select test cases to be executed.
  * Has built-in support for [variables](http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.7.6#variables), practical particularly for testing in different environments.


## News ##
  * _2014-06-30_ We have moved to **[GitHub](https://github.com/robotframework/robotframework)**.
  * _2014-06-17_ **[Robot Framework 2.8.5](ReleaseNotes28#Robot_Framework_2.8.5.md)** released with many new enhancements and bug fixes.  The distribution packages are hosted at [Pypi](https://pypi.python.org/pypi/robotframework).
  * _2014-02-12_ **[RIDE 1.3](https://github.com/robotframework/RIDE/wiki/Release-notes#wiki-ride-1-3)** released.
  * _2013-12-03_ **[Robot Framework 2.8.3](ReleaseNotes28#Robot_Framework_2.8.3.md)** released with some critical bug fixes and new kwargs support for Java and Remote libraries.  The distribution packages are hosted at [Pypi](https://pypi.python.org/pypi/robotframework).
  * _2013-11-26_ **[Robot Framework 2.8.2](ReleaseNotes28#Robot_Framework_2.8.2.md)** released. This is a minor version with lots of major features!  The distribution packages are hosted at [Pypi](https://pypi.python.org/pypi/robotframework).
  * _2013-06-14_ **[Robot Framework 2.8.1](ReleaseNotes28#Robot_Framework_2.8.1.md)** released with a fix that allows it work with SSHLibrary and Selenium2Library.
  * _2013-06-11_ **[Robot Framework 2.8](ReleaseNotes28#Robot_Framework_2.8.md)** released with loads of bigger and smaller enhancements and bug fixes.
  * _2013-04-04_ New project pages for the whole Robot Framework ecosystem available at **[http://robotframework.org](http://robotframework.org)**!
  * _2013-03-19_ Another **[Robot Framework Demo](https://bitbucket.org/robotframework/robotdemo/wiki/Home)** released.
  * _2013-03-08_ New demo project: **[Web testing with Robot Framework and Selenium2Library](https://bitbucket.org/robotframework/webdemo)**
  * _2013-02-26_ **[Robot Framework 2.7.7](ReleaseNotes27#Robot_Framework_2.7.7.md)** released with enhanced reports and other fixes/features.
  * _2013-02-20_ **[RIDE 1.1](http://code.google.com/p/robotframework-ride/)** released.
  * _2013-02-09_ **[SwingLibrary 1.5.3](https://github.com/robotframework/SwingLibrary)** released.
  * _2013-01-18_ **[RIDE 1.0.1](http://code.google.com/p/robotframework-ride/)** released.
  * _2013-01-07_ **[Robot Framework 2.7.6](ReleaseNotes27#Robot_Framework_2.7.6.md)** has been released.
  * _2012-12-20_ **[RIDE 1.0](https://github.com/robotframework/RIDE)** released.
  * _2012-12-18_ **[RIDE 0.55](https://github.com/robotframework/RIDE)** (a.k.a. 1.0 RC) released.
  * _2012-12-10_ **[RIDE 0.54](https://github.com/robotframework/RIDE)** released.
  * _2012-11-19_ **[RIDE 0.53](https://github.com/robotframework/RIDE)** released.
  * _2012-11-08_ **[RIDE 0.52](https://github.com/robotframework/RIDE)** released.
  * _2012-10-24_ **[Robot Framework 2.7.5](ReleaseNotes27#Robot_Framework_2.7.5.md)**, another bigger-than-normal minor release, is out.
  * _2012-10-15_ **[Mabot 0.9](http://code.google.com/p/robotframework-mabot/)** fixing support with Robot Framework 2.7 released.
  * _2012-10-14_ **[Eclipse Plugin](https://github.com/NitorCreations/RobotFramework-EclipseIDE/wiki)** for Robot Framework released by [Nitor Creations](http://nitorcreations.com/)!
  * _2012-10-09_ **[RIDE 0.51](https://github.com/robotframework/RIDE)** released.
  * _2012-10-01_ **[Jenkins Plugin 1.2.3](https://wiki.jenkins-ci.org/display/JENKINS/Robot+Framework+Plugin)** released.
  * _2012-09-18_ New **[MavenPlugin](http://robotframework.github.com/MavenPlugin)** released.
  * _2012-09-18_ **[SwingLibrary 1.4(.1)](https://github.com/robotframework/SwingLibrary)** released with new JavalibCore.
  * _2012-09-17_ **[JavalibCore 1.0](https://github.com/robotframework/JavalibCore)** released with reduced set of dependencies.
  * _2012-09-06_ **[Robot Framework 2.7.4](ReleaseNotes27#Robot_Framework_2.7.4.md)** released.
  * _2012-08-31_ **[SSHLibrary 1.1](http://code.google.com/p/robotframework-sshlibrary/)** released.
  * _2012-08-28_ **[RIDE 0.49](https://github.com/robotframework/RIDE)** released.
  * _2011-08-28_ **[SeleniumLibrary 2.9.1](http://code.google.com/p/robotframework-seleniumlibrary/)** released.
  * _2012-08-08_ **[RIDE 0.47](https://github.com/robotframework/RIDE)** released.
  * _2012-07-04_ **[RIDE 0.46.1](https://github.com/robotframework/RIDE)** released.
  * _2012-06-18_ **[Robot Framework 2.7.3](ReleaseNotes27#Robot_Framework_2.7.3.md)** released.
  * _2012-06-08_ **[Robot Framework 2.7.2](ReleaseNotes27#Robot_Framework_2.7.2.md)** released.
  * _2012-06-06_ **[RIDE 0.45](https://github.com/robotframework/RIDE)** released.
  * _2012-05-08_ **[RIDE 0.44](https://github.com/robotframework/RIDE)** released.
  * _2012-04-20_ **[JoyRide 0.0.7](https://github.com/robotframework/JoyRide)** Eclipse plugin prototype released.
  * _2012-03-26_ **[Robot Framework 2.7.1](ReleaseNotes27#Robot_Framework_2.7.1.md)** released.
  * _2012-03-14_ **[Robot Framework 2.7](ReleaseNotes27.md)** released.
  * _2012-03-12_ **[Selenium2Library 1.0](https://github.com/rtomac/robotframework-selenium2library)** is out.
  * _2012-02-29_ **[RIDE 0.42(.1)](https://github.com/robotframework/RIDE)** released.
  * _2012-02-13_ **[RIDE 0.41](https://github.com/robotframework/RIDE)** released.
  * _2012-01-16_ **[RIDE 0.40.2](https://github.com/robotframework/RIDE)** released.
  * _2011-12-19_ **[SeleniumLibrary 2.8.1](http://code.google.com/p/robotframework-seleniumlibrary/)** released with support for Firefox 8 via Selenium server 2.15.
  * _2011-10-22_ The first version of **[Selenium2Library](https://github.com/rtomac/robotframework-selenium2library)**, a drop-in-replacement for [SeleniumLibrary](http://code.google.com/p/robotframework-seleniumlibrary/) using [Selenium 2 WebDriver API](http://seleniumhq.org/projects/webdriver/), has been released.
  * _2011-09-30_ **[Robot Framework 2.6.3](ReleaseNotes26#Robot_Framework_2.6.3.md)** with fixed [.NET/IronPython support](DotNetSupport.md) released.
  * _2011-09-30_ **[Robot Framework 2.6.2](ReleaseNotes26#Robot_Framework_2.6.2.md)** with some bug fixes and enhancements such as sortable details table released.
  * _2011-09-27_ **[RIDE 0.39(.1)](http://code.google.com/p/robotframework-ride)** released.
  * _2011-09-01_ **[RIDE 0.38](http://code.google.com/p/robotframework-ride)** released.
  * _2011-08-09_ **[SeleniumLibrary 2.8](http://code.google.com/p/robotframework-seleniumlibrary/)** has been released with Selenium Server version 2.3 and Firefox 5 support.
  * _2011-08-08_ There is now a **[TextMate bundle](https://bitbucket.org/jussimalinen/robot.tmbundle/)** for Robot Framework syntax.
  * _2011-08-08_ **[RIDE 0.36](http://code.google.com/p/robotframework-ride)** released.
  * _2011-07-27_ **[Robot Framework 2.6.1](ReleaseNotes26#Robot_Framework_2.6.1.md)** released. This is a micro release that fixes library documentation generation tool and does not affect normal Robot Framework use. Windows installers for example are not updated.
  * _2011-07-26_ **[Robot Framework 2.6](ReleaseNotes26.md)** released. This is a new major release with new reports and logs and other smaller enhancements and bug fixes.
  * _2011-05-02_ **[SeleniumLibrary 2.7](http://code.google.com/p/robotframework-seleniumlibrary/)** released.
  * _2011-04-21_ **[Robot Framework 2.5.7](ReleaseNotes25#Robot_Framework_2.5.7.md)** a bug fix release with some minor enhancements released.
  * _2011-04-13_ **[RIDE 0.35](http://code.google.com/p/robotframework-ride)** released.
  * _2011-04-07_ 1.1 version of [Robot Framework Plugin for Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Robot+Framework+Plugin) released.
  * _2011-03-31_ **[RIDE 0.34](http://code.google.com/p/robotframework-ride)** released.
  * _2011-03-28_ Robot Framework has **[strong presence at XP 2011 conference](http://hereberobots.blogspot.com/2011/03/robot-framework-at-xp2011-conference.html)**.
  * [more news...](NewsArchive.md)