<template>
  <div class="text-white">
    <h1>선호하는 영화를 선택해주세요.</h1>
    <!-- 5개 이상 선택 했을 경우에 제출 가능하게-->
    <div>
      <hr>
      <div class="text-center" v-if="selectLikeMovies.length >= 5">
        <button @click="likeSelectMovie(selectLikeMovies)" class="btn btn-light">선택완료</button><hr>
      </div>
      <div v-else class="text-center">
        <h2 class="animate__animated animate__headShake animate__infinite">최소 5개 이상 선택해주세요!</h2>
        <i><b>{{ profile.username }}</b>님께 맞는 영화 추천에 사용됩니다.</i><hr>
        <!-- <span v-if="profile.like_movies.length > 5"> -->
          <button @click="$router.push({name: 'Movie'})" class="btn btn-light">다음에 고를래요!</button>
        <!-- </span> -->
      </div>
      <h5 class="text-center">{{ selectLikeMovies.length }} 개를 선택하셨습니다.</h5><br>
    </div>
    <div class="row row-cols-1 row-cols-md-5 g-4">
        <div v-for="(movie, idx) in choiceMovies" :key="idx" class="col">
          <div class="card">
            <img :src="movie.poster_path" alt="movie-poster" class="card-img-top"
            :class="{ 'animate__animated animate__pulse animate__infinite' : selectLikeMovies.includes(movie.id) }"
            @click="updateLikeMovies(movie.id)">
          </div>
        </div>
    </div>

  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieSelect',
  data: function () {
    return {
      selectLikeMovies: [],
    }
  },
  methods: {
    updateLikeMovies: function (data) {
      // 이미 눌렀으면
      if (this.selectLikeMovies.includes(data)) {
        // 취소
        let idx = this.selectLikeMovies.indexOf(data)
        this.selectLikeMovies.splice(idx,1)
      } else {
        // 없으면 추가
        this.selectLikeMovies.push(data)
      }
    },
    ...mapActions('movieStore', [
      'getLikeChoiceMovie',
      'likeSelectMovie',
    ]),
    ...mapActions('accountStore', [
      'getProfile',
    ]),
    ...mapActions([
      'updateShowNav',
    ]),
  },
  computed: {
    ...mapState('movieStore', [
      'choiceMovies',
    ]),
    ...mapState('accountStore', [
      'profile',
    ]),
    ...mapGetters([
      'jwtUsername',
    ]),
  },
  watch: {
    'profile': function() {
      if (this.profile.like_movies.length >= 5) {
        this.$router.push({name: 'Movie'})
      } 
      else {
        this.updateShowNav(false)
      }
    },
  },
  created: function () {
    this.getLikeChoiceMovie()
    this.getProfile(this.jwtUsername)
  },
}
</script>

<style scoped>
.animate__animated {
    --animate-duration  : 0.8s;
    --animate-delay     : 0.8s;
}
</style>