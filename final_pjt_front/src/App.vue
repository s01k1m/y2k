<template>
  <div id="app">
    <nav>
      <router-link to="/home"><img src="./assets/logo.svg" class="logo"></router-link>
      <router-link to="/stills">STILL's'</router-link>
      <form id="searchBar" class="form-group">
        <span class="form-group">
          <input type="text" class="" style="width: 250px; display: inline;" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">
          <button class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
        </span>
      </form>
      <router-link to="/create">CREATE</router-link>
      <router-link to="/login" v-if="!isLogined">LOG-IN</router-link>
      <router-link to="/user" v-if="isLogined">MyPage</router-link>
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
}

#searchBar {
  width:300px;
  display: inline;
  display: red;
}

.logo {
  height: 20px;
}

.form-contro {

}

nav {
  padding: 0px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin-left : 10px;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
