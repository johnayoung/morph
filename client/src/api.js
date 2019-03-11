import axios from 'axios';
import { API_BASE_URL } from './config';

const api = async (endpoint, input) => {
  const config = {
    baseURL: `${API_BASE_URL}/api/strings/${endpoint}`,
    method: 'post',
    data: {
      input
    }
  }
  const response = await axios(config);
  return response;
}

export default api;