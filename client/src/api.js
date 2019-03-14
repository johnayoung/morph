import axios from 'axios';

const api = async (input) => {
  const config = {
    baseURL: `https://warm-peak-72707.herokuapp.com/api/endpoints/proxy`,
    headers: {
      'x-url-string': `https://morph.now.sh/morph?input=${input}`
    },
    method: 'get',
  }
  const response = await axios(config);
  return response;
}

export default api;