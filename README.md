Installation
============

__First, download the source code.__ You can download it as a ZIP file from
GitHub. But if you're a developer, a better approach is to clone the source
code using Git, thus allowing you to easily pull updates and push your changes.

__Second, download ChromeDriver.__ You can download it for free from
(https://sites.google.com/a/chromium.org/chromedriver/downloads). It's an open
source interface to Google Chrome browser. Therefore, you also need to have
Google Chrome or Chromium browser installed.

Optionally, you can use Eclipse JDT as your IDE. Import the downloaded source
code into your Eclipse workspace.

How to Use
==========

Copy and Ensure your ChromeDriver is located in /Scripts Folder of your python, Therefore you don't need to specify the location.
Then run the project using _AutoMain.py_ as the main class.

Miscellaneous
=============

__IDE__
```
The Development of this python script is using Eclipse Oxygen with PyDev Plugin.
Ensure in Window>Preferences, your location of your "Python Interpreter" is correct 
or in the same environment as where Selenium lib and ChromeDriver are located.
```

__VirtualEnv__
```
Virtual environment of python is created and selenium is installed in it.
follow : https://virtualenv.pypa.io/en/stable/
```

__Selenium Installation__
```
follow : https://pypi.python.org/pypi/selenium
```

__Changing Git user name.__ Example:

```
git config --local user.name "John Doe"
git config --local user.email "john.doe@gmail.com"
```
