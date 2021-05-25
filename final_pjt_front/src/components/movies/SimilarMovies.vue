<template>
  <div>
    <carousel v-if="randomRecommendMovies.length > 0" :nav="false" :items="6">
      <div v-for="(movie, idx) in randomRecommendMovies" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top similar-transparent"
          @click="[showClickMovieDetail(),getRandomRecommendMovie()]">
                    <!-- @mouseover="moveDetail(movie.id)" -->

        </router-link>
      </div>

    </carousel>
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'SimilarMoives',
  data: function () {
    return {
      checkClick: false,
    }
  },
  components: {
    carousel,
  },
  computed: {
    ...mapState('movieStore', [
      'randomRecommendMovies',
    ])
  },
  methods: {
    ...mapActions('movieStore', [
      'getRandomRecommendMovie',
    ]),
    showClickMovieDetail: function () {
      this.checkClick = !this.checkClick
    },
    // moveDetail(movieId) {
    //     setTimeout(() => {
    //       this.$router.push({ name: 'MovieDetail', params: { movieId: movieId }})
    //       }, 2000)
    // },
  },
  created: function () {
    this.getRandomRecommendMovie()
  },
  
}
</script>

<style>
/* .similar-transparent{
    opacity: 0.4;
} */
</style>