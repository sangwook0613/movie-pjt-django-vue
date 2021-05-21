<template>
  <div>
    <h1>MovieDetail</h1>
    <!-- <router-view></router-view> -->
    <h3>{{$route.params.movieId}}</h3>
    <!-- <button @click="getMovieDetail($route.params.movieId)">click</button> -->
    <div>
      <h1>{{ }}</h1>
    </div>
    {{ movieDetail }}
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
  created: function () {
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