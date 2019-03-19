const path = require("path");

module.export = {
  productionSourceMap: false,
  devServer: {
    proxy: 'http://0.0.0.0:8001'
  }
}
