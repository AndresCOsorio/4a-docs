const { gql } = require('apollo-server');

const orderDetailTypeDefs = gql `
    input OrderDetail {
        ord_detail: Int!
        amount_prod: Int!
        id_prod: Int!
    }

    type OrderDetailConsult {
        id: Int
        ord_detail: Int
        amount_prod: Int
        id_prod: Int
        id_user: Int
    }

    type OrderDetailResponse {
        status: String!
        num_order_det: Int!
    }

    input OrderDetailAmount{
        amount_prod: Int!
    }

    extend type Mutation{
        createOrderDetail(user: Int!, orderDetailInput: OrderDetail!): OrderDetailResponse!
        updateOrderDetailProduct(user: Int!, pk: Int!, product: Int!, orderDetailInput: OrderDetailAmount!): OrderDetailConsult!
        deleteByIdOrderDetail(user: Int!, pk: Int!): String!
        deleteByIdOrderDetailByIdProduct(user: Int!, pk: Int!, product: Int!): String!
    }

    extend type Query{
        allOrderDetailByUser(user: Int!): [OrderDetailConsult]
        allByUserByOrderDetail(user: Int!, pk: Int!): [OrderDetailConsult]
        allByUserByOrderDetailByProduct(user: Int!, pk: Int!, product: Int!): OrderDetailConsult
    }
`;

module.exports = orderDetailTypeDefs;