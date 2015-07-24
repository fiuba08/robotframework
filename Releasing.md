

# Create Release Packages #

## Tag Release and Create Source Packages ##

Following shell commands create new tag and most of the needed packages. It is safer to copy-paste and run them one-by-one than to automate the whole procedure.

```
version=x.y.z
./package.py version $version final
sed -i "s/<version>.*</<version>${version}</" pom.xml
tools/tool2html.py all
doc/libraries/lib2html.py all
doc/userguide/ug2html.py zip
doc/api/generate.py
doc/quickstart/qs2html.py zip   # Not needed if Quick Start hasn't been updated
hg stat  # List changes and created packages
hg commit -m "Version $version"
hg tag $version
hg push
python setup.py sdist upload   # Upload source distribution to Pypi and create the new version there
python setup.py bdist_wheel upload  # Upload wheel to pypi
./package.py version trunk
hg commit -m "Version trunk"
hg push
```

## Create Windows Installers ##

Windows installer needs to be created separately on a Windows machine with commands:

```
hg pull 
hg update x.y.z
python package.py wininst keep
```

This needs to be done both on a 32 and 64 bit machines to create separate installers for both.

Upload the files to https://pypi.python.org/pypi/robotframework

## Create Jar Distribution ##

Jar package may be created either in Linux or Windows after version has been updated.
To create the jar, run:

```
python package.py jar keep
```

### Upload JAR to Sonatype repositories ###

Sonatype offers a service where users can upload jars and they will be synced to the maven central repository. Below are the instructions to upload the jar.

Prequisites:

  1. Install maven
  1. Create a [Sonatype account](https://issues.sonatype.org/secure/Dashboard.jspa)
  1. Add these lines (filled with the Sonatype account information) to your `settings.xml`
```
  <servers>
      <server>
          <id>sonatype-nexus-staging</id>
          <username></username>
          <password></password>
      </server>
  </servers>

```
  1. Create a PGP key according to [these instructions](https://docs.sonatype.org/display/Repository/How+To+Generate+PGP+Signatures+With+Maven#HowToGeneratePGPSignaturesWithMaven-MavenGPGPlugin)
  1. Apply for [publish rights](https://docs.sonatype.org/display/Repository/Sonatype+OSS+Maven+Repository+Usage+Guide) to org.robotframework project. (This will take some time from them to accept.)

The process:
  1. Run commands
```
export version=2.5.3
mvn gpg:sign-and-deploy-file -Dfile=dist/robotframework-$version.jar -DpomFile=pom.xml -Durl=http://oss.sonatype.org/service/local/staging/deploy/maven2/ -DrepositoryId=sonatype-nexus-staging
```
  1. Go to https://oss.sonatype.org/index.html#welcome, log in with Sonatype creadentials, find the staging repository and do close & release

After that, the released jar is synced to Maven central within an hour.


## Upload Packages ##

The source installer and windows installers should be at [Pypi](https://pypi.python.org/pypi/robotframework). The jar distribution is only at maven central.

Upload these packages to Google Code with specified labels:

  * User Guide (_Featured_, _Type-Docs_)
  * Quick Start Guide if it has been updated (_Featured_, _Type-Docs_)

Remember also to remove _Featured_ label from the previous release and possibly add _Deprecated_ to older ones.

Upload relevant packages also to NSN's internal download page.


# Update Wiki #

It is easier to edit wiki files locally and commit them than to use web access. Some scripts that help modifying wiki pages are available in `svn/wiki/tools`. Remember to use `hg diff` before commits and check that pages are rendered correctly on browser afterwards.

## Release Notes ##

Issue list can be added to release notes using [get\_issues.py](http://robotframework.googlecode.com/svn/wiki/tools/get_issues.py). Common usage is something like this:

```
  tools/get_issues.py notes robotframework 2.5.3 >> ReleaseNotes25.wiki
```

## User Guide, Library and Tool Pages ##

Library and tool wiki pages as well as User Guide page needs to be updated between releases. With major releases that can be done using `release_update.py`, and with minor releases it is normally enough to use `sed` e.g. like:

On Linux:

```
sed -i 's/2.6.2/2.6.3/g' *Tool.wiki
sed -i 's/2.6.2/2.6.3/g' *Library.wiki
sed -i 's/2.6.2/2.6.3/g' UserGuide.wiki
grep -rn '2.6.2' .
hg di
```

On OSX (because sed on OSX requires value for -i):

```
sed -i '' 's/2.6.2/2.6.3/g' *Tool.wiki
sed -i '' 's/2.6.2/2.6.3/g' *Library.wiki
sed -i '' 's/2.6.2/2.6.3/g' UserGuide.wiki
grep -rn '2.6.2' .
hg di
```

# Update NSN Wiki #

  * News to front page.
  * Upload downloads.

# Update Read the Docs #

API documentation is hosted in [Read the Docs](http://robot-framework.readthedocs.org/en/latest/). Use generic `robotframework` account to log in and update the versions to be built and published from the
[dashboard](http://readthedocs.org/dashboard/robot-framework/versions/).

# Announce Release #

## News to Project Front Page ##

Must be edited using Administer tab and can thus be done only by project owners.

## Send Announcements ##

With all releases:

  * Public users and announcement [mailing lists](MailingLists.md)
  * NSN internal users and announcement lists
  * Twitter (http://twitter.com/robotframework)

At least with major releases:

  * Submit news to http://opensourcetesting.org
  * agile-testing mailing list (http://tech.groups.yahoo.com/group/agile-testing)
  * testing-in-python mailing list (http://lists.idyll.org/listinfo/testing-in-python)
  * fi-testaus mailing list (http://tech.groups.yahoo.com/group/fi-testaus, preferably on Finnish)

Other possible places:

  * python-list (http://mail.python.org/mailman/listinfo/python-list)
  * jython-users (https://lists.sourceforge.net/lists/listinfo/jython-users)
  * SQAForums/Automated testing (http://www.sqaforums.com/postlist.php?Cat=0&Board=UBB34)
  * LinkedIn groups such as Test Automation and Agile Testing
