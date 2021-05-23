<template>
  <div class="container row">
    {{reviewDetail}}
    <div class="card col-6">
      <div class="card-body">
        <h3 class="card-title fw-bold">{{ reviewDetail.title }}</h3>
        <div class="card-text fs-5">{{ reviewDetail.content }}</div>
        <div>평점: {{ reviewDetail.rating }}</div>
        <div>작성일: {{ reviewDetail.created_at }}</div>
      </div>
      <div class="row">
        <div class="col-1"></div>
        <router-link
          :to="{ name: 'ReviewForm', params: { movieId: reviewDetail.movie.id }}"
          :reviewId=reviewDetail.id
          class="text-decoration-none text-dark btn btn-primary col-4 text-white"
        >
          리뷰 수정
        </router-link>
        <div class="col-2"></div>
        <button
          class="col-4 btn btn-danger"
          @click="deleteReview(reviewDetail.id)">리뷰 삭제</button>
        <div class="col-1"></div>
      </div>
    </div>
    <div class="poster-card col-6">
      <img :src="reviewDetail.movie.poster_path" alt="poster-image" style="height: 400px;">
    </div>
    <div class="comment-card mt-3">
      <h3 class="fw-bold">댓글</h3>
      <CommentCard/>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import CommentCard from '@/components/community/CommentCard'

export default {
  name: 'ReviewDetail',
  components: {
    CommentCard,
  },
  computed: {
    ...mapState('communityStore', [
      'reviewDetail',
    ])
  },
  methods: {
    ...mapActions('communityStore', [
      'getReviewDetail',
      'deleteReview',
    ])
  },
  created: function () {
    this.getReviewDetail(this.$route.params.reviewId)
  }
}
</script>

<style>
.poster-card .comment-card {
  /* padding-top: 20px; */
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  /* background-color: #fff; */
  background-clip: border-box;
  /* border: 1px solid rgba(0,0,0,.125); */
  border-radius: .25rem;
}
</style>