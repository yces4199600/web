# fcushopweb（前端Vue部分）
#### 如果覺得 heroku 後端反應過慢
在根目錄下新增 **`.env.local`** 並在檔案寫入
`VUE_APP_BACKEND_URL=http://localhost:8080/`專案就會優先讀取 **`.env.local`** 的環境變數

但要確保網址路徑和 port 號

.local 會被 git 忽略
####
---
### Install Node.js FIRST
#### Project setup
```
npm install
or
yarn install
```


**Compiles and hot-reloads for development**
```
npm run serve
or
yarn serve
```
投影片：
https://docs.google.com/presentation/d/1nWHkXlS47yxlrfkUAc-AwDmvR52EYIDNPgmSfHnug0c/edit#slide=id.p
