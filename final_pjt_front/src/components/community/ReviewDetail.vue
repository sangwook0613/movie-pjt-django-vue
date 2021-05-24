<template>
  <div class="container row">
    <div class="card col-6">
      <div class="card-body">
        <h3 class="card-title fw-bold">{{ reviewDetail.title }}</h3>
        <div class="card-text fs-5">{{ reviewDetail.content }}</div>
        <div>평점: {{ reviewDetail.rating }}</div>
        <div>작성일: {{ reviewDetail.created_at }}</div>
        <div>작성자: {{ reviewDetail.user }}</div>
      </div>
      <div class="row" v-if="reviewDetail.user === jwtUserId">
        <div class="col-1"></div>
        <router-link
          :to="{ name: 'ReviewForm', params: { movieId: reviewDetail.movie.id }}"
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
    <!-- {{reviewDetail}} -->
    <div class="comment-card col-12 mt-3">
      <h3 class="fw-bold">댓글</h3>
      <div>
        <input type="text" v-model.trim="commentInput.inputText" @keypress.enter="[createComment(commentInput), resetCommentInput()]">
        <button class="btn btn-info" @click="[createComment(commentInput), resetCommentInput()]">작성</button>
      </div>
      <div v-if="reviewDetail.comment_count !== 0">
        <div v-for="(comment, idx) in reviewDetail.review_comments" :key="idx" >
          <CommentCard :comment="comment" :movieId="reviewDetail.id"/>
        </div>
      </div>
      <div v-else>
        <h3 class="text-center">댓글이 없습니다.</h3>
      </div>
    </div>
    <!-- {{reviewDetail.id}}
    {{$route.params.reviewId}} -->
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import CommentCard from '@/components/community/CommentCard'

export default {
  name: 'ReviewDetail',
  components: {
    CommentCard,
  },
  data: function () {
    return {
      commentInput: {
        reviewId: this.$route.params.reviewId,
        inputText: '',
      },
    }
  },
  computed: {
    ...mapState('communityStore', [
      'reviewDetail',
    ]),
    ...mapGetters([
      'jwtUserId',
    ])
  },
  methods: {
    ...mapActions('communityStore', [
      'getReviewDetail',
      'deleteReview',
      'createComment',
    ]),
    resetCommentInput: function () {
      this.commentInput.inputText = ''
    }
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