# Code style #

In general, we follow the [Style Guide for Python Code (PEP-8)](http://www.python.org/dev/peps/pep-0008/) in all the code we write. Unless you have a very good
reason not to, follow this. In some projects/modules there might be a reason to
write code contradictory to PEP-8, but those exceptions should be clearly
documented.

Additionally, there are some guidelines that are not touched by PEP-8:

  * All the source code files must have the copyright notice.
  * We leave two blank lines between copyright notice and first import statement
  * We leave two blank lines between the last import and first function or class definition
  * We leave two blank lines between public top level functions. However, top-level function and associated helper function (whose name start with `_`) are separated by one blank line.

Everyone interested in writing good Python code should read
[Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html).

# Submitting patches #

The way to send code to Robot Framework or a related project is to create a patch.
**We do not accept whole files, only patches created with an appropriate tool.**

Patches should be submitted to the project's issue tracker, under relevant
issue. If no relevant issue is found, it is encouraged to open one. If the
patch doesn't directly belong to any single issue, or a suitable issue can't be
created, it may also be sent to
[Robot Framework development mailing list](http://groups.google.com/group/robotframework-devel).

Patches may be created with any `diff` program, for example `hg diff`.
After modifying a file, you can run hg diff, either in terminal or through the GUI client.
In terminal, a patch can be created like this:
```
hg diff src/robot/somefile.py > mypatch.diff
```

Graphical clients for different version control systems also support creating patches.

# Adding external files #

There may come a need to add an external file to a project, possibly with some changes.
In this case, following steps need to be followed:

  * make sure that the license of the external file is compatible with the license used in the project
  * make a commit that includes the file in its original form and specify the origin of the file in the commit message
  * make any necessary changes in a **separate commit**

# Version control #

Robot Framework itself and most of the related projects use Mercurial or Git as their
version control system. The project pages have `Source` tab with additional
instructions for checkout.


# Testing #

Most projects **do** have tests. These are located under `atest` and `utest`
directories in the project root. `atest` contains acceptance tests, usually
implemented with Robot Framework and `utest` contains unit tests, usually
implemented using Python's `unittest` module. These directories contain a
`README.txt` describing the procedure required to execute the tests.


# Becoming committer #

To become a committer you need to send some number of quality patches (tests
included!) that are relevant to the project. Additionally, you need to be
willing to adhere the coding guidelines (to the smallest detail) described
above.