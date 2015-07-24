

# Introduction #

Here's a quick and very basic example of using Robot Framework from [Maven](http://maven.apache.org/) builds. Notice that Robot Framework itself is [available through Maven](JavaIntegration.md).

If your looking for an advanced guide, please check out the excellent [blog post](http://blog.codecentric.de/en/2010/03/robot-framework-fachtests-in-eclipse-entwickeln-und-mit-maven-ausfuhren/) by Andreas Ebbert-Karroum.

There is nowadays also a separate [Maven Plugin for Robot Framework](http://code.google.com/p/robotframework-maven-plugin/) available.

# 1. Create a project #

```
mvn archetype:create -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.mycompany.app -DartifactId=my-app
```

# 2. Create a directory for robot tests #

```
cd my-app
mkdir -p src/test/resources/robot-tests
```

# 3. Create a robot test #

```
vim src/test/resources/robot-tests/test.txt
```
```
*** Test Cases ***
Hello World
    Log  Hello, World!
```

# 4. Add Robot test execution to Maven pom.xml #
```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>my-app</name>
  <url>http://maven.apache.org</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>1.1</version>
        <executions>
          <execution>
            <phase>integration-test</phase>
            <goals>
              <goal>exec</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <executable>pybot</executable>
          <workingDirectory>.</workingDirectory>
          <arguments>
            <argument>-d</argument>
            <argument>target/robot</argument>
            <argument>src/test/resources/robot-tests/test.txt</argument>
          </arguments>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

# 5. Run Robot tests with Maven #

```
mvn integration-test
```

# 6. Enjoy reports and greeness #

```
target/robot/log.html
```

# Resources #

[The example sources in a zip file](http://robotframework.googlecode.com/files/rf-mvn-example.zip)

Please read more about the Maven Exec-plugin and its configuration at the [Exec-plugin site](http://mojo.codehaus.org/exec-maven-plugin/).