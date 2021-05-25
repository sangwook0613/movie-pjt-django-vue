<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-dialog modal-xl">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">리뷰 수정</h4>
            <button type="button" class="close" @click="[openModal(), modalData.reviewUpdateModalStatus = false]"><span aria-hidden="true">&times;</span></button>
          </div>
          <div class="modal-body">
            <div class="form-group pt-2">
              <label for="reviewUpdateTitle">제목: </label>      
              <input type="text" class="form-control" v-model.trim="reviewUpdateData.title" required>
            </div>
            <div class="form-group pt-2">
              <label for="reviewUpdateContent">내용: </label>
              <textarea cols="30" rows="10" class="form-control" v-model.trim="reviewUpdateData.content" required></textarea>
              <!-- <input type="text" class="form-control" v-model.trim="reviewUpdateData.content" required> -->
            </div>
            <div class="form-group pt-3">
              <label for="rating-10">평점</label>
              <b-form-rating show-value show-value-max id="rating-10" v-model="reviewUpdateData.rating" stars="10"></b-form-rating>
              <!-- <p class="mt-2">: {{ reviewUpdateData.rating }}</p> -->
              <!-- <input type='number' v-model="reviewUpdateData.rating" min='1' max='10' step='1' required> -->
            </div>
            <br />
            <button
              @click="[updateReview(reviewUpdateData), openModal(), modalData.reviewUpdateModalStatus = false]"
              class="btn btn-primary"
            >수정 완료</button>
            <!-- <div align="center">
              <input type="button" class="btn btn-success btn-xs" v-model="actionButton" @click="submitData" />
            </div> -->
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ReviewUpdateModal',
  data: function () {
    return {
      reviewUpdateData: {
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
      'updateReview',
    ])
  }
}
</script>

<style scoped>

.modal-mask {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  padding: 20px;
  margin-top: 50px;
}
</style>