<template>
  <div id="app">
    <nav>
      <router-link to="/home"><img src="./assets/apple-logo.svg" class="logo"></router-link>
      <router-link to="/home">STILLs</router-link>
      <router-link to="/create">CREATE</router-link>
      <router-link to="/login">LOG-IN</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
