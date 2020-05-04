# VTEX Login Automation

This project was made to practice Python and get in touch with Selenium.

*Unfortunately this version only works on Windows*

---

Automation of the log in process using Google accounts with VTEX.

## Pre-setup

### Downloading Python
Go to [Python website](https://www.python.org/downloads/ "Download Python") and download the latest version to your system

Make sure that while installing you check the box to include Python in the PATH

### Creating environment variables:

- #### Your email
  - Type <kbd>win + R</kbd>, it will open a small window at the left bottom corner
  - Type **_setx VTEX_Login <your.google.account>_**
  - Hit <kbd>ENTER</kbd>

- #### Your password
  - Type <kbd>win + R</kbd> again
  - Type **_setx VTEX_Password_ <your.account.password>**
  - Hit <kbd>ENTER</kbd>

### Setup:

- Cloning the Repo
    ```
        git clone https://github.com/SamuelDenani/vtex-login-automation.git
        cd vtex-login-automation
        pip install -r requirements.txt
    ```
- Adding the repo to the PATH
  - Copy the path where you cloned the repo
  - Open the Windows Search by clicking on the Windows logo at the left bottom corner or by hitting the Windows Key on your keyboard
  -  Type **_env_**
  -  Click on **_Edit environment variables_**, it  will open a new window
  -  Inside that new window, click on **__Enviroment Variables__**, it will open another window
  -  Look for the Path variable on the top panel and once you find it, click on it and on <kbd>Edit</kbd> below
  -  Click on <kbd>New</kbd> and paste the path of the repo
  -  Then just click <kbd>OK</kbd> <kbd>OK</kbd> <kbd>OK</kbd>

### Usage:

*You can use this command from anywhere

```
    vtex <mystore.myvtex.com/admin/a>
```

Remenber to replace mystore with the name of your store.