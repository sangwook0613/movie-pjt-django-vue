<template>
  <div>
    <h1>MovieDetail</h1>
    <div class="card mb-3">
      <div class="row g-0">
        <div class="col-md-6">
          <div class="card-body">
            <h5 class="card-title">{{ movieDetail.title }}</h5>
            <p class="card-text">{{ movieDetail.overview }}</p>
          </div>
        </div>
        <div class="col-md-6 card">
          <img :src="movieDetail.backdrop_path" alt="backdrop-image">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  methods: {
    ...mapActions('movieStore', [
      'getMovieDetail',
    ])
  },
  computed: {
    ...mapState('movieStore', [
      'movieDetail',
    ])
  },
  watch: {
    '$route.params.movieId': function() {
      this.getMovieDetail(this.$route.params.movieId)
    },
  },
  created: function () {
    this.getMovieDetail(this.$route.params.movieId)
  }
  // created: function () {
  //   if (this.$store.getters.isLoggedIn) {
  //     this.getTodos()
  //   } else {
  //     this.$router.push({ name: 'Login' })
  //   }
  // },
}
</script>

<style>
</style>