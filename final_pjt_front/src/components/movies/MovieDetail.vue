<template>
  <div>
    <h1>MovieDetail</h1>
    <!-- <router-view></router-view> -->
    <h3>{{$route.params.movieId}}</h3>
    <!-- <button @click="getMovieDetail($route.params.movieId)">click</button> -->
    <div>
      <h1>{{ }}</h1>
    </div>
    {{ $store.state.movieDetail }}
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MovieDetail',
  methods: {
    ...mapActions([
      'getMovieDetail',
    ])
  },
  mounted: function () {
    this.getMovieDetail(this.$route.params.movieId)
    // if (this.$store.getters.isLoggedIn) {
    //   this.getTodos()
    // } else {
    //   this.$router.push({ name: 'Login' })
    // }
  },
}
</script>

<style>

</style>