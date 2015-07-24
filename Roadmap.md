

# Introduction #

This roadmap lists the highest priority tasks the [NSN](http://nsn.com) sponsored core development team will undertake during the spring 2010. External help in the form of feature request, bug reports and patches is highly appreciated. The wider community can obviously also work with other, totally different, Robot Framework related projects.

# Robot Framework #

## Robot Framework 2.1.3 ##

This minor release contains mainly [relatively simple fixes](http://code.google.com/p/robotframework/issues/list?can=1&q=target%3D2.1.3) that we want to release before starting the
bigger new development. Target is to get the release out
already in January. Act fast if you have fixes or features that
you want to be included into this release.

## Robot Framework 2.5 ##

This is a new major release with a [lot of new functionality](http://code.google.com/p/robotframework/issues/list?can=1&q=target%3D2.5). The final
scope is not decided yet and users will have a change to tell
their opinion when the actual development starts. The final release date will
depend highly on the scope but the original target is March/April.

This release will have Python/Jython 2.5 as the minimum version requirement.
This change is done to make it possible to use newer Python features, ease the core team's workload in testing with the older
versions, and to start the path towards supporting Python 3 in the
future. Users of the older Python and Jython version that cannot easily upgrade can keep using the RF 2.1.x series. Subsequent 2.1.x releases may still be created in the future if there is a need for bug fixes.

One of the major targets of the 2.5 release is to make Robot Framework's parsing
modules more flexible to use from outside by RIDE and other tools.
This will require large internal refactorings which aren't directly
visible when tests are executed.


# RIDE #

## RIDE 0.21 ##

[RIDE](http://code.google.com/p/robotframework-ride) 0.21 is mainly a [bug fix release](http://code.google.com/p/robotframework-ride/issues/list?can=1&q=target%3D0.21) after the big changes in the previous
versions. It contains, however, some nice enhancements like a possibility to execute tests
or other commands in the system. RIDE 0.21 will be released in January.

This will be the last RIDE version to support Robot Framework 2.1.x and thus Python
2.4. Subsequent 0.21.x maintenance releases with important bug fixes can be created if there is a need.

## Towards 1.0 ##

After Robot Framework 2.5 with more flexible test data parsing modules is ready,
it's time to start looking towards RIDE 1.0. It is still too early to
tell can this significant milestone be achieved this spring or what the
final scope will be. On the way towards the 1.0 there will be several 0.x releases with approximately one new release per month.


# Test libraries and supporting tools #

## SwingLibrary ##

[SwingLibrary](http://code.google.com/p/robotframework-swinglibrary) 1.1 with [various enhancements and fixes](http://code.google.com/p/robotframework-swinglibrary/issues/list?can=1&q=target%3D1.1) will be released in January. Other releases
are not planned but bug fix releases can be created if there's a need.

## JvmConnector ##

[JvmConnector](http://code.google.com/p/robotframework-javatools/wiki/JvmConnector) 1.0 with new [RemoteApplications](http://code.google.com/p/robotframework-javatools/wiki/RemoteApplications) library will be released in January. Bug fix releases will be done based on needs but otherwise no further development is planned.

## SeleniumLibrary ##

There will be at least [SeleniumLibrary](http://code.google.com/p/robotframework-seleniumlibrary) 2.2.3 [bug fix release](http://code.google.com/p/robotframework-seleniumlibrary/issues/list?can=1&q=target%3D2.2.3) but its schedule is still
open. New major release is also possible, especially if Selenium 2 is
released and SeleniumLibrary can be switched to use it easily.

## Hudson plugin ##

A prototype version of the [Hudson plugin](http://code.google.com/p/robotframework-javatools/wiki/HudsonPlugin) is already available and an
actual release will be created during the spring.

## Other libraries and tools ##

No new development is planned but bug fix releases will be created on
the need bases.