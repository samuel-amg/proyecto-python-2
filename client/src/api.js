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
  fetchReport(filter, filterData) {
    const params = {};
    params[filter] = filterData;
    return request({ url: '/api/reports', params });
  },
  createOrder(order) {
    return request({ url: '/api/orders', data: order, method: REST_METHODS.POST });
  }
};
