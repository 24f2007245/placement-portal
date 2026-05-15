import axios from 'axios'
import { startLoading, stopLoading } from './loadingState'

// Get API URL from environment variables
const API_URL = import.meta.env.VITE_API_URL

// Creating axios instance with base URL
const api = axios.create({
  baseURL: API_URL,
  withCredentials: true, //  credentials 
})

api.interceptors.request.use(
  (config) => {
    startLoading()
    return config
  },
  (error) => {
    stopLoading()
    return Promise.reject(error)
  }
)

api.interceptors.response.use(
  (response) => {
    stopLoading()
    return response
  },
  (error) => {
    stopLoading()
    if (error.response?.status === 401) {
      // Handle unauthorized
      console.error('Unauthorized access')
    }
    return Promise.reject(error)
  }
)

export default api
export { API_URL }
