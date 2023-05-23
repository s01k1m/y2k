<template>
  <div>
    <div>
      댓글: {{ comment.content }}
    </div>
    <div v-for="(comment, index) in child_comment_list" :key="index">
      <ChildComment :comment="comment"></ChildComment>
    </div>
    <div>
      <button @click="deleteComment">삭제</button>
    </div>
    <div>
      대댓: <input type="text" @keyup.enter="commentSubmit" v-model="comment_content">
    </div>
  </div>
</template>

<script>
import axios from "axios"
import ChildComment from "./ChildComment.vue"

export default {
  name: 'ParentComment',
  components: {
    ChildComment
  },
  props: {
    comment: Object,
    child_comment_list: Array
  },
  data() {
    return {
      comment_content: null,
    }
  },
  methods: {
    commentSubmit(e) {
      e.preventDefault()
      if (!this.comment_content) {
        alert('내용을 입력하세요.')
      } else {
        console.log('commentSubmit 진입!')
        let token = localStorage.getItem("access_token")
        console.log('token: ', token)
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/communities/${this.comment.id}/`,
          data: {
            'content': this.comment_content,
            'parent': this.comment.id,
          },
          headers: {
              Authorization: "Token " + token,
          },
        })
        .then((response) => {
          console.log('대댓글 작성 성공', response)
          this.comment_content = ''
          this.get_child_comment_list()
        })
        .catch((err) => {
          console.log('err: ', err)
        })
      }
    },
    deleteComment() {
      let token = localStorage.getItem("access_token")
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/communities/${this.comment.id}/delete/`,
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