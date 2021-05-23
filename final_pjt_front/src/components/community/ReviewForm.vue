<template>
  <div>
    <!-- <div v-if="formNum === 1"> -->
    <div class="review-form">
      <!-- <h1>{{ typeof(reviewId) === 'undefined' }}</h1> -->
      <h1>{{ reviewId }}</h1>
      <h1>리뷰 작성하기</h1>
      <div>
        <label for="reviewTitle">제목: </label>      
        <input type="text" v-model.trim="reviewFormData.title" required>
      </div>
      <div>
        <label for="reviewContent">내용: </label>
        <input type="text" v-model.trim="reviewFormData.content" required>
      </div>
      <div>
        <label for="reviewRating">평점: </label>
        <input type='number' v-model="reviewFormData.rating" min='1' max='10' step='1' required>
      </div>
      <button @click="createReview(reviewFormData)">작성 완료</button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'ReviewForm',
  props: {
    reviewId: {
      type: Number, 
    }
  },
  data: function () {
    return {
      reviewFormData: {
        title: '',
        content: '',
        rating: 0,
      }
    }
  },
  computed: {
    ...mapState('movieStore', [
      'movieDetail',
    ])
  },
  methods: {
    ...mapActions('communityStore', [
      'createReview',
    ]),
    ...mapActions('movieStore', [
      'getMovieDetail',
    ]),
  },
  created: function () {
    this.getMovieDetail(this.$route.params.movieId)
  },
}
</script>

<style>
.review-form {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>