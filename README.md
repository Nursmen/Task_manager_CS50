# Nurs.ga
> Some info

The program works like this:

![program](https://www.youtube.com/watch?v=vv7fCWbf4Nc)

```diff
+ "size-limit": [
+   {
+     "path": "dist/app-*.js"
+   }
+ ],
  "scripts": {
    "build": "webpack ./webpack.config.js",
+   "size": "npm run build && size-limit",
    "test": "jest && eslint ."
  }
```
