<template>
  <div>
    <carousel v-if="randomRecommendMovies.length > 0" :nav="false" :items="5">
      <div v-for="(movie, idx) in randomRecommendMovies" :key="idx" class='card'>
        <img :src="movie.poster_path" alt="movie-poster" class="card-img-top">
      </div>
    </carousel>
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'SimilarMoives',
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
  },
  created: function () {
    this.getRandomRecommendMovie()
  },
}
</script>

<style>

</style>