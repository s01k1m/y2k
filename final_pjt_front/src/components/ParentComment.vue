<template>
  <div>
    <div id="container">
      <div id="commentfooter">
        <input type="text" @keyup.enter="commentSubmit()" v-model="comment_content">
      </div>
      <div v-for="(comment, index) in comment_list" :key="index">
        <div id="commentcontainer">
          <div id="commentbody">
            <span id="userid">
              {{ comment.username }} 
            </span>
            <span id="content">
              {{ comment.content }}
            </span>
          </div>
          <div>
            <button id="deletebutton" @click="deleteComment(comment.id)">X</button>
          </div>
        </div>
        <ChildComment :comment_id="comment.id" :still_id="still_id" :child_comment_list="parseChildC(comment.id)" :key="componentKey" @child-comment-submit="emitToParent"></ChildComment>
        <hr>
      </div>
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

<style scoped>
#container {
  display: flex;
  flex-direction: column;
  text-align: left;
  justify-content: space-between;
  margin: 10px;
}
#userid {
  font-weight: 600;
  text-align: left;
  font-size: 18px;
  margin-right: 5px;
}
#content {
  text-align: left;
  font-weight: 400;
  font-size: 16px;
}
#commentcontainer {
  margin: 5px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
#commentbody {
  justify-content: space-between;
  flex-direction: row;
}
#commentfooter {
  height: 48px;
  border: none;
  border-radius: 24px;
  padding: 1px 2px;
  background-color: #e9e9e9;
  display: inline;
  padding: 0 20px;
  flex: 3;
  text-align: left;
  margin-bottom: 10px;
}
#deletebutton {
  width: 20px;
}
</style>