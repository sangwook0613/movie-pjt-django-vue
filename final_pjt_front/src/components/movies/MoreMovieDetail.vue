<template>
  <div class="card my-1 text-center">
    <!-- {{ movieDetailInfo }} -->
    <!-- {{movieDetailInfo.movie_reviews}} -->
    <h4 class="my-3">{{ movieDetailInfo.title }} 리뷰</h4>
    <div v-if="movieDetailInfo.movie_reviews.length === 0">
      <p><b>첫 번째 리뷰를 남겨주세요!</b></p>
      <router-link
        :to="{ name: 'ReviewForm', params: { movieId: movieDetailInfo.id }}"
        class="text-decoration-none btn btn-primary"
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