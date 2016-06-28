var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: './static/js/app.js',
  output: {
    libraryTarget: 'var',
    library: 'Opin',
    path: './static/bundles/',
    filename: '[name]-[hash].js'
  },
  externals: {
    'jquery': 'jQuery'
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
};
