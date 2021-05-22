<template>
  <div class="container-fuild overflow-hidden">
    <h1 class="mb-5">모든 리뷰!</h1>
    <div class="row g-5">
      <div class="col-12 col-lg-6" v-for="(review, idx) in reviews" :key="idx">
        <ReviewCard :review="review"/>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewCard from '@/components/community/ReviewCard'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Community',
  components: {
    ReviewCard,
  },
  computed: {
    ...mapState('communityStore', [
      'reviews',
    ]),
  },
  methods: {
    ...mapActions('communityStore', [
      'getReview',
    ]),
  },
  created: function () {
    this.getReview()
  },
}
</script>

<style>
</style>