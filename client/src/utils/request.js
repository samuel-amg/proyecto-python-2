import Axios from 'axios';

import { REST_METHODS } from '../config';

export default function request({
  url,
  params,
  method = REST_METHODS.GET,
  data
}) {
  return Axios({
    url: process.env.REACT_APP_API_URL + url,
    method,
    params,
    data
  }).then((res) => res.data);
}
