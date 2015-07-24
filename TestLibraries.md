**NOTE:** Due to problems with Google Code, library documentation might be intermittently unavailable. If you get "403 Forbidden" or similar error, download user guide with library documentation [from the Downloads page](Downloads.md).

**NOTE:** See http://robotframework.org for an updated list of available libraries as well as information about Robot Framework ecosystem in general.

# Standard test libraries #

These test libraries are automatically installed with Robot Framework.
They are always available for use but they need to be imported in the
test data, expect for the [BuiltIn library](BuiltInLibrary.md) which is
also imported automatically.

  * [BuiltIn](BuiltInLibrary.md)
  * [OperatingSystem](OperatingSystemLibrary.md)
  * [Screenshot](ScreenshotLibrary.md)
  * [Telnet](TelnetLibrary.md)
  * [Collections](CollectionsLibrary.md)
  * [String](StringLibrary.md)
  * [Dialogs](DialogsLibrary.md)
  * [Remote](RemoteLibrary.md)
  * [XML](XMLLibrary.md) (new in RF 2.7.4)
  * [Process](ProcessLibrary.md) (new in RF 2.8)
  * [DateTime](DateTimeLibrary.md) (new in RF 2.8)

# External test libraries #

This is a list of publicly available test libraries that can be used
with Robot Framework but need to be installed separately. Please refer
to the individual project pages for information about installing and
using them.

  * [SeleniumLibrary](http://code.google.com/p/robotframework-seleniumlibrary/) - A web testing library that uses popular [Selenium tool](http://seleniumhq.org/) internally.
  * [Selenium2Library](https://github.com/rtomac/robotframework-selenium2library#readme) - A drop-in-replacement for SeleniumLibrary using newer [Selenium 2 WebDriver API](http://seleniumhq.org/projects/webdriver/).
  * [Selenium2Library Java port](https://github.com/MarkusBernhardt/robotframework-selenium2library-java#readme) - Java implementation of Se2Lib. Compatible with Jython 2.5.
  * [watir-robot](https://github.com/semperos/watir-robot) - A web testing library that uses popular [Watir tool](http://watir.com/) via the [remote library interface](RemoteLibrary.md).
  * [WatinLibrary](http://code.google.com/p/robotframework-watinlibrary) - A web testing library that uses [Watin tool](http://www.watin.org/) (a .NET port of Watir) via the [remote library interface](RemoteLibrary.md).
  * [SwingLibrary](https://github.com/robotframework/SwingLibrary) - A Swing GUI testing library.
  * [EclipseLibrary](http://code.google.com/p/robotframework-eclipselibrary/) - A library for testing Eclipse RCP applications using SWT widgets.
  * [AutoItLibrary](http://code.google.com/p/robotframework-autoitlibrary/) - Windows GUI testing library that uses [AutoIt](http://www.autoitscript.com/) freeware tool as a driver.
  * [DatabaseLibrary (Java)](https://github.com/ThomasJaspers/robotframework-dblibrary) - A test library that provides common functionality for testing database contents. Implemented using Java so works only with Jython.
  * [DatabaseLibrary (Python)](http://franz-see.github.com/Robotframework-Database-Library/) - Another library for database testing. Implemented with Python and works also on Jython.
  * [SSHLibrary](http://code.google.com/p/robotframework-sshlibrary/) - A test library that enables SSH and SFTP.
  * [HTTP test library using livetest](http://github.com/peritus/robotframework-httplibrary)
  * [HTTP test library using Requests](http://github.com/bulkan/robotframework-requests)
  * [SudsLibrary](https://github.com/ombre42/robotframework-sudslibrary#readme) - library for testing SOAP-based web services
  * [AndroidLibrary](https://github.com/lovelysystems/robotframework-androidlibrary#readme) - Library for Android testing that uses [Calabash Android](https://github.com/calabash/calabash-android) internally.
  * [IOSLibrary](https://github.com/lovelysystems/robotframework-ioslibrary#readme) - Library for iOS testing that uses [Calabash iOS Server](https://github.com/calabash/calabash-ios-server) internally.
  * [Rammbock](https://github.com/robotframework/Rammbock#readme) - Generic network protocol test library.
  * [How-To: Sikuli and Robot Framework Integration](http://blog.mykhailo.com/2011/02/how-to-sikuli-and-robot-framework.html) - This is not really a library but these instructions explain how to integrate [Sikuli tool](http://sikuli.org/) with Robot Framework