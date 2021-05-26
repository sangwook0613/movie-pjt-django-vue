<template>
  <div>
    <h1 class="text-light">{{ movieDetail.title }} 리뷰</h1>
    <div class="col-6 offset-3">
      <!-- <div class="text-white">{{ movieDetail }}</div> -->
      <div class="card-body h-50 component-1 mb-2" v-for="(review, idx) in reverseReviews" :key="idx">
        <router-link
          :to="{ name: 'ReviewDetail', params: { movieId: review.movie, reviewId: review.id }}"
          class="text-decoration-none text-dark"
        >
          <div class="d-flex flex-column align-items-start">
            <div class=" d-flex justify-content-start">
              <img
                alt="profile-image"
                class="ellipse-2"
                src="https://static.overlay-tech.com/assets/eba0d02d-858f-4cab-9e4e-d897a0d4800d.png"
              />
              <div>
                <p class="username">{{ review.user.username }}</p>
                <p class="rating">평점 {{ review.rating }}</p>
              </div>
            </div>
            <div class="mb-3">
              <div class="title fw-bold">
                {{ review.title }}
              </div>
              <!-- 내용이 없음 -->
              <div class="content">
                {{ review.content }}
              </div>
              <div class="rating">&#43; 더보기</div>
            </div>
          </div>
        </router-link>
          <div class="d-flex align-items-center">
            <div :id="`likeCount-${review.id}`" class="" @click="updateReviewLikes(review, review.user.id)">
              <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInReviewLikes(review.likes)}"></i>
              <span class="ps-2 rating">{{ review.likes.length }}</span>
            </div>
            <div class="comment-count">
                <img
                  alt=""
                  class="vector"
                  src="https://static.overlay-tech.com/assets/6d5c72bb-4b13-4f8a-99e7-fc4b3a1c9049.svg"
                />
              <span class="ps-2 rating">{{ review.comment_count }}</span>
            </div>
          </div>
      </div>
        <!-- <div class="card p-2 mb-3">
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
        </div> -->
      </div>
    </div>
    <!-- <button @click="goBack" class="btn btn-info">이전 페이지로</button>
  </div> -->
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
    ]),
    reverseReviews: function () {
      return _.reverse(this.movieDetail.movie_reviews)
    }
  },
  created: function () {
    this.getMovieDetail(this.$route.params.movieId)
  },
  updated: function () {
      document.body.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),url(${this.movieDetail.backdrop_path})`;
  },
  beforeDestroy: function () {
    document.body.style.backgroundImage = ""
    document.body.style.backgroundColor = "#141414"
  }
}
</script>

<style scoped>
.card {
  background-color: #ffffff;
}
</style>