# Bulk Email-Sender GmailAPI 
___
> Author: [Koen de Jong](https://www.koendejong.net)
___

## Description
This is a simple GmailAPI bulk email sender. 
In short, it uses the GmailAPI to send emails to multiple recipients.

Edit the body.html file for the email. Any other files that are in the templates folder will be sent as attachments!

## Usage

### Google API Credentials
Before being able to use this tool, you need to have a Gmail or Google Suite account. 
You can create one by following the instructions:
1. Go to the [API Developer Console](https://console.cloud.google.com/apis/dashboard)
2. Create a new project
3. Go to credentials and create new OAuth client credentials
4. Download the JSON file and save it to your project directory

### Configuration
1. Rename the `example_config.json` the file `config.json` in your project directory
2. Fill in the fields to your liking and remove the descriptive part.

### Requirements
Install the following tools with pip3:
1. google-api-python-client 
2. google-auth-httplib2 
3. google-auth-oauthlib
4. pickle

### Running 
With a working configuration, you can run the tool with the following command:
`python3 run.py`

## Requirements
* [Python 3](https://www.python.org/downloads/)
* [pip3](https://pypi.org/project/pip/)

## TODO
* [ ] Add support for importing CSV files with dynamic content
