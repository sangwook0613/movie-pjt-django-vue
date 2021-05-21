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
    recommendMovies: [],
    movieDetail: [],
  },
  getters: {
    // 부모 store의 getters에 있는 config를 받아와서 사용
    config: function (state, getters, rootState, rootGetters) {
      return rootGetters.config
    }
  },
  mutations: {
    GET_MOVIES: function (state, movies) {
      state.movies = movies
    },
    GET_MOVIE_DETAIL: function (state, movie) {
      state.movieDetail = movie
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
    getMovieDetail: function ({ commit }, movieId) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.getMovie + movieId,
        method: 'get',
      })
      .then((res) => {
        commit('GET_MOVIE_DETAIL', res.data)
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}

const accountStore = {
  namespaced: true,
  state: {
    // profile: '',
  },
}



const store = new Vuex.Store({
  modules: {
    // 축약 상태 사용
    movieStore,
    accountStore,
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
