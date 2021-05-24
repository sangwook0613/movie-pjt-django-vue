<template>
  <div class="card">
    <h1>movieDetailInfo</h1>
    <!-- {{ movieDetailInfo }} -->
    <!-- {{movieDetailInfo.movie_reviews}} -->
    <h5>{{ movieDetailInfo.title }} 관련 리뷰</h5>
    <div v-if="movieDetailInfo.movie_reviews.length === 0">
      <h5>해당 영화에 작성된 리뷰가 없습니다.</h5>
      <router-link
        :to="{ name: 'ReviewForm', params: { movieId: movieDetailInfo.id }}"
        class="text-decoration-none text-dark btn btn-primary"
        @click="setFormType(1)"
      >
        리뷰 작성하기
      </router-link>
    </div>
    <!-- <MovieReviews v-if="movieDetailInfo.movie_reviews" :reviews="movieDetailInfo.movie_reviews"/> -->
  </div>
</template>

<script>
// import MovieReviews from '@/components/movies/MovieReviews'
import { mapActions } from 'vuex'

export default {
  name: 'MoreMovieDetail',
  // components: {
  //   MovieReviews,
  // },
  props: {
    movieDetailInfo: {
      type: [Object, Array],
    }
  },
  methods: {
    ...mapActions('communityStore', [
      'setFormType',
    ])
  }
}
</script>

<style>
</style>