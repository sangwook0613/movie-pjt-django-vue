<template>
  <div>
    <h1>SEARCH PAGE</h1>
    <!-- {{ searchedMovies }} -->
    <div v-if="searchedMovies">
      <VueSlickCarousel v-if="searchedMovies.length > 0" v-bind="settings">
        <div v-for="(movie, idx) in searchedMovies" :key="idx" class="card">
            <img :src="movie.poster_path" alt="movie-poster" class="card-img-top">
        </div>
      </VueSlickCarousel>
    </div>
  </div>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
import { mapGetters, mapState, mapActions } from 'vuex'

export default {
  name: 'Search',
  components: {
    VueSlickCarousel,
  },
  data: () => ({
				settings: {
          "centerMode": true,
          // "centerPadding": "15px",
          "focusOnSelect": true,
          "infinite": true,
          "slidesToShow": 5,
          "speed": 500,
				}
			}),
  methods: {
    ...mapActions('movieStore', [
      'clickSearchBtn',
      'clickSearchCancelBtn',
      'searchMovie',
    ])
  },
  computed: {
    ...mapGetters('movieStore', [
      'searchedMovies',
      'searchBtn',
      'searchInput',
    ]),
    ...mapState('movieStore', [
      'searchBtn',
      'searchedMovies',
      'searchInput',
    ])
  },
  watch: {
    '$route.query.q': function() {
      this.searchMovie()
    },
  },
  created: function () {
      this.searchMovie()
  }
}
</script>

<style>

</style>