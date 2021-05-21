const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  URL: SERVER_URL,
  ROUTES: {
    signup: '/api/a1/signup/',
    login: '/api/a1/api-token-auth/',
    profile: '/api/a1/profile/',

    // 영화 관련 API
    getMovie: '/api/m1/movie/',
    getRandomRecommendMovie: '/api/m1/movie/recommend/random/',
    getMostGenreRecommendMovie: '/api/m1/movie/recommend/genre/most/',
    getGenreRecommendMovie: '/api/m1/movie/recommend/genre/',
  }
}
