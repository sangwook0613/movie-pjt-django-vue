<template>
  <div>
    <hr>
      <div class="mx-3 mt-2">
        <div class="text-dark fw-bold d-flex justify-content-end"><h2>@  {{ profile.username }}</h2></div>
        <h3 class="d-flex justify-content-end">{{ profile.introduction }}</h3>
        <div class="d-flex justify-content-end">
          <span class="fw-bold mx-1 text-secondary fs-5">{{ profile.followings_count }}</span>
          <span class="text-secondary me-1 fs-5">팔로우 중</span>
          <span class="fw-bold mx-1 text-secondary fs-5">{{ profile.followers_count }}</span>
          <span class="text-secondary fs-5">팔로워</span>
        </div>
          <!-- <div v-for="(following, idx) in profile.followings" :key='idx'>
            {{ following.username }}</div>
      <div v-for="(follower, idx) in profile.followers" 
      :key="'A'+idx">
        {{ follower.username }}
        </div> -->
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


    <hr>
    <h3>작성한 리뷰</h3>
    <p v-for="(review,idx) in profile.reviews" :key="'B'+idx">
      제목: {{ review.title }}<br>
      내용: {{ review.content }}<br>
      평점: {{ review.rating }}</p>
    <hr>
    <h3>작성한 댓글</h3>
    <p v-for="(comment,idx) in profile.comments" :key="'C'+idx">
      {{ idx+1 }}.{{ comment.content }}</p>
    <hr>
    <h3>Like Reviews</h3>
    <p v-for="(likeReview,idx) in profile.like_reviews" :key="'D'+idx">
      {{ idx+1 }}.{{ likeReview.content }}</p>
    <hr>
    <h3>Like Movies</h3>
    <carousel v-if="profile.like_movies.length > 0" :nav="false" :items="5">
      <div v-for="(movie, idx) in profile.like_movies" :key="idx" class='card'>
        <router-link :to="{ name: 'ProfileMovieDetail', params: { movieId: movie.id }}">
          <img :src="movie.poster_path" alt="movie-poster" class="card-img-top">
        </router-link>
      </div>
    </carousel>
    <router-view></router-view>
    <!-- <p v-for="(likeMovie,idx) in profile.like_movies" :key="'E'+idx">
      {{ idx+1 }}.{{ likeMovie.title }}</p>
    <hr> -->
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
      this.getProfile(this.$route.params.username)
    },
  },
  created: function () {
    this.getProfile(this.$route.params.username)
  }
}
</script>

<style>

</style>