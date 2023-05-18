<template>
  <div class="user">
    <h1>MyPage</h1>
    <UserProfile></UserProfile>
    <UserCollection></UserCollection>
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
  }
}
</script>

<style>

</style>