<template>
  <div>
    <div class="comment-form">
      <div>
        <label for="reviewContent">내용: </label>
        <input type="text" v-model.trim="reviewFormData.content" required>
      </div>
      <button @click="createReview(reviewFormData)">작성 완료</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommentForm',
}
</script>

<style>

</style>