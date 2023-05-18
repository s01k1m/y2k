<template>
  <div class="login">
    <h1>로그인</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>
      <button type="submit" v-on:click="loginSubmit">Log in</button><br>
      <router-link :to="{ name: 'signup' }">아직 가입하지 않으셨나요?</router-link>
      <!-- <button type="submit" v-on:click="Signin">Sign in</button> -->
    </form>
  </div>  
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'LogInView',
  data() {
    return {
      username : null,
      password : null,
    }
  },
  methods: {
    loginSubmit(e) {
      e.preventDefault() // 폼 새로고침 방지

      const saveData = {}
      saveData.username = this.username
      saveData.password = this.password

      console.log(saveData)

      axios
        .post(`${API_URL}/accounts/login/`, saveData)

        .then((res) => {
          console.log(res.data) //
          const token = res.data.key
          // localStorage.setItem('access_token', token) // 토큰을 저장함

          // const refretoken = res.data.refresh_token
          // localStorage.setItem('refresh_token', refretoken) // 토큰을 저장함
          const config = {
            headers: {
              Authorization: 'Token ' + token
            }
          }
          axios
            .get(`${API_URL}/accounts/user/`, config) // 유저 요청
            .then((response) => {
                console.log(response)
              } // 유저 정보를 받아옴
            )
        })
    }
  }
}
</script>

<style>

</style>
