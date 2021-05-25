<template>
  <div class="card text-light">
    <div class="mb-3 my-4">
      <div class="row g-0">
        <div class="basic-info-card">
          <div class="card-body">
            <div class="d-flex justify-content-between align-items-center">
              <div class="card-title fw-bold fs-1">{{ movieDetail.title }}</div>
              <div>
                <button :id="`likeCount-${movieDetail.id}`" class="btn bg-light like-btn" @click="updateMovieLikes(movieDetail)">
                  <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInMovieLikes(movieDetail.likes)}"></i>
                  <span>{{ movieDetail.likes.length }}</span>
                </button>
              </div>
            </div>
            <div class="fw-bold mb-3">
              <span class="fs-4">{{ movieDetail.original_title }}</span>
              <span class="fs-6 ms-3">{{ movieDetail.release_date.slice(0, 4)}}년</span>
              <span class="fs-6 ms-1">{{ movieDetail.runtime }}분</span>
            </div>
            <div class="fs-5 fw-bold pt-3 pb-2">줄거리</div>
            <p class="card-text">{{ movieDetail.overview }}</p>

            <div><span class="fw-bold">감독: </span><span class="ms-2">{{ movieDetail.directors[0] }}</span></div>
            <div>
              <span class="fw-bold me-1">출연진: </span>
              <span class="ms-1" v-for="(actor, idx) in movieDetail.actors" :key="idx">{{ actor }}</span>
            </div>
            <div>
              <span class="fw-bold me-1">장르: </span>
              <span class="ms-1" v-for="(genre, idx) in movieDetail.genres" :key="idx">{{ genre }}</span>
            </div>
            <div>
              <span class="fw-bold me-1">키워드: </span>
              <span class="ms-1" v-for="(keyword, idx) in movieDetail.keywords" :key="idx">{{ keyword }}</span>
            </div>
            <!-- {{ movieDetail }} -->
            <!-- {{ movieDetail.likes.length }}
            {{ movieDetail.likes }}
            {{ movieDetail.id }} -->
            <!-- {{ movieDetail }} -->
          </div>
        </div>
        <!-- <div class="col-md-6 card">
          <img :src="movieDetail.backdrop_path" alt="backdrop-image">
        </div> -->
      </div>
    </div>
    <div class="my-3 d-flex justify-content-center">
      <button @click="showClickAdditionalDetail(0)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light">상세 정보</button>
      <button @click="showClickAdditionalDetail(1)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light">관련 영상</button>
      <button @click="showClickAdditionalDetail(2)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light">비슷한 작품</button>
    </div>
    <div class="additional-info-card d-flex flex-column align-items-center">
      <div class="d-flex flex-column align-items-center" v-if="checkMovieDetailClicked[0]">
        <NoMovieReview :movieDetailInfo="movieDetail"/>
        <MovieDetailReviews v-if="checkCondition(movieDetail.movie_reviews)" :reviews="movieDetail.movie_reviews"/>
      </div>
      <div v-if="checkMovieDetailClicked[1]">
        <MovieVideos v-if="checkCondition(movieDetail.title)" :movieTitle="movieDetail.title"/>
      </div>
      <div v-if="checkMovieDetailClicked[2]">
        <SimilarMovies/>
      </div>
    </div>
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
    checkCondition: function (item1) {
      if (Object.keys(item1).length !== 0) {
        return true
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
    // this.movieDetail.
  },
  beforeDestroy: function () {
    document.body.style.backgroundImage = "";
    document.body.style.backgroundColor = "rgba(0, 0, 0, 0.9)";

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
.basic-info-card {
  /* background-color: rgba(54, 61, 88, 0.8); */
  /* background-color: rgba(46, 51, 77, 0.9); */
  background-color: rgba(34, 41, 66, 0.7);
  border: 3px solid rgba(41, 146, 152, 1);
  border-radius: .3rem;
}

.card {
  background-color: inherit;
  /* background-color: transparent; */
}

.like-btn {
  border: 1px solid white;
  background-color: inherit;
}
/* .more-detail-btn {
  color: rgba(41, 146, 152, 1);
  text-decoration: underline;
} */
.additional-info-card {
  background-color: rgba(34, 41, 66, 0.7);
  border: 3px solid rgba(41, 146, 152, 1);
  border-radius: .3rem;
  padding-bottom: 30px;
  margin-bottom: 50px;
}
</style>