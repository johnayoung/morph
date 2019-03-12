import axios from 'axios';
import {WIT_CLIENT_TOKEN} from '../config';

const api = async (q) => {
  const config = {
    baseURL: `https://api.wit.ai/message?v=20170307&q=${q}`,
    method: 'get',
    headers: {
      Authorization: `Bearer ${WIT_CLIENT_TOKEN}`
    }
  }
  const response = await axios(config);
  return response;
}

export default api;