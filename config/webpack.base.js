const webpack = require('webpack');
const path = require('path');

const getPath = resolve => {
    return path.resolve(__dirname, resolve);
} 

const config = {
    entry: {
        app: getPath('../webapp/app.js'),
    },
    output: {
        filename: 'app.bundle.js',
        path: getPath('../server/static'),
    },
    module: {
        loaders: [
            { test: /\.js/, exclude: /node_modules/, loader: 'babel-loader' },
            { test: /third-party\.scss$/, loader: 'mixin-loader', enforce: 'pre', },
            { test: /\.scss$/, loaders: ['style-loader', 'css-loader', 'sass-loader'] },
            { test: /\.css$/, loaders: ['style-loader', 'css-loader'] },
            { test: /\.(jpe?g|png|gif|svg)$/i, loaders: 'file?hash=sha512&digest=hex&name=[path][name]-[hash].[ext]' },
            { test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/, loader : 'file-loader' },
            { test: /\.html$/, loader: 'html-loader?attrs[]=video:src' },
            { test: /\.mp4$/, loader: 'url?limit=10000&mimetype=video/mp4' },
        ]
    },
    resolve: { 
        alias: {
            components: getPath('../webapp/components'),
            actionConstants: getPath('../webapp/actionConstants'),
            reducers: getPath('../webapp/reducers'),
            actions: getPath('../webapp/actions'),
            layout: getPath('../webapp/components/layout'),
            pages: getPath('../webapp/components/pages'),
            style: getPath('../webapp/styles'),
            utils: getPath('../webapp/utils'),
            store: getPath('../webapp/store'),
            epics: getPath('../webapp/epics'),
            logic: getPath('../webapp/logic'),
            api: getPath('../webapp/api'),
        }
    }
};

module.exports = config;