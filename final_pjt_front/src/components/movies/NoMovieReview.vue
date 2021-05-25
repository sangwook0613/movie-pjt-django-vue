<template>
  <div class="card d-flex flex-column align-items-center">
    <!-- {{ movieDetailInfo }} -->
    <!-- {{movieDetailInfo.movie_reviews}} -->
    <div class="my-3 fs-4 fw-bold">{{ movieDetailInfo.title }} 리뷰</div>
    <div v-if="movieDetailInfo.movie_reviews.length === 0" class="d-flex flex-column align-items-center">
      <p><b>첫 번째 리뷰를 남겨주세요!</b></p>
      <input
        type="button"
        class="text-decoration-none text-dark btn btn-primary text-white btn-xs"
        @click="openReviewCreateModal"
        value="리뷰 작성하기"
      >
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'MoreMovieDetail',
  props: {
    movieDetailInfo: {
      type: [Object, Array],
    }
  },
  computed: {
    ...mapState([
      'modalData',
    ]),
  },
  methods: {
    ...mapActions([
      'openModal',
    ]),
    ...mapActions('communityStore', [
      'setFormType',
    ]),
    openReviewCreateModal: function () {
      this.openModal()
      this.modalData.reviewCreateModalStatus = true
    }
  }
}
</script>

<style>
</style>