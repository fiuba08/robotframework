

# Remote library #

The Remote library is one of the [standard libraries](TestLibraries.md) but totally
different than the others. It does not have any keywords of its own
but it works as a proxy between Robot Framework and actual test
library implementations elsewhere.

There are two main reasons for using the Remote library and the remote
library interface it provides:

  * It is possible to have test libraries running on different machines than where Robot Framework itself is executed. This allows interesting possibilities for distributed testing.
  * Test libraries can be implemented using any language that supports [XML-RPC protocol](http://www.xmlrpc.com). There are currently generic remote servers for Python/Jython, Ruby and .NET, and generic servers for other languages like Java and Perl may be implemented in the future.

The remote library interface is described in detail in the [User Guide](UserGuide.md).
This wiki page just gives a very high level overview and lists the available remote server implementations.


# High level architecture #

The Remote library interacts with actual library implementations
through remote servers, and the Remote library and servers communicate
using a simple remote protocol on top of an XML-RPC channel. The high
level architecture of all this is illustrated in the picture below.

![http://robotframework.googlecode.com/hg/doc/userguide/src/ExtendingRobotFramework/remote.png](http://robotframework.googlecode.com/hg/doc/userguide/src/ExtendingRobotFramework/remote.png)

# Available remote servers #

Following remote servers are available as separate projects. See the project pages for installation and usage instructions. Older versions of Python and Ruby servers are also distributed with Robot Framework 2.8.x source distributions but they will be removed in the future.

| **Language / Platform** | **Project Pages** |
|:------------------------|:------------------|
| Python                  | https://github.com/robotframework/PythonRemoteServer |
| Java                    | https://github.com/ombre42/jrobotremoteserver |
| Ruby                    | https://github.com/semperos/robot-remote-server-rb |
| .NET                    | https://github.com/claytonneal/nrobotremote |
| Clojure                 | https://github.com/semperos/robot-remote-server-clj |
| Perl                    | https://github.com/daluu/plrobotremoteserver |
| node.js                 | https://github.com/comick/node-robotremoteserver |
| PHP                     | https://github.com/daluu/phrrs |