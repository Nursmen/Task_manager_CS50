# Nurs.ga
> Some info

The program works like this:

![program](https://www.youtube.com/watch?v=vv7fCWbf4Nc)

 ```diff
   "scripts": {
     "build": "webpack ./webpack.config.js",
     "size": "npm run build && size-limit",
 -   "test": "jest && eslint ."
 +   "test": "jest && eslint . && npm run size"
   }
 ```
