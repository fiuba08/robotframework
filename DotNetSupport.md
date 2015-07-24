

# Introduction #

Robot Framework can be executed on the [.NET](http://www.microsoft.com/NET/) platform with [IronPython](http://ironpython.codeplex.com/).

**NOTE:**
> Starting from [Robot Framework 2.7](ReleaseNotes27.md) installation
> using IronPython is [officially supported](Installation.md).
> Instructions on this page explain how to install earlier versions.

> Robot Framework 2.6 - 2.6.2 do not support IronPython due to
> problems explained in [issue 917](https://code.google.com/p/robotframework/issues/detail?id=917). These problem have been fixed in
> [Robot Framework 2.6.3](ReleaseNotes26#Robot_Framework_2.6.3.md).

# Installation #

## Preconditions ##

  1. Install [.NET Framework](http://www.microsoft.com/NET/). We have only tested with the 4.0 series, but earlier and newer versions should work too assuming you can install IronPython on them.
  1. Install [IronPython](http://ironpython.codeplex.com). We have tested with 2.6.2 and 2.7 releases but possible newer 2.6.x and 2.7.x releases ought to work too.
  1. Install the source distribution of [elementtree](http://effbot.org/downloads/#elementtree) module. We have only tested with the 1.2.7 preview release, which should have better IronPython support than 1.2.6. See [Installing Python modules](#Installing_Python_modules.md) section below for installation instructions.
  1. If you are using IronPython 2.6.x with Robot Framework 2.6.3 or newer, install [IronPython.Zlib module](https://bitbucket.org/jdhardy/ironpythonzlib). This module is included into IronPython 2.7 so separate installation is not needed with that release.
  1. Optionally, you can add IronPython installation directory into `PATH` to ease running `ipy.exe` from the command line.

## Installing Python modules ##

  1. Get and extract the source distribution package of the module you want to install. Alternatively you may be able to checkout the source code directly from the project's version control.
  1. Go to the extracted or checked out directory from the command line.
  1. Install the module with command `ipy setup.py install`. If you do not have `ipy` in `PATH`, you need to use a full path to it. With IronPython 2.6.x you also need to add `--no-compile` option like in `ipy setup.py install --no-compile`.

## Robot Framework ##

  1. Get the source code either as [downloading](http://code.google.com/p/robotframework/downloads/list) a source distribution or by doing a [checkout](http://code.google.com/p/robotframework/source/checkout).
  1. See [Installing Python modules](#Installing_Python_modules.md) section above for installation instructions.

# Running tests #

## Start-up script ##

Robot Framework installation creates `pybot.bat` start-up script into `<IronPythonInstallation>\Scripts` directory. You can execute the script by using a full path to it or add the directory into `PATH`. If you do the latter, you may also want to rename the script to `ipybot.bat` to avoid a clash with the normal `pybot` start-up script.

## Execution ##

If you have renamed the script to `ipybot.bat` and have it in `PATH`, you can run tests simply with:

```
  ipybot path/to/tests.txt
```

# Future enhancements #

The main enhancements needed to support .NET better are:

  1. Better installation support to create `ipybot` script automatically ([issue 480](https://code.google.com/p/robotframework/issues/detail?id=480))
  1. Support for writing test libraries with C# ([issue 721](https://code.google.com/p/robotframework/issues/detail?id=721))