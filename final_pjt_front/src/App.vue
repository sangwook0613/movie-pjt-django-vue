<template>
  <div id="app">
    <div v-if="modalStatus">
      <BaseModal/>
    </div>
    <!-- <div v-if="showNav" class="navbar-sticky"> -->
    <div class="navbar-sticky">
      <Nav />
    </div>

    <div class="container mt-4">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Nav from '@/views/Nav'
import BaseModal from '@/views/BaseModal'
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    Nav,
    BaseModal,
  },
  methods: {
    ...mapActions('accountStore', [
      'getProfile',
    ]),
    ...mapActions([
      'updateShowNav',
    ]),
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'jwtUsername',
      'getShowNav'
    ]),
    ...mapState('accountStore', [
      'profile',
    ]),
    ...mapState([
      'showNav',
      'modalStatus',
    ]),
    
  },
  watch: {
    'this.profile.like_movies.length': function() {
      if (this.profile.like_movies.length >= 5) {
        this.updateShowNav(true)
      } else {
        this.updateShowNav(false)
      }
    },
  },
  updated: function () {
    this.getProfile(this.jwtUsername)
  },
}
</script>


<style>
/* .navbar-sticky{
  position: sticky; 
  top: 0; 
} */
body{
  /* background-image: url('https://images.squarespace-cdn.com/content/v1/5a173f16ace86416b07c25f1/1513939530902-DILPHAAJ9F0DI627449M/ke17ZwdGBToddI8pDm48kK0QKSDttGV1ap9dyeIseHF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0mxU0godxi02JM9uVemPLqw3ZQRv6tY2V6nZIOWGhJ3qaH6uCpMgOc4rPl-G2eiFCQ/fantasy+album+cover6+-+in+wide+format.jpg?format=1500w'); */
  /* background-image: url('https://t1.daumcdn.net/cfile/tistory/22568F4253F73C2C18'); */
  background-color: #141414 !important;
  background-size: 100%;
  background-attachment: fixed;
  /* background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
  url('https://images.squarespace-cdn.com/content/v1/5a173f16ace86416b07c25f1/1513939530902-DILPHAAJ9F0DI627449M/ke17ZwdGBToddI8pDm48kK0QKSDttGV1ap9dyeIseHF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0mxU0godxi02JM9uVemPLqw3ZQRv6tY2V6nZIOWGhJ3qaH6uCpMgOc4rPl-G2eiFCQ/fantasy+album+cover6+-+in+wide+format.jpg?format=1500w'); */
}
/* 
html, body {
    height: 100%;
} */

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

#app h1 {
  text-align: center;
}



/* animate.css 주기, 딜레이 설정 */
.animate__animated {
    --animate-duration  : 1s;
    --animate-delay     : 1s;
}

/* 블러처리: 쓸지도 몰라서 놔둠 */
.Blur {
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px); 
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(5px);
}

</style>
