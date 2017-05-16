Installation
============

1.  __Download the source code.__ You can download it as a ZIP file from
    GitHub. But if you're a developer, a better approach is to clone the source
    code using Git, thus allowing you to easily pull updates and push your
    changes.

2.  __Download ChromeDriver.__ You can download it for free from
    (https://sites.google.com/a/chromium.org/chromedriver/downloads). It's an
    open source interface to Google Chrome browser. Therefore, you also need to
    have Google Chrome or Chromium browser installed.

3.  __Install Python 3 and Python `virtualenv`.__

4.  __Create a new instance of Python environment.__ For example, using `venv`
    as its name and in Fedora Linux:

    ```
    $ pyvenv venv
    ```

5.  __Enable the Python environment.__

    ```
    $ source venv/bin/activate
    ```

6.  __Install the required Python packages.__ This includes Behave BDD
    framework, Requests HTTP library, and bindings for Selenium.

    ```
    $ pip install behave requests selenium
    ```

7.  __Copy ChromeDriver to a visible executable path.__ In Windows, this will
    be `venv\Scripts`. In other OS, hovewer, this will be `venv/bin`.


Usage
=====

First, make sure the Python environment is activated. You can activate the
environment below.

```
$ source venv/bin/activate
```

Then run the whole test.

```
$ behave
```

Alternatively, you can provide additional arguments. For example, if you're a
developer, you might be interested to only run the specific tests that you are
currently working on. You can temporarily mark such test features/scenarios
with @wip tags, and then run only tests with that tags as follows.

```
$ behave --tags=@wip
```



Miscellaneous
=============

__IDE__. The project can be imported to Eclipse IDE with PyDev plugin. Ensure
that the location of your _Python Interpreter_ in _Window > Preferences_ is
correct, or in the same environment as where Selenium library and ChromeDriver
are located.

__Changing Git user name.__ Example:

```
git config --local user.name "John Doe"
git config --local user.email "john.doe@gmail.com"
```
