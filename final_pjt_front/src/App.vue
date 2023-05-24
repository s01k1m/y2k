<template>
  <div id="app">
    <nav>
      <div class="nav-left">
        <router-link to="/home"><img src="./assets/logo.svg" class="logo"></router-link>
        <router-link to="/stills" class="go" >STILLs</router-link>
      </div>
      <input type="text" id="searchBar" placeholder="Search" aria-label="Search" aria-describedby="button-addon2"
        v-model="searchInput"
        @keyup.enter="search"
      >
      <div class="nav-right">
        <router-link to="/create" class="go" >CREATE</router-link>
        <router-link to="/login" v-if="!isLogined" class="go" >LOG-IN</router-link>
        <router-link to="/user" v-if="isLogined" class="go" >MyPage</router-link>
      </div>
    </nav>
    <router-view :key="$route.fullPath"/>
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
    search(e) {

      console.log('검색을 시작 : ',e.target.value)
      this.$router.push({name: 'search', params: { searchInput: this.searchInput}})
      .then(() => {e.target.value = ''})
      .catch((err)=>{
        console.log(err)
        e.target.value = ''
      })
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
  min-width: 560px;
}


#searchBar {
  height: 48px;
  min-width: 407px;
  border: none;
  border-radius: 24px;
  padding: 1px 2px;
  background-color: #e9e9e9;
  display: inline;
  padding: 0 20px;
  flex: 3;
}

.logo {
  height: 50px;
}

nav {
  margin: 10px 0 5px 0;
  padding: 0px;
  display: flex;
  align-items: center;
    padding: 12px;
}


nav a {
  font-size: 16px;
  text-decoration: none;
  font-weight: bold;
  color: #000000;
  margin-left : 10px;
  padding: 12px;

}

nav a.go:focus {
  color: #ffffff;
  background-color: black;

  border-radius: 24px;
}


nav .nav-left {
  flex: 2;
  /* background-color: green; */
  display: flex;

  justify-content: space-evenly;  
  align-items: center;
}

nav .nav-right {
  flex: 2;
  /* background-color: green; */
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
</style>