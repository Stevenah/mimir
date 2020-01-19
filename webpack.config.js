const path = require('path');

module.exports = env => {
    return require(path.resolve(__dirname, 'webpack.' + env + '.js'));
}