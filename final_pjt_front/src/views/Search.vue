<template>
  <div>
    <h2 class="fw-bold pt-1 text-white">'{{ this.$route.query.q }}' 검색 결과</h2><br>
    <div v-if="searchedMovies">
      <div class="row row-cols-1 row-cols-md-5 g-3">
        <div v-for="(movie, idx) in searchedMovies" :key="'xx'+idx" class="col">
          <div>
            <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}" >
              <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top scale">
            </router-link>
            <!-- <div class="card-footer bg-transparent border-dark">
              <p class="card-text text-center fw-bold text-dark">{{ movie.title }}</p>
            </div> -->
          </div>
        </div>
      </div>
    </div>
    <div v-else class="text-secondary fw-bold text-center text-white mt-5">
      <h2 class="fs-1 fw-bold">검색하신 영화를 찾을 수 없습니다.<br><br>
      <i class="fas fa-sad-cry"></i>  <i class="fas fa-sad-cry"></i>  <i class="fas fa-sad-cry"></i></h2>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState, mapActions } from 'vuex'

export default {
  name: 'Search',
  data(){
    return {
      backgroundLoading:'#141414',
    }
  },
  methods: {
    ...mapActions('movieStore', [
      'clickSearchBtn',
      'clickSearchCancelBtn',
      'searchMovie',
    ]),
    openLoadingBackground(){
      this.$vs.loading({background:this.backgroundLoading,color:'rgb(255, 255, 255)'})
      setTimeout( ()=> {
        this.$vs.loading.close()
      }, 1500);
    },
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
    ]),
  },
  watch: {
    '$route.query.q': function() {
      this.searchMovie()
      this.openLoadingBackground()
    },
  },
  created: function () {
    this.searchMovie()
    this.openLoadingBackground()
  },
}
</script>

<style scoped>
.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;   /* 부드러운 모션을 위해 추가*/
}
.scale:hover {
  transform: scale(1.1);
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
  opacity:0.5;
}
</style>