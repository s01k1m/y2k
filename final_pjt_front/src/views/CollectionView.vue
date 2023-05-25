<template>
  <div>
    <div id="columns">
      <figure v-for="(collection, index) in collectionList" :key="index">
        <CollectionCard :collection="collection"></CollectionCard>
      </figure>
    </div>
  </div>
</template>
<script>
import CollectionCard from '@/components/CollectionCard.vue'
import axios from "axios"

export default {
  name: 'CollectionView',
  components: {
    CollectionCard
  },
  data() {
    return {
      collectionList: []
    }
  },
  created() {
    this.get_collections()
  },
  methods: {
    get_collections() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/stills/collections/all/',
      })
      .then((response) => {
        this.collectionList = response.data
        console.log('콜렉션 불러오기 성공!', response)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style scoped>
#columns{
    column-width:350px;
    column-gap: 15px;
    margin: 0 10px;
}
#columns figure{
  display: inline-block;
  margin: 20px;
  margin-bottom: 15px;
  border-radius: 8px;
  width: 350px;
  height: 300px;
}
/* #columns figure img{
  border-radius: 20px;
  height:100%;
} */
#columns figure figcaption{
  border-top:1px solid rgba(0,0,0,0.2);
  padding:10px;
  margin-top:11px;
}
</style>