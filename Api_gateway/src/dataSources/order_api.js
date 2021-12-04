const { RESTDataSource } = require('apollo-datasource-rest');

const serverConfig = require('../server');

class OrderAPI extends RESTDataSource {
    constructor() {
        super();
        this.baseURL = serverConfig.order_api_url;
    }

    async createOrder(user, order) {
        //user = new Object(JSON.parse(JSON.stringify(user)));
        return await this.post(`/order/${user}/`, order);
    }

    async getOrderByUser(userId) {
        return await this.get(`/order/${userId}/`);
    }

    async getByUserByOrder(userId, orderId) {
        return await this.get(`/order/${userId}/${orderId}/`);
    }

    async delByUserByOrder(userId, orderId) {
        return await this.delete(`/order/${userId}/${orderId}/`);
    }

    async updByUserByOrder(userId, orderId, order) {
        return await this.put(`/order/${userId}/${orderId}/`, order);
    }
}

module.exports = OrderAPI;