<template>
  <div class="login">
    <img src="../assets/logo.svg" alt="logo" class="logo">
    <h1 class="header">Welcome To STILLER!</h1>
    <div class="loginform">

      <label for="username">User name</label><br>
      <input type="text" id="username" v-model="username"><br>
      <label for="password">Password</label><br>
      <input type="password" id="password" v-model="password"><br>
      <button v-on:click="loginSubmit">Log in</button><br>
    </div>
    <div class='router' >
      
      <router-link :to="{ name: 'signup' }">Don't have an account? Sign Up!</router-link>
    </div>
      <!-- <button type="submit" v-on:click="Signin">Sign in</button> -->
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
    loginSubmit() {

      const loginObj = {}
      loginObj.username = this.username
      loginObj.password = this.password


      console.log(loginObj)
      return this.$store.dispatch('login', loginObj)
    }
  }
}
</script>


<style scoped>



.logo {
  height: 100px;
}

h1 {
  margin: 50px;
  color: rgb(51, 51, 51);
  font-size: 32px;
  font-weight: 600;
  letter-spacing: -1.2px;
  padding-left: 16px;
  padding-right: 16px;
  -webkit-font-smoothing: antialiased;
  word-break: keep-all;
}

.loginform label {

  font-size: 14px;
  color: #111111;
}

 .loginform{
  width: 300px;
  margin: 0 auto;
  text-align: left;
}

.router {
  width: 300px;
  margin: 0 auto;
  text-align: center;
  border: none;
  padding: 0px;
  display: block;
  color: rgb(51, 51, 51);
  font-weight: bold;
}
.router > a{
  font-size: 12px;
  text-decoration: none;
  color: inherit;
}

.loginform > input{
  width: 100%;
  border-color: #cdcdcd;
  min-height: 48px;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-radius: 16px;
  border-style: solid;
  border-width: 2px;
  padding: 8px 16px;
  margin-bottom: 2px;
}

.loginform > button {
  margin: 0 auto;
  width: 100%;
  margin: 30px 0px;
  background-color: rgb(0, 0, 0);
  font-size: 15px;
  font-weight: bold;
  border-radius: 20px;
  padding: 0px 18px;
  border: 0px;
  height: 40px;
  vertical-align: middle;
  color: white;
}


</style>
