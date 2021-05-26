<template>
  <div>
    <div v-if="randomRecommendMovies.length > 0" class="d-flex">
      <div v-for="(movie, idx) in randomRecommendMovies.slice(0, 4)" :key="idx" class="mx-3">
        <div class="create-box rounded" :style="{ backgroundImage: `url(${movie.poster_path})`, backgroundSize: '100% 100%' }">
        </div>
        <!-- <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top similar-transparent"
          @click="[showClickMovieDetail(),getRandomRecommendMovie()]"> -->
                    <!-- @mouseover="moveDetail(movie.id)" -->

        <!-- </router-link> -->
      </div>

    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'SimilarMoives',
  data: function () {
    return {
      checkClick: false,
    }
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

.create-box {
  width: 210px;
  height: 350px;
}
</style>