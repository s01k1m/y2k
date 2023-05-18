<template>
  <div id="app">
    <nav>
      <div class="nav-left">
        <router-link to="/home"><img src="./assets/logo.svg" class="logo"></router-link>
        <router-link to="/stills">STILL's'</router-link>
      </div>
      <input type="text" id="searchBar" placeholder="Search" aria-label="Search" aria-describedby="button-addon2">
      <div class="nav-right">
        <router-link to="/create">CREATE</router-link>
        <router-link to="/login" v-if="!isLogined">LOG-IN</router-link>
        <router-link to="/user" v-if="isLogined">MyPage</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
  computed: {
    isLogined() {

      return this.$store.state.isLogin
    },
  },
  created() { // 로그인이 되어있는지 항상 access_token을 체크하는 로직입니다.
    let cat = localStorage.getItem('access_token')
    console.log('created: ',cat)

    if (cat) { //access_token이 있으면 로그인을 유지하도록
      return this.$store.dispatch('getMemberInfo') // 유저정보 가져오는 로직
    }
  }
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-width: 560px;
}


.logo {
  height: 20px;
}


nav {
  padding: 0px;
  display: flex;
  align-items: center;
}

#searchBar {
  background-color: purple;
  flex: 3;

}
nav a {
  font-weight: bold;
  color: #a4caf1;
  margin-left : 10px;

}

nav a.router-link-exact-active {
  color: #42b983;
}

nav .nav-left {
  flex: 2;
  background-color: green;
  display: flex;
  justify-content: space-evenly;  
  align-items: center;
}

nav .nav-right {
  flex: 2;
  background-color: green;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
</style>
