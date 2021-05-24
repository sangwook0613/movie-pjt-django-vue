<template>
  <div id="app">
    
    <div v-if="showNav">
      <Nav />
    </div>

    <div class="container mt-4">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Nav from '@/views/Nav'
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    Nav,
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

body{
    /* display: table; */
    background-color: #e0f2f1 !important;
}

html, body {
    height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

#nav {
  padding: 30px;
  text-align: center;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#app h1 {
  text-align: center;
}

.nav a.router-link-exact-active {
  color: #42b983;
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
