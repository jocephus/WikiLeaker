# WikiLeaker.py
A scraper inspired by the Datasploit module written in Python2. This script leverages pandas and Python3. This is also being submitted as a Recon-ng module.


## Prerequisites
+ Python3
+ Python3-pip
+ libre-dev
+ git
+ python3-lxml
+ re
+ pandas
+ bs4

### Installing Prerequisites
Make sure that Recon-ng is up to date and install the WikiLeaker module using the following commands in Recon-ng:
`marketplace install wikileaker`
To install the standalone version, run the following command:
`python3 -m pip install -U --user -r requirements.txt`

## Running Wikileaker.py
`python3 Wikileaker.py <domain of your choosing>`

Voila!

# Wikileaker Recon-ng Module
+ You may run `marketplace refresh` followed by `marketplace install wikileaker`
+ If the above does not work, copy the current repository from Github and move the contents of the `recon-ng module` into your directory for recon-ng (`/~/.recon-ng/modules` in Kali).
