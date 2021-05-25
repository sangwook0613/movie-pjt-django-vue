<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">소개글 수정</h4>
            <button type="button" class="close" @click="[openModal(), modalData.profileUpdateModalStatus = false]"><span aria-hidden="true">&times;</span></button>
          </div>
          <div class="modal-body">
            <div class="form-group pt-2">
              <!-- <label for="profileUpdateIntroduction">소개글 작성</label> -->
              <textarea cols="20" rows="5" v-model.trim="profileUpdateData.introduction" class="form-control"></textarea>
              <!-- <input type="text" class="form-control" v-model.trim="profileUpdateData.introduction" required> -->
            </div>
            <button
              @click="[updateProfile(profileUpdateData), openModal(), modalData.profileUpdateModalStatus = false]"
              class="btn btn-primary mt-3"
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
  margin-top: 50px;
}
</style>