<template>
  <div class="container row text-white review-detail">
    <div class="card col-6 review-card">
      <div class="card-body">
        <h3 class="card-title fw-bold">{{ reviewDetail.title }}</h3>
        <div class="card-text fs-5">{{ reviewDetail.content }}</div>
        <div>작성자: {{ reviewDetail.user.username }}</div>
        <!-- 별로 바꾸기 -->
        <div>평점: {{ reviewDetail.rating }}</div>
        <span>작성일: {{ reviewDetail.created_at|moment("from", "now") }} | </span>
        <span>수정일: {{ reviewDetail.updated_at|moment("from", "now") }}</span>
      </div>
      <div class="row" v-if="reviewDetail.user.id === jwtUserId">
        <div class="col-2"></div>
        <input
          type="button"
          class="text-decoration-none btn btn-primary col-3 btn-xs"
          @click="openUpdateReviewModal"
          value="수정"
        >
        <div class="col-2"></div>
        <button
          class="col-3 btn btn-danger"
          @click="deleteReview(reviewDetail.id)">삭제</button>
        <div class="col-1"></div>
      </div>
    </div>
    <!-- <div class="poster-card col-6">
      <img :src="reviewDetail.movie.poster_path" alt="poster-image" style="height: 400px;">
    </div> -->
    <!-- {{reviewDetail}} -->
    <div class="comment-card col-12 mt-3">
      <div>
        <input type="text" placeholder="댓글 입력" v-model.trim="commentInput.inputText" @keypress.enter="[createComment(commentInput), resetCommentInput()]">
        <button class="btn btn-info" @click="[createComment(commentInput), resetCommentInput()]">작성</button>
      </div>
      {{ reviewDetail.review_comments.length }}
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
    ...mapState([
      'modalData',
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
    ...mapActions([
      'openModal',
    ]),
    resetCommentInput: function () {
      this.commentInput.inputText = ''
    },
    openUpdateReviewModal: function () {
      this.openModal()
      this.modalData.reviewUpdateModalStatus = true
    }
  },
  created: function () {
    this.getReviewDetail(this.$route.params.reviewId)
  },
  beforeDestroy: function () {
    // document.body.style.backgroundImage = "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.squarespace-cdn.com/content/v1/5a173f16ace86416b07c25f1/1513939530902-DILPHAAJ9F0DI627449M/ke17ZwdGBToddI8pDm48kK0QKSDttGV1ap9dyeIseHF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0mxU0godxi02JM9uVemPLqw3ZQRv6tY2V6nZIOWGhJ3qaH6uCpMgOc4rPl-G2eiFCQ/fantasy+album+cover6+-+in+wide+format.jpg?format=1500w')";
    document.body.style.backgroundImage = ""
    document.body.style.backgroundColor = "rgba(0,0,0,0.9)"

  }
}
</script>

<style>
.review-card {
  background-color: inherit;
  border-color: white;
  border-width: 2.5px;
  border-style: solid;
}

.review-detail{
  margin-left: 50px;
  margin-top: 50px;
  padding-left: 50px;
  padding-top:50px;
  border-width: 2.5px;
  border-color: transparent;
  border-style: solid;
}

.poster-card .comment-card {
  /* padding-top: 20px; */
  /* position: relative; */
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  /* background-color: inherit; */
  background-clip: border-box;
  /* border: 1px solid rgba(0,0,0,.125); */
  border-radius: .25rem;
}

.card {
  position: inherit;
}


</style>