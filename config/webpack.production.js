const webpack = require('webpack');
const path = require('path');
const merge = require('webpack-merge');
const base = require(path.resolve(__dirname, 'webpack.base.js'));

module.exports = merge(base, {
    plugins: [
        new webpack.optimize.UglifyJsPlugin({
            compress: {
              warnings: false,
              screw_ie8: true,
              conditionals: true,
              unused: true,
              comparisons: true,
              sequences: true,
              dead_code: true,
              evaluate: true,
              if_return: true,
              join_vars: true
            },
            output: {
              comments: false
            },
        }),
        new webpack.HashedModuleIdsPlugin(),
        new webpack.optimize.ModuleConcatenationPlugin(),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('production')
        })
    ],  
});