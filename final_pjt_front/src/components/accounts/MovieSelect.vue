<template>
  <div class="text-white">
    <div class="fw-bold fs-1 mb-4 text-center">좋아하는 영화를 선택해주세요.</div>
    <!-- 5개 이상 선택 했을 경우에 제출 가능하게-->
    <div class="d-flex flex-column align-items-center mb-5">
      <div v-if="selectLikeMovies.length >= 5">
        <button @click="likeSelectMovie(selectLikeMovies)" class="btn custom-btn rounded-pill text-white fw-bold mb-4">선택완료</button>
      </div>
      <div v-else class="text-center mb-3 d-flex flex-column align-items-center">
        <div class="fw-bold fs-3 mb-2">최소 5개 이상 선택해주세요!</div>
        <i><span class="fw-bold fs-5" style="color: #00cecb;">{{ profile.username }}</span> 님께 맞는 영화 추천에 사용됩니다.</i>
        <div @click="$router.push({name: 'Movie'})" class="btn black-btn rounded-pill text-white fw-bold my-4">다음에 고를래요!</div>
      </div>
      <div class="fw-bold fs-4">{{ selectLikeMovies.length }} 개를 선택하셨습니다.</div>
    </div>
    <div class="row row-cols-1 row-cols-md-5 g-4">
        <div v-for="(movie, idx) in choiceMovies" :key="idx" class="col">
          <div>
            <img :src="movie.poster_path" alt="movie-poster" class="card-img-top" loading="lazy"
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
      backgroundLoading:'#141414',
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
    openLoadingBackground(){
      this.$vs.loading({background:this.backgroundLoading,color:'rgb(255, 255, 255)'})
      setTimeout( ()=> {
        this.$vs.loading.close()
      }, 2000);
    },
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
      // else {
      //   this.updateShowNav(false)
      // }
    },
  },
  created: function () {
    this.getLikeChoiceMovie()
    this.getProfile(this.jwtUsername)
    this.openLoadingBackground()
  },
}
</script>

<style scoped>
.black-btn {
  background-color: #292828;
  border: 2px solid #FFFFFF;
  padding: 10px;
  width: 190px;
}

.custom-btn {
  background-color: #00cecb;
  padding: 10px;
  width: 190px;
}

.animate__animated {
    --animate-duration  : 0.8s;
    --animate-delay     : 0.8s;
}
</style>