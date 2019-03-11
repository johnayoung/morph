import axios from 'axios';
import { API_BASE_URL } from '../config';

const parseSwagger = async () => {
  const config = {
    baseURL: `${API_BASE_URL}/swagger.json`,
    method: 'get',
  }
  const response = await axios(config);

  return response;
}

export default parseSwagger;