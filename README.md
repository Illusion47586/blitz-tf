# blitz-tf

### Works like this
Send `https://blitz-tf.herokuapp.com/get-tags?url=<IMAGEURL>`

You get a json
```json
{
  "type": {TYPE},
  "subType": {SUBTYPE},
  "color": {COLOR}
}
```

In the folder Model Training

Tag Generator.ipynb - This file is used to create the Model for Clothes Tag Generation.

makeCSV.py - This file is used to create the dataset by scraping Myntra Website.
