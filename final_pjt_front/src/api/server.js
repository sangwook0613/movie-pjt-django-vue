const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  URL: SERVER_URL,
  ROUTES: {
    signup: '/api/a1/signup/',
    login: '/api/a1/api-token-auth/',
    getMovie: '/api/m1/movie/',
  }
}
