import axios from 'axios'

// Get API URL from environment variables
const API_URL = import.meta.env.VITE_API_URL

// Creating axios instance with base URL
const api = axios.create({
  baseURL: API_URL,
  withCredentials: true, //  credentials 
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
      console.error('Unauthorized access')
    }
    return Promise.reject(error)
  }
)

export default api
export { API_URL }
