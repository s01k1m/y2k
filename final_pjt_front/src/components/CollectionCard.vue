<template>
  <div>
    {{ collection }}
    <img :src="'http://127.0.0.1:8000' + collection.stills" :alt="collection.collection_name" @click="getDetail(collection.id)">
  </div>
</template>

<script>
export default {
  name: 'CollectionCard',
  props: {
    collection: Object
  },
  methods: {
    getDetail(collectionId) {
      this.$router.push({ name: 'collectionDetail', params: {collectionId:collectionId}})
    }
  }
}
</script>

<style>

</style>