<template>
  <div class="main-page-movie" v-if="mostGenreRecommendMovie.length > 0">
    <VueSlickCarousel v-bind="settings">
      <div v-for="(movie, idx) in mostGenreRecommendMovie" :key="idx" >
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}" class="text-decoration-none">
          <div class="main-page-movie" :style="{ backgroundImage: `linear-gradient(to right, #141414, rgba(20, 20, 20, 0) 30%),
          linear-gradient(to left, #141414, rgba(20, 20, 20, 0) 30%),
          url(${movie.backdrop_path})`,
            backgroundRepeat: 'no-repeat',
            backgroundSize: 'cover' }"
          >
            <div class="image-text">{{ movie.title }}</div>
            <div class="image-text-sub">지금 이 영화를 알아보세요!</div>
          </div>
        </router-link>
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
        "arrows": false,
        "infinite": true,
        "slidesToShow": 1,
        "autoplay": true,
        "speed": 5000,
        "autoplaySpeed": 5000,
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
.main-page-movie {
  width: 1300px;
  height: 529px;
  margin-bottom: 40px;
}

.image-text {
  text-decoration: none;
  color: #FFFFFF;
  font-size: 50px;
  font-weight: 700;
  position: relative;
  top: 390px;
  left: 70px;
}

.image-text-sub {
  text-decoration: none;
  color: #FFFFFF;
  font-size: 20px;
  font-weight: 700;
  position: relative;
  top: 390px;
  left: 76px;
}
</style>