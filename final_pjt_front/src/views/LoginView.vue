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
// import axios from 'axios'



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

      const loginObj = {}
      loginObj.username = this.username
      loginObj.password = this.password


      console.log(loginObj)
      return this.$store.dispatch('login', loginObj)
    }
  }
}
</script>

<style>

</style>
