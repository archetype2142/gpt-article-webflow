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

1. Run article generator with `python3 app.py [number of topics] [title for single article]`
P.S. if title of single article is provided, `number of topics` is ingored, but is still a required param

2. Run uploader with `node app.js`

It will loop through all articles in article folder and upload it to the particular webflow collection

Contributor: [Tanvin Sharma](https://github.com/tanvinsharma)
