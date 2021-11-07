import Axios from 'axios';

const $axios = Axios.create({
    baseURL: 'http://127.0.0.1:8000/api',
    headers: {
        'Content-Type': 'application/json',
    },
});

//Example of a cross-cutting concern - client api error-handling
$axios.interceptors.response.use(
    response => response,
    error => {
        console.error(error);

        throw error;
    }
);
const setMd5 = (string) => $axios.post('/string/md5string', {string}).then(res=>res.data);

const service = {
    setMd5
};

export default service;