<template>
  <div>
    <h1>선호하는 영화를 선택해주세요.</h1>
    <!-- 5개 이상 선택 했을 경우에 제출 가능하게-->
    <div>
      <div class="text-center" v-if="selectLikeMovies.length >= 5">
        <hr><button @click="likeSelectMovie(selectLikeMovies)" class="btn btn-dark">선택완료</button><hr>
      </div>
      <div v-else class="text-center">
        <hr><h2 class="animate__headShake">최소 5개 이상 선택해주세요!</h2>
        <i><b>{{ profile.username }}</b>님에게 맞는 영화 추천에 사용됩니다.</i><hr>
        <span v-if="profile.like_movies.length > 5">
          <button @click="$router.push({name: 'Movie'})">건너뛰기</button>
        </span>
      </div>
    </div>

    <div class="row row-cols-1 row-cols-md-5 g-4">
        <div v-for="(movie, idx) in choiceMovies" :key="idx" class="col">
          <div class="card">
            <img :src="movie.poster_path" alt="movie-poster" class="card-img-top"
            :class="{ 'animate__animated animate__pulse animate__infinite' : (selectLikeMovies.includes(movie.id) || alreadyLikeMovies.includes(movie.id))  }"
            @click="updateLikeMovies(movie.id)">
          </div>
          <!-- animate__animated animate__pulse animate__infinite -->
          <!-- Blur -->
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
      alreadyLikeMovies: [],
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
    // 이미 좋아요 누른거 확인용
    updateAlreadyLikeMovies: function () {
      this.alreadyLikeMovies = this.profile.like_movies
      console.log(this.alreadyLikeMovies)
      for (let movie of this.alreadyLikeMovies) {
        this.alreadyLikeMovies.push(movie.id)
      }
      // console.log(this.choiceMovies)
    },
    ...mapActions('movieStore', [
      'getLikeChoiceMovie',
      'likeSelectMovie',
    ]),
    ...mapActions('accountStore', [
      'getProfile',
    ]),
    // ...mapActions([
    //   'updateShowNav',
    // ]),
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
      this.updateAlreadyLikeMovies(this.choiceMovies)
      if (this.profile.like_movies.length > 5) {
        // this.updateShowNav(true)
        this.$router.push({name: 'Movie'})
      } 
      // else {
      //   this.updateShowNav(false)
      // }
    },
  },
  created: function () {
    this.getLikeChoiceMovie()
    this.getProfile(this.jwtUsername)
  },
}
</script>

<style>
.animate__animated {
    --animate-duration  : 0.8s;
    --animate-delay     : 0.8s;
}
</style>