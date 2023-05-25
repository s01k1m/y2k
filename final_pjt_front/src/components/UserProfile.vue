<template>
  <div class="userprofile">
    <p>
      <span class="hi">Hi!</span>
      <span class="name">
           {{ userInfo.username }} 👋
      </span>
    </p>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    }
  }
}
</script>

<style scoped>
.hi {
  color: #757575;
  font-size: 50px;
  margin-right: 10px; 
}
.name {
  color: #424242;
  font-size: 50px;

}
</style>