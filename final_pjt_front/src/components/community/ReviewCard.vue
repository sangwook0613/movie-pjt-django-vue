<template>
  <div class="row card-body">
    <div class="col-1"></div>
    <router-link :to="{ name: 'ReviewDetail', params: { reviewId: review.id } }" class="col-10 row">
      <div class="review-card col-8" >
        <span class="fw-bold fs-4 pe-2">{{ review.title }}</span>
        <span :class="makeBadge" style="width: 30px">{{ review.rating }}</span>
        <!-- <span>{{ review.created_at }}</span> -->
      </div>
      <span class="col-4">
        <img :src="this.movie.poster_path" alt="movie-poster-image" style="width: 120px; height: 150px">
      </span>
    </router-link>
    <div class="col-1"></div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import axios from 'axios'
import SERVER from '@/api/server.js'

export default {
  name: 'CommunityDetail',
  data: function () {
    return {
      movie: '',
    }
  },
  props: {
    review: {
      type: Object, 
    }
  },
  methods: {
    ...mapActions('movieStore', [
      'getMovieDetail',
    ]),
    imageURL: function () {
      if (this.movieDetail.length === 0) {
        const config = {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
        axios({
          url: SERVER.URL + SERVER.ROUTES.getMovie + this.review.movie,
          method: 'get',
          headers: config,
        })
        .then((res) => {
          this.movie = res.data
          // console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
  },
  computed: {
    ...mapState('movieStore', [
      'movieDetail',
    ]),
    makeBadge: function () {
      if (this.review.rating >= 8) {
        return 'badge rounded-pill bg-primary'
      } else if (this.review.rating >= 4) {
        return 'badge rounded-pill bg-warning'
      } else {
        return 'badge rounded-pill bg-danger'
      }
    },
  },
  created: function () {
    this.imageURL()
  }
}
</script>

<style>

.review-card {
  position: relative;
  display: inline-block;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0,0,0,.125);
  border-radius: .25rem;
  height: 150px;
}
</style>