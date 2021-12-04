const orderDetailResolver = {
    Query: {
        allOrderDetailByUser: async(_, { user }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderDetailAPI.getOrderDetailByUser(user);
            } else return null;
        },
        allByUserByOrderDetail: async(_, { user, pk }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderDetailAPI.getByUserByOrderDetail(user, pk);
            } else return null;
        },
        allByUserByOrderDetailByProduct: async(_, { user, pk, product }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderDetailAPI.getByUserByOrderDetailByProduct(user, pk, product);
            } else return null;
        }
    },
    Mutation: {
        createOrderDetail: async(_, { user, orderDetailInput }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderDetailAPI.createOrderDetail(user, orderDetailInput);
            } else return null;
        },
        updateOrderDetailProduct: async(_, { user, pk, product, orderDetailInput }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderDetailAPI.updByUserByOrderDetailByProduct(user, pk, product, orderDetailInput);
            } else return null;
        },
        deleteByIdOrderDetail: async(_, { user, pk }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderDetailAPI.delByUserByOrderDetail(user, pk);
            } else return null;
        },
        deleteByIdOrderDetailByIdProduct: async(_, { user, pk, product }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderDetailAPI.delByUserByOrderDetailByProduct(user, pk, product);
            } else return null;
        }
    }
};

module.exports = orderDetailResolver;