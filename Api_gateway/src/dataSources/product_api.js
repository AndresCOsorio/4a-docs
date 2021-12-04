const { RESTDataSource } = require('apollo-datasource-rest');
const {product_api_url} = require('../server');
class ProductAPI extends RESTDataSource {
    constructor() {
        super();
        this.baseURL = product_api_url;
    }

    async createProduct(product) {
        product = new Object(JSON.parse(JSON.stringify(product)));
        return await this.post('/product', product);
    }

    async getProductAll(){
        return await this.get(`/`);
    }

    async getProductById(id) {
        return await this.get(`/getProduct/${id}`);
    }

    async updateProductById(id, product) {
        product = new Object(JSON.parse(JSON.stringify(product)));
        return await this.put(`/product/${id}`, product);
    }

    async updateAmountProduct(product){
        product = new Object(JSON.parse(JSON.stringify(product)));
        return await this.put(`/product`, product)
    }

    async deleteProduct(id){
        return await this.delete(`/product/${id}`);
    }
}
module.exports = ProductAPI;