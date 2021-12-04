const userResolver = {
    Query: {
        userDetailById: async(_, { userId }, { dataSources, userIdToken }) => {
            //userIdToken = (await dataSources.authAPI.getUser(userIdToken)).id;
            if (userId == userIdToken) {
                return await dataSources.authAPI.getUser(userId);
            } else return null;
        }
    },
    Mutation: {
        signUpUser: async(_, { userInput }, { dataSources }) => {
            return await dataSources.authAPI.createUser(userInput);
        },
        logIn: async(_, { credentials }, { dataSources }) => {
            return await dataSources.authAPI.authResquest(credentials);
        },
        refreshToken: (_, { refresh }, { dataSources }) => {
            return dataSources.authAPI.refreshToken(refresh);
        },
        updateUser: async(_, { userId, userInput }, { dataSources, userIdToken }) => {
            if (userId == userIdToken) {
                return await dataSources.authAPI.updUser(userId, userInput);
            } else return null;
        }
    }
};

module.exports = userResolver;