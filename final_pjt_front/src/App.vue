<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ name: 'Movie' }">Movie</router-link> |
      <router-link :to="{ name: 'Community' }">Community</router-link> |
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'Profile', params: { username: jwtUsername } }">Profile</router-link> |
        <router-link @click.native="logout" to="#">로그아웃</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">회원가입</router-link> |
        <router-link :to="{ name: 'Login' }">로그인</router-link>
      </span>
      <span v-if="searchBtn">
        <input type="text" v-model.trim="searchInput" @keypress.enter="searchMovie(searchInput)">
        <!-- <input type="text" :searchInput="searchInput" @keypress.enter="searchMovie(searchInput)"> -->
        <button @click="clickSearchCancelBtn">
          <router-link to="/search/hi">Search</router-link>
        </button>
      </span>
      <span v-else>
        <button @click="clickSearchBtn">Search</button>
      </span>
    </div>
    <router-view/>
    <div v-if="searchInput">
      <carousel :nav="false" :items="5">
        <div v-for="(searchedMovie, idx) in searchedMovies" :key="idx" class='card'>
          <img :src="searchedMovie.poster_path" alt="movie-poster" class="card-img-top">
        </div>
      </carousel>
    </div>
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'
import { mapGetters, mapActions, mapState } from 'vuex'

export default {
  name: 'App',
  data: function () {
    return {
      searchInput: '',
    }
  },
  components: {
    carousel,
  },
  methods: {
    ...mapActions([
      'logout',
    ]),
    ...mapActions('movieStore', [
      'searchMovie',
      'clickSearchBtn',
      'clickSearchCancelBtn',
    ]),
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'jwtUsername',
    ]),
    ...mapGetters('movieStore', [
      'searchBtn',
      'searchInput',
    ]),
    ...mapState('movieStore', [
      // searchInput: state => state.searchInput,
      'searchBtn',
      'searchedMovies',
    ])
  },
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
</style>
