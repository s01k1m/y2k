<template>
  <div class="stillcard">
    <img :src="'http://127.0.0.1:8000' + still.still_image" :alt="still.still_image" @click="getDetail(still.id)">
  </div>
</template>

<script>

export default {
  name: 'StillCard',
  props: {
    still: Object,
  },
  methods: {    
    getDetail(stillId) {
      this.$router.push({name: 'detail', params: {stillId:stillId}})
    }
  }
}
</script>

<style>

</style>