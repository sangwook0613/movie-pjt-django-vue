<template>
  <div>
    <div v-if="similarRecommendMovie.length > 0" class="d-flex">
      <div v-for="(movie, idx) in similarRecommendMovie.slice(0, 4)" :key="idx" class="mx-3">
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <div class="create-box rounded scale" :style="{ backgroundImage: `url(${movie.poster_path})`, backgroundSize: '100% 100%' }">
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

<style scoped>
/* .similar-transparent{
    opacity: 0.4;
} */

.create-box {
  width: 210px;
  height: 350px;
}
.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;   /* 부드러운 모션을 위해 추가*/
}
.scale:hover {
  transform: scale(1.05);
  -webkit-transform: scale(1.05);
  -moz-transform: scale(1.05);
  -ms-transform: scale(1.05);
  -o-transform: scale(1.05);
  opacity:0.8;
}
</style>