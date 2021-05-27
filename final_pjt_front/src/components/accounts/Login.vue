<template>
  <div class="login d-flex flex-column align-items-center justify-content-center mt-5 pt-5 row">
    <h1 class="text-light fw-bold animate__animated animate__heartBeat animate__infinite">환상의 SSAFY에 오신걸 환영합니다.</h1>
    <div class="py-5 px-5 form-signin text-dark login-card mt-5 col-3">
      <div class="form-floating pb-3">
        <input type="text" class="form-control" id="floatingInput" placeholder="Username" v-model="credentials.username">
        <label for="floatingInput">Username</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="credentials.password" @keypress.enter="login(credentials)">
        <label for="floatingPassword">Password</label>
      </div>
      <div class="d-flex justify-content-center align-items-center mt-5">
        <button type="submit" class="btn white-btn rounded-pill"
        @click="login(credentials)">로그인</button>
        <router-link :to="{ name: 'Signup' }" class="btn black-btn rounded-pill ms-3">회원가입</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions([
      'login',
    ])
  },
  created: function () {
    document.body.style.backgroundImage = "linear-gradient(rgba(20, 20, 20, 0.5), rgba(20, 20, 20, 0.5)), url('https://image.tmdb.org/t/p/original/vVpEOvdxVBP2aV166j5Xlvb5Cdc.jpg')";
  },
  beforeDestroy: function () {
    document.body.style.backgroundImage = "";
    document.body.style.backgroundColor = "rgb(20, 20, 20)";
  }
} 
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
.login {
  color: #FFFFFF;
}

.login-card {
  padding: 20px;
  border-radius: 8px;
  background-color: rgba(41, 40, 40, 0.9);
}

.white-btn {
  border-color: #292828;
  background-color: #FFFFFF;
  width: 100px;
}

.black-btn {
  background-color: #292828;
  border-color: #FFFFFF;
  width: 100px;
  color: #FFFFFF;
}

.animate__animated {
    --animate-duration  : 2.5s;
    --animate-delay     : 1s;
}
</style>