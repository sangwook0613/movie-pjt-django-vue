<template>
  <div>
    <div class="card" v-for="(comment, idx) in comments" :key="idx">
      {{ comment }}
    </div>
    <h1>hihi</h1>
  </div>
</template>

<script>
export default {
  name: 'CommentCard',
}
</script>

<style>

</style>