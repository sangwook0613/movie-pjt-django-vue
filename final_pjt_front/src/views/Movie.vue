<template>
  <div class="movie container">
    <h1>홈페이지!</h1>
    <!-- 랜덤 추천 영화 -->
    <h3>랜덤 추천 영화</h3>
    <carousel v-if="randomRecommendMovies.length > 0" :nav="false" :items="5">
      <div v-for="(movie, idx) in randomRecommendMovies" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(1)">
        </router-link>
      </div>
    </carousel>
    <!-- 제일 많이 좋아하는 장르 추천 영화 -->
    <h3>제일 많이 좋아하는 장르 추천 영화</h3>
    <carousel v-if="mostGenreRecommendMovie.length > 0" :nav="false" :items="5">
      <div v-for="(movie, idx) in mostGenreRecommendMovie" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(2)">
        </router-link>
      </div>
    </carousel>
    <!-- 장르 추천 영화 -->
    <h3>장르 추천 영화</h3>
    <carousel v-if="genreRecommendMovie.length > 0" :nav="false" :items="5">
      <div v-for="(movie, idx) in genreRecommendMovie" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(3)">
        </router-link>
      </div>
    </carousel>
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'Movie',
  components: {
    carousel,
  },
  computed: {
    ...mapState('movieStore', [
      'randomRecommendMovies',
      'mostGenreRecommendMovie',
      'genreRecommendMovie',
    ]),
    ...mapState([
      'showNav',
    ])
  },
  methods: {
    ...mapActions('movieStore', [
      'getRandomRecommendMovie',
      'getMostGenreRecommendMovie',
      'getGenreRecommendMovie',
    ]),
    ...mapActions([
      'updateShowNav',
    ]),
    showClickMovieDetail: function (idx) {
      this.checkClicked = [false, false, false, false, false]
      this.checkClicked[idx] = true
    },
  },
  created: function () {
    this.getRandomRecommendMovie()
    this.getMostGenreRecommendMovie()
    this.getGenreRecommendMovie()
    this.updateShowNav(true)
    // document.body.style.backgroundImage = "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.squarespace-cdn.com/content/v1/5a173f16ace86416b07c25f1/1513939530902-DILPHAAJ9F0DI627449M/ke17ZwdGBToddI8pDm48kK0QKSDttGV1ap9dyeIseHF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0mxU0godxi02JM9uVemPLqw3ZQRv6tY2V6nZIOWGhJ3qaH6uCpMgOc4rPl-G2eiFCQ/fantasy+album+cover6+-+in+wide+format.jpg?format=1500w')";

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