<template>
  <div>
    <h1>회원 가입</h1>
    <!-- <div>
      <label for="userId">아이디: </label>
      <input type="text" id="userId" v-model="credentials.userId">
    </div> -->
    <div>
      <label for="username">아이디: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="email">이메일 주소: </label>
      <input type="email" id="email" v-model="credentials.email">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input
        type="password"
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup(credentials)"
      >
    </div>
    <button @click="signup(credentials)">회원 가입</button>
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

<style>

</style>