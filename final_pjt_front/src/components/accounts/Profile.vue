<template>
  <div class="profile">
      <div class="mx-3 mt-3">
        <div class="text-dark fw-bold">
        <p><i class="fw-bold far fa-user-circle big-icon fa-5x"></i></p>
          <h3>@{{ profile.username }}</h3>
        </div>
        <div>
          <span class="text-secondary">게시글</span>
          <span class="fw-bold mx-1 text-secondary pe-1">{{ profile.reviews.length }}</span>
          <span class="text-secondary">팔로잉</span>
          <span class="fw-bold mx-1 text-secondary pe-1">{{ profile.followings.length }}</span>
          <span class="text-secondary">팔로워</span>
          <span class="fw-bold mx-1 pe-1 text-secondary">{{ profile.followers.length }}</span>
        </div>
        <h4 v-if=profile.introduction class="fw-bold pt-3">{{ profile.introduction }}</h4>

      <div v-if="isMyself">
        <span v-if="isFollow">
          <button @click="followUser($route.params.username)" class="mt-3 btn btn-danger btn-sm text-white">팔로우 취소</button>
        </span>
        <span v-else>
          <button @click="followUser($route.params.username)" class="mt-3 btn btn-sm btn-primary">팔로우</button>
        </span>
      </div>
      <div v-else class="mt-3">
        <!-- <button @click="followUser($route.params.username)" class="mt-3 btn btn-primary">프로필 수정</button> -->
        <span type="button"
          class="material-icons md-28"
          @click="openReviewCreateModal">settings</span>
        <!-- <input
          type="button"
          class="text-decoration-none text-dark btn btn-primary text-white btn-xs"
          @click="openReviewCreateModal"
          value="소개글 변경"
        > -->
      </div>
    </div>
    <h3 class="pt-4 fw-bold">Post Reviews</h3>
    <p>리뷰 또는 영화를 클릭하면 해당 페이지로 이동합니다.</p>
    <div class="row d-flex justify-content-evenly profile-detail mx-3">
      <div v-for="(review,idx) in profile.reviews" :key="'B'+idx" class="mt-3 card col-3 ms-3 me-3 card-css">
        <p class="mt-3"><b>{{ idx+1 }}. 
        <router-link
        :to="{ name: 'ReviewDetail',
        params: { movieId: review.movie.id, reviewId: review.id }}"
        class="text-decoration-none text-dark">
        {{ review.title }}</router-link>
        </b></p>

        <p><router-link
        :to="{ name: 'MovieDetail', params: { movieId: review.movie.id }}"
        class="text-decoration-none text-dark">
        {{ review.movie.title }}</router-link></p>

        <p><b>{{ review.rating }}/10</b></p>
      </div>
    </div>
    
    <h3 class="pt-4 fw-bold">Like Reviews</h3>
    <p>제목 또는 작성자를 클릭하면 해당 정보로 이동합니다.</p>
    <div class="profile-detail">
      <div v-for="(likeReview,idx) in profile.like_reviews" :key="'D'+idx" class="my-2 card col-3 mx-5 card-css">
        <h5 class="mt-2">{{ idx+1 }}. 
          <b><router-link :to="{ name: 'ReviewDetail',
          params: { movieId: likeReview.movie.id, reviewId: likeReview.id }}"
          class="text-decoration-none text-dark">
          {{ likeReview.title }}</router-link>
          </b></h5>
          <a :href="`./${likeReview.user.username}`"
          class="nav-link active text-decoration-none text-primary">
          @{{ likeReview.user.username }}</a>
        <!-- <router-link :to="{ name: 'Profile', params: { username:likeReview.user.username } }"
        class="fw-bold nav-link active text-decoration-none text-success">
          @{{ likeReview.user.username }}</router-link> -->
      </div>
    </div>

    <h3 class="pt-4 fw-bold">Like Movies</h3>
    <p>이미지를 클릭하면 해당 영화 정보로 이동합니다.</p>
    <carousel v-if="profile.like_movies.length > 0" :nav="false" :items="5" class="mx-3 profile-detail">
      <div v-for="(movie, idx) in profile.like_movies" :key="idx" class='card'>
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top">
        </router-link>
      </div>
    </carousel>
    <router-view></router-view>
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Profile',
  components: {
    carousel,
  },
  methods: {
    ...mapActions([
      'openModal',
    ]),
    ...mapActions('accountStore', [
      'getProfile',
      'followUser',
    ]),
    openReviewCreateModal: function () {
      this.openModal()
      this.modalData.profileUpdateModalStatus = true
    }
  },
  computed: {
    ...mapState([
      'modalData',
    ]),
    ...mapState('accountStore', [
      'profile',
      'isFollow',
      'isMyself',
    ]),
  },
  watch: {
    '$route.params.username': function() {
      console.log(this.$route.params.username)
      // this.getProfile(this.$route.params.username)
      this.$router.push({ name: 'Profile', params: { username: this.$route.params.username } })
    },
  },
  created: function () {
    this.getProfile(this.$route.params.username)
  },
}
</script>

<style scoped>
.material-icons.md-28 { font-size: 29px; }

.profile {
  background: rgba(250,250,250,0.9);
  text-align: center;
  padding: 20px;
  border-width: 5px;
  border-color: rgba(37,150,151,0.7);
  border-style: solid;
}
.profile-detail{
  padding: 20px;
  border-width: 1.5px;
  border-style: solid;
  border-color: rgba(37,150,151,0.5);
}
.card-css {
  background-color: rgba(188,188,188,0.4);
  border-width: 1.5px;
  border-style: solid;
  border-color: rgba(37,150,151,0.5);
}
</style>