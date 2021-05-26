<template>
  <div>
    <VueSlickCarousel :arrows="true" v-bind="settings">
      <div v-for="(movie, idx) in mostGenreRecommendMovie" :key="'k'+idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img loading="lazy" :src="movie.backdrop_path" alt="movie_backdrop_path" class="card-img-top">
        </router-link>
        <h3 class="text-center">{{ movie.title }}</h3>
      </div>
    </VueSlickCarousel>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name: 'MovieMainPage',
  components: {
    VueSlickCarousel,
  },
  data: function () {
    return {
      settings: {
        "edgeFriction": 0.35,
        "infinite": false,
        "speed": 500,
        "slidesToShow": 1,
        "slidesToScroll": 1
        },
    }
  },
  computed: {
    ...mapState('movieStore', [
      'mostGenreRecommendMovie',
    ]),
  },
  methods: {
    ...mapActions('movieStore', [
      'getMostGenreRecommendMovie',
    ]),
  },
  created: function () {
    this.getMostGenreRecommendMovie()
  }
}
</script>

<style>

</style>