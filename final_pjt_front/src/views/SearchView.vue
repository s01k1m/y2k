<template>
  <div class="search">
    <h1>Stills of Movie "{{ getSearchInput }}" </h1>
    <!-- 검색 결과 props로 보냄 -->
    <SearchResult :ResultList="stillsResult"></SearchResult>
  </div>
</template>

<script>
import axios from 'axios'
import SearchResult from '@/components/SearchResult.vue'

export default {
  name: 'SearchView',
  components: {
    SearchResult
  },
  data() {
    return {
      stillsResult: [],
    }
  },
  computed: {
    getSearchInput() {
      return this.$route.params.searchInput
    }
  },
  created() {
    this.getSearchResult();
  },
  methods: {
    getSearchResult() {
      // params를 axios로 보내 api에서 데이터를 받아옴
      axios
        .get(`http://127.0.0.1:8000/stills/search/${this.$route.params.searchInput}/`)
        .then((response) => {
          this.stillsResult = response.data;
          console.log(response.data)
        })
        .catch((error) => {
          console.error(error);
        });
    }
  }
}
</script>

<style>
h1 {
  margin-bottom: 30px;
}
</style>