<template>
  <div>
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
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'

export default {
  name: 'Nav',
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

}
</script>


<style>

</style>
