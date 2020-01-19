'use strict';

const webpack = require('webpack');

const config = {
    devtool: 'source-map',
    module: {
        rules: [
            { test: /\.js/, exclude: [/node_modules/, /dist/ ], loader: 'babel-loader' },
            { test: /third-party\.scss$/, loader: 'mixin-loader', enforce: 'pre', },
            { test: /\.scss$/, loaders: ['style-loader', 'css-loader', 'sass-loader'] },
            { test: /\.css$/, loaders: ['style-loader', 'css-loader'] },
            { test: /\.(jpe?g|png|gif|svg)$/i, loaders: 'file?hash=sha512&digest=hex&name=[path][name]-[hash].[ext]' }
        ]
    },
    resolve: { 
        alias: {
            components: __dirname + '/webapp/components',
            styles: __dirname + '/webapp/styles',
            reducers: __dirname + '/webapp/reducers',
            store: __dirname + '/webapp/store',
            epics: __dirname + '/webapp/epics',
            pages: __dirname + '/webapp/pages',
            api: __dirname + '/webapp/api',
            actions: __dirname + '/webapp/actions',
            actionTypes: __dirname + '/webapp/actionTypes',

        },
    }
};

module.exports = config;