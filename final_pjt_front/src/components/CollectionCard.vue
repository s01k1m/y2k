<template>
  <div>
    <div id="collectioncontainer" @click="getDetail(collection.id)">
      <img id="collectionImg" :src="'http://127.0.0.1:8000' + collection.stills[0].still_image" :alt="collection.collection_name">
      <div id="collectionName">{{collection.collection_name}}</div>
      <div id="collectionfooter">
        <span id="stilllength">{{ collection.stills.length }} stillcuts</span>
        <span>{{ collection.username }}</span>
      </div>
    </div>
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
      console.log('collection getDetail 진입')
      this.$router.push({ name: 'collectionDetail', params: {collectionId:collectionId}})
    }
  }
}
</script>

<style scoped>
#collectioncontainer {
  display: flex;
  flex-direction: column;

}
#collectionImg {
  height: 200px;
  border-radius: 8px;
}
#collectionName {
  margin: 15px 0 8px;
  line-height: 24px;
  font-size: 22px;
  font-weight: 700;
  color: #424242;
  word-break: keep-all;
  word-wrap: break-word;
}
#collectionfooter {
  display: flex;
  justify-content: space-between;
  color: #757575;
  font-size: 18px;
  line-height: 17px;
  text-align: center;
  margin: 0 5px;
}
</style>