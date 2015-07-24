

# Introduction #

**NOTE:**
> These instructions apply for Robot Framework 2.6 and older. Robot
> Framework 2.7 can be installed according to the
> [new instructions](Installation.md).

These instructions cover the basic procedure for getting Robot Framework installed. See the [User Guide](UserGuide.md) for more detailed installation instructions, as well as for information where files are installed, how to install the framework manually without Python, etc.

Robot Framework can be installed from [source](#Installing_from_source.md) or using [Windows installer](#Using_Windows_installer.md) or [Easy Install](#Using_Easy_Install.md). Before using any of these methods, you need to make sure that needed [preconditions](#Preconditions.md) are installed. Windows users can use
[One Click Installer](#Using_One_Click_Installer.md) to install
[preconditions](#Preconditions.md) and Robot Framework itself in one go. To make the life of Java people easy, Robot Framework is also available as [standalone JAR package](#Standalone_JAR_package.md).

After a successful installation you should be able to execute following commands on the command prompt:

```
   $ pybot --version
   Robot Framework 2.5.6 (Python 2.5.4 on linux2)

   $ jybot --version
   Robot Framework 2.5.6 (Jython 2.5.1 on java1.6.0_20)
```

The latter command works only if you have installed Jython. In both cases, the exact version and platform information can, of course, differ from these. With `jybot` you also get some notifications from Jython package manager upon the first execution.

To continue from here, you can take a look at the [Quick Start Guide](QuickStartGuide.md) which introduces the most important features and acts also as an executable demo.


# Installing from source #

This installation method can be used on any operating system having Python installed. Installing _from source_ can sound a bit scary for some people, but the procedure is actually pretty straightforward. A benefit of this approach is that you get all documentation, tools and templates with the source code.

You can get the source code either as a
[source distribution package](http://code.google.com/p/robotframework/downloads)
or checkout it directly from our
[version control system](http://code.google.com/p/robotframework/source).
In the former case, first extract the package somewhere, and as a result, you have
a directory named _robotframework-`<`version`>`_. After that you just need to go to the created directory on the command prompt and run the following command there:

```
   python setup.py install
```

When installing Robot Framework 2.5 or older with Python, the installation tries to also detect Jython installation from the same machine and create `jybot` script with correct information. Robot Framework 2.5 and newer can also be installed directly with Jython and without having Python installed at all:

```
   jython setup.py install
```

For more detailed instructions about installation from the source using Python and Jython see the [User Guide](UserGuide.md). For installation using IronPython, a .NET implementation of Python programming language, see [.NET support wiki page](DotNetSupport.md).

# Using Windows installer #

There are separate graphical installers for 32 bit (more common) and
64 bit Windows systems. The former installer has name in format
`robotframework-<version>.win32.exe` and the latter
`robotframework-<version>.win-amd64.exe`. After you have
[downloaded an appropriate installer](http://code.google.com/p/robotframework/downloads) just follow the easy instructions.

**NOTE:**
> If you are installing Robot Framework using Python 2.6 or 2.7, you need to
> set the Python installation directory to PATH environment variable
> _before_ the installation. How to set environment variables is
> explained below.

> On Windows Vista and Windows 7 installing Robot Framework requires administrator
> privileges. Select `Run as administrator` from the context menu when
> starting the installer.

> Environment variable `PYTHONCASEOK` should be not set on Windows machines. Robot Framework
> will not work correctly with it.

After the installation, you probably want to make Robot Framework's runner scripts easily available from the command line. This is done by editing PATH environment variable as follows:

  1. Open _Start > Settings > Control Panel > System > Advanced > Environment Variables_. There are _User variables_ and _System variables_, and the difference between them is that _User variables_ affect only the current users, whereas _System variables_ affect all users.
  1. To edit the existing PATH, select _Edit_ and add _;<PythonInstallationDir>\Scripts\_ at the end of the value. Note that the leading colon (;) is important, as it separates different entries. To add a new value, select _New_ and provide both the name and the value, this time without the colon.
  1. Start a new command prompt for the changes to take effect.

Notice that _<PythonInstallationDir>\Scripts_ directory is not created by Python installer, but it will be created automatically when Robot Framework is installed.


# Using Easy Install #

If Python package managing tool
[Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall)
is available, installing Robot Framework is as easy as running command
`easy_install robotframework` or something like `easy_install robotframework==2.0.4`
if you want to get a specific version.

When using Easy Install on Windows, you need to run
_robot\_postinstall.py_ script after the installation to configure the
runner scripts (`pybot`, `jybot`, `rebot`). The installation output
should define where the post-install script is located, and you can
execute it by double clicking it or running it from the command line like
`python <PythonInstallationDir>\Scripts\robot_postinstall.py`.

**NOTE:**
> If you need to use a proxy to access the Internet, you can tell Easy Install
> to use it by setting the `http_proxy` environment variable.

> Easy Install has a "feature" that unless a specific version is given, it installs
> the latest possible version even if that is an alpha or beta release. For example,
> if there is 2.6 beta 1 available, running `easy_install robotframework` will
> install it and not the latest stable version. A workaround is giving the version
> explicitly like in `easy_install robotframework==2.5.7`.

> At the momemt it is not possible to install Robot Framework using
> [pip](http://www.pip-installer.org). For more information see [issue 885](https://code.google.com/p/robotframework/issues/detail?id=885).

# Using One Click Installer #

If you are using Windows XP (32 bit) and do not have
[preconditions](#Preconditions.md) installed, you can use
[One Click Installer](OneClickInstaller.md) to both install everything and to set needed environment
variables. To use One Click Installer, you need to download also Robot
Framework, Python and Jython (optional) installers separately. For
more details, see [One Click Installer's wiki page](OneClickInstaller.md).


# Standalone JAR package #

Robot Framework is also available as a standalone [robotframework.jar package](JavaIntegration.md). This package contains Jython and thus requires only JVM as a dependency.


# Preconditions #

Robot Framework runs both on [Python](http://python.org) and
[Jython](http://www.jython.org), and you need to have at least one of them to be
able to use it. However, some of the provided installers only work with Python, so installing it is always recommended.

## Python installation ##

On most UNIX-like systems, you have Python installed by default. If you are on
Windows or otherwise need to install Python yourself, your best place to start
is probably the [Python homepage](http://python.org). There you can download a
suitable installer and get more information about the installation and Python
in general.

Starting from Robot Framework 2.5, Python 2.5 is the minimum supported Python
version. Earlier versions support also Python 2.3 and 2.4. Robot Framework is
currently not compatible with Python 3.x versions.

**NOTE:**
> On Windows, and especially on Windows Vista, it is recommended to install Python to all users, and to run the installation as an administrator.

## Jython installation ##

Using test libraries implemented with Java or using Java tools internally
requires running Robot Framework on Jython, which in turn requires Java Runtime
Environment (JRE). Minimum required JRE version depends on the Jython version
used.  Jython 2.5 requires Java 1.5 or newer, whereas Jython 2.2 works also with
Java 1.4. Both Sun and IBM Java implementations are supported.

Starting from Robot Framework 2.5, the minimum supported Jython version is 2.5.
Earlier Robot Framework versions support also Jython 2.2.

Installing Jython is a fairly easy procedure, and the first step is getting an
installer from the [Jython homepage](http://www.jython.org). Note that the
installer is an executable JAR package, which you need to run as `java -jar jython_installer-<version>.jar`.

If you have Jython installed when Robot Framework is installed with Python,
`jybot` runner script will be (most of the time) created correctly. The details,
as well as instructions how to install Robot Framework using only Jython can be found
from the [User Guide](UserGuide.md).


# Uninstallation #

If Robot Framework has been installed using a source distribution, it can be uninstalled with command:

> `python install.py uninstall`

If Windows installer has been used, the uninstallation can be done using _Control Panel > Add/Remove Programs_. Robot Framework is listed under Python applications.

If uninstallation fails somehow or you have used Easy Install, Robot Framework can be uninstalled by removing the framework code and runner scripts manually. See the [User Guide](UserGuide.md) for more details.


# Upgrading #

The procedure when upgrading or downgrading Robot Framework depends on the versions used:

  * If you are upgrading from one minor Robot Framework version to another (for example, from 2.0 to 2.0.1), it is safe to install the new version over the old one, unless stated otherwise.
  * If you are upgrading from one major Robot Framework version to another (for example, from 2.0 to 2.1), then it is highly recommended to uninstall the old version before the new installation.
  * If you are downgrading, the rules are the same as for upgrading.

With source distributions, you first need to get the new package, and after that run the following command, which automatically takes care of the uninstallation:

> `python install.py reinstall`

With Easy Install you can simply run:

> `easy_install robotframework==<new-version>`

Regardless on the version or installation method, you do not need to reinstall preconditions or set PATH environment variable again.