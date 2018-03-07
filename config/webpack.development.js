const webpack = require('webpack');
const path = require('path');
const merge = require('webpack-merge');
const base = require(path.resolve(__dirname, 'webpack.base.js'));

module.exports = merge(base, {
    devtool: 'inline-source-map',
    devServer: {
        contentBase: path.resolve(__dirname, '../server/templates'),
        historyApiFallback: true,
        compress: true,
        port: 8080,
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('development')
        })
    ],  
});