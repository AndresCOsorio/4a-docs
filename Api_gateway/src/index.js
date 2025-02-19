const { ApolloServer } = require('apollo-server');
const typeDefs = require('./typeDefs');
const resolvers = require('./resolvers');
const OrderAPI = require('./dataSources/order_api');
const AuthAPI = require('./dataSources/auth_api');
const OrderDetailAPI = require('./dataSources/order_detail_api');
const ProductAPI = require('./dataSources/product_api');
const authentication = require('./utils/authentication');

const server = new ApolloServer({
    context: authentication,
    typeDefs,
    resolvers,
    dataSources: () => ({
        orderAPI: new OrderAPI(),
        orderDetailAPI: new OrderDetailAPI(),
        authAPI: new AuthAPI(),
        productAPI: new ProductAPI()
    }),
    introspection: true,
    playground: true
});
server.listen(process.env.PORT || 4000).then(({ url }) => {
    console.log(`🚀 Server ready at ${url}`);
});