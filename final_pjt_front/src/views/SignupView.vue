<template>
  <div class="signup">
    <h1>회원가입</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <label for="email">email : </label>
      <input type="text" id="email" v-model="email"><br>
      <label for="password"> password1 : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <label for="password"> password2 : </label>
      <input type="password" id="password2" v-model="password2"><br>
      <button type="submit" v-on:click="signup">Log in</button><br>

      <!-- <button type="submit" v-on:click="Signin">Sign in</button> -->
    </form>
  </div>  
</template>
<script>
// import { mapActions } from "vuex";

export default {
  name: 'SignUpView',
  data() {
    return {
      username : null,
      email: null,
      password1 : null,
      password2 : null,
    }
  },
  components: {

  },
  methods: {
    signup() {
      const loginObj = {}
      loginObj.username = this.username
      loginObj.email = this.email
      loginObj.password1 = this.password1
      loginObj.password2 = this.password2
      console.log(loginObj)
      return this.$store.dispatch('signup', loginObj)
    }
      // ...mapActions(["signup"])
  }
}
</script>