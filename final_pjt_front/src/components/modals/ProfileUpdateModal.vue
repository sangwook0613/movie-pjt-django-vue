<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title fw-bold fs-4">소개글 수정</h4>
            <div class="close" @click="[openModal(), modalData.profileUpdateModalStatus = false]">
              <i class="fas fa-times 5x fs-3 my-3 me-3"></i>
            </div>
          </div>
          <div class="modal-body">
            <div class="form-group pt-2">
              <label class="fw-bold fs-6 pb-2" for="profileUpdateIntroduction">소개글을 입력해주세요.</label>
              <textarea cols="20" rows="5" v-model.trim="profileUpdateData.introduction" class="form-control"></textarea>
            </div>
            <div class="d-flex justify-content-end mt-3">
              <div
                @click="[updateProfile(profileUpdateData), openModal(), modalData.profileUpdateModalStatus = false]"
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
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ProfileUpdateModal',
  data: function () {
    return {
      profileUpdateData: {
        introduction: '',
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
    ...mapActions('accountStore', [
      'updateProfile',
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
  width: 120px;
}
</style>