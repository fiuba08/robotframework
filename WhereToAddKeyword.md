

# Introduction #

This document contains notes on what to take into account when creating a new keyword and trying to decide if ti should be a library keyword, test suite keyword, or a resource file keyword.

# Should my keyword be in this file or library or some shared resource file? #

  * If your keyword has complicated logic -> In a library!
    * When things seem too complicated in Robot Framework, its best not to force it

<table>
<tr><th><code>handle_steps.txt</code></th><th><code>handle_steps.py</code></th></tr>
<tr><td>
<pre><code>*** Keywords ***<br>
Get Step Message     [Arguments]    ${step}<br>
  ${init result} =  Run Keyword If  ${step}==0  <br>
                  ...  System Initialization<br>
  ${step result} =  Run Keyword If  ${step}&gt;0   <br>
                  ...  Call System Step  ${step}<br>
  ${illegal result} Run Keyword If  ${step}&lt;0  Illegal Step<br>
  ${result} =  Set Variable If  ${step}==0  ${init result}<br>
               ...              ${step}&gt;0   ${step result}<br>
               ...              ${illegal result}<br>
  [Return]    ${result}<br>
</code></pre>
</td>
<td>
<pre><code>def get_step_message_python(step):<br>
     if (step == 0):<br>
          return system_initialization()<br>
     if (step &gt; 0):<br>
          return call_system_step(step)<br>
     else:<br>
          return illegal_step()<br>
</code></pre>
</td></tr>
</table>

  * Remember that you can call Robots keyword libraries from python

```
from robot.libraries.BuiltIn import BuiltIn

def do_something(argument):
    output = do_something_that_creates_a_lot_of_output(argument)
    outputdir = BuiltIn().replace_variables('${OUTPUTDIR}')
    write_output(outputdir)
```


  * From Robot 2.5 onwards you can get an active library instance also in keyword

```
from robot.libraries.BuiltIn import BuiltIn

def title_should_start_with(expected):
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    title = seleniumlib.get_title()
    if not title.startswith(expected):
        raise AssertionError("Title '%s' did not start with '%s'"
                             % (title, expected))
```

  * Choosing between test suite file and a shared resource file depends from the situation.

  * If your keyword could be useful to others its best to move it shared resource. Always better to avoid duplicate work.
    * Document your keyword. Especially if you take arguments or return values.
    * Make sure that you dont do unnessary sleeps. Always use Wait Until Keyword Succeeds if possible.
    * Avoid "Set Test Variable", "Set Suite Variable", and "Set Global Variable" in shared keywords.

<table>
<tr><th><code>Withdraw.txt</code></th><th><code>Withdraw.txt</code></th></tr>
<tr><td>
<pre><code>*** Test Cases ***<br>
Withdraw From Account<br>
  ${status} =  Withdraw From Account   50$<br>
  Withdraw Should Have Succeeded    ${status}<br>
<br>
*** Keywords ***<br>
Withdraw From Account<br>
  [arguments]  ${amount}<br>
  ${status} =  Withdraw From  ${USER}  ${amount}<br>
  [return]     ${status}<br>
<br>
Withdraw Should Have Succeeded<br>
  [arguments]   ${status}<br>
  Should Be Equal   ${status}   SUCCESS<br>
</code></pre>
</td>
<td>
<pre><code>*** Test Cases ***<br>
Withdraw From Account<br>
  Withdraw From Account    50$<br>
  Withdraw Should Have Succeeded<br>
<br>
*** Keywords ***<br>
Withdraw From Account<br>
  [arguments]  ${amount}<br>
  ${status} =  Withdraw From  ${USER}  ${amount}<br>
  Set Test Variable   ${status}<br>
<br>
Withdraw Should Have Succeeded<br>
  Should Be Equal   ${status}   SUCCESS<br>
</code></pre>
</td></tr>
</table>