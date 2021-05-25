<template>
  <div>
    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-expand-sm navbar-dark transparent">
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">

            <li class="nav-item">
                <router-link :to="{ name: 'Movie' }" class="nav-link active">
                  <span class="material-icons md-24">home</span>
                </router-link>
            </li>
          <div class="d-flex">
            <input class="form-control-sm mx-2" @input="updateSearchInput" 
            @keypress.enter="$router.push({name: 'Search', query: {q: searchInput}})" 
            type="text" placeholder="찾을 영화를 입력해주세요."
            style="width:224px;"
            >
            <button class="btn btn-success" @click="$router.push({name: 'Search', query: {q: searchInput}})">검색</button>
          </div>
        </ul>

          <ul class="navbar-nav mr-auto me-3 ms-5 d-flex align-items-center">
            <li class="nav-item">
              <router-link @click.native="logout" to="#" class="nav-link text-dark">
                <i class="material-icons md-32">logout</i>
                
                </router-link>
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
.material-icons.md-18 { font-size: 18px; }
.material-icons.md-24 { font-size: 24px; }
.material-icons.md-36 { font-size: 36px; }
.material-icons.md-32 { font-size: 32px; }

.navbar.transparent.navbar-inverse .navbar-inner {
    border-width: 0px;
    -webkit-box-shadow: 0px 0px;
    box-shadow: 0px 0px;
    background-color: rgba(0,0,0,0.0);
    background-image: -webkit-gradient(linear, 50.00% 0.00%, 50.00% 100.00%, color-stop( 0% , rgba(0,0,0,0.00)),color-stop( 100% , rgba(0,0,0,0.00)));
    background-image: -webkit-linear-gradient(270deg,rgba(0,0,0,0.00) 0%,rgba(0,0,0,0.00) 100%);
    background-image: linear-gradient(180deg,rgba(0,0,0,0.00) 0%,rgba(0,0,0,0.00) 100%);
}
</style>
