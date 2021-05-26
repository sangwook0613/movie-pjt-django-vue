<template>
  <div>
    <div v-if="similarRecommendMovie.length > 0" class="d-flex">
      <div v-for="(movie, idx) in similarRecommendMovie.slice(0, 4)" :key="idx" class="mx-3">
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <div class="create-box rounded" :style="{ backgroundImage: `url(${movie.poster_path})`, backgroundSize: '100% 100%' }">
          </div>
        </router-link>
          <!-- <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top"> -->


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
      'similarRecommendMovie',
    ])
  },
  methods: {
    ...mapActions('movieStore', [
      'getSimilarRecommendMovie',
    ]),
    showClickMovieDetail: function () {
      this.checkClick = !this.checkClick
    },
  },
  watch: {
    '$route.params.movieId': function() {
    this.getSimilarRecommendMovie(this.$route.params.movieId)
    },
  },
  created: function () {
    // console.log(this.$route.params.movieId)
    this.getSimilarRecommendMovie(this.$route.params.movieId)
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