<template>
  <li class="item" @click="SET_SELECTED_VIDEO(video)">
    <img :src="youtubeImageSrc" alt="youtube-thumbnail-image">
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'
import { mapMutations } from 'vuex'

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
    ])

  },
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
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
  display: flex;
  margin-bottom: 1rem;
  cursor: pointer;
}

.video-list .item:hover {
  background: #eee;
}

.video-list .item img {
  height: fit-content; 
  margin-right: 0.5rem;
}
</style>
