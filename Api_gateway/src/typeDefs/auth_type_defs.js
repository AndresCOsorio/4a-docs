const { gql } = require('apollo-server');

const authTypeDefs = gql `
    type Tokens {
        refresh: String!
        access: String!
    }

    type Access {
        access: String!
    }

    input CredentialsInput {
        email: String!
        password: String!
    }

    input SingUpInput {
       name: String!
       lastName: String!
       document: Int!
       email: String!
       password: String!
       cellphone: String! 
    }

    type UserDetail {
        id_usu: Int!
        name: String!
        lastName: String!
        document: Int!
        email: String!
        password: String!
        cellphone: String!
        is_staff: Boolean
    }
    
    type Mutation{
        signUpUser(userInput: SingUpInput!): Tokens!
        logIn(credentials: CredentialsInput!): Tokens!
        refreshToken(refresh: String!): Access!
        updateUser(userId: Int!, userInput: SingUpInput!): UserDetail!
    }

    type Query{
        userDetailById(userId: Int!): UserDetail!
    }
`;

module.exports = authTypeDefs;