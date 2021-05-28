<template>
  <div class="text-light">
    <div class="mb-3 my-4">
      <div class="row g-0 rounded" :style="{ 
        backgroundImage: `linear-gradient(to right, #141414, rgba(20, 20, 20, 0) 50%), linear-gradient(to left, #141414, rgba(20, 20, 20, 0) 30%), url(${movieDetail.backdrop_path})`,
        backgroundSize: '840px 100%',
        backgroundPosition: 'right center',
        backgroundRepeat: 'no-repeat'}">
        <div class="col-5">
          <div class="card-body">
            <div class="d-flex justify-content-between align-items-center">
              <div class="card-title fw-bold fs-1">{{ movieDetail.title }}</div>
              <div>
                <div :id="`likeCount-${movieDetail.id}`" @click="updateMovieLikes(movieDetail)" class="d-flex align-items-center">
                  <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInMovieLikes(movieDetail.likes)}"></i>
                  <span class="text-white fw-bold fs-5 ms-2 me-4">{{ movieDetail.likes.length }}</span>
                </div>
              </div>
            </div>
            <div class="fw-bold mb-3">
              <span class="fs-4">{{ movieDetail.original_title }}</span>
              <span class="fs-7 ms-3">{{ movieDetail.release_date.slice(0, 4)}}년</span>
              <span class="fs-7 ms-2">{{ movieDetail.runtime }}분</span>
            </div>
            <div class="fs-5 fw-bold pt-3 pb-2">줄거리</div>
            <p class="card-text">{{ movieDetail.overview }}</p>
            <div class="feature-box row">
              <div class="fw-bold col-2">감독: </div>
              <div class="col">
                <span class="underline" 
                @click="[updateSearchQuery(movieDetail.directors[0].name) ,
              $router.push({name: 'Search', query: {q: movieDetail.directors[0].name }})]">
              {{ movieDetail.directors[0].name }}
              </span>
              </div>
            </div>
            <div class="feature-box row">
              <span class="fw-bold col-2">출연진: </span>
              <div class="col">
                <span @click="[updateSearchQuery(actor.name) ,$router.push({name: 'Search', query: {q: actor.name }})]" 
                class="me-1 underline" v-for="(actor, idx) in movieDetail.actors" :key="idx">{{ actor.name }} </span>
              </div>
            </div>
            <div class="feature-box row">
              <span class="fw-bold col-2">장르: </span>
              <div class="col">
                <span class="me-1" v-for="(genre, idx) in movieDetail.genres" :key="idx">{{ genre.name }} </span>
              </div>
            </div>
            <div class="feature-box row">
              <span class="fw-bold col-2">키워드: </span>
              <div class="col">
                <span class="me-1" v-for="(keyword, idx) in movieDetail.keywords" :key="idx">{{ keyword.keyword_eng_name }} </span>
              </div>
            </div>
          </div>
        </div>
        <div class="col-6">
        </div>
      </div>
    </div>
    <div class="my-3 d-flex justify-content-center moreinfo-tag py-2 rounded">
      <div @click="showClickAdditionalDetail(0)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light"
        :style="this.checkMovieDetailClicked[0] ? 'border-bottom:3px solid #FFFFFF; padding-bottom:3px;' : ''"
      >리뷰 정보</div>
      <div @click="showClickAdditionalDetail(1)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light"
        :style="this.checkMovieDetailClicked[1] ? 'border-bottom:3px solid #FFFFFF; padding-bottom:3px;' : ''"
      >관련 영상</div>
      <div @click="showClickAdditionalDetail(2)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light"
        :style="this.checkMovieDetailClicked[2] ? 'border-bottom:3px solid #FFFFFF; padding-bottom:3px;' : ''"
      >비슷한 작품</div>
    </div>
    <div class="additional-info-card d-flex flex-column align-items-center">
      <div v-if="checkMovieDetailClicked[0]">
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
      'updateSearchQuery',
    ]),
    updateMovieLikes: function (movieDetail) {
      const headers = this.config
      console.log(movieDetail.likes)
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
        if (likeCountImage.style.color === '' || likeCountImage.style.color === 'white' ) {
          likeCountImage.style.color = 'crimson'
          likeCountNum.innerText++
        } else {
          likeCountImage.style.color = 'white'
          likeCountNum.innerText--
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    checkUserIncludeInMovieLikes: function (movie_likes) {
      if (_.includes(movie_likes, this.jwtUserId)) {
        return 'crimson'
      }
      return 'white'
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
    ...mapGetters([
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
    document.body.style.backgroundImage = "";
    document.body.style.backgroundColor = "rgb(20, 20, 20)";
  }
}
</script>


<style>
.card {
  background-color: inherit;
}

/* .card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
} */

.additional-info-card {
  /* border-radius: .3rem; */
  padding-bottom: 30px;
  margin-bottom: 50px;
}

.feature-box {
  display: flex;
}

.moreinfo-tag {
  background-color: #292828;
}
span.underline:hover {
  /* text-decoration: underline; */
  font-weight: bold;
  color:#00cecb !important;
}
</style>