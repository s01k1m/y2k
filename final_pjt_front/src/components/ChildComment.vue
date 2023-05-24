<template>
  <div>
    <div v-for="(comment, index) in child_comment_list" :key="index">
      ㄴ {{ comment.content }}
      <button @click="deleteComment(comment.id)">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'ChildComment',
  props: {
    child_comment_list: Array,
  },
  methods: {
    deleteComment(id) {
      let token = localStorage.getItem("access_token")
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/communities/${id}/delete/`,
        headers: {
              Authorization: "Token " + token,
          },
      })
      .then((response) => {
        console.log('삭제 성공: ', response)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>