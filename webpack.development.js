const webpack = require('webpack');
const merge = require('webpack-merge');
const base = require(__dirname + '/webpack.base.js');

const libraryName = 'mimir.reporting';

const devConfig = {
    apiUrl: 'http://localhost:8000',
}

module.exports = merge(base, {
    mode: 'development',
    entry: [
        __dirname + '/webapp/index.js',
    ],
    output: {
        filename: libraryName.toLocaleLowerCase() + '.min.js',
        path: __dirname + '/server/static',
    },
    devtool: 'inline-source-map',
    devServer: {
        contentBase: __dirname + '/server/templates',
        publicPath: '/static/',
        historyApiFallback: true,
        compress: true,
        port: 8082,
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('development')
        })
    ],
    externals: {
        'config': JSON.stringify(devConfig)
    }
});