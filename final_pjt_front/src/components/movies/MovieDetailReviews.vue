<template>
  <div class="container row d-flex justify-content-center">
    <div class="col-6 card-body h-50" v-for="(review, idx) in reviews.slice(0, 4)" :key="idx">
      <div class="card p-2 review-short-card">
        <div class="d-flex justify-content-between">
          <span class="fw-bold fs-5 pe-2">{{ review.title }}</span>
          <button :id="`likeCount-${review.id}`" class="btn" @click="updateReviewLikes(review, review.user)">
            <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInReviewLikes(review.likes)}"></i>
            <span>{{ review.likes.length }}</span>
          </button>
        </div>
        <div class="d-flex justify-content-between">
          <span :class="[makeBadge(review.rating), 'text-center']" style="width: 80px">평점: {{ review.rating }}</span>
          <router-link
            :to="{ name: 'ReviewDetail', params: { movieId: review.movie, reviewId: review.id }}"
            class="text-decoration-none text-dark text-end"
          >
            리뷰 상세보기
          </router-link>
        </div>
      </div>
    </div>
    <!-- {{ reviews[0].movie}} -->
    <div class="d-flex justify-content-end">
      <div v-if="reviews.length > 4">
        <router-link :to="{ name: 'MovieReviews', params: { movieId: reviews[0].movie } }" class="text-decoration-none text-dark btn btn-info">
          더 많은 리뷰
        </router-link>  
      </div>
      <input
        type="button"
        class="text-decoration-none text-dark btn btn-primary text-white btn-xs mx-3"
        @click="openReviewCreateModal"
        value="리뷰 작성"
      >
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState, mapActions } from 'vuex'
import _ from 'lodash'
import axios from 'axios'
import SERVER from '@/api/server.js'

export default {
  name: 'MovieReviews',
  props: {
    reviews: {
      type: Array,
    }
  },
  methods: { 
    ...mapActions([
      'openModal',
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
      } else {
        alert('본인이 작성한 리뷰는 좋아요를 누를 수 없습니다.')
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
    }
  },
  computed: {
    ...mapGetters([
      'config',
      'jwtUserId',
    ]),
    ...mapState([
      'modalData',
    ])
  },
  watch: {
    review: function() {
      console.log('hi')
    },
  },
}
</script>

<style scoped>
.review-card {
  position: relative;
  display: inline-block;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0,0,0,.125);
  border-radius: .25rem;
  height: 120px;
}

.review-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}

.review-short-card {
  background-color: rgba(41, 146, 152, 1);
  border: 3px solid rgba(34, 41, 66, 0.9);
}
</style>