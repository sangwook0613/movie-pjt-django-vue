<template>
  <div>
    <h1 class="text-light">{{ movieDetail.title }} 리뷰</h1>
    <div>
      <!-- {{ movieDetail.movie_reviews }} -->
      <div v-for="(review, idx) in movieDetail.movie_reviews" :key="idx">
        <!-- {{ review }} -->
        <div class="card p-2 mb-3">
          <div class="d-flex justify-content-between pb-2">
            <div class="d-flex align-items-center">
              <span class="fw-bold fs-5 pe-2">{{ review.title }}</span>
              <span :class="[makeBadge(review.rating), 'text-center']" style="width: 80px">평점: {{ review.rating }}</span>
            </div>
            <button :id="`likeCount-${review.id}`" class="btn" @click="updateReviewLikes(review, review.user)">
              <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInReviewLikes(review.likes)}"></i>
              <span>{{ review.likes.length }}</span>
            </button>
          </div>
          <div class="d-flex justify-content-between">
            <span>작성자: {{ review.user }}</span>
            <router-link
              :to="{ name: 'ReviewDetail', params: { movieId: review.movie, reviewId: review.id }}"
              class="text-decoration-none text-dark text-end"
            >
              리뷰 상세보기
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <button @click="goBack" class="btn btn-info">이전 페이지로</button>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import _ from 'lodash'
import axios from 'axios'
import SERVER from '@/api/server.js'

export default {
  name: 'MovieReviews',
  methods: {
    ...mapActions([
      'openModal',
    ]),
    ...mapActions('movieStore', [
      'getMovieDetail',
    ]),
    updateReviewLikes: function (review, user_id) {
      const headers = this.config
      if (user_id !== this.jwtUserId && !_.includes(review.likes, this.jwtUserId)) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.review + `${review.id}/like/`,
          method: 'post',
          headers,
        })
        .then(() => {
          const likeCountImage = document.querySelector(`#likeCount-${review.id} > i`)
          const likeCountNum = document.querySelector(`#likeCount-${review.id} > span`)
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
    makeBadge: function (num) {
      if (num >= 8) {
        return 'badge rounded-pill bg-primary'
      } else if (num >= 4) {
        return 'badge rounded-pill bg-warning'
      } else {
        return 'badge rounded-pill bg-danger'
      }
    },
    checkUserIncludeInReviewLikes: function (review_likes) {
      if (_.includes(review_likes, this.jwtUserId)) {
        return 'crimson'
      }
      return 'black'
    },
    openReviewCreateModal: function () {
      this.openModal()
      this.modalData.reviewCreateModalStatus = true
    },
    goBack: function () {
      this.$router.go(-1)
    }
  },
  computed: {
    ...mapGetters([
      'config',
      'jwtUserId',
    ]),
    ...mapState([
      'modalData',
    ]),
    ...mapState('movieStore', [
      'movieDetail',
    ])
  },
  created: function () {
    this.getMovieDetail(this.$route.params.movieId)
  }
}
</script>

<style scoped>
.card {
  background-color: #ffffff;
}
</style>