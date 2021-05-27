<template>
  <div class="signup d-flex flex-column align-items-center justify-content-center mt-5 pt-5 row">
    <h1 class="text-light fw-bold animate__animated animate__heartBeat animate__infinite">환상의 SSAFY에 오신걸 환영합니다.</h1>
    <div class="py-5 px-5 form-signin text-dark signup-card mt-5 col-3">
      <div class="form-floating pb-3">
        <input type="text" class="form-control" id="floatingInput" placeholder="Username" v-model="credentials.username">
        <label for="floatingInput">Username</label>
      </div>
      <div class="form-floating pb-3">
        <input type="text" class="form-control" id="floatingInput" placeholder="Email" v-model="credentials.email">
        <label for="floatingInput">Email</label>
      </div>
      <div class="form-floating pb-3">
        <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="credentials.password">
        <label for="floatingPassword">Password</label>
      </div>
      <div class="form-floating">
        <input 
          type="password" 
          class="form-control" 
          id="floatingPasswordConfirm"
          placeholder="PasswordConfirm"
          v-model="credentials.passwordConfirmation"
          @keypress.enter="signup(credentials)"
        >
        <label for="floatingPasswordConfirm">PasswordConfirm</label>
      </div>
      <div class="d-flex flex-column justify-content-center align-items-center mt-4">
        <button type="submit" class="btn white-btn rounded-pill my-3"
        @click="signup(credentials)">회원가입</button>
        <router-link :to="{ name: 'Login' }" class="btn black-btn rounded-pill">로그인 페이지로</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        email: '',
      }
    }
  },
  methods: {
    ...mapActions([
      'signup',
    ])
  },
  created: function () {
    document.body.style.backgroundImage = "linear-gradient(rgba(20, 20, 20, 0.5), rgba(20, 20, 20, 0.5)), url('https://image.tmdb.org/t/p/original/i34ijHY5hr52uYcKZ48wq7K6yUs.jpg')";
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
.signup {
  color: #FFFFFF;
}

.signup-card {
  padding: 20px;
  border-radius: 8px;
  background-color: rgba(41, 40, 40, 0.9);
}

.white-btn {
  border-color: #292828;
  background-color: #FFFFFF;
  width: 150px;
}

.black-btn {
  background-color: #292828;
  border-color: #FFFFFF;
  width: 150px;
  color: #FFFFFF;
}
</style>