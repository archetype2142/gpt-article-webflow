# ChatGPT Webflow Article

Automate writing and uploading articles to webflow 🚀

Create .env file in root and include the following
```
WEBFLOW_TOKEN=""
COLLECTION_ID=""
CHATGPT_TOKEN=""
```

Install all dependencies
1. `yarn install` or `npm install`
2. `pip3 -r requirements.txt`

Run article generator with `python3 app.py`
Run uploader with `node app.js`

It will loop through all articles in article folder and upload it to the particular webflow collection

Contributor: [Tanvin Sharma](https://github.com/tanvinsharma)
