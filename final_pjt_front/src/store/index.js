import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import jwt_decode from "jwt-decode"
import SERVER from '@/api/server.js'
import router from '@/router/index.js'

Vue.use(Vuex)

const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

const movieStore = {
  namespaced: true,
  state: {
    movies: [],
    randomRecommendMovies: [],
    mostGenreRecommendMovie: [],
    genreRecommendMovie: [],
    movieDetail: [],
    // 영화 관련 영상 state
    movieVideos: [],
    selectedVideo: '',
    // 검색 state
    searchedMovies: [],
    searchBtn: false,
    searchInput: '',
    choiceMovies: [],
  },
  getters: {
    // 부모 store의 getters에 있는 config를 받아와서 사용
    config: function (state, getters, rootState, rootGetters) {
      return rootGetters.config
    },
    searchBtn: function (state) {
      return state.searchBtn
    },
    searchedMovies: function (state) {
      return state.searchedMovies
    },
  },
  mutations: {
    GET_MOVIES: function (state, movies) {
      state.movies = movies
    },
    GET_MOVIE_DETAIL: function (state, movie) {
      state.movieDetail = movie
    },
    GET_LIKE_CHOICE_MOVIES: function (state, movies) {
      state.choiceMovies = movies
    },
    GET_RANDOM_RECOMMEND_MOVIES: function (state, movies) {
      state.randomRecommendMovies = movies
    },
    GET_MOST_GENRE_RECOMMEND_MOVIES: function (state, movies) {
      state.mostGenreRecommendMovie = movies
    },
    GET_GENRE_RECOMMEND_MOVIES: function (state, movies) {
      state.genreRecommendMovie = movies
    },
    // 영화 영상 관련 mutations
    SET_MOVIE_VIDEOS: function (state, videos) {
      state.movieVideos = videos
    },
    SET_SELECTED_VIDEO: function (state, selectedDetailVideo) {
      state.selectedVideo = selectedDetailVideo
    },
    SET_THUMBNAIL_VIDEO: function (state, videos) {
      state.selectedVideo = videos[0]
    },
    // 검색 관련 mutations
    SEARCH_MOVIES: function (state, searchData) {
      state.searchedMovies = searchData
    },
    CLICK_SEARCH_BTN: function (state) {
      state.searchBtn = !state.searchBtn
    },
    CLICK_SEARCH_CANCEL_BTN: function (state) {
      state.searchedMovies = []
      state.searchBtn = false
    },
    UPDATE_SEARCH_INPUT: function (state, inputText) {
      state.searchInput = inputText
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
    getLikeChoiceMovie: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.getLikeChoiceMovie,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_LIKE_CHOICE_MOVIES', res.data)
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    likeSelectMovie: function ({ getters }, selectMovies) {
      const headers = getters.config
      for (let selectMovie of selectMovies) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.getMovie + `${selectMovie}/likes/`,
          method: 'post',
          headers,
        })
        .then(() => {
          // console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      }
      router.push({ name: 'Movie' })
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
        console.log(res)
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
    getRelatedVideos: function ({ state, commit }, movieTitle) {
      const params = {
        key: YOUTUBE_API_KEY,
        part: 'snippet',
        type: 'video',
        q: movieTitle,
        maxResults: 3,
      }
      console.log(movieTitle)
      axios({
        url: SERVER.TUBE,
        method: 'get',
        params, 
      })
      .then((res) => {
        console.log(res)
        commit('SET_MOVIE_VIDEOS', res.data.items)
        
        if (!state.selectedVideo) {
          commit('SET_THUMBNAIL_VIDEO', state.movieVideos[0])
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    searchMovie: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.movieSearch + `${movieStore.state.searchInput}/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        console.log(res.data)
        commit('SEARCH_MOVIES', res.data)
        // if (res.status === 204) {
        //   alert('검색 결과가 없습니다.')
        // }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    clickSearchBtn: function ({ commit }) {
      commit('CLICK_SEARCH_BTN')
    },
    clickSearchCancelBtn: function ({ commit }) {
      commit('CLICK_SEARCH_CANCEL_BTN')
    },
    updateSearchInput: function ({ commit }, inputText) {
      commit('UPDATE_SEARCH_INPUT', inputText.target.value)
      console.log(inputText)
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
    createFormType: '',
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
    SET_FORM_TYPE: function (state, num) {
      state.createFormType = num
      console.log(state.createFormType)
    }
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
    createReview: function ({ getters }, inputData) {
      const headers = getters.config
      const inputForm = {
        ...inputData,
        rating: parseInt(inputData.rating),
        movie: movieStore.state.movieDetail.id,
        user: store.getters.jwtUserId
      }
      if (inputData.title !== '' && inputData.content !== '') {
        axios({
          url: SERVER.URL + SERVER.ROUTES.review,
          method: 'post',
          data: inputForm,
          headers,
        })
        .then((res) => {
          router.push({ name: 'ReviewDetail', params: { movieId: res.data.id.movie, reviewId: res.data.id }})
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        alert('모든 내용을 기입해주세요!')
      }
    },
    updateReviewLikes: function ({ getters }, reviewId) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.review + `${reviewId}/like/`,
        method: 'post',
        headers,
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteReview: function ({ getters }, reviewId) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.review + `${reviewId}/`,
        method: 'delete',
        headers,
      })
      .then((res) => {
        // 리뷰 모음 페이지로 넘길 수 있게 수정?
        console.log(res)
        router.push({ name: 'Movie' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createComment: function ({ getters, dispatch }, commentInput) {
      const headers = getters.config
      const inputForm = {
        content: commentInput.inputText,
        movie: movieStore.state.movieDetail.id,
        user: store.getters.jwtUserId
      }
      console.log(commentInput)
      console.log(inputForm)
      if (inputForm.content !== '') {
        axios({
          url: SERVER.URL + SERVER.ROUTES.review + `${commentInput.reviewId}/comments/`,
          method: 'post',
          data: inputForm,
          headers,
        })
        .then((res) => {
          dispatch('getReviewDetail', commentInput.reviewId)
          // console.log(router)
          // console.log(router.currentRoute)
          // console.log(router.currentRoute.path)
          // router.push(router.currentRoute.path)
          router.push({ name: 'ReviewDetail', params: { movieId: res.data.id.movie, reviewId: res.data.id }})
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        alert('내용을 기입해주세요!')
      }
    },
    deleteComment: function ({ getters, dispatch }, commentInfo) {
      const headers = getters.config
      axios({
        url: SERVER.URL + SERVER.ROUTES.comment + `${commentInfo.commentId}/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        dispatch('getReviewDetail', commentInfo.reviewId)
        // router.push(router.currentRoute.path)
        router.push({ name: 'ReviewDetail', params: { movieId: commentInfo.movieId, reviewId: commentInfo.reviewId }})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    setFormType: function ({ commit }, num) {
      commit('SET_FORM_TYPE', num)
      console.log('hihi')
    },
    updateReview: function ({ getters, state, dispatch }, updateData) {
      // console.log(updateData)
      // console.log(state.reviewDetail.id)
      // console.log(state.reviewDetail)
      // console.log(movieStore.state.movieDetail.id)
      const headers = getters.config
      const inputForm = {
        ...updateData,
        rating: parseInt(updateData.rating),
        movie: state.reviewDetail.movie.id,
        user: store.getters.jwtUserId
      }
      console.log(inputForm)
      if (updateData.title !== '' && updateData.content !== '') {
        axios({
          url: SERVER.URL + SERVER.ROUTES.review + `${state.reviewDetail.id}/`,
          method: 'put',
          data: inputForm,
          headers,
        })
        .then((res) => {
          console.log(res)
          console.log(res.data)
          dispatch('getReviewDetail', state.reviewDetail.id)
          router.push({ name: 'ReviewDetail', params: { movieId: res.data.movie, reviewId: res.data.id }})
          // router.push({ name: 'MovieDetail', params: { movieId: res.data.movie }})
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        alert('모든 내용을 기입해주세요!')
      }
    }
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
    showNav: true,
    modalStatus: false,
    modalData: {
      reviewUpdateModalStatus: false,
      movieDetailModalStatus: false,
    },
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
    },
    jwtUserId: function (state) {
      const decode = jwt_decode(state.authToken)
      return decode.user_id
    },
    // getShowNav: function (state) {
    //   return state.showNav
    // },
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
    UPDATE_SHOW_NAV: function (state, data) {
      state.showNav = data
      console.log(state.showNav)
    },
    SET_MODAL_DATA: function (state) {
      state.modalStatus = !state.modalStatus
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
        router.push({ name: 'MovieSelect' })
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
      console.log(movieStore.state)
      // 다음 이동할 주소는?
      router.push({ name: 'Login' })
    },
    updateShowNav: function ({ commit }, data) {
      commit('UPDATE_SHOW_NAV', data)
      console.log(data)
    },
    openModal: function ({ commit }) {
      commit('SET_MODAL_DATA')
    },
  },
})

export default store
