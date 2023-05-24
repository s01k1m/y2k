<template>
  <div>
    <div v-for="(comment, index) in comment_list" :key="index">
      {{ comment.username }}: {{ comment.content }}
      <button @click="deleteComment(comment.id)">삭제</button>
      <ChildComment :comment_id="comment.id" :still_id="still_id" :child_comment_list="parseChildC(comment.id)" :key="componentKey" @child-comment-submit="emitToParent"></ChildComment>
    </div>
    댓: <input type="text" @keyup.enter="commentSubmit()" v-model="comment_content">
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
      componentKey: 0,
    }
  },
  created() {
    this.get_comment_list()
  },
  methods: {
    get_comment_list() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/communities/${this.still_id}`
      })
      .then((response) => {
        response.data.forEach(element => {
          if (!element.parent){
            this.comment_list.push(element)
          } else {
            this.child_comment_list.push(element)
          }
        });
      
      })
      .catch((err) => {
        console.log('err: ', err)
      })
    },
    parseChildC(parent){
      return this.child_comment_list.filter((comment)=>{
        return comment.parent === parent
      })
    },
    emitToParent() {
      this.$emit('child-comment-submit')
    },
    commentSubmit() {
      if (!this.comment_content) {
        alert('내용을 입력하세요.')
      } else {
        let token = localStorage.getItem("access_token")
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/communities/${this.still_id}/`,
          data: {
            'content': this.comment_content,
            'parent': null,
          },
          headers: {
              Authorization: "Token " + token,
          },
        })
        .then((response) => {
          console.log('댓글 작성 성공', response)
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
        this.$emit('child-comment-submit')
      })
      .catch(() => {
        alert('본인이 작성한 댓글만 삭제할 수 있습니다.')
      })
    },
    // getCommentUserName(commentId) {
    //   console.log('getCommentUserName 진입, commentId: ', commentId)
    //   axios({
    //     method: 'get',
    //     url: `http://127.0.0.1:8000/communities/comments/${commentId}/`,
    //   })
    //   .then((response) => {
    //     console.log('댓글 이름 가져오기!: ', response)
    //   })
    // }
  }
}
</script>

<style>

</style>