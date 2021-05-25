<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-dialog modal-xl">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">리뷰 작성</h4>
            <button type="button" class="close" @click="[openModal(), modalData.reviewCreateModalStatus = false]"><span aria-hidden="true">&times;</span></button>
          </div>
          <div class="modal-body">
            <div class="form-group pt-2">
              <label for="reviewCreateTitle">제목: </label>      
              <input type="text" class="form-control" v-model.trim="reviewCreateData.title" required>
            </div>
            <div class="form-group pt-2">
              <label for="reviewCreateContent">내용: </label>
              <input type="text" class="form-control" v-model.trim="reviewCreateData.content" required>
            </div>
            <div class="form-group pt-3">
              <label for="reviewCreateRating">평점: </label>
              <input type='number' v-model="reviewCreateData.rating" min='1' max='10' step='1' required>
            </div>
            <br />
            <button
              @click="[createReview(reviewCreateData), openModal(), modalData.reviewCreateModalStatus = false]"
              class="btn btn-primary"
            >작성</button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ReviewCreateModal',
  data: function () {
    return {
      reviewCreateData: {
        title: '',
        content: '',
        rating: '',
      }
    }
  },
  computed: {
    ...mapState([
      'modalStatus',
      'modalData',
    ])
  },
  methods: {
    ...mapActions([
      'openModal',
    ]),
    ...mapActions('communityStore', [
      'createReview',
    ])
  }
}
</script>

<style>

.modal-mask {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  padding: 20px;
  margin-top: 50px;
}
</style>