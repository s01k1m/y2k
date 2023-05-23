<!-- Signup Vue -->
<template>
  <div class="signup">
    <img src="../assets/logo.svg" alt="logo" class="logo">
    <h1 class="header">Welcome To STILLER!</h1>
    <div class="signupform">
      <label for="username">Username</label>
      <input type="text" id="username" v-model="username">
      <label for="email">Email</label>
      <input type="text" id="email" v-model="email">
      <label for="password"> Password</label>
      <input type="password" id="password1" v-model="password1">
      <label for="password"> Confirm Password</label>
      <input type="password" id="password2" v-model="password2">
      <v-btn type="submit" v-on:click="signup">Sign up</v-btn>

      <!-- <button type="submit" v-on:click="Signin">Sign in</button> -->
    </div>
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

<style scoped>
.logo {
  height: 100px;
}

.header {
  font-size: 32px; 
  font-weight: 600; 
  letter-spacing: -1.2px; 
  padding-left: 16px; 
  padding-right: 16px;
  margin: 50px;
}

.signupform {
  display: flex;
  flex-direction: column;
  text-align: left;
  text-decoration: #cdcdcd;
  justify-content: flex-start;
  width: 300px;
  margin: auto;
}

input {
  border: solid 2px #cdcdcd;
  border-radius: 16px;
  height: 48px;
  padding: 8px 16px;
  margin-bottom: 2px;
}

label{
  font-size: 14px;
  color: #111111;
}

button {
  border: 0px;
  height: 40px;
  display: inline-block;
  border-radius: 20px;
  -webkit-font-smoothing: antialiased;
  padding: 0px 18px;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  margin-top: 8px;
  vertical-align: middle;
  text-align: center;
  background-color: black;
  color: rgb(255, 255, 255);
  width: 100%;
  margin: 30px 0px;
}


button:hover {
  animation: shine 0.8s ease forwards;
}

button:active {
  transform: translateY(0);
  animation: shine 0.8s ease forwards;
}


/* 로그인 버튼 애니메이션 */
@keyframes shine {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1);
  }
  100% {
    transform: scale(1);
    color: white;
    background-color: black;
    box-shadow: 0 4px 8px 0 rgb(172, 172, 172);
  }
}
</style>