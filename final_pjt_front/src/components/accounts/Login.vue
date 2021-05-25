<template>
  <div class="login">
    <br><br><br><br><br><br><br><br>
    <h1 class="text-light fw-bold animate__animated animate__heartBeat animate__infinite">환상의 SSAFY에 오신걸 환영합니다.</h1>
    <br>
    <!-- ID -->
    <div class="row py-5 px-5">
      <div class="input-group mt-3 mb-1 justify-content-center">
        <div class="input-group-prepend">
          <span class="input-group-text" id="basic-addon1">아이디</span>
          </div>
          <input type="text" name="username" class="form-control"
            placeholder="ID를 입력해주세요."
            style="width:30%;"
            v-model="credentials.username">
        </div>
      <!-- PASSWORD -->
      <div class="input-group mb-2 justify-content-center">
        <div class="input-group-prepend">
          <span class="input-group-text" id="basic-addon1">비밀번호</span>
        </div>
        <input type="password" name="password" class="form-control input-lg"
        style="width:30%;"
          placeholder="Password를 입력해주세요."
          v-model="credentials.password"
          @keypress.enter="login(credentials)">
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <button type="submit" class="btn btn-light btn-block"
      @click="login(credentials)">로그인</button>
      <router-link :to="{ name: 'Signup' }" class="btn btn-light btn-block mx-3">회원가입</router-link>

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
} 
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
.login {
  color: white;
  font-family: 'Lobster', cursive;
}
.animate__animated {
    --animate-duration  : 2.5s;
    --animate-delay     : 1s;
}

/* 
.medium-small {
    font-size: 0.9rem;
    margin: 0;
    padding: 0;
}

.login-form {
    width: 280px;
}

.login-form-text {
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.8rem;
}

.login-text {
    margin-top: -6px;
    margin-left: -6px !important;
}

.margin {
    margin: 0 !important;
}

.pointer-events {
  pointer-events: auto !important;
}

.input-field >.material-icons  {
  padding-top:10px;
}

.input-field div.error{
    position: relative;
    top: -1rem;
    left: 3rem;
    font-size: 0.8rem;
    color:#FF4081;
    -webkit-transform: translateY(0%);
    -ms-transform: translateY(0%);
    -o-transform: translateY(0%);
    transform: translateY(0%);
} */
</style>