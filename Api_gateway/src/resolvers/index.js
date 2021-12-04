const authResolver = require('./auth_resolver');
const orderDetailResolver = require('./order_detail_resolver');
const orderResolver = require('./order_resolver');
const productResolver = require('./product_resolver');

const lodash = require('lodash');

const resolvers = lodash.merge(authResolver, orderDetailResolver, orderResolver, productResolver);

module.exports = resolvers;