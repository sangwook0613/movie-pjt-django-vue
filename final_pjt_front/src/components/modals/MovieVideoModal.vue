<template>
  <transition name="modal">
    <div class="modal-mask">
      <!-- style="width: 100%; height: 100%;" -->
      <div class="close text-white text-end" @click="openModal"><i class="fas fa-times 5x fs-3 my-3 me-5"></i></div>
      <div class="video-detail" v-if="selectedVideo">
        <div class="video-container d-flex justify-content-center">
          <iframe :src="videoURL" frameborder="0"></iframe>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

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
    ]),
    ...mapState('movieStore', [
      'selectedVideo',
    ]),
    ...mapGetters('movieStore', [
      'videoURL',
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
  background: rgba(0, 0, 0, 0.6);
  position: fixed;
  padding: 20px;
  padding-top: 40px;
  /* margin-top: 30px; */
}

/* .video-detail {
  width: 70%;
  padding-right: 1rem;
} */

.video-container {
  position: relative;
  padding-top: 56.25%;
}

.video-container > iframe {
  position: absolute;
  top: 0;
  width: 70%;
  height: 70%;
}

</style>