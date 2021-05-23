<template>
  <div class="container">
    <div class="row card-body" v-for="(review, idx) in reviews" :key="idx">
      <div class="col-1"></div>
      <router-link :to="{ name: 'ReviewDetail', params: { reviewId: review.id } }" class="col-10 row">
        <div class="review-card" >
          <span class="fw-bold fs-4 pe-2">{{ review.title }}</span>
          <span :class="makeBadge(review.rating)" style="width: 30px">{{ review.rating }}</span>
          <!-- <span>{{ review.created_at }}</span> -->
        </div>
      </router-link>
      <div class="col-1"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieReviews',
  props: {
    reviews: {
      type: Array,
    }
  },
  methods: {
    makeBadge: function (num) {
      if (num >= 8) {
        return 'badge rounded-pill bg-primary'
      } else if (num >= 4) {
        return 'badge rounded-pill bg-warning'
      } else {
        return 'badge rounded-pill bg-danger'
      }
    },
  }
}
</script>

<style>

</style>