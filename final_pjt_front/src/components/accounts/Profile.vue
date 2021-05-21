<template>
  <div>
    <hr>
    <h1>{{profile.username}}'s 프로필</h1>
    <hr>
    <h2>Introduction</h2>
    <h3>{{ profile.introduction }}</h3>
    <hr>
    <h3>팔로잉: {{ profile.followings_count }}명<br>
      <span v-for="(following, idx) in profile.followings" 
      :key='idx'>
        {{ following.username }}</span></h3>
    <h3>팔로워: {{ profile.followers_count}}명<br>
      <span v-for="(follower, idx) in profile.followers" 
      :key="'A'+idx">
        {{ follower.username }}</span></h3>
    <div v-if="isMyself">
      <p v-if="isFollow">
        <button @click="followUser($route.params.username)" class="follow-btn">언팔로우</button>
      </p>
      <p v-else>
        <button @click="followUser($route.params.username)" class="follow-btn">팔로우</button>
      </p>
    </div>

    <hr>
    <h3>작성한 리뷰</h3>
    <p v-for="(review,idx) in profile.reviews" :key="'B'+idx">
      제목: {{ review.title }}<br>
      내용: {{ review.content }}</p>
    <hr>
    <h3>작성한 댓글</h3>
    <p v-for="(comment,idx) in profile.comments" :key="'C'+idx">
      {{ idx+1 }}.{{ comment.content }}</p>
    <hr>
    <h3>좋아요 한 리뷰</h3>
    <p v-for="(likeReview,idx) in profile.like_reviews" :key="'D'+idx">
      {{ idx+1 }}.{{ likeReview.content }}</p>
    <hr>
    <h3>좋아하는 영화</h3>
    <p v-for="(likeMovie,idx) in profile.like_movies" :key="'E'+idx">
      {{ idx+1 }}.{{ likeMovie.title }}</p>
    <hr>
    <h3>싫어하는 영화</h3>
    <p v-for="(hateMovie,idx) in profile.hate_movies" :key="'F'+idx">
      {{ idx+1 }}.{{ hateMovie.title }}</p>
    <hr>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Profile',
  methods: {
    ...mapActions('accountStore', [
      'getProfile',
      'followUser',
    ])
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