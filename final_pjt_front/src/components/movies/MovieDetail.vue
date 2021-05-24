<template>
  <div class="card">
    <h1>MovieDetail</h1>
    <div class="mb-3">
      <div class="row g-0">
        <div class="col-md-6">
          <div class="card-body">
            <h5 class="card-title">{{ movieDetail.title }}</h5>
            <p class="card-text">{{ movieDetail.overview }}</p>
          </div>
        </div>
        <div class="col-md-6 card">
          <img :src="movieDetail.backdrop_path" alt="backdrop-image">
        </div>
      </div>
    </div>
    <div>
      <button @click="showClickAdditionalDetail(0)">상세 정보</button>
      <button @click="showClickAdditionalDetail(1)">관련 영상</button>
      <button @click="showClickAdditionalDetail(2)">비슷한 작품</button>
    </div>
    <MoreMovieDetail v-if="checkMovieDetailClicked[0]" :movieDetailInfo="movieDetail"/>
    <MovieReviews v-if="checkCondition(movieDetail.movie_reviews, checkMovieDetailClicked[0])" :reviews="movieDetail.movie_reviews"/>
    <MovieVideos v-if="checkCondition(movieDetail.title, checkMovieDetailClicked[1])" :movieTitle="movieDetail.title"/>
    <SimilarMovies v-if="checkMovieDetailClicked[2]"/>
  </div>
</template>

<script>
import SimilarMovies from '@/components/movies/SimilarMovies'
import MoreMovieDetail from '@/components/movies/MoreMovieDetail'
import MovieVideos from '@/components/movies/MovieVideos'
import MovieReviews from '@/components/movies/MovieReviews'

import { mapActions, mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  components: {
    SimilarMovies,
    MoreMovieDetail,
    MovieVideos,
    MovieReviews,
  },
  data: function () {
    return {
      checkMovieDetailClicked: [true, false, false]
    }
  },
  methods: {
    ...mapActions('movieStore', [
      'getMovieDetail',
    ]),
    showClickAdditionalDetail: function (idx) {
      this.checkMovieDetailClicked = [false, false, false]
      this.checkMovieDetailClicked[idx] = true
    },
    checkCondition: function (item1, item2) {
      if (Object.keys(item1).length !== 0) {
        if (item2) {
          return true
        }
      }
      return false
    }
  },
  computed: {
    ...mapState('movieStore', [
      'movieDetail',
    ])
  },
  watch: {
    '$route.params.movieId': function() {
      this.getMovieDetail(this.$route.params.movieId)
    },
  },
  created: function () {
    this.getMovieDetail(this.$route.params.movieId)
  },
  // created: function () {
  //   if (this.$store.getters.isLoggedIn) {
  //     this.getTodos()
  //   } else {
  //     this.$router.push({ name: 'Login' })
  //   }
  // },
}
</script>

<style>
</style>