const path = require("path");

module.exports = {
  productionSourceMap: false,
  devServer: {
    proxy: 'http://0.0.0.0:8001'
  }
}
