<template>
  <div class="stillcard">
    <h1>StillCard</h1>
    <StillCut></StillCut>
    <MovieDetail></MovieDetail>
    <AddLike></AddLike>
  </div>
</template>

<script>
import StillCut from './StillCut.vue'
import MovieDetail from './MovieDetail.vue'
import AddLike from './AddLike.vue'

export default {
  name: 'StillCard',
  components: {
    StillCut,
    MovieDetail,
    AddLike
  }
}
</script>

<style>

</style>