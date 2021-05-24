<template>
  <div>
    <div class="card" >
      <div class="d-flex">
        <div class="p-3">{{ comment.user }}</div>
        <div class="p-3">{{ comment.content }}</div>
        <button
          v-if="comment.user === jwtUserId"
          class="btn btn-danger"
          @click="deleteComment(commentInfo)"
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