import axios from 'axios';
import { API_BASE_URL } from './config';

const api = async (endpoint, input) => {
  const config = {
    baseURL: `https://warm-peak-72707.herokuapp.com/api/endpoints/proxy`,
    headers: {
      'x-url-string': `https://morph.now.sh/${endpoint}`
    },
    method: 'get',
  }
  const response = await axios(config);
  return response;
}

export default api;