<template>
  <div>
    <br><br><br><br><br><br><br><br><br><br>
    <h1 class="text-primary fw-bold">환상의 SSAFY에 오신걸 환영합니다.</h1>
    <br>
    <!-- ID -->
    <div class="row col-lg-4 d-flex">
      <div class="input-group mt-3 mb-1 justify-content-center">
        <div class="input-group-prepend">
          <span class="input-group-text" id="basic-addon1">ID</span>
          </div>
          <input type="text" name="username" class="form-control"
            placeholder="ID를 입력해주세요."
            v-model="credentials.username">
        </div>
      <!-- PASSWORD -->
      <div class="input-group mb-2 justify-content-center">
        <div class="input-group-prepend">
          <span class="input-group-text" id="basic-addon1">PW</span>
        </div>
        <input type="password" name="password" class="form-control"
          placeholder="Password를 입력해주세요."
          v-model="credentials.password"
          @keypress.enter="login(credentials)">
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <button type="submit" class="btn btn-dark btn-block"
      @click="login(credentials)">로그인</button>
      <button type="button" class="btn btn-dark btn-block mx-3"
      onclick="location.href='/signup/'">회원가입</button>
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
  }
} 
</script>

<style>

</style>