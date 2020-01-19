const webpack = require('webpack');
const merge = require('webpack-merge');
const base = require(__dirname + '/webpack.base.js');

const libraryName = 'app';

module.exports = merge(base, {
    mode: 'production',
    entry: [
        __dirname + '/webapp/index.js',
    ],
    output: {
        filename: libraryName.toLocaleLowerCase() + '.bundle.js',
        libraryTarget: 'umd',
        publicPath: '/server/static',
        umdNamedDefine: true,
        path: __dirname + '/server/static',
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('production')
        })
    ],
    optimization: {
        minimize: true,
    }
});