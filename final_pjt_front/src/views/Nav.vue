<template>
  <div>
    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-expand-sm navbar-dark bg-dark">
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item mt-1 ms-2">
              <i class="fas fa-dragon text-success fs-3"></i>
            </li>

            <li class="nav-item ms-4">
                <router-link :to="{ name: 'Movie' }" class="nav-link active">Home</router-link>
            </li>
          <div class="d-flex">
            <input class="form-control-sm mx-2" @input="updateSearchInput" 
            @keypress.enter="$router.push({name: 'Search', query: {q: searchInput}})" 
            type="text" placeholder="찾을 영화를 입력해주세요."
            style="width:220px;"
            >
            <button class="btn btn-outline-success" @click="$router.push({name: 'Search', query: {q: searchInput}})">검색</button>
          </div>
        </ul>



          <ul class="navbar-nav mr-auto me-3 ms-5 d-flex align-items-center dropdown">
            <li class="nav-item">
              <router-link @click.native="logout" to="#" class="nav-link bg-danger rounded-pill text-light">로그아웃</router-link>
            </li>
            <li class="nav-item mx-1">
              <router-link :to="{ name: 'Profile', params: { username: jwtUsername } }" class="nav-link active">
                <i class="fs-2 fw-bold far fa-user-circle"></i>
              </router-link>
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
