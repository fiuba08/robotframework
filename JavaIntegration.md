

# Introduction #

Starting from Robot Framework 2.5.2, RF is distributed also as a jar file. This jar file allows execution of Robot Framework without having Python installed, but it also contains a programmatic entry point for using RF within Java code.

The latest jar distribution is available from the download page.


# Using the Robot Framework Jar #

## Running tests ##

It is possible to execute tests using the jar file with command like these:

```
  java -jar robotframework-2.5.3.jar --help
  java -jar robotframework-2.5.3.jar mytests.txt
  java -jar robotframework-2.5.3.jar --variable name:value mytests.txt

```

## Using additional Java libraries ##


Due to the fact that `java -jar` does not read `CLASSPATH` environment
variable, or offer any other way to alter the class path at startup, Robot Framework has to be started a bit differently when class path has to be altered.

For example, here's how the SwingLibrary demo can be executed using the Robot Framework jar:
```
java -cp lib/swinglibrary-0.14.jar:lib/registration-0.1.jar:robotframework-2.5.3.jar org.robotframework.RobotFramework example.html
```

It is also possible to insert additional jar files to class path using the
`Xbootclasspath` option. In this case, robotframework.jar does not need to be in class path.

Here's the above example using `Xbootclasspath`:
```
java -Xbootclasspath/a:lib/swinglibrary-0.14.jar:lib/registration-0.1.jar -jar  robotframework-2.5.3.jar  example.html 
```


## Using rebot ##

Rebot can be used like this:
```
  java -jar robotframework-2.5.3.jar rebot --help
  java -jar robotframework-2.5.3.jar rebot output.xml
  java -jar robotframework-2.5.3.jar rebot --name Combined outputs/*.xml

```

# Using the Programmatic API #

Currently, an API exists only for test execution. [User Guide](UserGuide.md) contains an example.

Javadocs for individual release are found below:

  * [2.5.3](http://robotframework.googlecode.com/svn/tags/robotframework-2.5.3/doc/java/index.html)

# Extending the Robot Framework Jar #


NOTE: robotframework-2.5.3.jar contains (accidentally) two MANIFEST.MF files,
which causes `jar` command to fail. robotframework-2.5.3.jar can be extended
using `zip` command.

Adding additional test libraries or support code to the Robot Framework jar is
quite starightforward using the `jar` command distributed with JDK. Python code
must be placed in `Lib` directory inside the jar and Java code can be placed
directly to the root of the jar, according to package structure.

For example, to add Python package `mytestlib` to the jar, first copy the
`mytestlib` directory under a directory called `Lib`, then run command:

```
jar uf /path/to/robotframework-2.5.4.jar Lib
```

in the directory where `Lib` is located.

To add compiled java classes to the jar, you must have a directory structure
corresponding to the Java package structure and add that recursively to the
zip.

For example, to add class `MyLib.class`, in package org.test, the file must be
in `org/test/MyLib.class` and you can execute:

```
jar uf /path/to/robotframework-2.5.4.jar org
```

# Robot Framework as Maven Dependency #

Robot Framework jar is also available in the Maven central repository, and you can add it as a dependency with the following snippet:

```
    <dependency>
        <groupId>org.robotframework</groupId>
        <artifactId>robotframework</artifactId>
        <version>2.5.3</version>
    </dependency>

```