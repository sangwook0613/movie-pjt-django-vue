<template>
  <div id="app">
    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item mt-1 ms-2">
              <i class="fas fa-dragon text-success fs-3"></i>
            </li>

            <li class="nav-item ms-4">
                <router-link :to="{ name: 'Movie' }" class="nav-link active">Movie</router-link>
            </li>
            <li class="nav-item mx-1">
                <router-link :to="{ name: 'Community' }" class="nav-link active">Community</router-link>
            </li>
            <li class="nav-item mx-1">
              <router-link :to="{ name: 'Profile', params: { username: jwtUsername } }" class="nav-link active">Profile</router-link>
            </li>
          </ul>

          <div class="d-flex">
            <input class="form-control-sm mx-2" @input="updateSearchInput" @keypress.enter="$router.push({name: 'Search', query: {q: searchInput}})" type="text" placeholder="제목으로 검색">
            <button class="btn btn-outline-success" @click="$router.push({name: 'Search', query: {q: searchInput}})">검색</button>
          </div>

          <ul class="navbar-nav mr-auto me-3 ms-5">
            <li class="nav-item">
            <router-link @click.native="logout" to="#" class="nav-link text-white">로그아웃</router-link>
            </li>
          </ul>
          
        </div>
      </div>
    </nav>

    <div class="container mt-4">
      <router-view/>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'

export default {
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
