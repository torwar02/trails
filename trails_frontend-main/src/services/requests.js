import axios from 'axios'

const baseURL =
  process.env.NODE_ENV === 'production'
    ? 'http://google.com'
    : 'http://localhost:3000'
const instance = axios.create({
  baseURL
})

export default instance
