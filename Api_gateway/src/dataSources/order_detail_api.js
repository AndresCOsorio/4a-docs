const { RESTDataSource } = require('apollo-datasource-rest');

const serverConfig = require('../server');

class OrderDetailAPI extends RESTDataSource {
    constructor() {
        super();
        this.baseURL = serverConfig.order_api_url;
    }

    async createOrderDetail(userId, orderDetail) {
        //user = new Object(JSON.parse(JSON.stringify(user)));
        return await this.post(`/orderDetail/${userId}/`, orderDetail);
    }

    async getOrderDetailByUser(userId) {
        return await this.get(`/orderDetail/${userId}/`);
    }

    async getByUserByOrderDetail(userId, orderDetailId) {
        return await this.get(`/orderDetail/${userId}/${orderDetailId}/`);
    }

    async getByUserByOrderDetailByProduct(userId, orderDetailId, productId) {
        return await this.get(`/orderDetail/${userId}/${orderDetailId}/${productId}/`);
    }

    async delByUserByOrderDetail(userId, orderDetailId) {
        return await this.delete(`/orderDetail/${userId}/${orderDetailId}/`);
    }

    async delByUserByOrderDetailByProduct(userId, orderDetailId, productId) {
        return await this.delete(`/orderDetail/${userId}/${orderDetailId}/${productId}/`);
    }

    async updByUserByOrderDetailByProduct(userId, orderDetailId, productId, orderDetailAmount) {
        return await this.put(`/orderDetail/${userId}/${orderDetailId}/${productId}/`, orderDetailAmount);
    }
}

module.exports = OrderDetailAPI;