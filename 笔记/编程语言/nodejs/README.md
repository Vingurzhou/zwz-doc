# npm

<!-- TOC -->
* [npm](#npm)
  * [Cannot read pro...](#cannot-read-pro)
<!-- TOC -->

## Cannot read pro...
Cannot read properties of null (reading 'pickAlgorithm')
```shell
npm cache clean --force
rm -rf node_modules
rm -rf package-lock.json
npm install
```