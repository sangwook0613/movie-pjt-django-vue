import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import jwt_decode from "jwt-decode"
import SERVER from '@/api/server.js'
import router from '@/router/index.js'

Vue.use(Vuex)


const movieStore = {
  namespaced: true,
  state: {
    movies: [],
    randomRecommendMovies: [],
    mostGenreRecommendMovie: [],
    genreRecommendMovie: [],
    movieDetail: [],
    searchedMovies: [],
    searchInput: '',
    searchBtn: false,
  },
  getters: {
    // 부모 store의 getters에 있는 config를 받아와서 사용
    config: function (state, getters, rootState, rootGetters) {
      return rootGetters.config
    },
    searchInput: function (state) {
      return state.searchInput
    },
    searchBtn: function (state) {
      return state.searchBtn
    },
  },
  mutations: {
    GET_MOVIES: function (state, movies) {
      state.movies = movies
    },
    GET_MOVIE_DETAIL: function (state, movie) {
      state.movieDetail = movie
    },
    GET_RANDOM_RECOMMEND_MOVIES: function (state, movies) {
      state.randomRecommendMovies = movies
    },
    SEARCH_MOVIES: function (state, searchData) {
      state.searchedMovies = searchData
    },
    CLICK_SEARCH_BTN: function (state) {
      state.searchBtn = true
    },
    CLICK_SEARCH_CANCEL_BTN: function (state) {
      state.searchInput = ''
      state.searchedMovies = []
      state.searchBtn = false
    },
    GET_MOST_GENRE_RECOMMEND_MOVIES: function (state, movies) {
      state.mostGenreRecommendMovie = movies
    },
    GET_GENRE_RECOMMEND_MOVIES: function (state, movies) {
      state.genreRecommendMovie = movies
    },
  },
  actions: {
    getMovie: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.getMovie,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_MOVIES', res.data)
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovieDetail: function ({ commit, getters }, movieId) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.getMovie + movieId,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_MOVIE_DETAIL', res.data)
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getRandomRecommendMovie: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.getRandomRecommendMovie,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_RANDOM_RECOMMEND_MOVIES', res.data)
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMostGenreRecommendMovie: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.getMostGenreRecommendMovie,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_MOST_GENRE_RECOMMEND_MOVIES', res.data)
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getGenreRecommendMovie: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.getGenreRecommendMovie,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_GENRE_RECOMMEND_MOVIES', res.data)
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    searchMovie: function ({ commit, getters }, searchData) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.movieSearch + `${searchData}/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('SEARCH_MOVIES', res.data, searchData)
        console.log(res)
        if (res.status === 204) {
          alert('검색 결과가 없습니다.')
        }
      })
      .catch((err) => {
        console.log(err)
        if (!this.state.searchInput){
          alert('검색어를 입력해주세요') 
        }
      })
    },
    clickSearchBtn: function ({ commit }) {
      commit('CLICK_SEARCH_BTN')
    },
    clickSearchCancelBtn: function ({ commit }) {
      commit('CLICK_SEARCH_CANCEL_BTN')
    }
  },
}

const accountStore = {
  namespaced: true,
  state: {
    profile: null,
    isFollow: false,
    isMyself: false,
  },
  getters: {
    // 부모 store의 getters에 있는 config를 받아와서 사용
    config: function (state, getters, rootState, rootGetters) {
      return rootGetters.config
    },
    isFollow : function (state) {
      return state.isFollow
    },
    isMyself: function (state) {
      return state.isMyself
    },
  },
  mutations: {
    GET_PROFILE: function (state, profile) {
      state.profile = profile
      const currentUsername = store.getters.jwtUsername

      // 현재 사용자가 자기자신이면 isMyself = false
      // 본인 프로필에서 팔로우 버튼 숨기기용
      if (profile.username === currentUsername) {
        state.isMyself = false
      } else {
        state.isMyself = true
      }
      // 현재 로그인한 사용자가 팔로워 목록에 있는지 확인
      // 생성될 때 확인해야 팔로우 버튼 제대로 가능
      for (let follower of profile.followers) {
        if (currentUsername === follower.username) {
          // 있으면 isFollow = true
          state.isFollow = true
          break
        } else {
          state.isFollow = false
        }
      }
    },
    FOLLOW_USER: function (state, profile) {
      state.profile = profile
      state.isFollow = !state.isFollow
    },
  },
  actions: {
    getProfile: function ({ commit, getters }, username) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.profile + username,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_PROFILE', res.data)
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    followUser: function ({ commit, getters }, username) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.profile + `${username}/follow/`,
        method: 'post',
        headers,
      })
      .then((res) => {
        commit('FOLLOW_USER', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}


const communityStore = {
  namespaced: true,
  state: {
    reviews: [],
    reviewDetail: [],
  },
  getters: {
    // 부모 store의 getters에 있는 config를 받아와서 사용
    config: function (state, getters, rootState, rootGetters) {
      return rootGetters.config
    },
  },
  mutations: {
    GET_REVIEWS: function (state, reviews) {
      state.reviews = reviews
    },
    GET_REVIEW_DETAIL: function (state, review) {
      state.reviewDetail = review
    },
  },
  actions: {
    getReview: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.review,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_REVIEWS', res.data)
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getReviewDetail: function ({ commit, getters }, reviewId) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.review + reviewId,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_REVIEW_DETAIL', res.data)
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}



const store = new Vuex.Store({
  modules: {
    // 축약 상태 사용
    movieStore,
    accountStore,
    communityStore,
  },
  // 공통으로 사용하는 state 와 mutation, action 들은 모두 token의 생성과 등록에 관련된 내용들
  state: {
    authToken: localStorage.getItem('jwt'),
  },
  getters: {
    isLoggedIn: function (state) {
      return state.authToken ? true : false
    },
    config: function (state) {
      return {
        Authorization: `JWT ${state.authToken}`
      }
    },
    jwtUsername: function (state) {
      const decode = jwt_decode(state.authToken)
      return decode.username
    }
  },
  mutations: {
    SET_TOKEN: function (state, token) {
      state.authToken = token
      localStorage.setItem('jwt', token)
    },
    REMOVE_TOKEN: function (state) {
      state.authToken = ''
      localStorage.removeItem('jwt')
    },
  },
  actions: {
    login: function ({ commit }, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.login,
        method: 'post',
        data: credentials,
      })
      .then((res) => {
        commit('SET_TOKEN', res.data.token)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    signup: function (context, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.signup,
        method: 'post',
        data: credentials,
      })
      .then(() => {
        router.push({ name: 'Login' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout: function ({ commit }) {
      commit('REMOVE_TOKEN')
      // 다음 이동할 주소는?
      router.push({ name: 'Login' })
    },
  },
})

export default store
