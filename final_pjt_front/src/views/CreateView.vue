<template>
  <div class="create">
    <h1>스틸컷을 크리에이트하는 포스팅 페이지입니다. </h1>
  </div>
</template>
<script>
export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      image: null,
      movie_id: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.state.isLogin
    }
  },
  created() {
    this.isLogined()
  },
  methods: {
    isLogined() {
      if (!this.isLogin) {
        console.log('if')
        alert('로그인이 필요합니다.')
        this.$router.push({ name: 'login' })
      } 
    }
  }
}
</script>

<style>
#create {
  margin: 24px;
}

</style>