# Get live updates on COVID-19

This Python program will collect COVID-19 worldwide stats and send it to your mobile phone in text message.

### Demo

<p align="center">
  <img src="https://jixjiastorage.blob.core.windows.net/blog-resources/covid19-monitoring-stats/demo-half.gif" width="400">
</p>

### Twilio Account

You will need your own _Twilio phone number_, _Account SID_ and _Authentication Token_ in order to send SMS using [Twilio API](https://www.twilio.com/). Fill in the credentials to `config.py` file under the following section:

```python
TO = ['{TO_NUMBER}', '{TO_NUMBER}', '{TO_NUMBER}']
FROM_ = '{YOUR_TWILIO_NUMBER}'
ACCOUNT_SID = '{YOUR_ACCOUNT_SID}'
AUTH_TOKEN = '{YOUR_AUTH_TOKEN}'
```

### Choose Countries

You can configure which countries' stats to include in the SMS message. Add the list of desired countries in `config.py` file like below:

For example

```python
# Country List
countries = ['China', 'U.K.', 'USA', 'Australia', 'Canada', 'Japan']
```

### How-To Guide

To see how to set up this Python program as an automated serverless function using **Azure Functions**, follow this easy-to-read blog on my blog site https://jixjia.com/2020/02/18/python-serverless-function

### Credit

Special thanks to www.worldometers.info for kindly providing reliable digest information on the 2019-nCoV update sourced from CDC and WHO.
