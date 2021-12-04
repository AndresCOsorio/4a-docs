const { RESTDataSource } = require('apollo-datasource-rest');

const serverConfig = require('../server');

class AuthAPI extends RESTDataSource {
    constructor() {
        super();
        this.baseURL = serverConfig.auth_api_url;
    }

    async createUser(user) {
        user = new Object(JSON.parse(JSON.stringify(user)));
        return await this.post('/user/', user)
    }

    async getUser(userId) {
        return await this.get(`/user/${userId}/`);
    }

    async updUser(userId, user) {
        return await this.put(`/user/${userId}/`, user);
    }

    async authResquest(credentials) {
        return await this.post('/login/', credentials);
    }

    async refreshToken(token) {
        token = { refresh: token };
        return await this.post('/refresh/', token);
    }
}

module.exports = AuthAPI;