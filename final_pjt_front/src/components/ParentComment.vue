<template>
  <div>
    <div v-for="(comment, index) in comment_list" :key="index">
      댓글: {{ comment.content }}
      <button @click="deleteComment(comment.id)">삭제</button>
      <ChildComment :child_comment_list="parseChildC(comment.id)"></ChildComment>
      대댓: <input type="text" @keyup.enter="commentSubmit(comment.id)" v-model="comment_content">
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
    still_id: Number,
  },
  data() {
    return {
      comment_content: null,
      comment_list: [],
      child_comment_list: [],
    }
  },
  created() {
    this.get_comment_list()
  },
  methods: {
    parseChildC(parent){
      return this.child_comment_list.filter((comment)=>{
        return comment.parent === parent
      })
    },
    commentSubmit(comment_id) {
      if (!this.comment_content) {
        alert('내용을 입력하세요.')
      } else {
        console.log('commentSubmit 진입!')
        let token = localStorage.getItem("access_token")
        console.log('token: ', token)
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
        })
        .catch((err) => {
          console.log('err: ', err)
        })
      }
    },
    get_comment_list() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/communities/${this.still_id}`
      })
      .then((response) => {
        console.log('response data: ', response.data)
        response.data.forEach(element => {
          console.log('ele: ', element)
          if (!element.parent){
            this.comment_list.push(element)
          } else {
            this.child_comment_list.push(element)
          }
          console.log('대댓글 리스트', this.child_comment_list)
        });
      
      })
      .catch((err) => {
        console.log('err: ', err)
      })
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