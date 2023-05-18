<template>
  <div class="Signup">
    <h1>회원가입</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>
      <button type="submit" v-on:click="signup">Log in</button><br>

      <!-- <button type="submit" v-on:click="Signin">Sign in</button> -->
    </form>
  </div>  
</template>
<script>
export default {
  name: 'SignupView',
  components: {

  },
  methods: {
    signup() {
      console.log("회원가입")
    }
  }
}
</script>