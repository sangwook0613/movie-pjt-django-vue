<template>
  <div class="container px-4">
    <div class="row d-flex justify-content-center g-2">
      <div class="col-xl-3 card-body h-50 component-1" v-for="(review, idx) in reviews.slice(0, 4)" :key="idx">
        <div class="d-flex flex-column align-items-start">
          <router-link
            :to="{ name: 'ReviewDetail', params: { movieId: review.movie, reviewId: review.id }}"
            class="text-decoration-none text-dark"
          >
            <div class=" d-flex justify-content-start">
              <img
                alt="profile-image"
                class="ellipse-2"
                src="https://static.overlay-tech.com/assets/eba0d02d-858f-4cab-9e4e-d897a0d4800d.png"
              />
              <div>
                <p class="username">usernamegoeshere</p>
                <p class="rating">평점 {{ review.rating }}</p>
              </div>
            </div>
            <div class="mb-3">
              <div class="title fw-bold">
                러빙 빈센트는 진짜 그림이 다했다 {{ review.title }}
              </div>
              <div class="content">
                얼씨구절씨구얼씨구절씨구얼씨구절씨얼씨구절씨구얼씨구절씨구얼씨구절씨구얼씨구...
              </div>
              <div class="rating">&#43; 더보기</div>
            </div>
          </router-link>
          <div class="d-flex align-items-center">
            <div :id="`likeCount-${review.id}`" class="" @click="updateReviewLikes(review, review.user)">
              <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInReviewLikes(review.likes)}"></i>
              <span class="ps-2 rating">{{ review.likes.length }}</span>
            </div>
            <div class="comment-count">
                <img
                  alt=""
                  class="vector"
                  src="https://static.overlay-tech.com/assets/6d5c72bb-4b13-4f8a-99e7-fc4b3a1c9049.svg"
                />
              <!-- comment 수 필요 -->
              <span class="ps-2 rating">5</span>
            </div>
          </div>
        </div>
        <!-- <div class="card p-2 review-short-card">
          <div class="d-flex justify-content-between">
            <span class="fw-bold fs-5 pe-2">
              <router-link
                :to="{ name: 'ReviewDetail', params: { movieId: review.movie, reviewId: review.id }}"
                class="text-decoration-none text-dark text-end"
              >
                {{ review.title }}
              </router-link>
            </span>
            <button :id="`likeCount-${review.id}`" class="btn" @click="updateReviewLikes(review, review.user)">
              <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInReviewLikes(review.likes)}"></i>
              <span>{{ review.likes.length }}</span>
            </button>
          </div>
          <div class="d-flex justify-content-between">
            <span :class="[makeBadge(review.rating), 'text-center']" style="width: 80px">평점: {{ review.rating }}</span>
            <span>{{ review.user }}</span>
          </div>
        </div> -->
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
/* .review-card {
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
} */

.component-1 {
  background-color: #292828;
  border-radius: 8px;
}
/* .frame-11 {
  width: calc(100% - 48px);
  height: calc(100.73% - 48px);
  padding: 24px;
  position: absolute;
  left: 0;
  top: -1px;
} */
.frame-10 {
  margin-bottom: 24px;
}
.ellipse-2 {
  width: 48px;
  height: 48px;
  margin-right: 15px;
  border-radius: 50%;
}
.frame-7 {
  padding: 0 44px 0 0;
}
.username {
  color: #FFFFFF;
  margin-bottom: 4px;
  @include noto-sans-kr-14-bold;
}
.rating {
  color: #FFFFFF;
  @include noto-sans-kr-14-regular;
}
.title {
  color: #FFFFFF;
  margin-bottom: 14px;
  @include noto-sans-kr-14-bold;
}
.content {
  color: #FFFFFF;
  margin-bottom: 14px;
  @include noto-sans-kr-14-regular;
}
.frame-12 {
  margin-right: 14px;
}
.favorite-border-black-24dp-1 {
  margin-right: 8px;
  padding: 3px 2px 2.65px;
}
.vector {
  width: 50%;
  height: 50%;
}
.comment-count {
  margin-left: 10px;
  /* padding: 2px; */
}
</style>