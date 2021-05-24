<template>
  <div>
    <h2 class="fw-bold pt-1">'{{ this.$route.query.q }}' 검색 결과</h2><br>
    <div v-if="searchedMovies">
      <div class="row row-cols-1 row-cols-md-5 g-3">
        <div v-for="(movie, idx) in searchedMovies" :key="'xx'+idx" class="col">
          <div class="card ">
            <img :src="movie.poster_path" alt="movie-poster" class="card-img-top ">
            <!-- <div class="card-footer bg-transparent border-dark">
              <p class="card-text text-center fw-bold text-dark">{{ movie.title }}</p>
            </div> -->
          </div>
        </div>
      </div>
    </div>
    <div v-else class="text-secondary fw-bold text-center text-danger">
      <br><br><br><br><br><br><br><br><br><br><br><br>
      <h2 class="fs-1">검색하신 영화가 없습니다<br><br>
      <i class="fas fa-sad-cry"></i>  <i class="fas fa-sad-cry"></i>  <i class="fas fa-sad-cry"></i></h2>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState, mapActions } from 'vuex'

export default {
  name: 'Search',
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
  },
}
</script>

<style>

</style>