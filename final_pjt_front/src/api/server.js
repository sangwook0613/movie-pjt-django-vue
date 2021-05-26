const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  URL: SERVER_URL,
  TUBE: YOUTUBE_API_URL,
  ROUTES: {
    signup: '/api/a1/signup/',
    login: '/api/a1/api-token-auth/',
    profile: '/api/a1/profile/',

    // 영화 관련 API
    movieSearch:'/api/m1/search/',
    getMovie: '/api/m1/movie/',
    getLikeChoiceMovie: '/api/m1/movie/selectlike/',
    getRandomRecommendMovie: '/api/m1/movie/recommend/random/',
    getMostGenreRecommendMovie: '/api/m1/movie/recommend/genre/most/',
    getGenreRecommendMovie: '/api/m1/movie/recommend/genre/',
    getKeywordRecommendMovie: '/api/m1/movie/recommend/keyword/',
    getNewRecommendMovie: '/api/m1/movie/recommend/new/',
    getRatingRecommendMovie: '/api/m1/movie/recommend/rating/',
    getRuntimeRecommendMovie: '/api/m1/movie/recommend/runtime/',

    // 리뷰 관련 API
    review: '/api/c1/review/',
    comment: '/api/c1/comments/',

  }
}
