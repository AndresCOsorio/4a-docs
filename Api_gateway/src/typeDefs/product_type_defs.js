const { gql } = require('apollo-server');

const productTypeDefs = gql `

type Product {
    id: Int!
	name_pro: String!
	category: String!
	description: String!
	image: String!
	unit_price: Float!
	amount_prod: Int
	colour: String!
	cantidad: Int
}
type responseDelete{
	response: Boolean
}

input ProductInput {
	id: Int!
	name_pro: String!
	category: String!
	description: String!
	image: String!
	unit_price: Float!
	amount_prod: Int
	colour: String!
	cantidad: Int
}

input ProductById{
	id: Int!
}

type Query {
    getProductAll(user: Int!): [Product]
	getProductId(user: Int!, idProduct: Int!): Product!
}

type Mutation {
	createProduct(user: Int!, product: ProductInput!): Product
	updateProductById(user: Int!, idProduct: Int!, product: ProductInput!): Product
	updateAmountProduct(user: Int!, product: [ProductInput]): [Product]
	deleteProduct(user: Int!, id: Int!):responseDelete
}

`;

module.exports = productTypeDefs;