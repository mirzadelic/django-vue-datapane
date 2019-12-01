import axios from 'axios'

var newAxios = axios.create({
  baseURL: 'http://localhost:8000/'
})

export default newAxios
