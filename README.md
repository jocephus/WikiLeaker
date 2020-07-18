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
`sudo ./setup.sh`

## Running Wikileaker.py
`python3 WikiLeaker.py <domain of your choosing>`

Voila!

# Wikileaker Recon-ng Module
The setup script should copy the recon-ng module into your `.recon-ng/modules/domain-contacts/` directory in your home directory. If the directory does not exist, you will need to install Recon-ng from github if you want to use Recon-ng and the module instead of the standalone version.
+ You may run `marketplace refresh` followed by `marketplace install wikileaker`
+ If the above does not work, copy the current repository from Github and run `setup.sh` again
