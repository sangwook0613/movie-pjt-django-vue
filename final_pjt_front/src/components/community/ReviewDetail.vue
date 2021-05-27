<template>
  <div class="row text-white review-detail">
    <div class="d-flex align-items-center justify-content-center">
      <router-link :to="{ name: 'MovieDetail', params: { movieId: reviewDetail.movie.id } }"
        class="text-decoration-none pb-2 fw-bold text-light pe-5"
      >
        <i class="fas fa-film pe-1"></i>
        {{ reviewDetail.movie.title }} 정보 보기
      </router-link>
      <router-link :to="{ name: 'MovieReviews', params: { movieId: reviewDetail.movie.id } }"
        class="text-decoration-none pb-2 fw-bold text-light ps-5"
      >
        <i class="fas fa-list pe-1"></i>
        {{ reviewDetail.movie.title }} 전체 리뷰
      </router-link>
    </div>
    <div class="card col-6 offset-3 review-card">
      <div class="d-flex flex-column align-items-start">
        <!-- {{reviewDetail}} -->
        <div class="d-flex justify-content-start mt-3">
          <img
            alt="profile-image"
            class="profile-image"
            src="https://static.overlay-tech.com/assets/eba0d02d-858f-4cab-9e4e-d897a0d4800d.png"
          />
          <div>
            <router-link :to="{ name: 'Profile', params: { username: reviewDetail.user.username } }"
              class="text-decoration-none"
            >
              <p class="username fw-bold fs-6">{{ reviewDetail.user.username }}</p>
            </router-link>
            <p class="rating">평점 {{ reviewDetail.rating }}</p>
          </div>
        </div>
        <div class="mb-3">
          <div class="review-date mb-3">
            <span><span class="fw-bold pe-2">작성일</span>{{ reviewDetail.created_at|moment("from", "now") }}</span>
            <span class="ps-3"><span class="fw-bold pe-2">수정일</span>{{ reviewDetail.updated_at|moment("from", "now") }}</span>
          </div>
          <div class="title fw-bold fs-5">
            {{ reviewDetail.title }}
          </div>
          <div class="content fs-6" style="word-break:break-all; word-wrap:break-word;">
            {{ reviewDetail.content }}
          </div>
        </div>
        <div class="d-flex align-items-center">
          <div :id="`likeCount-${reviewDetail.id}`" class="" @click="updateReviewLikes(reviewDetail, reviewDetail.user.id)">
            <i class="fas fa-heart fa-lg me-1" :style="{ color: checkUserIncludeInReviewLikes(reviewDetail.likes)}"></i>
            <span class="ps-2 rating">{{ reviewDetail.likes.length }}</span>
          </div>
          <div class="comment-count d-flex align-items-center">
            <img
              alt=""
              class="vector"
              src="https://static.overlay-tech.com/assets/6d5c72bb-4b13-4f8a-99e7-fc4b3a1c9049.svg"
            />
            <div class="ps-2 rating">{{ reviewDetail.comment_count }}</div>
          </div>
        </div>
      </div>
      <div v-if="reviewDetail.user.id === jwtUserId" class="d-flex justify-content-end">
        <input
          type="button"
          class="fw-bold btn white-btn rounded-pill mt-3 me-3"
          @click="openUpdateReviewModal"
          value="수정"
        >
        <button
          class="fw-bold btn rounded-pill mt-3 black-btn text-light"
          @click="deleteReview(reviewDetail.id)">삭제</button>
      </div>
    </div>
    <div class="comment-create-card col-6 offset-3 mt-3 py-3">
      <div class="fw-bold pb-4">댓글 남기기</div>
      <div>
        <textarea v-model.trim="commentInput.inputText" @keypress.enter="[createComment(commentInput), resetCommentInput()]" class="text-light">
        </textarea>
        <button class="fw-bold btn white-btn rounded-pill mt-3" @click="[createComment(commentInput), resetCommentInput()]">작성</button>
      </div>
    </div>
    <div class="col-6 offset-3 mt-3 mb-4">
      <div v-if="reviewDetail.comment_count !== 0">
        <div v-for="(comment, idx) in reverseComments" :key="idx">
          <CommentCard :comment="comment" :movieId="reviewDetail.id" class="mt-3 comment-card"/>
        </div>
      </div>
      <div v-else>
        <h3 class="text-center">댓글이 없습니다.</h3>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import CommentCard from '@/components/community/CommentCard'
import _ from 'lodash'
import axios from 'axios'
import SERVER from '@/api/server.js'

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
      'config',
      'jwtUserId',
    ]),
    reverseComments: function () {
      return _.reverse(this.reviewDetail.review_comments)
    }
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
    updateReviewLikes: function (review, user_id) {
      const headers = this.config
      if (user_id !== this.jwtUserId) {
        axios({
          url: SERVER.URL + SERVER.ROUTES.review + `${review.id}/like/`,
          method: 'post',
          headers,
        })
        .then(() => {
          const likeCountImage = document.querySelector(`#likeCount-${review.id} > i`)
          const likeCountNum = document.querySelector(`#likeCount-${review.id} > span`)
          if (likeCountImage.style.color === '' || likeCountImage.style.color === 'white' ) {
            likeCountImage.style.color = 'crimson'
            likeCountNum.innerText++
          } else {
            likeCountImage.style.color = 'white'
            likeCountNum.innerText--
          }
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        alert('본인이 작성한 리뷰는 좋아요를 누를 수 없습니다.')
      }
    },
    checkUserIncludeInReviewLikes: function (review_likes) {
      if (_.includes(review_likes, this.jwtUserId)) {
        return 'crimson'
      }
      return 'white'
    },
    openUpdateReviewModal: function () {
      this.openModal()
      this.modalData.reviewUpdateModalStatus = true
    },
    resetCommentInput: function () {
      this.commentInput.inputText = ''
    },
  },
  created: function () {
    this.getReviewDetail(this.$route.params.reviewId)
  },
  beforeDestroy: function () {
    // document.body.style.backgroundImage = "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.squarespace-cdn.com/content/v1/5a173f16ace86416b07c25f1/1513939530902-DILPHAAJ9F0DI627449M/ke17ZwdGBToddI8pDm48kK0QKSDttGV1ap9dyeIseHF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0mxU0godxi02JM9uVemPLqw3ZQRv6tY2V6nZIOWGhJ3qaH6uCpMgOc4rPl-G2eiFCQ/fantasy+album+cover6+-+in+wide+format.jpg?format=1500w')";
    document.body.style.backgroundImage = ""
    document.body.style.backgroundColor = "#141414"

  }
}
</script>

<style>
.review-card {
  padding: 20px;
  border-radius: 8px;
  background-color: #292828;
}

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

textarea {
  width: 100%;
  height: 100px;
  padding: 12px 20px;
  box-sizing: border-box;
  border-radius: 4px;
  border-color: #434242;
  background-color: #434242;
  resize: none;
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

.review-date {
  font-size: 12px;
}
</style>