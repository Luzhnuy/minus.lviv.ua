var webpack = require('webpack');

module.exports = {
  context: __dirname,
  devtool: "source-map",
  entry: "./static/js/app.js",
  output: {
    path: __dirname + "/static/js/dist/",
    filename: "bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: ["file-loader"]
      }
    ]
  }
};