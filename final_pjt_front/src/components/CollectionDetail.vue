<template>
  <div>
    <div id="card">
      <div id="collectionDetail">
        <div id="collectionName">
          {{ collection_detail.collection_name }}
        </div>
        <div id="collectionInfo">
          <div>
            created by 
            <span id="userName">
              {{ collection_detail.username }}
            </span>
          </div>
          <div>
            {{ collection_detail.stills.length }} stillcuts
          </div>
        </div>
      </div>
      <div id="columns">
        <figure v-for="(still, index) in collection_detail.stills" :key="index">
          <StillCard :still="still" :index="index"></StillCard>
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import StillCard from "./StillCard.vue"

export default {
  name: 'CollectionDetail',
  data() {
    return {
      collection_detail: [],
    }
  },
  components: {
    StillCard
  },
  created() {
    this.get_detail()
  },
  methods: {
    get_detail() {
      const collectionId = this.$route.params.collectionId;
      axios
      .get(`http://127.0.0.1:8000/stills/collections/${collectionId}/`)
      .then((response) => {
          this.collection_detail = response.data;
      })
      .catch((err) => {
          console.error(err);
      });
    },
  }
}
</script>

<style>
#card {
  width: 80%;
  height: 80%;
  margin: 0 auto 20px auto;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0 4px 8px 0 rgb(172, 172, 172);
}
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
#collectionDetail {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 15px 20px 20px 30px;
}
#collectionName {
  margin: 15px 0 8px;
  line-height: 24px;
  font-size: 40px;
  font-weight: 700;
  color: #424242;
  word-break: keep-all;
  word-wrap: break-word;
}
#collectionInfo {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: right;
  color: #757575;
  font-size: 18px;
  line-height: 17px;
}
#userName {
  color: #424242;
  font-weight:bold;
}
</style>