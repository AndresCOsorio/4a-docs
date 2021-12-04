const authTypeDefs = require('./auth_type_defs');
const orderDetailTypeDefs = require('./order_detail_type_defs');
const orderTypeDefs = require('./order_type_defs');
const productTypeDefs = require('./product_type_defs');


const schemasArrays = [authTypeDefs, orderDetailTypeDefs, orderTypeDefs, productTypeDefs];

module.exports = schemasArrays;