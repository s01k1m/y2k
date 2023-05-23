<template>
  <div class="searchresult">

    <div v-show="!ResultList.length" class="noContents">There's no Stills!
    <br>
    :'(
    </div>
    <div id="columns">
      <figure v-for="(still, index) in ResultList" :key="index">
        <StillCard :still="still" :index="index"></StillCard>
      </figure>
    </div>
  </div>
</template>

<script>
import StillCard from './StillCard.vue';


export default {
  name: 'SearchResult',
  props : {
    ResultList: Object,
  },
  components: {
    StillCard
  },
  data() {
    return {
      stillBasedOnSearch:'',
    }
  },
  created() {
    this.stillBasedOnSearch = this.ResultList
  }
}
</script>

<style scoped>

#category {
  margin-bottom: 25px;
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
.noContents {
  margin: 200px 200px;
  font-size: x-large;
}
</style>