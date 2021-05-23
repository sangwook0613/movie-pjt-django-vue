<template>
  <div>
    <br><br><br><br><br><br><br>
    <div id="login-page" class="row">
      <div class="input-field col s12 center">
        <h1>회원 가입</h1>
        <p class="text-center">환상의 SSAFY에 오신걸 환영합니다!</p>
      </div>
          
      <div class="row">
          <div class="input-group mt-3 mb-1 justify-content-center">
            <div class="input-group-prepend">
              <span class="input-group-text" id="basic-addon1">ID</span>
            </div>
          <input type="text" name="username" class="form-control"
          placeholder="ID를 입력해주세요."
          v-model="credentials.username">
          </div>
      </div>

      <div class="row">
          <div class="input-field col s12">
            <div class="input-group mt-3 mb-1 justify-content-center">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">e-mail</span>
              </div>
            <input type="text" name="e-mail" class="form-control"
            placeholder="e-mail을 입력해주세요."  id="e-mail"
            v-model="credentials.email">
            </div>
        </div>
      </div>

      <div class="row">
        <div class="input-field col s12">
            <div class="input-group mt-3 mb-1 justify-content-center">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">Password</span>
              </div>
            <input type="password" id="password" name="password" class="form-control"
            placeholder="password를 입력해주세요."
            v-model="credentials.password">
          </div>
        </div>
      </div>

      <div class="row">
        <div class="input-field col s12">
            <div class="input-group mt-3 mb-1 justify-content-center">
              <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1">Password Confirm</span>
              </div>
            <input type="password" id="passwordConfirmation" name="passwordConfirmation" class="form-control"
            placeholder="password를 다시 입력해주세요."
            v-model="credentials.passwordConfirmation">
            </div>
        </div>
      </div>

      <div class="d-flex justify-content-end">
        <div class="input-field">
          <button type="submit" class="btn waves-effect waves-light col s12 bg-dark text-white"
          @click="signup(credentials)">가입하기</button>
        </div>

        <div class="input-field mx-4">
          <router-link :to="{ name: 'Login' }" class="btn btn-dark btn-block">로그인 페이지로</router-link>
        </div>
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
  }
}
</script>

<style scoped>
body{
    display: table;
    background-color: #e0f2f1 !important;
}

html, body {
    height: 100%;
}

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
}
</style>