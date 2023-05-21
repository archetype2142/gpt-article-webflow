require('dotenv').config({ path: __dirname + '/.env' })
const Webflow = require('webflow-api');
const fs = require('fs');
const path = require('path')

const webflow = new Webflow({
  token: process.env.WEBFLOW_TOKEN,
  version: "1.0.0",
  headers: {
    "User-Agent": "My Webflow App / 1.0",
  },
});

const files = fs.readdirSync('./articles/');

files.forEach(fileName => {
  fs.readFile(`./articles/${fileName}`, 'utf8', (err, data) => {
    if(fileName == 'test.json') return;
    if (err) {
      console.error(err);
      return;
    }
    uploadArticle(JSON.parse(data).article)
    console.log(JSON.parse(data).article);
  });
})

async function uploadArticle(article) {
  const created_item = await webflow.createItem({
    collectionId: process.env.COLLECTION_ID,
    fields: { 
      slug: article.slug,
      name: article.name,
      _archived: false,
      _draft: false,
      'post-body': article.body,
      image: {
        url: article.image_url
      }
    }
  })
  console.log(created_item)
}
