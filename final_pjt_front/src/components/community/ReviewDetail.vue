<template>
  <div>
    <div>{{ reviewDetail.content }}</div>
    <div>{{ reviewDetail.rating }}</div>
    {{ reviewDetail }}
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ReviewDetail',
  computed: {
    ...mapState('communityStore', [
      'reviewDetail',
    ])
  },
  methods: {
    ...mapActions('communityStore', [
      'getReviewDetail',
    ])
  },
  created: function () {
    this.getReviewDetail(this.$route.params.reviewId)
  }
}
</script>

<style>

</style>