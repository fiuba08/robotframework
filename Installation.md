

# Introduction #

These instructions cover the basic procedure for installing Robot
Framework and its preconditions on different operating systems.
The [User Guide](UserGuide.md) contains more detailed description of the
installation, information of where files are installed, and so on.

If you are familiar with installing Python packages and have
[pip](http://pip-installer.org) available, just run the following command:

```
    pip install robotframework
```

**NOTE:**

> These instructions apply for Robot Framework 2.7 and newer. Robot
> Framework 2.6 or earlier can be installed according to the
> [old instructions](Installation26.md). List of changes compared to 2.6 are also
> [listed separately](#Changes_compared_to_Robot_Framework_2.6_and_earlier.md).

## Supported installation approaches ##

Robot Framework is implemented using [Python](http://python.org) and
also runs on [Jython](http://jython.org) (JVM) and
[IronPython](http://ironpython.codeplex.com) (.NET) interpreters. An
obvious [precondition](#Preconditions.md) is that you need to install
the interpreters you want to use.

Robot Framework itself can be installed from [source](#Installing_from_source.md),
using [Windows installer](#Windows_installer.md), or using
[Python package managers](#Python_package_managers.md) such as `pip` and
`easy_install`. There is also a [standalone JAR package](#Standalone_JAR_package.md)
that  contains Jython and thus requires only Java to be installed.

Windows XP users can use [One Click Installer](#One_Click_Installer.md) to
install [preconditions](#Preconditions.md) and Robot Framework itself in
one go.

## Different start-up scripts ##

Robot Framework has different entry points for running tests and for
creating reports and logs based on earlier test results. For both of
these usages there are also different start-up scripts for different
interpreters:

| **Interpreter** | **Test execution** | **Report/log creation** |
|:----------------|:-------------------|:------------------------|
| Python          | `pybot`            | `rebot`                 |
| Jython          | `jybot`            | `jyrebot`               |
| IronPython      | `ipybot`           | `ipyrebot`              |

In addition to using these start-up scripts, it is possible to both
run tests and create reports and logs by executing the entry points
directly using a selected interpreter. It is possible to both execute
entry points as modules using `-m` option and to run them as
scripts. Both of these are illustrated by these examples:

```
   # Run tests with Python by executing `robot.run` module.
   python -m robot.run

   # Run tests with Jython by running `robot/run.py` script.
   jython path/to/robot/run.py

   # Create reports/logs with IronPython by executing `robot.rebot` module.
   ipy -m robot.rebot

   # Create reports/logs with Python by running `robot/rebot.py` script.
   python path/to/robot/rebot.py
```

## Verifying installation ##

After a successful installation with Python you should be able to
execute the following commands on the command prompt. To verify
installation on Jython or IronPython, you need to replace `pybot`
with `jybot` or `ipybot`, respectively.

```
   $ pybot --version
   Robot Framework 2.7 (Python 2.6.6 on linux2)
```

## Changes compared to Robot Framework 2.6 and earlier ##

Robot Framework installation has changed quite a bit between 2.6 and
2.7 versions:

  1. Installation using [pip](#Python_package_managers.md) is finally supported.
  1. Installation using [IronPython](#IronPython_installation.md) is officially supported. As a result you get new `ipybot` and `ipyrebot` start-up scripts.
  1. Installation using [Jython](#Jython_installation.md) creates new `jyrebot` start-up script in addition to `jybot`. `rebot` script is not created anymore with Jython.
  1. Installing [from source](#Installing_from_source.md) or [with package managers](#Python_package_managers.md) on [Python](#Python_installation.md) **does not** create `jybot` script anymore. You need to install the framework from source using Jython or use [Windows installers](#Windows_installer.md) to create it.
  1. All start-up scripts (`pybot`, `rebot`, `jybot`, ...) require the appropriate interpreter to be in [PATH](#Setting_PATH.md).
  1. Outside Windows, start-up scripts are implemented in Python to, for example, ease using them with virtualenv.
  1. Source distribution only contains actual source code and tools. You need to download User Guide and Quick Start Guide separately or view them online.

# Preconditions #

Robot Framework is supported on [Python](http://python.org),
[Jython](http://www.jython.org) and [IronPython](http://ironpython.codeplex.com)
and should also run on [PyPy](http://pypy.org). The interpreter you want to
use should be installed before installing the framework.

If you just want to test the framework and do not have any special
needs, it is recommended to try it first with Python.

## Python installation ##

On most UNIX-like systems such as Linux and OSX you have Python
installed by default. If you are on Windows or otherwise need to
install Python yourself, your best place to start is probably the
[Python homepage](http://python.org). There you can download a suitable
installer and get more information about the installation and Python
in general.

Starting from Robot Framework 2.5, Python 2.5 is the minimum supported
Python version. Earlier versions support also Python 2.3 and
2.4. Robot Framework is currently not compatible with Python 3.x
versions.

**NOTE:**
> On Windows, and especially on Windows Vista and Windows 7, it is
> recommended to install Python to all users, and to run the
> installation as an administrator.

> Running Robot Framework on Python using the `pybot` start-up script
> requires `python` to be executable directly in the system. This
> means that you need to make sure it is in [PATH](#Setting_path.md).

> Environment variable `PYTHONCASEOK` should be not set on Windows
> machines. Robot Framework will not work correctly with it.

## Jython installation ##

Using test libraries implemented with Java or using Java tools
internally requires running Robot Framework on Jython, which in turn
requires Java Runtime Environment (JRE). Starting from Robot Framework
2.5, the minimum supported Jython version is 2.5 which requires Java
1.5 (a.k.a. Java 5) or newer. Earlier Robot Framework versions support
also Jython 2.2.

Installing Jython is a fairly easy procedure, and the first step is
getting an installer from the [Jython homepage](http://www.jython.org).
The installer is an executable JAR package, which you can run from the
command line like `java -jar jython_installer-<version>.jar`.
Depending on the system configuration, it may also be possible to just
double-click the installer.

**NOTE:**
> Running Robot Framework on Jython using the `jybot` start-up script
> requires `jython` to be executable directly in the system. This
> means that you need to make sure it is in [PATH](#Setting_path.md).

## IronPython installation ##

[IronPython](http://ironpython.codeplex.com) allows running Robot
Framework on the [.NET platform](http://www.microsoft.com/NET/). Robot
Framework is only officially supported and tested on IronPython 2.7
using the .NET 4.0 series.

An additional dependency is installing
[elementtree](http://effbot.org/downloads/#elementtree) module 1.2.7
preview release. This is required because the `elementtree` version
distributed with IronPython
[is broken](http://ironpython.codeplex.com/workitem/31923). You can do
the installation by downloading the
[elementtree](http://effbot.org/downloads/#elementtree) source
distribution, unzipping it, and running `ipy setup.py install` on the
command prompt in the created directory.

**NOTE:**
> Running Robot Framework on IronPython using the `ipybot` start-up script
> requires `ipy` to be executable directly in the system. This
> means that you need to make sure it is in [PATH](#Setting_path.md).

## Setting `PATH` ##

The `PATH` environment variable lists locations where commands
executed in a system are searched from. To make using Robot Framework
easier from the command line, it is recommended to add the locations
where the start-up scripts are installed into `PATH`. The start-up
scripts themselves require the matching interpreter to be in `PATH`,
so that installation location must be added there too.

When using Python on UNIX-like machines both Python itself and scripts
installed with should be automatically in `PATH` and no extra actions
needed. On Windows and with other interpreters `PATH` must be edited.

### What directories to add ###

What directories you need to add to `PATH` depends on the
interpreter. The first location is the installation directory of the
interpreter (e.g. `C:\Python27`) and the other is the location where
scripts are installed with that interpreter. Both Python and
IronPython install scripts to `Scripts` directory under the
installation directory (e.g. `C:\Python27\Scripts`) but Jython uses
`bin` directory (e.g. `C:\jython2.5.2\bin`).

Notice that `Scripts` and `bin` directory may not be created
as part of the interpreter installation. In that case they will be
automatically created when Robot Framework or some other third party
module is installed.

### Setting `PATH` on Windows ###

On Windows you can configure `PATH` by following the steps
below. Notice that the exact setting names may be different on
different Windows versions, but the basic approach is still the same.

  1. Open `Start > Settings > Control Panel > System > Advanced > Environment Variables`. There are `User variables` and `System variables` and the difference between them is that `User variables` affect only the current users, whereas `System variables` affect all users.
  1. To edit existing `PATH`, select `Edit` and add `;<InterpreterInstallationDir>;<InterpreterInstallationDir>\Scripts\` at the end of the value. Note that the leading colon (`;`) is important, as it separates different entries. To add a new value, select `New` and provide both the name and the value, this time without the leading colon.
  1. Start a new command prompt for the changes to take effect.

**NOTE:**

> Do not add quotes around directories you add into `PATH`.
> For example, never use `"C:\Python27\Scripts"`. Quotes
> [can cause problems with Python programs](http://bugs.python.org/issue17023)
> and they are not needed even if the directory path contains spaces.

### Setting `PATH` on UNIX-like systems ###

On UNIX-like systems you typically you need to edit either some system
wide or user specific configuration file. Which file to edit and how
depends on the system and you need to consult your operating system
documentation for more details.

# Installation #

## Installing from source ##

This installation method can be used on any operating system with any
of the supported interpreters. Installing _from source_ can sound a
bit scary, but the procedure is actually pretty straightforward.

You typically get the source by downloading a
[source distribution package](https://pypi.python.org/pypi/robotframework)
but you can also check it out directly from the
[version control system](http://code.google.com/p/robotframework/source).
In the former case, first extract the package somewhere, and as a
result, you have a directory named `robotframework-<version>`. After
that you just need to go to the created directory on the command
prompt and run one, or more, of the following commands, depending on
the interpreter you want to use:

```
   # Installing with Python. Creates `pybot` and `rebot` scripts.
   python setup.py install

   # Installing with Jython. Creates `jybot` and `jyrebot` scripts.
   jython setup.py install

   # Installing with IronPython. Creates `ipybot` and `ipyrebot` scripts.
   ipy setup.py install
```

**NOTE:**
> Starting from Robot Framework 2.7, installation using Python **does
> not** create `jybot` script anymore. To create that, you need to
> install the framework separately using Jython.

## Windows installer ##

There are separate graphical installers for 32 bit and 64 bit Windows
systems. The former installer has name in format
`robotframework-<version>.win32.exe` and the latter
`robotframework-<version>.win-amd64.exe`. After you have
[downloaded an appropriate installer](https://pypi.python.org/pypi/robotframework),
you just need to double-click it and follow the easy instructions.

Unlike the other provided installers, these Windows installers also automatically create `jybot` and `ipybot` scripts. To be able to use the created runner scripts, both the `Scripts` directory containing them and the appropriate interpreters need to be in `PATH` .

**NOTE:**
> If you are installing Robot Framework using Python 2.6 or 2.7, you
> need to set the Python installation directory into [PATH](#Setting_PATH.md)
> _before_ the installation.

> On Windows Vista and Windows 7 installing Robot Framework requires
> administrator privileges. Select `Run as administrator` from the
> context menu when starting the installer.

## Python package managers ##

Python nowadays has various good package managers available for
installing Python packages. The most well known ones are
[easy\_install](http://peak.telecommunity.com/DevCenter/EasyInstall) and
its successor [pip](http://pip-installer.org). We highly recommend
`pip` as it is more actively developed and has nice features such as
uninstallation support.

Different package managers have different usage, but with
`pip` and `easy_install` the basic usage is similar:

```
    # Install the latest version
    pip install robotframework
    easy_install robotframework

    # Upgrade to the latest version
    pip install --upgrade robotframework
    easy_install --upgrade robotframework

    # Install a specific version
    pip install robotframework==2.7.1
    easy_install robotframework==2.7.1

    # Uninstall -- only supported by pip
    pip uninstall robotframework
```

If you need to use a proxy to access the Internet, you can use
`http_proxy` environment variable both with `pip` and
`easy_install`. In addition to that, `pip` supports also `--proxy`
command line option.

**NOTE:**
> Only Robot Framework 2.7 and newer support installation using `pip`.

> When using `easy_install` with Python, `jybot` script is not created
> anymore. With `pip` it has never been created.

> Both `easy_install` and `pip` have a "feature" that unless a
> specific version is given, they install the latest possible version
> even if that is an alpha or beta release. For example, if there is
> 2.7 beta 1 available, running `easy_install robotframework` will
> install it and not the latest stable version. A workaround is giving
> the version explicitly like in `easy_install robotframework==2.5.7`.

## One Click Installer ##

If you are using Windows XP (32 bit) and do not have
[preconditions](#Preconditions.md) installed, you can use the
[One Click Installer](OneClickInstaller.md) to both install everything and
to set the needed environment variables. To use the One Click
Installer, you need to download also Robot Framework, Python and
Jython (optional) installers separately. For more details, see
[One Click Installer's wiki page](OneClickInstaller.md).

## Stand-alone JAR package ##

Robot Framework is also available as a stand-alone
[robotframework.jar package](JavaIntegration.md). This package contains Jython and
thus requires only JVM as a dependency.

# Uninstallation #

As [discussed above](#Python_package_managers.md), `pip` package
manager supports also uninstallation:

```
   pip uninstall robotframework
```

An especially nice feature of `pip` is that it can uninstall packages
even if installation has been done using some other tool. If you do
not have `pip`, another easy way to uninstall Robot Framework is using
the custom `install.py` script that is included in the source
distribution:

```
   python install.py uninstall
```

If Windows installer has been used, the uninstallation can be done
using `Control Panel > Add/Remove Programs`. Robot Framework is listed
under Python applications.

If uninstallation fails somehow, Robot Framework can be uninstalled by
removing the framework code and runner scripts manually. See the
[User Guide](UserGuide.md) for more details.

If you have set `PATH` or configured your environment otherwise, you
need to undo these changes separately.

# Upgrading #

When upgrading or downgrading Robot Framework, it is safe to
install a new version over the existing when switching between two
minor versions (e.g. from 2.7 to 2.7.1). This typically works also
when upgrading to a new major version (e.g. from 2.6.3 to 2.7), but
uninstalling the old version is always safer.

A very nice feature of [pip](#Python_package_managers.md) is that it
automatically uninstalls old versions when upgrading. This happens
both when changing to a specific version or when upgrading to the
latest version:

```
   pip install robotframework==2.7.1
   pip install --upgrade robotframework
```

If you do not have `pip`, an other easy solution for upgrading is
using the custom `install.py` script that is included in the source
distribution:

```
   python install.py reinstall
```

Regardless on the version and installation method, you do not need to
reinstall preconditions or set `PATH` environment variable again.