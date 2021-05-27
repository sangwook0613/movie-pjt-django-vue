<template>
  <div class="d-flex flex-column align-items-start">
    <div class="d-flex justify-content-between mt-3">
      <div class="d-flex justify-content-between">
        <img
          alt="profile-image"
          class="profile-image"
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
    <div class="content fs-6 pt-2" style="word-break:break-all; word-wrap:break-word;">
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
.comment-card {
  padding: 20px;
  border-radius: 8px;
  background-color: #292828;
}

.comment-create-card {
  padding: 20px;
  border-radius: 8px;
  background-color: #292828;
}

.card {
  position: inherit;
}

.profile-image {
  width: 48px;
  height: 48px;
  margin-right: 15px;
  border-radius: 50%;
}

.username {
  color: #FFFFFF;
  margin-bottom: 4px;
}

.rating {
  color: #FFFFFF;
}

.title {
  color: #FFFFFF;
  margin-bottom: 14px;
}

.content {
  color: #FFFFFF;
  margin-bottom: 14px;
}

.vector {
  width: 50%;
  height: 50%;
}
.comment-count {
  margin-left: 10px;
  /* padding: 2px; */
}

.custom-btn {
  background-color: #00cecb;
}

.black-btn {
  background-color: #292828;
  border-color: #FFFFFF;
  width: 90px;
}

.white-btn {
  border-color: #292828;
  background-color: #FFFFFF;
  width: 90px;
}
</style>