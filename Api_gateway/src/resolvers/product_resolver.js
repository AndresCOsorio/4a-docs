const productResolver = {
    Query: {
        getProductAll: async(_, { user }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.productAPI.getProductAll()
            } else return null;
        },

        getProductId: async(_, { user, idProduct }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.productAPI.getProductById(idProduct)
            } else return null;
        }
    },

    Mutation: {
        createProduct: async(_, { user, product }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.productAPI.createProduct(product)
            } else return null;
        },
        updateProductById: async(_, { user, idProduct, product }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                return await dataSources.productAPI.updateProductById(idProduct, product)
            } else return null;
        },
         updateAmountProduct: async(_, { user, product }, { dataSources, userIdToken }) => {
             if (user == userIdToken) {
                return await dataSources.productAPI.updateAmountProduct(product)
             } else return null;
         },
        deleteProduct: async(_, { user, id }, { dataSources, userIdToken }) => {
            if (user == userIdToken) {
                dataSources.productAPI.deleteProduct(id)
            } else return null;
        }

    }
};
module.exports = productResolver;