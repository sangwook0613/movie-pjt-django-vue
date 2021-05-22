<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ name: 'Movie' }">Movie</router-link> |
      <router-link :to="{ name: 'Community' }">Community</router-link> |
      <router-link to='#'>Search</router-link> |
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'Profile', params: { username: jwtUsername } }">Profile</router-link> |
        <router-link @click.native="logout" to="#">로그아웃</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">회원가입</router-link> |
        <router-link :to="{ name: 'Login' }">로그인</router-link>
      </span>
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'App',
  methods: {
    ...mapActions([
      'logout',
    ])
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'jwtUsername',
    ])
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
