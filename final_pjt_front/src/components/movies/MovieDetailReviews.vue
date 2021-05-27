<template>
  <div class="px-4">
    <div class="row d-flex justify-content-center">
      <div class="col-3 card-body main-card" v-for="(review, idx) in reviews.slice(0, 4)" :key="idx">
        <div class="d-flex flex-column align-items-start card-text">
          <router-link
            :to="{ name: 'ReviewDetail', params: { movieId: review.movie, reviewId: review.id }}"
            class="text-decoration-none"
          >
            <div class=" d-flex justify-content-start">
              <img
                alt="profile-image"
                class="profile-image"
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
              <div class="content" style="word-break:break-all; word-wrap:break-word;">
                {{ review.content }}
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
      </div>
    </div>
    <div class="d-flex justify-content-end mt-3">
      <div v-if="reviews.length > 4">
        <router-link :to="{ name: 'MovieReviews', params: { movieId: reviews[0].movie } }" class="text-decoration-none rounded-pill fw-bold btn custom-black-btn">
          리뷰 모음
        </router-link>  
      </div>
      <input
        type="button"
        class="text-decoration-none btn custom-btn rounded-pill fw-bold text-white ms-3"
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
      if (user_id !== this.jwtUserId) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.review + `${review.id}/like/`,
          method: 'post',
          headers,
        })
        .then(() => {
          const likeCountImage = document.querySelector(`#likeCount-${review.id} > i`)
          const likeCountNum = document.querySelector(`#likeCount-${review.id} > span`)
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
      } else {
        alert('본인이 작성한 리뷰는 좋아요를 누를 수 없습니다.')
      }
    },
    checkUserIncludeInReviewLikes: function (review_likes) {
      if (_.includes(review_likes, this.jwtUserId)) {
        return 'crimson'
      }
      return 'white'
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
.main-card {
  background-color: #292828;
  border-radius: 8px;
}

.profile-image {
  width: 48px;
  height: 48px;
  margin-right: 15px;
  border-radius: 50%;
}

.username {
  color: #FFFFFF;
  margin-bottom: 4px;
}

.rating {
  color: #FFFFFF;
}

.title {
  color: #FFFFFF;
  margin-bottom: 14px;
}

.content {
  color: #FFFFFF;
  margin-bottom: 14px;
}

.vector {
  width: 50%;
  height: 50%;
}

.comment-count {
  margin-left: 10px;
}

.custom-btn {
  background-color: #00cecb;
  width: 110px;
}

.custom-black-btn {
  border: 2px solid #00cecb;
  background-color: #292828;
  color: #00cecb;
  width: 110px;
}

.card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>