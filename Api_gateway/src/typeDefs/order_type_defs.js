const { gql } = require('apollo-server');

const orderTypeDefs = gql `
    input Order{
        date: String!
        send_type: String!
        send_price: String!
        total_charge: Int!
        order_status: String!
        pay: Int!
        pay_type: String!
        order_detail: Int!
    }

    type DetailOrder{
        id: Int
        date: String
        send_type: String
        send_price: String
        total_charge: Int
        order_status: String
        pay: Int
        pay_type: String
        order_detail: Int
        user: Int
    }

    type OrderResponse{
        status: String!
        message: String!
    }

    extend type Mutation{
        createOrder(user: Int!, order:Order!): OrderResponse!
        updateOrder(user: Int!, pk: Int!, order:Order!): DetailOrder!
        deleteOrder(user: Int!, pk: Int!): String!
    }

    extend type Query{
        orderByUser(user: Int!): [DetailOrder]
        ByUserByOrder(user: Int!, pk: Int!): DetailOrder
    }
`;
module.exports = orderTypeDefs;