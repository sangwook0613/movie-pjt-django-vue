<template>
  <div>
    <div class="fw-bold fs-2 text-light text-center mb-3">{{ movieDetail.title }} 리뷰</div>
    <div class="d-flex align-items-center justify-content-center">
      <router-link :to="{ name: 'MovieDetail', params: { movieId: movieDetail.id } }"
        class="text-decoration-none pb-2 fw-bold text-light"
      >
        <i class="fas fa-film pe-1"></i>
        {{ movieDetail.title }} 정보 보기
      </router-link>
    </div>
    <div class="col-6 offset-3">
      <!-- <div class="text-white">{{ movieDetail }}</div> -->
      <div class="card-body review-card mb-2" v-for="(review, idx) in reverseReviews" :key="idx">
        <router-link
          :to="{ name: 'ReviewDetail', params: { movieId: review.movie, reviewId: review.id }}"
          class="text-decoration-none"
        >
          <div class="d-flex flex-column align-items-start">
            <div class=" d-flex justify-content-start">
              <img
                alt="profile-image"
                class="profile-image"
                src="https://static.overlay-tech.com/assets/eba0d02d-858f-4cab-9e4e-d897a0d4800d.png"
              />
              <div>
                <p class="username fw-bold fs-6">{{ review.user.username }}</p>
                <p class="rating">평점 {{ review.rating }}</p>
              </div>
            </div>
            <div class="mb-3">
              <div class="title fw-bold fs-5">
                {{ review.title }}
              </div>
              <div class="content fs-6" style="word-break:break-all; word-wrap:break-word;">
                {{ review.content }}
              </div>
            </div>
          </div>
        </router-link>
          <div class="d-flex align-items-center">
            <div :id="`likeCount-${review.id}`" class="" @click="updateReviewLikes(review, review.user.id)">
              <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInReviewLikes(review.likes)}"></i>
              <span class="ps-2 rating">{{ review.likes.length }}</span>
            </div>
            <div class="comment-count d-flex align-items-center">
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
      return 'white'
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

.review-card {
  padding: 20px;
  border-radius: 8px;
  background-color: #292828;
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
.card {
  background-color: #ffffff;
}
</style>