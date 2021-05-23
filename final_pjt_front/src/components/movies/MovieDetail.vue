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
      <button @click="showClickAdditionalDetail(1)">리뷰 정보</button>
      <button @click="showClickAdditionalDetail(2)">관련 영상</button>
      <button @click="showClickAdditionalDetail(3)">비슷한 작품</button>
    </div>
    <MovieReviews v-if="checkMovieDetailClicked[0]" :reviews="movieDetail.movie_reviews"/>
    <MovieVideos v-if="[movieDetail.title, checkMovieDetailClicked[2]]" :movieTitle="movieDetail.title"/>
    <SimilarMovies v-if="checkMovieDetailClicked[3]"/>
  </div>
</template>

<script>
import SimilarMovies from '@/components/movies/SimilarMovies'
import MovieReviews from '@/components/movies/MovieReviews'
import MovieVideos from '@/components/movies/MovieVideos'

import { mapActions, mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  components: {
    SimilarMovies,
    MovieReviews,
    MovieVideos,
  },
  data: function () {
    return {
      checkMovieDetailClicked: [true, false, false, false]
    }
  },
  methods: {
    ...mapActions('movieStore', [
      'getMovieDetail',
    ]),
    showClickAdditionalDetail: function (idx) {
      this.checkMovieDetailClicked = [false, false, false, false]
      this.checkMovieDetailClicked[idx] = true
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