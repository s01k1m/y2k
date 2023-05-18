<template>
  <div class="user">
    <h1>MyPage</h1>
    <UserProfile></UserProfile>
    <UserCollection></UserCollection>
    <button @click="logout">logout</button>
  </div>
</template>

<script>
import UserProfile from '@/components/UserProfile.vue'
import UserCollection from '@/components/UserCollection.vue'

export default {
  name: 'UserView',
  components: {
    UserProfile,
    UserCollection
  },
  methods: {
    logout() {
      return this.$store.dispatch('logout')
    }
  }
}
</script>

<style>

</style>