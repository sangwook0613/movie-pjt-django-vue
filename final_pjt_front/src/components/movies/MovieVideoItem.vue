<template>
  <div class="item col-3" @click="SET_SELECTED_VIDEO(video)">
    <div class="d-flex flex-column justify-content-start align-items-center" @click="openVideoModal">
      <div class="thumbnail-box rounded my-3" :style="{ backgroundImage: `url(${youtubeImageSrc})`, backgroundSize: 'cover' }">
      </div>
      <!-- {{ video.snippet.title | stringUnescape }} -->
      <div class="fw-bold video-title">
        <p>{{ video.snippet.title | stringUnescape }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState, mapMutations, mapActions } from 'vuex'

export default {
  name: 'MovieVideoItem',
  props: {
    video: {
      type: Object, 
    }
  },
  methods: {
    ...mapMutations('movieStore', [
      'SET_SELECTED_VIDEO',
    ]),
    ...mapActions([
      'openModal',
    ]),
    openVideoModal: function () {
      this.openModal()
      this.modalData.movieVideoModalStatus = true
    },
  },
  computed: {
    ...mapState([
      'modalData',
    ]),
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.high.url
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>
.video-list .item {
  margin-bottom: 1rem;
  cursor: pointer;
  background-color: #292828;
  border-radius: 8px;
}

.video-list .item:hover {
  background: #292828;
}

.video-list .item img {
  height: fit-content; 
  margin-right: 0.5rem;
}

.thumbnail-box {
  width: 270px;
  height: 200px;
}

.video-title {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
</style>
