# Rapq
App search engine for HUAWEI-AppGallery
 
## Funtionality
Rapq is a web application that allows people to perform a natural language search for apps. Rapq re-creates the experience of browsing through an application store. Search apps of interest and click on a product that is linked to an online store where it can be checked and installed.
 
## Dependency
App data are crawled using my [huawei-spider](https://github.com/wy-go/huawei-spider)

## Run Rapq
1. Terminal run:
```
 docker run -p 8050:8050 scrapinghub/splash
 brew services restart elasticsearch-full
```
2. Run 'huawei-spider/huawei_spider/run'
3. Wait to get data
4. Run 'Rapq/runserver'

## Preview

### Search page:
![](https://raw.githubusercontent.com/wy-go/Rapq/main/readme-files/search.png)

### Search result:
![](https://raw.githubusercontent.com/wy-go/Rapq/main/readme-files/search-result.png)

## Technologies used
Frontend:
- Bootstrap
- JS, jQuery

Backend:
- Python
- Elasticsearch
- Flask
- Template engine: Jinja

## Reference
https://github.com/MieszkoMakuch/news-search/
