<template>
  <div class="profile row">
    <div class="col-6 offset-3">
      <div class="d-flex flex-column align-items-center profile-card">
        <img
          alt="profile-image"
          class="ellipse-2 mb-2"
          src="https://randomuser.me/api/portraits/lego/1.jpg"
        />
        <h3>@{{ profile.username }}</h3>
        <div class="point-color">
          <span class="ms-3">게시글</span>
          <span class="fw-bold mx-1  pe-1">{{ profile.reviews.length }}</span>
          <span>팔로잉</span>
          <span class="fw-bold mx-1  pe-1">{{ profile.followings.length }}</span>
          <span>팔로워</span>
          <span class="fw-bold mx-1 pe-1 ">{{ profile.followers.length }}</span>
        </div>
        <h4 v-if=profile.introduction class="fw-bold pt-3">{{ profile.introduction }}</h4>
        <div v-if="isMyself">
          <span v-if="isFollow">
            <button @click="followUser($route.params.username)" class="mt-3 btn btn-danger btn-sm text-white">팔로우 취소</button>
          </span>
          <span v-else>
            <button @click="followUser($route.params.username)" class="mt-3 btn btn-sm btn-primary">팔로우</button>
          </span>
        </div>
        <div v-else class="mt-3">
          <span type="button"
            class="material-icons md-28"
            @click="openReviewCreateModal">settings</span>
        </div>
      </div>
    </div>
    
    <div class="my-3 d-flex justify-content-center moreinfo-tag py-2 rounded">
      <button @click="showClickAdditionalDetail(0)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light">작성한 리뷰</button>
      <button @click="showClickAdditionalDetail(1)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light">좋아요한 리뷰</button>
      <button @click="showClickAdditionalDetail(2)" class="btn btn-sm mx-1 more-detail-btn fs-5 fw-bold text-light">좋아요한 작품</button>
    </div>
    <div class="additional-info-card d-flex flex-column align-items-center">
      <div class="d-flex flex-column align-items-center" v-if="checkMovieDetailClicked[0]">
        <div class="d-flex flex-column justify-content-center">
          <div class="py-2 fw-bold fs-6 text-center">리뷰 또는 영화를 클릭하면 해당 페이지로 이동합니다.</div>
          <div class="row d-flex justify-content-evenly mx-3">
            <div v-for="(review,idx) in profile.reviews" :key="'B'+idx" class="col-3 mx-3 mb-3 profile-card">
              <router-link
                :to="{ name: 'ReviewDetail',
                params: { movieId: review.movie.id, reviewId: review.id }}"
                class="text-decoration-none text-light"
              >
                <div class="fs-5 fw-bold py-2" style="word-break:break-all; word-wrap:break-word;">{{ review.title }}</div>
              </router-link>

              <router-link
              :to="{ name: 'MovieDetail', params: { movieId: review.movie.id }}"
              class="text-decoration-none text-light">
              {{ review.movie.title }}</router-link>

              <div class="fw-bold pt-2">{{ review.rating }}/10</div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="checkMovieDetailClicked[1]">
        <div class="py-2 fw-bold fs-6 text-center">제목 또는 작성자를 클릭하면 해당 정보로 이동합니다.
          <div>
            <div v-for="(likeReview,idx) in profile.like_reviews" :key="'D'+idx" class="my-2 col-3 mx-5 profile-card"> 
              <router-link :to="{ name: 'ReviewDetail',
                params: { movieId: likeReview.movie.id, reviewId: likeReview.id }}"
                class="text-decoration-none text-light py-2"
                style="word-break:break-all; word-wrap:break-word;"
              >
                {{ likeReview.title }}
              </router-link>
              <a :href="`./${likeReview.user.username}`"
                class="nav-link active text-decoration-none text-primary"
              >
                @{{ likeReview.user.username }}
              </a>
            </div>
          </div>
        </div>
        <!-- <MovieVideos v-if="checkCondition(movieDetail.title)" :movieTitle="movieDetail.title"/> -->
      </div>
      <div v-if="checkMovieDetailClicked[2]">
        <h3 class="pt-4 fw-bold">Like Movies</h3>
        <p>이미지를 클릭하면 해당 영화 정보로 이동합니다.</p>
        <carousel v-if="profile.like_movies.length > 0" :nav="false" :items="5" class="mx-3 profile-detail">
          <div v-for="(movie, idx) in profile.like_movies" :key="idx" class='card'>
            <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
              <img :src="movie.poster_path" alt="movie-poster" class="card-img-top">
            </router-link>
          </div>
        </carousel>
        <!-- <SimilarMovies/> -->
      </div>
    </div>    
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Profile',
  components: {
    carousel,
  },
  data: function () {
    return {
      checkMovieDetailClicked: [true, false, false]
    }
  },
  methods: {
    ...mapActions([
      'openModal',
    ]),
    ...mapActions('accountStore', [
      'getProfile',
      'followUser',
    ]),
    openReviewCreateModal: function () {
      this.openModal()
      this.modalData.profileUpdateModalStatus = true
    },
    showClickAdditionalDetail: function (idx) {
      this.checkMovieDetailClicked = [false, false, false]
      this.checkMovieDetailClicked[idx] = true
    },
    checkCondition: function (item1) {
      if (Object.keys(item1).length !== 0) {
        return true
      }
      return false
    },
  },
  computed: {
    ...mapState([
      'modalData',
    ]),
    ...mapState('accountStore', [
      'profile',
      'isFollow',
      'isMyself',
    ]),
  },
  watch: {
    '$route.params.username': function() {
      console.log(this.$route.params.username)
      // this.getProfile(this.$route.params.username)
      this.$router.push({ name: 'Profile', params: { username: this.$route.params.username } })
    },
  },
  created: function () {
    this.getProfile(this.$route.params.username)
  },
}
</script>

<style scoped>
.material-icons.md-28 { font-size: 29px; }

.profile {
  padding: 20px;
  border-width: 5px;
  color: #FFFFFF;
}

.profile-card {
  padding: 20px;
  border-radius: 8px;
  background-color: #292828;
}

/* .profile-detail{
  padding: 20px;
  border-width: 1.5px;
  border-style: solid;
  border-color: rgba(37,150,151,0.5);
} */
.card-css {
  background-color: rgba(188,188,188,0.4);
  border-width: 1.5px;
  border-style: solid;
  border-color: rgba(37,150,151,0.5);
}

.ellipse-2 {
  width: 100px;
  height: 100px;
  margin-left: 20px;
  border-radius: 50%;
}

.point-color {
  color: #00cecb;
}

.black-btn {
  background-color: #292828;
  border-color: #FFFFFF;
  color: #FFFFFF;
  width: 90px;
}

.white-btn {
  border-color: #292828;
  background-color: #FFFFFF;
  width: 120px;
}
</style>