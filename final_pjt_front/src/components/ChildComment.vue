<template>
  <div>
    <div v-for="(comment, index) in child_comment_list" :key="index">
      ㄴ {{ comment.username }}: {{ comment.content }}
      <button @click="deleteComment(comment.id)">삭제</button>
    </div>
    대댓: <input type="text" @keyup.enter="commentSubmit(comment_id)" v-model="comment_content">
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'ChildComment',
  props: {
    child_comment_list: Array,
    comment_id: Number,
    still_id: Number
  },
  data() {
    return {
      comment_content: null,
    }
  },
  methods: {
    emitToParent() {
      this.$emit('child-comment-submit')
    },
    commentSubmit(comment_id) {
      if (!this.comment_content) {
        alert('내용을 입력하세요.')
      } else {
        let token = localStorage.getItem("access_token")
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/communities/${this.still_id}/`,
          data: {
            'content': this.comment_content,
            'parent': comment_id,
          },
          headers: {
              Authorization: "Token " + token,
          },
        })
        .then((response) => {
          console.log('대댓글 작성 성공', response)
          this.comment_content = ''
          this.emitToParent()
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
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
        this.emitToParent()
      })
      .catch(() => {
        alert('본인이 작성한 댓글만 삭제할 수 있습니다.')
      })
    },
  }
}
</script>

<style>

</style>