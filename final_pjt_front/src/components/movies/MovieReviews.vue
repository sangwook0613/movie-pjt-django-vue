<template>
  <div class="container row">
    <div class="col-6 card-body h-50" v-for="(review, idx) in reviews.slice(0, 4)" :key="idx">
      <div class="card p-2">
        <div class="d-flex justify-content-between">
          <span class="fw-bold fs-5 pe-2">{{ review.title }}</span>
          <button id="likeCount" class="btn" @click="updateReviewLikes(review.id, review.user)">
            <i class="fas fa-heart fa-lg me-1"></i>
            <span>{{ review.likes.length }}</span>
          </button>
        </div>
        <div class="d-flex justify-content-between">
          <span :class="[makeBadge(review.rating), 'text-center']" style="width: 80px">평점: {{ review.rating }}</span>
          <router-link :to="{ name: 'ReviewDetail', params: { movieId: review.movie, reviewId: review.id } }" class="text-decoration-none text-dark text-end">
            리뷰 상세보기
          </router-link>
        </div>
      </div>
    </div>
    <!-- <router-link :to="{ name: 'MovieReviewMore', params: { reviewId: review.id } }" class="text-decoration-none text-dark btn btn-info">
      더 많은 리뷰보기
    </router-link> -->
    <router-link :to="{ name: 'ReviewForm', params: { movieId: reviews[0].movie } }" class="text-decoration-none text-dark btn btn-primary">
      리뷰 작성하기
    </router-link>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
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
    // ...mapActions('communityStore', [
    //   'updateReviewLikes',
    // ]),
    
    updateReviewLikes: function (reviewId, user_id) {
      const headers = this.config
      if (user_id !== this.jwtUsername.user_id) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.review + `${reviewId}/like/`,
          method: 'post',
          headers,
        })
        .then(() => {
          const likeCountImage = document.querySelector('#likeCount > i')
          const likeCountNum = document.querySelector('#likeCount > span')
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
  },
  computed: {
    ...mapGetters([
      'config',
      'jwtUsername',
    ])
  },
  watch: {
    review: function() {
      console.log('hi')
    },
  },
}
</script>

<style>
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

</style>