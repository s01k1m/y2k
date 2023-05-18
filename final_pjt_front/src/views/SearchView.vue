<template>
  <div class="search">
    <h1>SearchView</h1>
    <SearchResult></SearchResult>
  </div>
</template>

<script>
import SearchResult from '@/components/SearchResult.vue'

export default {
  name: 'SearchView',
  components: {
    SearchResult
  }
}
</script>

<style>

</style>