<template>
  <div class="create">
    <h1>다른 사람들과 콜렉션을 공유하는 페이지입니다.</h1>
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
        url: 'http://127.0.0.1:8000/stills/collections/'
      })
      .then((response) => {
        this.collectionList = response.data
        console.log('콜렉션 불러오기 성공!')
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>
#columns{
    column-width:350px;
    column-gap: 15px;
    margin: 0 10px;
}
#columns figure{
  display: inline-block;
  /* border:1px solid rgba(0,0,0,0.2); */
  margin:0;
  margin-bottom: 15px;
  border-radius: 20px;
  /* box-shadow: 2px 2px 5px rgba(0,0,0,0.5);; */
}
#columns figure img{
  border-radius: 20px;
  width:100%;
}
#columns figure figcaption{
  border-top:1px solid rgba(0,0,0,0.2);
  padding:10px;
  margin-top:11px;
}
</style>