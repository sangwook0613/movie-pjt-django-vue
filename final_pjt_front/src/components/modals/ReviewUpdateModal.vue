<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-dialog modal-xl">
        <div class="modal-content">
          <div class="modal-header fw-bold fs-4">
            <h4 class="modal-title">리뷰 수정</h4>
            <div class="close" @click="[openModal(), modalData.reviewUpdateModalStatus = false]">
              <i class="fas fa-times 5x fs-3 my-3 me-3"></i>
            </div>
          </div>
          <div class="modal-body">
            <div class="form-group pt-2">
              <label class="fw-bold fs-6" for="reviewUpdateTitle">제목</label>      
              <input type="text" class="form-control" v-model.trim="reviewUpdateData.title" required>
            </div>
            <div class="form-group pt-2">
              <label class="fw-bold fs-6" for="reviewUpdateContent">내용</label>
              <textarea cols="30" rows="10" class="form-control" v-model.trim="reviewUpdateData.content" required></textarea>
            </div>
            <div class="form-group pt-2">
              <label class="fw-bold fs-6" for="rating-10">평점</label>
              <b-form-rating show-value show-value-max id="rating-10" v-model="reviewUpdateData.rating" stars="10"></b-form-rating>
            </div>
            <br />
            <div class="d-flex justify-content-end">
              <div
                @click="[updateReview(reviewUpdateData), openModal(), modalData.reviewUpdateModalStatus = false]"
                class="btn rounded-pill custom-btn text-white fw-bold me-2"
              >
                수정 완료
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState, mapActions, } from 'vuex'

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
    ]),
    ...mapState('communityStore', [
      'reviewDetail'
    ]),

  },
  methods: {
    ...mapActions([
      'openModal',
    ]),
    ...mapActions('communityStore', [
      'updateReview',
    ])
  },
  // 생성될 때 data값 가져온다.
  created: function () {
    this.reviewUpdateData.title = this.reviewDetail.title
    this.reviewUpdateData.content = this.reviewDetail.content
    this.reviewUpdateData.rating = this.reviewDetail.rating
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
  width: 120px;
}
</style>