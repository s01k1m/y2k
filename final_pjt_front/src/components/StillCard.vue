<template>
  <div class="stillcard">
    <img :src="'http://127.0.0.1:8000' + still.still_image" :alt="still.still_image" @click="getDetail(still.id)">
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'StillCard',
  props: {
    still: Object,
  },
  methods: {    
    getDetail(stillId) {
      console.log('getDetail 진입!!')
      axios
      .get(`http://127.0.0.1:8000/stills/detail/${stillId}/`)
      .then((response) => {
        console.log('detail view response: ', response)
        this.$router.push({name: `detail`, params: {stillId:stillId, stillDetail:response.data}})
      })
      .catch((err) => {
        console.error(err)
      })
    }
  }
}
</script>

<style>

</style>