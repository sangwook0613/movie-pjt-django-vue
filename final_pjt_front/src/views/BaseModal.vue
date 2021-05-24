<template>
  <div>
    <div v-if="modalData.reviewUpdateModalStatus">
      <ReviewUpdateModal/>
    </div>
    <!-- <div v-if="modalData.reviewUpdateModalStatus">
      <ReviewUpdateModal/>
    </div> -->

  </div>
  <!-- <transition name="modal">
    <div class="modal-mask">
      <div class="modal-dialog modal-xl">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">ModalTitle</h4>
            <button type="button" class="close" @click="openModal"><span aria-hidden="true">&times;</span></button>
          </div>
          <div class="modal-body">
            <div class="form-group">
              <label>Enter First Name</label>
              <input type="text" class="form-control" v-model="modalData.first_name" />
            </div>
            <div class="form-group">
              <label>Enter Last Name</label>
              <input type="text" class="form-control" v-model="modalData.last_name" />
            </div>
            <br />
            <div align="center">
              <input type="hidden" v-model="hiddenId" />
              <input type="button" class="btn btn-success btn-xs" v-model="actionButton" @click="submitData" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition> -->
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ReviewUpdateModal from '@/components/modals/ReviewUpdateModal'

export default {
  name: 'BaseModal',
  components: {
    ReviewUpdateModal,
  },
  computed: {
    ...mapState([
      'modalData',
    ])
  },
  methods: {
    ...mapActions([
      'openModal',
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