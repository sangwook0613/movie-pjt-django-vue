<template>
  <div class="mb-5">
    <!-- 가장 좋아하는 장르 추천 영화 -->
    <div v-if="mostGenreRecommendMovie.length > 0" class="mt-3">
      <h3 class="fw-bold">가장 좋아하는 장르 추천 영화</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie, idx) in mostGenreRecommendMovie" :key="idx">
          <div class="mx-2">
            <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
              <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(2)">
            </router-link>
          </div>

  <div class="movie container">
    <!-- <h1 class="text-white">홈페이지!</h1> -->
    <!-- 랜덤 추천 영화 -->
    <div>
      <MovieMainPage />
    </div>

    <h3>랜덤 추천 영화</h3>
    <VueSlickCarousel v-if="randomRecommendMovies.length > 0" :arrows="true" v-bind="settings">
      <div v-for="(movie, idx) in randomRecommendMovies" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(1)">
        </router-link>
      </div>
    </VueSlickCarousel>
    <!-- <carousel v-if="randomRecommendMovies.length > 0" :nav="false" :items="6">
      <template slot="prev"><span class="prev nav-btn prev-slide"><i class='fa fa-chevron-left'></i></span></template>
      <div v-for="(movie, idx) in randomRecommendMovies" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(1)">
        </router-link>
      </div>
      <template slot="next"><span class="next nav-btn next-slide"><i class='fa fa-chevron-right'></i></span></template>
    </carousel> -->
    <!-- 제일 많이 좋아하는 장르 추천 영화 -->
    <div v-if="mostGenreRecommendMovie.length > 0">
      <h3>제일 많이 좋아하는 장르 추천 영화</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie, idx) in mostGenreRecommendMovie" :key="idx" class='card'>
          <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
            <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(2)">
          </router-link>
        </div>
      </VueSlickCarousel>
    </div>
    <!-- 장르 추천 영화 -->
    <div v-if="genreRecommendMovie.length > 0" class="mt-3">
      <h3 class="fw-bold">장르 추천 영화</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie, idx) in genreRecommendMovie" :key="idx">
          <div class="mx-2">
            <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
              <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(3)">
            </router-link>
          </div>
        </div>
      </VueSlickCarousel>
    </div>
    <div v-if="keywordRecommendMovie.length > 0" class="mt-3">
      <h3 class="fw-bold">키워드 추천 영화</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie, idx) in keywordRecommendMovie" :key="idx">
          <div class="mx-2">
            <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
              <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(3)">
            </router-link>
          </div>
        </div>
      </VueSlickCarousel>
    </div>
    <h1 v-else class="text-light">
      <hr>좋아하는 영화를 선택하시면 추천 영화를 볼 수 있습니다.<hr>
      <router-link :to="{ name: 'MovieSelect'}">
        <button class="btn btn-light">선택하러 가기</button>
      </router-link>
    </h1>
    <!-- 랜덤 추천 영화 -->
    <div class="mt-3">
      <h3 class="fw-bold">랜덤 추천 영화</h3>
      <VueSlickCarousel v-if="randomRecommendMovies.length > 0" :arrows="true" v-bind="settings">
        <div v-for="(movie, idx) in randomRecommendMovies" :key="idx">
          <div class="mx-2">
            <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
              <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(1)">
            </router-link>
          </div>
        </div>
      </VueSlickCarousel>
    </div>


    <div v-if="genreRecommendMovie.length > 0">
      <h3>장르 추천 영화</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie, idx) in genreRecommendMovie" :key="idx" class='card'>
          <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
            <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(3)">
          </router-link>
        </div>
      </VueSlickCarousel>
    </div>


    <div v-if="keywordRecommendMovie.length > 0">
      <h3>키워드 추천 영화</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie, idx) in keywordRecommendMovie" :key="'k'+idx" class='card'>
          <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
            <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(4)">
          </router-link>
        </div>
      </VueSlickCarousel>
    </div>
    <!-- <carousel v-if="genreRecommendMovie.length > 0" :nav="false" :items="6">
      <div v-for="(movie, idx) in genreRecommendMovie" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(3)">
        </router-link>
      </div>
    </carousel> -->

    <h3>따끈 따끈한 최신 영화</h3>
    <VueSlickCarousel :arrows="true" v-bind="settings">
      <div v-for="(movie, idx) in newRecommendMovie" :key="'x'+idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(5)">
        </router-link>
      </div>
    </VueSlickCarousel>

    <h3>평점이 높은 영화</h3>
    <VueSlickCarousel :arrows="true" v-bind="settings">
      <div v-for="(movie, idx) in keywordRecommendMovie" :key="'y'+idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(6)">
        </router-link>
      </div>
    </VueSlickCarousel>

    <h3>가볍게 시간 떼우기 좋은 영상 추천</h3>
    <VueSlickCarousel :arrows="true" v-bind="settings">
      <div v-for="(movie, idx) in runtimeRecommendMovie" :key="'z'+idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img loading="lazy" :src="movie.poster_path" alt="movie-poster" class="card-img-top" @click="showClickMovieDetail(7)">
        </router-link>
      </div>
    </VueSlickCarousel>
  </div>
</template>

<script>
// import carousel from 'vue-owl-carousel'
import MovieMainPage from '@/components/movies/MovieMainPage'
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'Movie',
  components: {
    // carousel,
    VueSlickCarousel,
    MovieMainPage
  },
  data: function () {
    return {
      backgroundLoading:'#141414',
      settings: {
        // "dots": true,
        // "infinite": true,
        "initialSlide": 2,
        "speed": 500,
        "slidesToShow": 6,
        "slidesToScroll": 1,
        "swipeToSlide": true,
        // "adaptiveHeight": true,
        // "variableWidth": true,
      },
    }
  },
  computed: {
    ...mapState('movieStore', [
      'randomRecommendMovies',
      'mostGenreRecommendMovie',
      'genreRecommendMovie',
      'keywordRecommendMovie',
      'newRecommendMovie',
      'ratingRecommendMovie',
      'runtimeRecommendMovie',
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
      'getKeywordRecommendMovie',
      'getNewRecommendMovie',
      'getRatingRecommendMovie',
      'getRuntimeRecommendMovie',

    ]),
    ...mapActions([
      'updateShowNav',
    ]),
    showClickMovieDetail: function (idx) {
      this.checkClicked = [false, false, false, false, false, false, false, false]
      this.checkClicked[idx] = true
    },
    openLoadingBackground(){
      this.$vs.loading({background:this.backgroundLoading,color:'rgb(255, 255, 255)'})
      setTimeout( ()=> {
        this.$vs.loading.close()
      }, 2000);
    },
  },

  created: function () {
    this.openLoadingBackground()
    this.getRandomRecommendMovie()
    this.getMostGenreRecommendMovie()
    this.getGenreRecommendMovie()
    this.getKeywordRecommendMovie()
    this.getNewRecommendMovie()
    this.getRatingRecommendMovie()
    this.getRuntimeRecommendMovie()
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

<style scoped>
h3 {
  color: white;
}

.nav-btn{
  height: 47px;
  position: absolute;
  width: 26px;
  cursor: pointer;
  top: 100px !important;
}

/* .prev-slide{
  background: no-repeat scroll 0 0;
  left: -33px;
}
.next-slide{
  background: no-repeat scroll -24px 0px;
  right: -33px;
} */
.prev-slide:hover{
  background-position: 0px -53px;
}
.next-slide:hover{
  background-position: -24px -53px;
}   

</style>