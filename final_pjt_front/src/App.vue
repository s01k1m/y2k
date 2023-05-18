<template>
  <div id="app">
    <nav>
      <router-link to="/home"><img src="./assets/logo.svg" class="logo"></router-link>
      <router-link to="/stills">STILL's'</router-link>
      <input type="text" id="searchBar" placeholder="Search" aria-label="Search" aria-describedby="button-addon2"
        v-model="searchInput"
        @keyup.enter="search"
      >
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
  data() {
    return {
      searchInput: null,
    }
  },
  computed: {
    isLogined() {

      return this.$store.state.isLogin
    },
  },
  methods: {
    search() {
      this.$router.push({name: 'search', params: { searchInput: this.searchInput}})
    }
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
  height: 48px;
  min-width: 407px;
  border: none;
  border-radius: 24px;
  padding: 1px 2px;
  background-color: #e9e9e9;
  display: inline;
  padding: 20px 20px;
}

.logo {
  height: 20px;
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
