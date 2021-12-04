const orderResolver = {
    Query: {
        orderByUser: async(_, { user }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderAPI.getOrderByUser(user);
            } else return null;
        },
        ByUserByOrder: async(_, { user, pk }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderAPI.getByUserByOrder(user, pk);
            } else return null;
        },
    },
    Mutation: {
        createOrder: async(_, { user, order }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderAPI.createOrder(user, order);
            } else return null;
        },
        updateOrder: async(_, { user, pk, order }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderAPI.updByUserByOrder(user, pk, order);
            } else return null;
        },
        deleteOrder: async(_, { user, pk }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.orderAPI.delByUserByOrder(user, pk);
            } else return null;
        },
    }
};

module.exports = orderResolver;