<template>
  <div>
    <div class="card" >
      <div class="d-flex bd-highlight">
        <div class="p-2 bd-highlight">{{ comment.user.username }}:</div>
        <div class="p-2 bd-highlight">{{ comment.content }}</div>
        <div class="p-2 bd-highlight">{{ comment.id }}</div>
          <button
            v-if="comment.user.id === jwtUserId"
            class="btn btn-danger btn-sm ms-auto p-2 bd-highlight"
            @click="[deleteComment(commentInfo), commentInfo.commentId = comment.id+1]"
          >삭제</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentCard',
  props: {
    comment: {
      type: Object,
    },
    movieId: {
      type: Number,
    },
  },
  data: function () {
    return {
      commentInfo : {
        commentId: this.comment.id,
        reviewId: this.comment.review,
        movieId: this.movieId,
      }
    }
  },
  computed: {
    ...mapGetters([
      'jwtUserId',
    ])
  },
  methods: {
    ...mapActions('communityStore', [
      'deleteComment',
    ]),
    getReviewId: function (inputId) {
      this.reviewId = inputId
    }
  }
}
</script>

<style>

</style>