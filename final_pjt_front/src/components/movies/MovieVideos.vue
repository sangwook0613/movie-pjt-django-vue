<template>
  <div>
    {{ movieTitle }}
    <ul class="video-list">
      <MovieVideoItem
        v-for="(video, idx) in movieVideos" 
        :key="idx"
        :video="video"
      />
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import MovieVideoItem from '@/components/movies/MovieVideoItem'

export default {
  name: 'VideoList',
  components: {
    MovieVideoItem,
  },
  props: {
    movieTitle: {
      type: String,
    }
  },
  computed: {
    ...mapState('movieStore', [
      'movieVideos',
    ])
  },
  methods: {
    ...mapActions('movieStore', [
      'getRelatedVideos',
    ])
  },
  // created: function () {
  //   this.getRelatedVideos(this.movieTitle)
  // }
}
</script>

<style>
.video-list {
  padding: 0;
  margin: 0;
  list-style-type: none;
}
</style>
