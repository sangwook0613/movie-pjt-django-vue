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
            class="material-icons md-28 hovering"
            @click="openReviewCreateModal">settings</span>
        </div>
      </div>
    </div>
    
    <div class="my-3 d-flex justify-content-center moreinfo-tag py-2 rounded">
      <div @click="showClickAdditionalDetail(0)" class="mx-1 more-detail-btn fs-5 px-2 fw-bold text-light"
      :style="this.checkProfileDetailClicked[0] ? 'border-bottom:3px solid #FFFFFF; padding-bottom:3px;' : ''">작성한 리뷰</div>
      <div @click="showClickAdditionalDetail(1)" class="mx-1 more-detail-btn fs-5 px-2 fw-bold text-light"
      :style="this.checkProfileDetailClicked[1] ? 'border-bottom:3px solid #FFFFFF; padding-bottom:3px;' : ''">좋아요한 리뷰</div>
      <div @click="showClickAdditionalDetail(2)" class="mx-1 more-detail-btn fs-5 px-2 fw-bold text-light"
      :style="this.checkProfileDetailClicked[2] ? 'border-bottom:3px solid #FFFFFF; padding-bottom:3px;' : ''">좋아요한 영화</div>
    </div>
    <div class="d-flex flex-column align-items-center">
      <div class="d-flex flex-column align-items-center" v-if="checkProfileDetailClicked[0]">
        <div class="d-flex flex-column justify-content-center">
          <div class="py-2 fw-bold fs-6 text-center">리뷰 또는 영화를 클릭하면 해당 페이지로 이동합니다.</div>
          <div class="row d-flex justify-content-evenly mx-3">
            <div v-for="(review,idx) in profile.reviews" :key="'B'+idx" class="col-3 mx-3 mb-3 profile-card">
              <router-link
                :to="{ name: 'ReviewDetail',
                params: { movieId: review.movie.id, reviewId: review.id }}"
                class="text-decoration-none text-light hovering"
              >
                <div class="fs-5 fw-bold py-2" style="word-break:break-all; word-wrap:break-word;">{{ review.title }}</div>
              </router-link>

              <router-link
              :to="{ name: 'MovieDetail', params: { movieId: review.movie.id }}"
              class="text-decoration-none text-light hovering">
              {{ review.movie.title }}</router-link>

              <div class="fw-bold pt-2">{{ review.rating }}/10</div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="checkProfileDetailClicked[1]">
        <div class="py-2 fw-bold fs-6 text-center">제목 또는 작성자를 클릭하면 해당 정보로 이동합니다.
          <div>
            <div v-for="(likeReview,idx) in profile.like_reviews" :key="'D'+idx" class="my-2 col-6 profile-card"> 
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
      </div>
      <div v-if="checkProfileDetailClicked[2]">
        <div class="py-2 fw-bold fs-6 text-center">이미지를 클릭하면 해당 영화 정보로 이동합니다.</div>
        <div class="container row">
          <div v-for="(movie, idx) in profile.like_movies" :key="idx" class="col-3 mb-2">
            <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
              <div class="create-box rounded scale" :style="{ backgroundImage: `url(${movie.poster_path})`, backgroundSize: '100% 100%' }">
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>    
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Profile',
  data: function () {
    return {
      checkProfileDetailClicked: [true, false, false],
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
      this.checkProfileDetailClicked = [false, false, false]
      this.checkProfileDetailClicked[idx] = true
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

.create-box {
  width: 210px;
  height: 350px;
}

.card-css {
  background-color: rgba(188,188,188,0.4);
  border-width: 1.5px;
  border-style: solid;
  border-color: rgba(37,150,151,0.5);
}

.ellipse-2 {
  width: 100px;
  height: 100px;
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

.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;   /* 부드러운 모션을 위해 추가*/
}

.scale:hover {
  transform: scale(1.05);
  -webkit-transform: scale(1.05);
  -moz-transform: scale(1.05);
  -ms-transform: scale(1.05);
  -o-transform: scale(1.05);
  opacity:0.7;
}
.hovering:hover {
  color:#00cecb !important;
}
</style>