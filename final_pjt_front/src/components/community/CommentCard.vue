<template>
  <div>
    <div class="card" v-for="(comment, idx) in comments" :key="idx">
      <div class="d-flex">
        <div class="p-3">{{ comment.user }}</div>
        <div class="p-3">{{ comment.content }}</div>
        <button v-if="comment.user === jwtUserId" class="btn btn-danger">삭제</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'CommentCard',
  props: {
    comments: {
      type: Array,
    }
  },
  computed: {
    ...mapGetters([
      'jwtUserId',
    ])
  }
}
</script>

<style>

</style>