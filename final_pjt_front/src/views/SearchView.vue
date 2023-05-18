<template>
  <div class="search">
    <h1>SearchView</h1>
    <p>{{ searchInput }}</p>
    <SearchResult></SearchResult>
  </div>
</template>

<script>
import SearchResult from '@/components/SearchResult.vue'

export default {
  name: 'SearchView',
  components: {
    SearchResult
  },
  computed: {
    searchInput() {
      return this.$route.query.searchInput
    }
  }
}
</script>

<style>

</style>