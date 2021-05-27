<template>
  <div>
    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-expand-sm navbar-dark transparent">
      <div class="container-fluid d-flex justify-content-between">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="navbar-nav me-auto mb-2 mb-lg-0">
            <div class="nav-item">
              <router-link :to="{ name: 'Movie' }" class="nav-link active logo-img">
                <img src="@/assets/logo.png" alt="logo-image" >
              </router-link>
            </div>
            <div class="d-flex align-items-center">
              <input class="form-control-sm mx-2" @input="updateSearchInput" 
              @keypress.enter="$router.push({name: 'Search', query: {q: searchInput}})" 
              type="text" placeholder="찾을 영화를 입력해주세요."
              style="width:224px; height: 35px;"
              >
              <i class="fas fa-search fa-lg text-white ms-1" @click="$router.push({name: 'Search', query: {q: searchInput}})"></i>
            </div>
          </div>

        <div class="dropdown mr-auto me-3 ms-5 d-flex align-items-center">
          <a href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false" class="text-light">
            <i class="fs-2 fw-bold far fa-user-circle"></i>
          </a>
          <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuLink">
            <li><a href="http://127.0.0.1:8000/admin" class="dropdown-item fw-bold text-primary" v-if="profile.is_superuser">관리자 페이지</a></li>
            <li><router-link :to="{ name: 'Profile', params: { username: jwtUsername } }" class="dropdown-item fw-bold">
              프로필 수정</router-link></li>
            <li><router-link @click.native="logout" to="#" class="dropdown-item text-danger fw-bold">로그아웃</router-link></li>
          </ul>
        </div>



          <!-- <ul class="navbar-nav mr-auto me-3 ms-5 d-flex align-items-center">
            <li class="nav-item" v-if="profile.is_superuser">
              <a href="http://127.0.0.1:8000/admin" class="nav-link bg-primary rounded-pill text-light">관리자 페이지</a>
            </li>

            <li class="nav-item">
              <router-link @click.native="logout" to="#" class="nav-link bg-danger rounded-pill text-light">로그아웃</router-link>
            </li>
            <li class="nav-item mx-1">
              <router-link :to="{ name: 'Profile', params: { username: jwtUsername } }" class="nav-link active">
                <i class="fs-2 fw-bold far fa-user-circle"></i>
              </router-link>
            </li>
          </ul> -->

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
    ...mapState('accountStore', [
      'profile'
    ]),
  },

}
</script>


<style scoped>
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

.logo-img {
  max-width: 100px;
  max-height: 50px;
  overflow: hidden;
}

.logo-img > img {
  max-width: 100px;
  margin-top: -36%;
  margin-left: -10%;
}
</style>
