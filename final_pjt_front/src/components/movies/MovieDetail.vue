<template>
  <div class="card text-light">
    <div class="mb-3 my-4">
      <div class="row g-0">
        <div class="col-md-6">
          <div class="card-body">
            <h5 class="card-title my-3">{{ movieDetail.title }}</h5>
            <p class="card-text">{{ movieDetail.overview }}</p>
            {{ movieDetail.likes.length }}
            {{ movieDetail.likes }}
            {{ movieDetail.id }}
            <!-- {{ movieDetail }} -->
            <button :id="`likeCount-${movieDetail.id}`" class="btn bg-light" @click="updateMovieLikes(movieDetail)">
              <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInMovieLikes(movieDetail.likes)}"></i>
              <span>{{ movieDetail.likes.length }}</span>
            </button>
          </div>
        </div>
        <!-- <div class="col-md-6 card">
          <img :src="movieDetail.backdrop_path" alt="backdrop-image">
        </div> -->
      </div>
    </div>
    <div class="my-3 d-flex justify-content-start">
      <button @click="showClickAdditionalDetail(0)" class="btn btn-primary btn-sm bg-success mx-1">상세 정보</button>
      <button @click="showClickAdditionalDetail(1)" class="btn btn-primary btn-sm bg-success mx-1">관련 영상</button>
      <button @click="showClickAdditionalDetail(2)" class="btn btn-primary btn-sm bg-success mx-1">비슷한 작품</button>
    </div>
    <NoMovieReview v-if="checkMovieDetailClicked[0]" :movieDetailInfo="movieDetail"/>
    <MovieDetailReviews v-if="checkCondition(movieDetail.movie_reviews, checkMovieDetailClicked[0])" :reviews="movieDetail.movie_reviews"/>
    <MovieVideos v-if="checkCondition(movieDetail.title, checkMovieDetailClicked[1])" :movieTitle="movieDetail.title"/>
    <SimilarMovies v-if="checkMovieDetailClicked[2]"/>
  </div>
</template>

<script>
import SimilarMovies from '@/components/movies/SimilarMovies'
import NoMovieReview from '@/components/movies/NoMovieReview'
import MovieVideos from '@/components/movies/MovieVideos'
import MovieDetailReviews from '@/components/movies/MovieDetailReviews'

import _ from 'lodash'
import axios from 'axios'
import SERVER from '@/api/server.js'

import { mapActions, mapState, mapGetters } from 'vuex'

export default {
  name: 'MovieDetail',
  components: {
    SimilarMovies,
    NoMovieReview,
    MovieVideos,
    MovieDetailReviews,
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
    updateMovieLikes: function (movieDetail) {
      const headers = this.config
      if (!_.includes(movieDetail.likes, this.jwtUserId)) {
        console.log(!_.includes(movieDetail.likes, this.jwtUserId))
        console.log(movieDetail.id, this.jwtUserId)
        axios({
          url: SERVER.URL + SERVER.ROUTES.getMovie + `${movieDetail.id}/like/`,
          method: 'post',
          headers,
        })
        .then(() => {
          const likeCountImage = document.querySelector(`#likeCount-${movieDetail.id} > i`)
          const likeCountNum = document.querySelector(`#likeCount-${movieDetail.id} > span`)
          if (likeCountImage.style.color === '' || likeCountImage.style.color === 'black' ) {
            likeCountImage.style.color = 'crimson'
            likeCountNum.innerText++
          } else {
            likeCountImage.style.color = 'black'
            likeCountNum.innerText--
          }
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    checkUserIncludeInMovieLikes: function (movie_likes) {
      if (_.includes(movie_likes, this.jwtUserId)) {
        return 'crimson'
      }
      return 'black'
    },
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
    },
  },
  computed: {
    ...mapState([
      'jwtUserId',
    ]),
    ...mapState('movieStore', [
      'movieDetail',
    ]),
    ...mapGetters('movieStore', [
      'config',
    ])
  },
  watch: {
    '$route.params.movieId': function() {
      this.getMovieDetail(this.$route.params.movieId)
    },
  },
  created: function () {
    this.getMovieDetail(this.$route.params.movieId)
    this.checkMovieDetailClicked = [true, false, false]
  },
  beforeDestroy: function () {
    // document.body.style.backgroundImage = "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.squarespace-cdn.com/content/v1/5a173f16ace86416b07c25f1/1513939530902-DILPHAAJ9F0DI627449M/ke17ZwdGBToddI8pDm48kK0QKSDttGV1ap9dyeIseHF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0mxU0godxi02JM9uVemPLqw3ZQRv6tY2V6nZIOWGhJ3qaH6uCpMgOc4rPl-G2eiFCQ/fantasy+album+cover6+-+in+wide+format.jpg?format=1500w')";
    document.body.style.backgroundImage = ""
    document.body.style.backgroundColor = "rgba(0,0,0,0.9)"
  }

  // created: function () {
  //   if (this.$store.getters.isLoggedIn) {
  //     this.getTodos()
  //   } else {
  //     this.$router.push({ name: 'Login' })
  //   }
  // },
}
</script>

<style scoped>
.card{
  background-color: transparent;
}
</style>