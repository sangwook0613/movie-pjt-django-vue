<template>
  <div class="d-flex flex-column align-items-start">
    <div class="d-flex justify-content-between mt-3">
      <div class="d-flex justify-content-between">
        <img
          alt="profile-image"
          class="ellipse-2"
          src="https://static.overlay-tech.com/assets/eba0d02d-858f-4cab-9e4e-d897a0d4800d.png"
        />
        <div>
          <p class="username fw-bold fs-6">{{ comment.user.username }}</p>
          <div class="review-date mb-3">
            <span>{{ comment.created_at|moment("from", "now") }}</span>
          </div>
        </div>
      </div>
      <div 
        v-if="comment.user.id === jwtUserId"
        @click="[deleteComment(commentInfo), commentInfo.commentId = comment.id+1]"
      >
        <i class="fas fa-times 5x fs-6 ps-3 text-light"></i>
      </div>
    </div>
    <div class="content fs-6 pt-2">
      <div>{{ comment.content }}</div>
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