import { REST_METHODS } from './config';
import request from './utils/request';

export const api = {
  fetchSandwichSizes() {
    return request({ url: '/api/sizes' });
  },
  fetchSandwichesExtras() {
    return request({ url: '/api/ingredients' });
  },
  fetchAllOrders() {
    return request({ url: '/orders' });
  },
  fetchOrderByDate(date) {
    return request({ url: '/orders', params: { date } });
  },
  fetchOrdersBySandwichSize(size = 'ALL') {
    return request({ url: '/orders', params: { size } });
  },
  fetchOrdersByExtra(extra = 'ALL') {
    return request({ url: '/orders', params: { extra } });
  },
  fetchOrdersByClient(clientId) {
    return request({ url: '/orders', params: { client_id: clientId } });
  },
  createOrder(order) {
    return request({ url: '/api/orders', data: order, method: REST_METHODS.POST });
  }
};
