# emailspoofingcheck
Simple tool to check for SPF, DMARC and DKIM issues in a list of domains



## Installation and usage:

```
git clone https://github.com/stark0de/emailissuescheck

cd emailissuescheck

pip install mailspoof

sudo updatedb

locate mailspoof # get path of mailspoof, mine was in /home/stark0de/.local/bin/mailspoof

python3 emailissues.py listwithdomains mailspoofpath verbose

The verbose option will just print the errors and the reason of the errors
```
