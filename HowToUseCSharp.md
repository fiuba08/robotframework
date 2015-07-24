_Example of using C# from Robot Framework test libraries via IronPython. UNDER CONSTRUCTION_



# Introduction #

This simple example demonstrates how to use C# language from Robot Framework test libraries. The example assumes that you have the **.Net framework** and **IronPython** installed on your system. More information on such an implementation can be found <a href='http://code.google.com/p/robotframework/wiki/DotNetSupport'>here</a>. This example is implemented and tested on Windows.

# Running the example #

Create a file ipybot.bat as follows. Make sure to replace [[IRONPYTHON\_INSTALL\_FOLDER](IRONPYTHON_INSTALL_FOLDER.md)] with the installation path of IronPython on your system:

```
:: IronPython executable to use.

set ironpython="[IRONPYTHON_INSTALL_FOLDER]\ipy.exe"

:: Path to robot\runner.pypath

set runner="[IRONPYTHON_INSTALL_FOLDER]\lib\site-packages\robot\runner.py"

:: Run Robot on IronPython interpreter

%ironpython% %runner% %*
```

This file emulates the pybot.bat that comes with the installation of the Robot framework on Python. Once all the other files have been created and copied to the same directory, run the command:

> ipybot.bat <test file>


# System under test #

The demo application is a very simple C# class whose two methods simply add two numbers and concatenate two strings, which should be enough for the purpose of this exercise.

Combine.cs (to be compiled as a Dll)

```
namespace Test
{
    public class Combine
    {
        public int AddNumbers(int number1, int number2)
        {
            return number1 + number2;
        }
 
        public string AddStrings(string string1, string string2)
        {
            return string1 + " " + string2;
        }
    }
}
```


# Test library #

A simple test library that can interact with the above using the .Net CLR. The methods’ names in that library will act as keywords for the Robot Framework.

CombineLibrary.py

```

import clr
clr.AddReferenceToFileAndPath('Combine.dll') #include full path to Dll if required
from Test import Combine
 
def add_two_numbers(num1, num2):
       try:
              intNum1 = int(num1)
              intNum2 = int(num2)
       except:
              raise Exception("Values must be integer numbers!")
       cmb = Combine()
       total = cmb.AddNumbers(intNum1, intNum2)
       return str(total)
                          
def add_two_words(word1, word2):
       cmb = Combine()
       return cmb.AddStrings(word1, word2)

```


# Test cases #

| `*** Settings ***`        |                      |                 |       ||
|:--------------------------|:---------------------|:----------------|:------|:|
| Library                   | CombineLibrary.py    |                 |       ||
|                           |                      |                 |       ||
| `*** Test Cases ***`      |                      |                 |       ||
|Valid\_Element\_Combination |                      |                 |       ||
|                           | Words Should Combine |                 |       ||
|                           | Numbers Should Add Up|                 |       ||
|                           |                      |                 |       ||
| `*** Keywords ***`        |                      |                 |       ||
| Words Should Combine      | ${new\_word} =       | add\_two\_words   | Hello | World! |
|                           | Should Be Equal      | ${new\_word}     | Hello World! ||
| Numbers Should Add Up     | ${total} =           | add\_two\_numbers | 21    | 14 |
|                           | Should Be Equal      | ${total}        | 35    ||


