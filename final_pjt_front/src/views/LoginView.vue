<template>
  <div class="Signup">
    <h1>로그인</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>
      <button type="submit" v-on:click="loginSubmit">Log in</button>
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
      e.preventDefault()
      console.log(this.username, this.password)
      const saveData = {}
      saveData.username = this.username
      saveData.password = this.password
      console.log(saveData)
      axios
        .post(`${API_URL}/accounts/login/`, saveData)
        .then((res) => {
          console.log(res.data)
          const token = res.data.access_token
          localStorage.setItem('access_toke', token) // 토큰을 저장함
          const refretoken = res.data.refesh_token
          localStorage.setItem('refresh_token', refretoken) // 토큰을 저장함
        })
        .catch((err) =>{
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>
