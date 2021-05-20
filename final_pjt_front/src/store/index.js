import Vue from 'vue'
import Vuex from 'vuex'

import SERVER from '@/api/server.js'
import router from '@/router/index.js'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: localStorage.getItem('jwt'),
  },
  getters: {
    isLoggedIn: function (state) {
      return state.authToken ? true : false
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
    }
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
        // console.log(res.data)
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
    }
  },
  modules: {
  }
})
