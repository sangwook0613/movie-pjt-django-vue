<template>
  <div class="profile">
    <br>
      <div class="mx-3 mt-2">
        <div class="text-dark fw-bold d-flex justify-content-end"><h2>@  {{ profile.username }}</h2></div>
        <h4 class="d-flex justify-content-end">{{ profile.introduction }}</h4>
        <div class="d-flex justify-content-end">
          <span class="fw-bold mx-1 text-secondary">{{ profile.followings.length }}</span>
          <span class="text-secondary me-1">팔로우 중</span>
          <span class="fw-bold mx-1 text-secondary">{{ profile.followers.length }}</span>
          <span class="text-secondary">팔로워</span>
        </div>

      <div v-if="isMyself" class="d-flex justify-content-end">
        <span v-if="isFollow">
          <button @click="followUser($route.params.username)" class="mt-3 btn btn-danger text-white">팔로우 취소</button>
        </span>
        <span v-else>
          <button @click="followUser($route.params.username)" class="mt-3 btn btn-primary">팔로우</button>
        </span>
      </div>
      <div v-else class="d-flex justify-content-end">
        <button @click="followUser($route.params.username)" class="mt-3 btn btn-primary">프로필 수정</button>
      </div>
    </div>
    <br><hr>
    <h3 class="my-4 fw-bold">Post Reviews</h3>
    <div v-for="(review,idx) in profile.reviews" :key="'B'+idx" class="mt-3 card bg-white mx-5">
      <p class="mt-3"><b>{{ idx+1 }}. 
      <router-link
      :to="{ name: 'ReviewDetail',
      params: { movieId: review.movie.id, reviewId: review.id }}"
      class="text-decoration-none text-dark">
      {{ review.title }}</router-link>
      </b></p>
      <p><b>{{ review.movie.title }}</b></p>
      <p>평점: <b>{{ review.rating }}/10</b></p>
    </div>
    <hr>
    
    <h3 class="my-4 fw-bold">Like Reviews</h3>

    <div v-for="(likeReview,idx) in profile.like_reviews" :key="'D'+idx" class="my-2 card bg-light mx-5">
      <h5 class="mt-2">{{ idx+1 }}. 
        <b>
        <router-link :to="{ name: 'ReviewDetail',
        params: { movieId: likeReview.movie.id, reviewId: likeReview.id }}"
        class="text-decoration-none text-dark">
        {{ likeReview.title }}</router-link>
        </b></h5>
        <a :href="`http://localhost:8080/profile/${likeReview.user.username}`"
        class="fw-bold nav-link active text-decoration-none text-success">
        @{{ likeReview.user.username }}</a>
      <!-- <router-link :to="{ name: 'Profile', params: { username:likeReview.user.username } }"
      class="fw-bold nav-link active text-decoration-none text-success">
        @{{ likeReview.user.username }}</router-link> -->
        
    </div>
    <hr>
    <h3 class="my-4 fw-bold">Like Movies</h3>
    <carousel v-if="profile.like_movies.length > 0" :nav="false" :items="5" class="mx-3">
      <div v-for="(movie, idx) in profile.like_movies" :key="idx" class='card'>
        <router-link :to="{ name: 'ProfileMovieDetail', params: { movieId: movie.id }}">
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
    ...mapActions('accountStore', [
      'getProfile',
      'followUser',
    ]),
  },
  computed: {
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
.profile {
  background: beige;
  text-align: center;
  margin: 3px;
  border-width: 5px;
  border-style: solid;
}
</style>