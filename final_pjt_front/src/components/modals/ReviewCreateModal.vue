<template>
<!-- 원본 -->
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-dialog modal-xl">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title fw-bold fs-4">리뷰 작성</h4>
            <div class="close" @click="[openModal(), modalData.reviewCreateModalStatus = false]">
              <i class="fas fa-times 5x fs-3 my-3 me-3"></i>
            </div>
          </div>
          <div class="modal-body">
            <div class="form-group pt-2">
              <label class="fw-bold fs-6" for="reviewCreateTitle">제목</label>      
              <input type="text" class="form-control" v-model.trim="reviewCreateData.title" required>
            </div>
            <div class="form-group pt-2">
              <label class="fw-bold fs-6" for="reviewCreateContent">내용</label>
              <textarea cols="30" rows="10" class="form-control" v-model.trim="reviewCreateData.content" required></textarea>
            </div>
            <label class="fw-bold fs-6 pt-2" for="rating-10">평점</label>
            <b-form-rating show-value show-value-max id="rating-10" v-model="reviewCreateData.rating" stars="10"></b-form-rating>
            <br />
            <div class="d-flex justify-content-end">
              <div
                @click="[createReview(reviewCreateData), openModal(), modalData.reviewCreateModalStatus = false]"
                class="btn rounded-pill custom-btn text-white fw-bold me-2"
              >
                작성
              </div>
            </div>
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
      value10: null,
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

<style scoped>
.modal-mask {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  padding: 20px;
  padding-top: 50px;
}

.custom-btn {
  background-color: #00cecb;
  width: 70px;
}
</style>