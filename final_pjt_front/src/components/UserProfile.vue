<template>
  <div class="userprofile">
    <h1>UserProfile</h1>
    <h2>{{ userInfo.username }}</h2>
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

<style>

</style>