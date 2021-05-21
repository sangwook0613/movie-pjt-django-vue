<template>
  <div class="movie container">
    <h1>홈페이지!</h1>
    <p>{{ movies }}</p>
    <!-- <carousel v-if="$store.state.movies.length > 0" :nav="false" :items="5">
      <div v-for="(movie, idx) in $store.state.movies" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top">
        </router-link>
      </div>
    </carousel> -->
    <!-- <div class="row row-cols-1 row-cols-md-2 row-cols-xl-4 g-4">
      <MovieCard
        v-for="(movie, idx) in $store.state.movies"
        :key="idx"
        :movie="movie"
      />
    </div> -->
    <!-- <router-view></router-view> -->
  </div>
</template>

<script>
// import carousel from 'vue-owl-carousel'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'Movie',
  // components: {
  //   carousel,
  // },
  computed: {
    ...mapState({
      movies: state => state.movieStore.movies
      // movies: 'hi',
    })
  },
  methods: {
    ...mapActions('movieStore', [
      'getMovie',
      // getMovie: actions => actions.movieStore.getMovie
    ])
  },
  // computed: {
  //     ...mapState({
  //     a: state => state.some.nested.module.a,
  //     b: state => state.some.nested.module.b
  //   })
  // },
  created: function () {
    this.getMovie()
    // if (this.$store.getters.isLoggedIn) {
    //   this.getTodos()
    // } else {
    //   this.$router.push({ name: 'Login' })
    // }
  },
}
</script>
