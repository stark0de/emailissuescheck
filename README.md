# emailissuescheck
Simple tool to check for SPF, DMARC and DKIM issues in a list of domains



## Installation and usage:

```
git clone https://github.com/stark0de/emailissuescheck

cd emailissuescheck

pip3 install -r requirements.txt

pip install mailspoof

sudo updatedb

locate mailspoof # get path of mailspoof, mine was in /home/stark0de/.local/bin/mailspoof

python3 emailissues.py /pathto/listwithdomains mailspoofpath verbose

The verbose option will just print the errors and the reason of the errors
```
## Notes:

DKIM is only checked to be present in the TXT record of the domains provided, to check it completely we would need to know the DKIM selector of the domain, in case you know it, validate that here: https://www.dmarcanalyzer.com/es/dkim-3/dkim-record-check/. If you own the domain, send an email to yourself and in the original message you will find the DKIM-Signature header, the s=whatever value is the selector you need to introduce in the above link.
