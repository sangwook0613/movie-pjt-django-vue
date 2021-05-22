<template>
  <div id="app">
    <span v-if="isLoggedIn">
      <div id="nav">
        <router-link :to="{ name: 'Movie' }">Movie</router-link> |
        <router-link :to="{ name: 'Community' }">Community</router-link> |
        <span v-if="isLoggedIn">
          <router-link :to="{ name: 'Profile', params: { username: jwtUsername } }">Profile</router-link> |
          <router-link @click.native="logout" to="#">로그아웃</router-link> |
        </span>
        <span v-else>
          <router-link :to="{ name: 'Signup' }">회원가입</router-link> |
          <router-link :to="{ name: 'Login' }">로그인</router-link> |
        </span>
        <input @input="updateSearchInput" @keypress.enter="$router.push({name: 'Search', query: {q: searchInput}})" type="text" placeholder="제목으로 검색">
        <button @click="$router.push({name: 'Search', query: {q: searchInput}})">검색</button>
      </div>
    </span>

    <!-- v-else하면 안보임 -->
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'
// import Start from './views/Start.vue'

export default {
  // components: { Start },
  name: 'App',
  methods: {
    ...mapActions([
      'logout',
    ]),
    ...mapActions('movieStore',[
      'updateSearchInput',
      'searchMovie',
    ]),
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'jwtUsername',
    ]),
    ...mapState('movieStore', [
      'searchInput'
    ]),
  },
  // watch: {
  //   'searchInput': function() {
  //     this.updateSearchInput(this.searchInput)
  //   },
  // }, 
}
</script>


<style>
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

#nav a.router-link-exact-active {
  color: #42b983;
}

html {
    display: table;
    margin: auto;
}
</style>
